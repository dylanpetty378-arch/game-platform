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
    cur = {}
    for e in db.read('events'): cur[str(e['pid'])] = e
    return cur

def ingest_inbox():
    files = sorted(glob.glob(os.path.join(ROOT, 'db', 'inbox', '*.json'))); n = 0
    have = {(str(r['pid']), r.get('run')) for r in db.read('lens')}
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
            ev.append({'ts': ts, 'pid': pid, 'stage': 'flagged' if x.get('f') else 'lensed', 'run': run,
                       'data': {'med': x.get('med'), 'ratio': x.get('ratio')}})
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
    scoring.LEARNED = scoring.learned_weights(list(db.read('lens')), Lby)
    print('learned category weights:', scoring.LEARNED)
    fresh = [r for r in rows if str(r['pid']) not in known]
    scored = [(scoring.score(r), r) for r in fresh]
    scored = [x for x in scored if x[0] > -99]
    scored.sort(key=lambda x: (-x[0], -x[1]['posted']))
    seen_img = set(); pick = []
    for s, r in scored:
        if r['imgs'][0] in seen_img: continue           # cross-posted duplicates share the first photo
        seen_img.add(r['imgs'][0]); pick.append((s, r))
        if len(pick) >= per_cycle: break
    db.append('harvests', {'harvest_id': hid, 'source': 'craigslist', 'hours': hours, 'cats': harvest_cl.CATS, 'n_listings': len(rows),
                           'n_new': len(fresh), 'n_selected': len(pick), 'learned': scoring.LEARNED, 'failed_requests': fails, 'requests': jobs, 'by_cat': by, 'by': 'github-actions'})
    db.append('listings', [{'pid': str(r['pid']), 'source': 'craigslist', 'harvest_id': hid, 'posted': r['posted'], 'price': r['price'],
                            'title': r['title'], 'area': r['area'], 'region': r['region'], 'cat': r['cat'], 'imgs': r['imgs'], 'score': s,
                            'url': f"https://www.craigslist.org/view/d/{r['slug']}/{r['uuid']}"} for s, r in pick])
    db.append('events', [{'pid': str(r['pid']), 'stage': 'queued', 'run': hid, 'data': {'score': s}} for s, r in pick])
    print(f'harvest {hid}: {len(rows)} listings, {len(fresh)} new, {len(pick)} queued, {fails}/{jobs} failed requests')
    return hid

def build_queue(maxn=3000, days=10):
    cur = latest_stage(); cutoff = time.time() - days * 86400
    L = {str(r['pid']): r for r in db.read('listings')}
    pend = [L[p] for p, e in cur.items() if e['stage'] == 'queued' and p in L and (L[p].get('posted') or 0) >= cutoff]
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
    open(os.path.join(ROOT, 'q', 'current', 'queue.txt'), 'w').write(';'.join(f"{r['imgs'][0]},{r['price']},{r['pid']}" for r in pend))
    qid = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d-%H%M')
    json.dump({'id': qid, 'n': len(pend), 'made': db.now()}, open(os.path.join(ROOT, 'q', 'current', 'meta.json'), 'w'))
    print(f'queue {qid}: {len(pend)} pending'); return len(pend)

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
    build_queue(); status()
