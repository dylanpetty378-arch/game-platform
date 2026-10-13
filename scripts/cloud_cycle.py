#!/usr/bin/env python3
"""One cycle of the always-on cloud worker (run by .github/workflows/refurbish-cycle.yml on game-platform `main`,
which checks out this `refurbish` branch, runs this, and commits the result). Safe to run by hand too:

  python3 scripts/cloud_cycle.py [--hours 6] [--per-cycle 800] [--no-harvest]

Steps
  1. INGEST  db/inbox/*.json — Lens results the Chrome loop uploaded (needs the optional token, see docs) — into
             db/lens + db/events, then delete the inbox files.
  2. HARVEST Craigslist nationwide for the last --hours (overlapping windows are fine; pids are deduplicated).
  3. SELECT  score every new listing for seller ignorance (scoring.py); the best --per-cycle that the database has
             never seen become `listings` rows + `queued` events.
  4. QUEUE   q/current/queue.txt = the top 3,000 listings still waiting for Lens (latest stage 'queued', posted in the
             last 10 days), best score first. Format: "img,price,pid;img,price,pid;…". q/current/meta.json has an id.
  5. STATUS  STATUS.md + status.json at the branch root: counts per stage, the flagged worklist waiting for a human/Claude
             look, finds, last harvest. This is what a Claude chat with no repo reads first.
"""
import json, os, sys, glob, time, argparse, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import db, scoring

ROOT = db.ROOT
RAW = 'https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish'

def latest_stage():
    # latest event by timestamp (ties: later line) — Lens results can be ingested after a review decision was logged
    cur = {}
    for e in db.read('events'):
        p = str(e['pid']); o = cur.get(p)
        if o is None or (e.get('ts') or '') >= (o.get('ts') or ''): cur[p] = e
    return cur

def ingest_inbox():
    Lt = {str(r['pid']): r for r in db.read('listings')}
    files = sorted(glob.glob(os.path.join(ROOT, 'db', 'inbox', '*.json'))); n = 0
    have = {(str(r['pid']), r.get('run')) for r in db.read('lens')}
    relens_count = {}
    for e in db.read('events'):
        if e.get('status') == 'relens' and e.get('note', '').startswith('empty Lens read'): relens_count[str(e['pid'])] = relens_count.get(str(e['pid']), 0) + 1
    for p in files:
        try: recs = json.load(open(p))
        except Exception: print('bad inbox file', p); continue
        rows, ev = [], []
        for x in recs:
            pid = str(x.get('pid') or ''); run = x.get('run') or 'chrome'
            if not pid or (pid, run) in have: continue
            have.add((pid, run))
            ts = datetime.datetime.fromtimestamp((x.get('ts') or time.time() * 1000) / 1000, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            rows.append({'ts': ts, 'pid': pid, 'run': run, 'i': x.get('i'), 'img': x.get('img'), 'price': x.get('price'), 'best': x.get('best'),
                         'med': x.get('med'), 'n': x.get('n'), 'ratio': x.get('ratio'), 'collect': x.get('c'), 'sources': x.get('s'),
                         'ai': x.get('ai'), 'ai_value': x.get('av'), 'flag': x.get('f')})
            # an empty/incomplete read ("Results are personalized", nothing priced, no AI text) goes straight back to the
            # queue as a re-run (at most twice per listing) instead of counting as 'lensed'
            empty = ('personalized' in (x.get('best') or '') or not x.get('best')) and not x.get('n') and len(x.get('ai') or '') < 20
            tries = relens_count.get(pid, 0)
            if empty and not x.get('f') and tries < 2:
                relens_count[pid] = tries + 1
                ev.append({'ts': ts, 'pid': pid, 'stage': 'queued', 'status': 'relens', 'run': run, 'note': 'empty Lens read, auto re-queued'})
            else:
                mm = scoring.mismatch((Lt.get(pid) or {}).get('title'), x.get('ai'), x.get('best'))
                ev.append({'ts': ts, 'pid': pid, 'stage': 'flagged' if (x.get('f') or mm) else 'lensed', 'run': run,
                           'note': ('Lens names ' + ', '.join(mm) + ' — title does not') if mm else None,
                           'data': {'med': x.get('med'), 'ratio': x.get('ratio'), 'mismatch': mm}})
        db.append('lens', rows); db.append('events', ev); os.remove(p); n += len(rows)
    print(f'inbox: {len(files)} files, {n} Lens results ingested'); return n

def harvest_and_select(hours, per_cycle):
    import harvest_cl
    rows, fails, jobs = harvest_cl.harvest(harvest_cl.CATS, hours)
    hid = 'craigslist-' + datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d-%H%M')
    by = {}
    for r in rows: by[r['cat']] = by.get(r['cat'], 0) + 1
    known = db.known_pids()
    # learn category weights from every Lens result so far (self-improving prioritisation)
    Lby = {str(r['pid']): r for r in db.read('listings')}
    scoring.LEARNED = scoring.learned_weights(list(db.read('events')), Lby)
    try:   # retrain the title→type model so new encyclopedia entries/reviews count immediately
        import type_model; type_model.build(); type_model._M = None
    except Exception as e: print('type model build failed', e)
    print('learned category weights:', scoring.LEARNED)
    fresh = [r for r in rows if str(r['pid']) not in known]
    scored = [(scoring.score(r), r) for r in fresh]
    scored = [x for x in scored if x[0] > -99]
    scored.sort(key=lambda x: (-x[0], -x[1]['posted']))
    # Image pre-ranking: CLIP scores the first photo of the best CLIP_N title candidates ("looks collectible" vs junk).
    # combined = title score + CLIP_W * clip score. Falls back to title-only if torch/open_clip are unavailable.
    clip_n = int(os.environ.get('CLIP_N', '12000')); clip_w = float(os.environ.get('CLIP_W', '0.6'))
    if clip_n > 0:
        try:
            import clip_rank
            t0 = time.time(); cr = clip_rank.ClipRanker(); head = scored[:clip_n]
            res = cr.score_listings([r for _, r in head])
            for (s0, r), (cs, _) in zip(head, res): r['clip'] = cs
            head = [((s0 + clip_w * r['clip']) if r.get('clip') is not None else s0 - 3, r) for s0, r in head]
            head.sort(key=lambda x: (-x[0], -x[1]['posted']))
            scored = head + scored[clip_n:]
            print(f'CLIP ranked {len(res)} candidates in {time.time()-t0:.0f}s')
        except Exception as e:
            print('CLIP unavailable, title-only ranking:', repr(e)[:200])
    seen_img = set(); pick = []
    for s, r in scored:
        if r['imgs'][0] in seen_img: continue           # cross-posted duplicates share the first photo
        seen_img.add(r['imgs'][0]); pick.append((s, r))
        if len(pick) >= per_cycle: break
    db.append('harvests', {'harvest_id': hid, 'source': 'craigslist', 'hours': hours, 'cats': harvest_cl.CATS, 'n_listings': len(rows),
                           'n_new': len(fresh), 'n_selected': len(pick), 'learned': scoring.LEARNED, 'failed_requests': fails, 'requests': jobs, 'by_cat': by, 'by': 'github-actions'})
    db.append('listings', [{'pid': str(r['pid']), 'source': 'craigslist', 'harvest_id': hid, 'posted': r['posted'], 'price': r['price'],
                            'title': r['title'], 'area': r['area'], 'region': r['region'], 'cat': r['cat'], 'imgs': r['imgs'], 'score': round(s, 2), 'clip': r.get('clip'),
                            'url': f"https://www.craigslist.org/view/d/{r['slug']}/{r['uuid']}"} for s, r in pick])
    db.append('events', [{'pid': str(r['pid']), 'stage': 'queued', 'run': hid, 'data': {'score': round(s, 2), 'clip': r.get('clip')}} for s, r in pick])
    print(f'harvest {hid}: {len(rows)} listings, {len(fresh)} new, {len(pick)} queued, {fails}/{jobs} failed requests')
    return hid

def build_queue(maxn=3000, days=10):
    cur = latest_stage(); cutoff = time.time() - days * 86400
    L = {str(r['pid']): r for r in db.read('listings')}
    pend = [L[p] for p, e in cur.items() if e['stage'] == 'queued' and p in L and (L[p].get('posted') or 0) >= cutoff and e.get('status') != 'relens']
    # re-runs (incomplete earlier Lens reads) go first, flagged 'r' so the worker runs them even if already in its DONE set
    relens = [L[p] for p, e in cur.items() if e['stage'] == 'queued' and e.get('status') == 'relens' and p in L]
    # size rule applies to listings queued before it existed too
    big = lambda r: scoring.is_bulky(r.get('title'))
    pend = [r for r in pend if not big(r) and not scoring.POLICY.search(r.get('title') or '')]; relens = [r for r in relens if not big(r)]
    # same photo = same item posted twice (or in two cities): Lens it once
    seen_img, dd = set(), []
    for r in sorted(pend, key=lambda r: -(r.get('score') or 0)):
        k = (r.get('imgs') or [''])[0]
        if k in seen_img: continue
        seen_img.add(k); dd.append(r)
    pend = dd
    # best score first; within one score, newest first and rotated across areas so one big metro can't fill the queue
    pend.sort(key=lambda r: (-(r.get('score') or 0), -(r.get('posted') or 0)))
    out, i = [], 0
    while i < len(pend) and len(out) < maxn:
        j = i
        while j < len(pend) and (pend[j].get('score') or 0) == (pend[i].get('score') or 0): j += 1
        tier, by = pend[i:j], {}
        for r in tier: by.setdefault(r.get('area'), []).append(r)
        lanes = list(by.values())
        while any(lanes) and len(out) < maxn:
            for ln in lanes:
                if ln and len(out) < maxn: out.append(ln.pop(0))
            lanes = [ln for ln in lanes if ln]
        i = j
    pend = out
    os.makedirs(os.path.join(ROOT, 'q', 'current'), exist_ok=True)
    pend = relens + pend[:max(0, maxn - len(relens))]
    open(os.path.join(ROOT, 'q', 'current', 'queue.txt'), 'w').write(';'.join(f"{r['imgs'][0]},{r['price']},{r['pid']}" + (',r' if r in relens else '') for r in pend))
    qid = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d-%H%M')
    json.dump({'id': qid, 'n': len(pend), 'made': db.now()}, open(os.path.join(ROOT, 'q', 'current', 'meta.json'), 'w'))
    print(f'queue {qid}: {len(pend)} pending'); return len(pend)

def liveness(maxn=400):
    """Re-check open leads (flagged, photo-review keepers, finds) and log `expired` when the posting is gone (HTTP 404/410
    or a deletion notice). Only dead listings get an event, so this never spams the log. Saves review time on dead items."""
    import urllib.request, urllib.error, re as _re
    from concurrent.futures import ThreadPoolExecutor
    cur = latest_stage(); L = {str(r['pid']): r for r in db.read('listings')}
    open_ = [p for p, e in cur.items() if (e['stage'] == 'flagged' or (e['stage'] == 'photo_review' and e.get('status') == 'keep')
             or (e['stage'] in ('identified', 'comps', 'decided', 'contacted') and e.get('status') not in ('kill', 'pass'))) and (L.get(p) or {}).get('url')]
    open_ = open_[:maxn]
    def chk(p):
        try:
            rq = urllib.request.Request(L[p]['url'], headers={'User-Agent': 'Mozilla/5.0 (Macintosh)'})
            h = urllib.request.urlopen(rq, timeout=20).read().decode('utf8', 'ignore')
            return p, 'dead' if _re.search(r'has been deleted|has expired|flagged for removal', h) else ('live' if 'postingbody' in h else '?')
        except urllib.error.HTTPError as e:
            return p, 'dead' if e.code in (404, 410) else '?'
        except Exception:
            return p, '?'
    with ThreadPoolExecutor(8) as ex: res = list(ex.map(chk, open_))
    dead = [p for p, r in res if r == 'dead']
    db.append('events', [{'ts': db.now(), 'pid': p, 'stage': 'expired', 'run': 'liveness',
                          'note': f"posting gone (was {cur[p]['stage']}/{cur[p].get('status') or ''})"} for p in dead])
    print(f"liveness: {len(open_)} open leads checked, {len(dead)} expired, {sum(1 for _, r in res if r == '?')} unknown"); return len(dead)

def status():
    cur = latest_stage(); L = {str(r['pid']): r for r in db.read('listings')}
    lens = {}
    for r in db.read('lens'): lens[str(r['pid'])] = r
    counts = {}
    for p, e in cur.items():
        k = e['stage'] + (('/' + e['status']) if e.get('status') else ''); counts[k] = counts.get(k, 0) + 1
    flagged = [p for p, e in cur.items() if e['stage'] == 'flagged']
    flagged.sort(key=lambda p: -((lens.get(p) or {}).get('ratio') or 0))
    finds = [p for p, e in cur.items() if e['stage'] in ('decided', 'contacted', 'bought') and e.get('status') in ('find', 'ask', None)]
    H = list(db.read('harvests'))[-5:]
    tables = {t: sum(1 for _ in db.read(t)) for t in db.TABLES}
    st = {'updated': db.now(), 'tables': tables, 'stages': counts, 'last_harvests': H,
          'flagged_waiting': [{'pid': p, **{k: (L.get(p) or {}).get(k) for k in ('title', 'price', 'area', 'url')},
                               **{k: (lens.get(p) or {}).get(k) for k in ('best', 'med', 'ratio', 'ai_value')}} for p in flagged],
          'finds': [{'pid': p, **{k: (L.get(p) or {}).get(k) for k in ('title', 'price', 'area', 'url')}, 'note': cur[p].get('note'),
                     'stage': cur[p]['stage'], 'status': cur[p].get('status')} for p in finds]}
    json.dump(st, open(os.path.join(ROOT, 'status.json'), 'w'), indent=1)
    md = [f"# Refurbish status — {st['updated']}", '',
          'Machine-written by scripts/cloud_cycle.py after every cycle (GitHub Actions, every 4 h, plus after each Lens upload). Instructions: [docs/START-HERE.md](docs/START-HERE.md).', '',
          '## Pipeline', '', '| stage | listings |', '|---|---|'] + [f'| {k} | {v} |' for k, v in sorted(counts.items(), key=lambda x: -x[1])]
    md += ['', '## Tables', ''] + [f'- {t}: {n}' for t, n in tables.items()]
    md += ['', '## Last harvests', ''] + [f"- {h.get('harvest_id')} — {h.get('n_listings')} listings, {h.get('n_new', '?')} new, {h.get('n_selected', '?')} queued" for h in H]
    def thumb(pid, w=120):
        im = ((L.get(pid) or {}).get('imgs') or [None])[0]
        return f'<img src="https://images.craigslist.org/{im}_300x300.jpg" width="{w}">' if im else ''
    md += ['', f'## Finds and open leads ({len(finds)})', '']
    if finds:
        md += ['| photo | item | price | where | status / next step |', '|---|---|---|---|---|']
        for f in st['finds']:
            md.append(f"| {thumb(f['pid'], 160)} | [{(f['title'] or '')[:60]}]({f['url']}) | ${f['price']} | {f['area']} | **{f['stage']}/{f['status']}** — {(f['note'] or '').replace('|', '/')[:220]} |")
    else:
        md.append('_None yet._')
    md += ['', f'## Flagged by Lens, waiting for photo review ({len(flagged)})', '',
           'Highest Lens price ratio first. Lens often matches the category, not the item: the photo review decides.', '',
           '| photo | pid | price | area | title | Lens best match | match median | ratio |', '|---|---|---|---|---|---|---|---|']
    for f in st['flagged_waiting'][:120]:
        md.append(f"| {thumb(f['pid'])} | {f['pid']} | ${f['price']} | {f['area']} | [{(f['title'] or '')[:50]}]({f['url']}) | {(f['best'] or '').replace('|', '/')[:60]} | {f['med']} | {f['ratio']} |")
    open(os.path.join(ROOT, 'STATUS.md'), 'w').write('\n'.join(md) + '\n')
    print('status written')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--hours', type=float, default=6); ap.add_argument('--per-cycle', type=int, default=800)
    ap.add_argument('--no-harvest', action='store_true'); a = ap.parse_args()
    ingest_inbox()
    if not a.no_harvest: harvest_and_select(a.hours, a.per_cycle)
    try: liveness()
    except Exception as e: print('liveness failed', e)
    build_queue(); status()
