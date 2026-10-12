"""Nationwide Craigslist harvest via the public sapi JSON endpoint (same logic as cl_nat.py, importable).

  python3 scripts/harvest_cl.py <cats> <hours> [out.json]
  from harvest_cl import harvest; rows = harvest(CATS, 6)

Every US area (413) x each category, owner listings only, price <= $200, posted within <hours>, with photos.
Needs areas.json (https://reference.craigslist.org/Areas) — downloaded automatically if missing.
"""
import json, time, sys, os, urllib.parse, urllib.request, concurrent.futures as cf

CATS = 'ata,cba,clt,ele,emd,hab,hsh,jwa,mus,pha,spo,sys,tls,tag,vga,bik,bop,boo,clo,mob,mpo,rvs,wan,for,hsd,gms,art,fua,atq'
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
    def work(j):
        ar, c = j
        p = {'batch': f"{ar['AreaID']}-0-360-0-0", 'cc': 'US', 'lang': 'en', 'searchPath': c, 'lat': ar['Latitude'], 'lon': ar['Longitude'],
             'search_distance': 150, 'sort': 'date', 'max_price': 200, 'purveyor': 'owner'}
        raw = _get('https://sapi.craigslist.org/web/v8/postings/search/full?' + urllib.parse.urlencode(p))
        try: return _parse(json.loads(raw)['data'], ar, c, since)
        except Exception: return None
    with cf.ThreadPoolExecutor(threads) as ex:
        for n, res in enumerate(ex.map(work, jobs)):
            if res is None: fails += 1; continue
            for r in res: out.setdefault(r['pid'], r)
            if n % 1000 == 0: log(f'{n}/{len(jobs)} jobs, {len(out)} listings, {fails} failed')
    log(f'DONE {len(out)} listings, {fails}/{len(jobs)} failed requests')
    return list(out.values()), fails, len(jobs)

if __name__ == '__main__':
    rows, f, n = harvest(sys.argv[1] if len(sys.argv) > 1 else CATS, float(sys.argv[2]) if len(sys.argv) > 2 else 24)
    out = sys.argv[3] if len(sys.argv) > 3 else f'cl_nat_{int(time.time())}.json'
    json.dump(rows, open(out, 'w')); print(out)
