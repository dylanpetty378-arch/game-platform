"""Nationwide Craigslist harvest via the public sapi JSON endpoint (same logic as cl_nat.py, importable).

  python3 scripts/harvest_cl.py <cats> <hours> [out.json]
  from harvest_cl import harvest; rows = harvest(CATS, 6)

Every US area (413) x each category, owner listings only, price <= $500 ($200–500 only clears at profit ≥ 10× price), posted within <hours>, with photos.
Needs areas.json (https://reference.craigslist.org/Areas) — downloaded automatically if missing.
"""
import json, time, sys, os, urllib.parse, urllib.request, concurrent.futures as cf

CATS = 'ata,cba,clt,ele,emd,hab,hsh,jwa,msa,pha,spo,sys,tls,tag,vga,bik,bop,boo,clo,mob,mpo,rvs,wan,for,hsd,gms,art,fua,atq'
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36'}

def _get(url, tries=3, timeout=40):
    for t in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception:
            time.sleep(2 + 3 * t)
    return None

def areas():
    p = os.path.join(HERE, 'areas.json')
    if not os.path.exists(p):
        open(p, 'wb').write(_get('https://reference.craigslist.org/Areas'))
    return [x for x in json.load(open(p)) if x['Country'] == 'US']

def _parse(d, ar, cat, since):
    dec = d.get('decode')
    if not isinstance(dec, dict): return []
    res = []
    for it in d['items']:
        rec = {'pid': dec['minPostingId'] + it[0], 'posted': dec['minPostedDate'] + it[1], 'price': it[3], 'title': it[-1],
               'imgs': [], 'slug': None, 'uuid': None, 'area': ar['Hostname'], 'region': ar['Region'], 'cat': cat}
        for x in it[4:-1]:
            if isinstance(x, list):
                if x[0] == 4: rec['imgs'] = [i.split(':', 1)[1] for i in x[1:]]
                elif x[0] == 6: rec['slug'] = x[1]
                elif x[0] == 13: rec['uuid'] = x[1]
        if rec['posted'] >= since and rec['imgs']: res.append(rec)
    return res

def harvest(cats=CATS, hours=24, threads=10, log=print):
    cats = cats.split(',') if isinstance(cats, str) else cats
    since = time.time() - float(hours) * 3600
    A = areas(); jobs = [(ar, c) for ar in A for c in cats]; out = {}; fails = 0
    stat = {'splits': 0, 'capped': 0}
    def query(ar, c, lo, hi):
        # Each Craigslist site's OWN listings (no lat/lon radius: radius queries overlap neighbouring sites and hit
        # the 360 cap sooner). Price window [lo, hi].
        p = {'batch': f"{ar['AreaID']}-0-360-0-0", 'cc': 'US', 'lang': 'en', 'searchPath': c, 'sort': 'date',
             'min_price': lo, 'max_price': hi, 'purveyor': 'owner'}
        raw = _get('https://sapi.craigslist.org/web/v8/postings/search/full?' + urllib.parse.urlencode(p))
        try: d = json.loads(raw)['data']
        except Exception: return None
        rows = _parse(d, ar, c, 0)
        # The API returns at most the newest 360. If we got 360 and the oldest is still inside the window, there are
        # more: split the price range in two and query both halves (adaptive price-band splitting).
        if len(d.get('items', [])) >= 360 and rows and min(r['posted'] for r in rows) > since and hi - lo >= 2:
            stat['splits'] += 1; mid = (lo + hi) // 2
            a = query(ar, c, lo, mid); b = query(ar, c, mid + 1, hi)
            if a is not None or b is not None: rows = rows + (a or []) + (b or [])
        elif len(d.get('items', [])) >= 360 and rows and min(r['posted'] for r in rows) > since:
            stat['capped'] += 1
        return [r for r in rows if r['posted'] >= since]
    def work(j):
        ar, c = j
        return query(ar, c, 1, 500)
    with cf.ThreadPoolExecutor(threads) as ex:
        for n, res in enumerate(ex.map(work, jobs)):
            if res is None: fails += 1; continue
            for r in res: out.setdefault(r['pid'], r)
            if n % 1000 == 0: log(f'{n}/{len(jobs)} jobs, {len(out)} listings, {fails} failed')
    log(f"DONE {len(out)} listings, {fails}/{len(jobs)} failed requests, {stat['splits']} price splits, {stat['capped']} still capped")
    return list(out.values()), fails, len(jobs)

if __name__ == '__main__':
    rows, f, n = harvest(sys.argv[1] if len(sys.argv) > 1 else CATS, float(sys.argv[2]) if len(sys.argv) > 2 else 24)
    out = sys.argv[3] if len(sys.argv) > 3 else f'cl_nat_{int(time.time())}.json'
    json.dump(rows, open(out, 'w')); print(out)
