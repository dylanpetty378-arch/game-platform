#!/usr/bin/env python3
"""Outcomes (Oct 22 2026): what things ACTUALLY sold for, so the system learns from the market instead of from guesses.

Runs daily in the eye-shortlist workflow (free). Three jobs:

  python3 scripts/outcomes.py sgw [--days 2]     # ShopGoodwill closed auctions (sold, final >= $10) in our categories
                                                 #   -> db/outcomes/sgw/<date>.jsonl.gz   (~7k sold lots a day, photo + final)
  python3 scripts/outcomes.py join               # last shortlist's rows + our flags/verdicts, joined to their final prices
                                                 #   -> db/outcomes/shortlist.jsonl      (calibration: did our score/eye work?)
  python3 scripts/outcomes.py misses [--date D]  # lots that sold high while the title said nothing about why
                                                 #   -> research/pools/misses/<date>.md  (what pickers saw that we didn't)

Why: ShopGoodwill buyers are mostly resellers, so a final price there is a picker's price — a conservative floor for
what the thing is worth. Thousands a day, each with a photo, is the training set for "ones like this sell for $X"
(scripts/knn.py) and the evidence for which visual tells matter (weekly misses review, docs/low-usage.md).
eBay: the Browse API is tried for last shortlist's ended eBay rows; whatever it returns is recorded with the row.
"""
import os, sys, re, json, gzip, glob, time, datetime as dt, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
ODIR = os.path.join(ROOT, 'db', 'outcomes')
SGWDIR = os.path.join(ODIR, 'sgw')
MISSDIR = os.path.join(ROOT, 'research', 'pools', 'misses')
MIN_FINAL = 10

def today(): return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')

def read_gz(p):
    try:
        with gzip.open(p, 'rt') as f: return [json.loads(l) for l in f if l.strip()]
    except Exception: return []

def recent_sgw(days=60):
    """All stored SGW outcome rows from the last <days> daily files (newest last)."""
    fs = sorted(glob.glob(os.path.join(SGWDIR, '*.jsonl.gz')))[-days:]
    return [r for f in fs for r in read_gz(f)]

# ---------------------------------------------------------------- ShopGoodwill closed auctions
def _closed_cat(c, days):
    import sgw
    out, page, err = [], 1, 0
    while page <= 600:
        try: d = sgw.search(selectedCategoryIds=c, searchClosedAuctions='true', closedAuctionDaysBack=str(days),
                            lowPrice=str(MIN_FINAL), page=str(page))
        except Exception as e:
            err += 1
            if err > 8 or ('403' in str(e) and page == 1): break     # some bulk categories always 403; others rate-limit
            time.sleep(5 * err); continue
        it = d['searchResults']['items']
        if not it: break
        out += it; page += 1; err = 0
    return out

def pull_sgw(days=2):
    import sgw
    with cf.ThreadPoolExecutor(3) as ex: res = list(ex.map(lambda c: _closed_cat(c, days), sgw.CATS))
    print("sgw closed fetched", {sgw.CATS[c]: len(o) for c, o in zip(sgw.CATS, res)}, flush=True)
    seen = {r['id'] for f in sorted(glob.glob(os.path.join(SGWDIR, '*.jsonl.gz')))[-4:] for r in read_gz(f)}
    rows, unsold = {}, 0
    for i in (i for o in res for i in o):
        if (i.get('numBids') or 0) < 1: unsold += 1; continue          # unsold (or a buy-now that never sold)
        if any(x in (i.get('catFullName') or '') for x in sgw.DROP): continue
        k = f"sgw{i['itemId']}"
        if k in seen or k in rows: continue
        rows[k] = {'id': k, 't': i['title'], 'cat': i.get('catFullName') or i.get('categoryName'), 'start': i.get('startingPrice'),
                   'final': i['currentPrice'], 'bids': i['numBids'], 'end': (i.get('endTime') or '')[:19] + ' PT',
                   'img': (i.get('imageURL') or '').replace('\\', '/'), 'seller': i.get('sellerId')}
    os.makedirs(SGWDIR, exist_ok=True)
    p = os.path.join(SGWDIR, today() + '.jsonl.gz')
    old = read_gz(p)
    with gzip.open(p, 'wt') as f:
        for r in old + sorted(rows.values(), key=lambda r: r['end']): f.write(json.dumps(r, ensure_ascii=False) + '\n')
    fin = sorted(r['final'] for r in rows.values())
    print(f"sgw outcomes: {len(rows)} new sold lots (unsold skipped {unsold}); median ${fin[len(fin)//2] if fin else 0}, "
          f">= $100: {sum(x >= 100 for x in fin)} -> {p}", flush=True)
    if len(rows) < 500: print(f'::warning::only {len(rows)} SGW outcomes pulled', flush=True)

# ---------------------------------------------------------------- join last shortlist to outcomes
def _ebay_final(r):
    try:
        import ebay_api
        d = ebay_api._get('browse', f"/buy/browse/v1/item/v1|{r['id'][2:]}|0", {}) or {}
    except Exception as e: return {'err': str(e)[:80]}
    if d.get('error') or not d.get('itemId'): return {'err': str(d.get('error') or d)[:120]}
    return {'final': float((d.get('currentBidPrice') or d.get('price') or {}).get('value') or 0) or None,
            'bids': d.get('bidCount'), 'status': (d.get('estimatedAvailabilities') or [{}])[0].get('estimatedAvailabilityStatus'),
            'end': d.get('itemEndDate')}

def join():
    """Rows from the shortlist that is about to be replaced, plus every lowuse verdict, with their final prices."""
    sl = os.path.join(ROOT, 'research', 'pools', 'shortlist.json')
    if not os.path.exists(sl): print('no shortlist'); return
    S = json.load(open(sl)); made = S.get('made', '')[:19]
    done = set()
    jp = os.path.join(ODIR, 'shortlist.jsonl')
    if os.path.exists(jp):
        for l in open(jp):
            try: done.add(json.loads(l)['made'])
            except Exception: pass
    if made in done: print('shortlist', made, 'already joined'); return
    verdict = {}
    lp = os.path.join(ROOT, 'research', 'pools', 'lowuse-log.jsonl')
    if os.path.exists(lp):
        for l in open(lp):
            try: x = json.loads(l); verdict[x['pid']] = x['verdict']
            except Exception: pass
    fin = {r['id']: r for r in recent_sgw(5)}
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    eb = [r for r in S['rows'] if r['src'] == 'ebay' and (r.get('end') or 'Z') < now]
    with cf.ThreadPoolExecutor(6) as ex: ebf = dict(zip([r['id'] for r in eb], ex.map(_ebay_final, eb))) if os.environ.get('EBAY_CLIENT_ID') else {}
    out = []
    for r in S['rows']:
        o = fin.get(r['id']) if r['src'] == 'sgw' else ebf.get(r['id'])
        out.append({'made': made, 'id': r['id'], 'src': r['src'], 'p': r['p'], 'b': r['b'], 't': r['t'][:90],
                    'score': r.get('score'), 'egg': r.get('egg'), 'tval': r.get('tval'), 'down': r.get('down'),
                    'types': [t[0] for t in r.get('types', [])][:2], 'knn': (r.get('knn') or {}).get('p50'),
                    'melt': (r.get('melt') or {}).get('net'), 'mark': bool((r.get('ocr') or {}).get('makers')),
                    'verdict': verdict.get(r['id']), 'final': (o or {}).get('final'), 'fbids': (o or {}).get('bids'),
                    'oerr': (o or {}).get('err')})
    os.makedirs(ODIR, exist_ok=True)
    with open(jp, 'a') as f:
        for x in out: f.write(json.dumps(x, ensure_ascii=False) + '\n')
    k = {s: sum(1 for x in out if x['src'] == s and x['final']) for s in ('ebay', 'sgw')}
    n = {s: sum(1 for x in out if x['src'] == s) for s in ('ebay', 'sgw')}
    print(f'joined shortlist {made}: finals found {k} of {n} -> {jp}', flush=True)
    errs = [x['oerr'] for x in out if x['oerr']][:2]
    if errs: print('  ebay sample errors:', errs, flush=True)

# ---------------------------------------------------------------- misses: sold high, title silent
SAYS = re.compile(r'\b(\d+ ?k|\d+ ?kt|karat|carat|ct|ctw|gold|sterling|925|800|900|silver|platinum|plat|diamonds?|sapphire|'
                  r'ruby|emerald|opal|pearls?|jade|turquoise|signed|marked|hallmarked|rolex|omega|tiffany|cartier|leica|nikon|'
                  r'canon|hasselblad|zeiss|gibson|fender|martin|lot of|lots?|bulk|grams?|g\b|ozt?|dwt)', re.I)

def misses(date=None, top=60, minf=100):
    date = date or today()
    rows = read_gz(os.path.join(SGWDIR, date + '.jsonl.gz'))
    if not rows: print('no outcomes for', date); return
    try:
        from shortlist import load_makers
        mk = load_makers()
    except Exception: mk = None
    shown = {}
    try: shown = json.load(open(os.path.join(ROOT, 'research', 'pools', 'shown.json')))
    except Exception: pass
    verdict = {}
    lp = os.path.join(ROOT, 'research', 'pools', 'lowuse-log.jsonl')
    if os.path.exists(lp):
        for l in open(lp):
            try: x = json.loads(l); verdict[x['pid']] = x['verdict']
            except Exception: pass
    # Dylan's never-show categories (Oct 24 2026) and by-the-pound lots are not misses — Oct 27 review: 33 of 96 misses were
    # instruments and 20 were grab-bags sold at a known $/lb, none of which the eye should learn from.
    NEVER = re.compile(r'(Musical Instruments|Trading Cards|Funko|Furniture|Appliances|Speakers|Amplifiers|Audio)', re.I)
    BULK = re.compile(r'\b(\d+\s*(?:lb|lbs|pound|pounds)|mystery box|grab bag|by the pound|unsearched)\b', re.I)
    hit = [r for r in rows if r['final'] >= minf and not SAYS.search(r['t']) and not (mk and mk.search(r['t']))
           and not NEVER.search((r.get('cat') or '') + ' ' + r['t']) and not BULK.search(r['t'])]
    hit.sort(key=lambda r: -r['final'])
    os.makedirs(MISSDIR, exist_ok=True)
    md = [f'# Misses {date} — SGW lots that sold >= ${minf} with titles that do not say why',
          f'{len(hit)} of {len(rows)} sold lots. Columns: final · bids · start · seen by us? · title · category · photo.',
          'Weekly review (docs/low-usage.md): for each, what is it and what in the PHOTO showed it? Turn repeat answers into',
          'encyclopedia tells / CLIP prompts. "seen" = it was on our shortlist (and the verdict, if the eye flagged it).\n']
    for r in hit[:top]:
        seen = ('SHORTLISTED' + (f" ({verdict[r['id']]})" if r['id'] in verdict else '')) if r['id'] in shown else 'not seen'
        md.append(f"- ${r['final']:.0f} · {r['bids']} bids · start ${r.get('start')} · {seen} · {r['t'][:90]} · {r.get('cat')} · {r['img']}")
    import sgw, collections                       # where the $100+ sales are vs where the harvest looks
    c, n = collections.Counter(), collections.Counter()
    for r in rows:
        k = (' > '.join((r.get('cat') or '?').split(' > ')[:2]), any(f in (r.get('cat') or '') for f in sgw.FIRST))
        n[k] += 1; c[k] += r['final'] >= minf
    tot = sum(c.values()) or 1; cov = sum(v for (k, i), v in c.items() if i)
    md.append(f'\n## Coverage: {cov} of {tot} (${minf}+) sales ({cov / tot:.0%}) were in categories the harvest looks at')
    for (k, i), v in c.most_common(15): md.append(f"- {v} of {n[(k, i)]} sold · {'harvested' if i else 'NOT HARVESTED'} · {k}")
    p = os.path.join(MISSDIR, date + '.md'); open(p, 'w').write('\n'.join(md) + '\n')
    print(f'misses {date}: {len(hit)} (shortlisted {sum(r["id"] in shown for r in hit)}) -> {p}', flush=True)

if __name__ == '__main__':
    a = sys.argv[1:]
    opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    if not a: print(__doc__)
    elif a[0] == 'sgw': pull_sgw(int(opt('--days', 2)))
    elif a[0] == 'join': join()
    elif a[0] == 'misses': misses(opt('--date', None))
