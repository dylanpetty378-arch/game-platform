#!/usr/bin/env python3
"""eBay comps from the cloud, using eBay's official free developer APIs. No browser, no laptop.

Needs two GitHub Actions secrets (Dylan creates them; Claude never handles keys):
  EBAY_CLIENT_ID, EBAY_CLIENT_SECRET   (developer.ebay.com → Application Keys → Production keyset)

  python3 scripts/ebay_api.py check                  # can we get a token? which APIs are allowed?
  python3 scripts/ebay_api.py comps "query" [...]    # print comps for queries
  python3 scripts/ebay_api.py leads                  # comps for every open lead's type queries → db
  python3 scripts/ebay_api.py rotate --n 150         # refresh the encyclopedia's stalest type queries → db

Two data sources, best first:
  - Marketplace Insights API (SOLD items, last 90 days). eBay restricts it: the app must be approved for the
    `buy.marketplace.insights` scope. Rows are stored with source `ebay-sold-90d`.
  - Browse API (ACTIVE listings), allowed for every developer app. Asking prices, not sales, so they're stored with
    source `ebay-active` and are only used as a ceiling. A lead still needs a sold comp before it goes to Dylan.
Calls are paced at 1.2 s, well under the default limit of 5,000 Browse calls a day.
"""
import os, sys, json, time, base64, statistics, urllib.request, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
API = 'https://api.ebay.com'
SCOPES = {'browse': 'https://api.ebay.com/oauth/api_scope',
          'insights': 'https://api.ebay.com/oauth/api_scope/buy.marketplace.insights'}
_tok = {}

def token(kind):
    if kind in _tok: return _tok[kind]
    cid, sec = os.environ.get('EBAY_CLIENT_ID'), os.environ.get('EBAY_CLIENT_SECRET')
    if not cid or not sec: raise SystemExit('EBAY_CLIENT_ID / EBAY_CLIENT_SECRET not set')
    req = urllib.request.Request(API + '/identity/v1/oauth2/token', method='POST',
        data=urllib.parse.urlencode({'grant_type': 'client_credentials', 'scope': SCOPES[kind]}).encode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded',
                 'Authorization': 'Basic ' + base64.b64encode(f'{cid}:{sec}'.encode()).decode()})
    try: _tok[kind] = json.load(urllib.request.urlopen(req, timeout=30))['access_token']
    except Exception: _tok[kind] = None
    return _tok[kind]

def _get(kind, path, params):
    t = token(kind)
    if not t: return None
    req = urllib.request.Request(API + path + '?' + urllib.parse.urlencode(params),
        headers={'Authorization': 'Bearer ' + t, 'X-EBAY-C-MARKETPLACE-ID': 'EBAY_US'})
    try: return json.load(urllib.request.urlopen(req, timeout=30))
    except Exception as e: return {'error': str(e)}

def prices(items, key):
    out = []
    for it in items or []:
        p = (it.get(key) or {}).get('value') if isinstance(it.get(key), dict) else None
        try: out.append((float(p), (it.get('title') or '')[:70]))
        except Exception: pass
    return out

def comps(q):
    """{'source', 'n', 'p25', 'p50', 'p75', 'top'} using sold data when allowed, else active asks."""
    d = _get('insights', '/buy/marketplace_insights/v1_beta/item_sales/search', {'q': q, 'limit': 50})
    if d and d.get('itemSales') is not None:
        ps, src = prices(d.get('itemSales'), 'lastSoldPrice'), 'ebay-sold-90d'
    else:
        d = _get('browse', '/buy/browse/v1/item_summary/search', {'q': q, 'limit': 50, 'filter': 'buyingOptions:{FIXED_PRICE}'})
        ps, src = prices((d or {}).get('itemSummaries'), 'price'), 'ebay-active'
    v = sorted(p for p, _ in ps)
    qt = lambda x: v[min(len(v) - 1, int(len(v) * x))] if v else None
    return {'q': q, 'source': src, 'n': len(v), 'p25': qt(.25), 'p50': qt(.5), 'p75': qt(.75),
            'top': [f'${p} {t}' for p, t in ps[:6]]}

def store(rows, run):
    import db
    db.append('searches', [{'site': r['source'], 'query': r['q'], 'purpose': r.get('purpose', ''), 'results': r['n'], 'run': run} for r in rows])
    db.append('comps', [{'type': r.get('type'), 'query': r['q'], 'source': r['source'], 'prices': [], 'median': r['p50'],
                         'n': r['n'], 'pid': r.get('pid'), 'run': run,
                         'note': json.dumps({'p25': r['p25'], 'p75': r['p75'], 'top': r['top']})} for r in rows if r['n']])

def run_queries(pairs, run):
    rows = []
    for slug, q, pid in pairs:
        r = comps(q); r.update(type=slug, pid=pid, purpose=f'cloud comps: {slug}'); rows.append(r); time.sleep(1.2)
    store(rows, run); print(len(rows), 'queries,', sum(1 for r in rows if r['n']), 'with results,',
                             sum(1 for r in rows if r['source'] == 'ebay-sold-90d'), 'sold-data')
    return rows

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    run = 'ebay-api-' + time.strftime('%Y%m%d-%H%M')
    if a[0] == 'check':
        print('browse token:', bool(token('browse')), '| insights (sold) token:', bool(token('insights')))
    elif a[0] == 'comps':
        for q in a[1:]: print(json.dumps(comps(q))); time.sleep(1.2)
    elif a[0] == 'leads':
        import db
        cur = {}
        for e in db.read('events'):
            p = str(e['pid']); o = cur.get(p)
            if o is None or (e.get('ts') or '') >= (o.get('ts') or ''): cur[p] = e
        L = {str(r['pid']): r for r in db.read('listings')}
        pairs = [(e.get('type'), (L.get(p) or {}).get('title', ''), p) for p, e in cur.items()
                 if e['stage'] == 'decided' and e.get('status') in ('ask', 'find') and (L.get(p) or {}).get('title')]
        run_queries(pairs, run)
    elif a[0] == 'rotate':
        n = int(a[a.index('--n') + 1]) if '--n' in a else 150
        import db
        done = {}
        for c in db.read('comps'):
            if c.get('query'): done[c['query']] = max(done.get(c['query'], ''), c.get('ts') or '')
        Q = []
        for f in ('research/tp_queries_wave1.json', 'research/tp_queries_wave2.json'):
            p = os.path.join(os.path.dirname(HERE), f)
            if os.path.exists(p): Q += json.load(open(p))
        Q.sort(key=lambda sq: done.get(sq[1], ''))          # never-queried first, then stalest
        run_queries([(s, q, None) for s, q in Q[:n]], run)
