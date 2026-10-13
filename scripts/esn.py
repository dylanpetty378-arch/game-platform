#!/usr/bin/env python3
"""EstateSales.net → eye-screen pool: every photo of every estate sale near Keller TX this week (no login).

  python3 scripts/esn.py pool [days=7] [miles=45]     # -> /tmp/eye/esn-<date>/pool.json, then eye_screen.py sheets esn-<date>
Briefs: research/ESTATE_EYE_BRIEF.md (sheets) → research/ESTATE_DEEP_BRIEF.md (full-size + auction records).
Companies caption what they researched (~10% of photos); eggs are in the uncaptioned photos.
"""
import json, os, sys, time, datetime, urllib.request, concurrent.futures as cf
H = {'User-Agent': 'Mozilla/5.0'}
def _get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60))
def v(x): return x.get('_value') if isinstance(x, dict) else x

def pool(days=7, miles=45):
    S = _get(f'https://www.estatesales.net/api/sale-details?bypass=bycoordinatesanddistance:32.934_-97.229_{miles}')
    now = datetime.datetime.utcnow(); end = (now + datetime.timedelta(days=days)).isoformat(); start = now.isoformat()[:10]
    keep = [s for s in S if s['typeName'] != 'OnlineOnlyAuctions' and (v(s.get('firstUtcStartDate')) or '') < end and (v(s.get('lastUtcEndDate')) or '') >= start]
    def pics(s):
        for _ in range(3):
            try: return s, _get(f"https://www.estatesales.net/api/sale-details/{s['id']}?include=pictures").get('pictures') or []
            except Exception: time.sleep(2)
        return s, []
    with cf.ThreadPoolExecutor(8) as ex: R = list(ex.map(pics, keep))
    out = [{'pid': f"esn{s['id']}-{k}", 'source': 'estatesales', 'price': 0, 'title': (p.get('description') or '').strip()[:120],
            'thumb': p.get('thumbnailUrl'), 'imgs': [p.get('url')], 'url': 'https://www.estatesales.net' + s['url'], 'cat': s['typeName'],
            'area': s['cityName'], 'region': s.get('orgName') or '', 'posted': 0, 'ends': v(s.get('lastUtcEndDate')), 'sale': s['name'],
            'captioned': bool(p.get('description'))} for s, P in R for k, p in enumerate(P)]
    run = 'esn-' + now.strftime('%Y%m%d'); d = f'/tmp/eye/{run}'; os.makedirs(d + '/th', exist_ok=True)
    json.dump(out, open(d + '/pool.json', 'w'))
    print(run, len(keep), 'sales,', len(out), 'photos,', sum(p['captioned'] for p in out), 'captioned')

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == 'pool': pool(int(a[1]) if len(a) > 1 else 7, int(a[2]) if len(a) > 2 else 45)
