#!/usr/bin/env python3
"""ShopGoodwill auctions → eye-screen pool (Oct 13 2026: golden-egg hunt beyond Craigslist).

ShopGoodwill's public buyer API needs no login to search (bidding needs Dylan's own account). ~720k open items;
~100k end every day. Goodwill staff title items fast, so mislabeled art, jewelry, militaria and antiques slip through.

  python3 scripts/sgw.py harvest <hours> [--first]   # items ending within <hours> in the egg categories -> /tmp/eye/sgw-<ts>/pool.json
  python3 scripts/sgw.py detail <itemId|sgwID> [...]   # description, bids, weight and ALL photo URLs
  python3 scripts/sgw.py markpool <run> <n> <out.json>    # markings run: n soonest-ending rows, titles not naming metal, full detail
  python3 scripts/sgw.py sold "<query>"               # ShopGoodwill's own closed auctions (what pros actually pay there)
  python3 scripts/eye_screen.py sheets sgw-<ts>        # then the usual contact sheets / ingest

Times from the API are US Pacific. Search pages are 40 items; results sort by ending soonest.
--first = the densest egg categories only (art, antiques, antique books, bulk lots, science, misc, art glass,
knives, advertising, militaria, watches, rings).
"""
import json, os, sys, time, datetime, urllib.request, concurrent.futures as cf
API = 'https://buyerapi.shopgoodwill.com/api/Search/ItemListing'
CATS = {'1': 'antiques', '15': 'art', '2257': 'bulk art', '2246': 'bulk collectibles', '2250': 'bulk jewelry', '2260': 'bulk glass',
        '2251': 'bulk instruments', '2259': 'bulk cameras', '2261': 'bulk misc', '4': 'collectibles', '6': 'jewelry', '170': 'cameras',
        '14': 'glass', '13': 'instruments', '113': 'misc', '132': 'antique books', '2229': 'antique tools', '431': 'vintage electronics', '364': 'science'}
DROP = ['Toys/Dolls/Games', 'Costume Jewelry', 'Earrings', 'Plush', 'Collector Plates', 'Action Figures', 'Digital Cameras', 'Camcorders',
        'Security', 'Cell Phones', 'Salt & Pepper', 'Cookie Jars', 'Lunch Boxes', 'Sports Cards', 'Die Cast', 'Jewelry Boxes', 'Fiction', 'Children',
        'Amplifiers', 'Instruments > Electronic', 'Pro Audio', 'Keyboards', 'Pianos']     # untested electronics / too big (Dylan's rules)
FIRST = ['Art', 'Antiques', 'Books > Antique', 'Bulk', 'Science', 'Miscellaneous', 'Art Glass', 'Knives', 'Advertising', 'Military',
         'Watches', 'Rings', 'Precious Metal', 'Fine Jewelry', 'Indigenous', 'Vintage Cameras', 'Lenses', 'Pottery', 'Sculptures',
         # Oct 22 2026 outcomes: 66% of $100+ SGW sales were in categories missing above — jewelry by type and instruments
         'Necklaces', 'Bracelets', 'Jewelry Sets', 'Brooches', 'Pendants', 'Jewelry & Gemstones']   # instruments removed Oct 27 2026: Dylan's never-show list (Oct 24)

def search(**kw):
    p = {"searchText": "", "selectedCategoryIds": "", "selectedSellerIds": "", "lowPrice": "0", "highPrice": "999999", "searchBuyNowOnly": "",
         "searchPickupOnly": "false", "searchNoPickupOnly": "false", "searchOneCentShippingOnly": "false", "searchDescriptions": "false",
         "searchClosedAuctions": "false", "closedAuctionEndingDate": "1/1/0001", "closedAuctionDaysBack": "7", "searchCanadaShipping": "false",
         "searchInternationalShippingOnly": "false", "sortColumn": "1", "page": "1", "pageSize": "40", "sortDescending": "false",
         "savedSearchId": 0, "useBuyerPrefs": "true", "searchUSOnlyShipping": "true", "categoryLevelNo": "1", "categoryLevel": 1,
         "categoryId": 0, "partNumber": "", "catIds": ""}
    p.update(kw)
    r = urllib.request.Request(API, data=json.dumps(p).encode(),
                               headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0', 'Origin': 'https://shopgoodwill.com'})
    return json.load(urllib.request.urlopen(r, timeout=60))

def _cat(c, lim):
    out, page = [], 1
    while page <= 400:
        try: d = search(selectedCategoryIds=c, page=str(page))
        except Exception: time.sleep(3); continue
        it = d['searchResults']['items']
        if not it: break
        out += [i for i in it if i['endTime'] <= lim]
        if it[-1]['endTime'] > lim: break
        page += 1
    return out

def harvest(hours, first=False):
    now_pt = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=7)
    lim = (now_pt + datetime.timedelta(hours=hours)).strftime('%Y-%m-%dT%H:%M:%S')
    with cf.ThreadPoolExecutor(8) as ex: res = list(ex.map(lambda c: _cat(c, lim), CATS))
    items = {i['itemId']: i for o in res for i in o}
    pool = []
    for i in sorted(items.values(), key=lambda i: i['endTime']):
        cn = i.get('catFullName') or ''
        if any(d in cn for d in DROP): continue
        if first and not any(f in cn for f in FIRST): continue
        pool.append({'pid': f"sgw{i['itemId']}", 'source': 'shopgoodwill', 'price': i['currentPrice'], 'title': i['title'],
                     'thumb': i['imageURL'].replace('\\', '/'), 'imgs': [i['imageURL'].replace('\\', '/')],
                     'url': f"https://shopgoodwill.com/item/{i['itemId']}", 'ends': i['endTime'] + ' PT', 'bids': i['numBids'],
                     'cat': cn, 'area': f"seller {i['sellerId']}", 'region': 'SGW', 'posted': 0})
    run = 'sgw-' + time.strftime('%Y%m%d-%H%M', time.gmtime())
    d = f'/tmp/eye/{run}'; os.makedirs(d + '/th', exist_ok=True)
    json.dump(pool, open(d + '/pool.json', 'w'))
    print(run, len(items), 'items ending within', hours, 'h;', len(pool), 'in pool')

def _detail(item_id):
    import re, html
    iid = str(item_id).replace('sgw', '')
    r = urllib.request.Request(f'https://buyerapi.shopgoodwill.com/api/ItemDetail/GetItemDetailModelByItemId/{iid}', headers={'User-Agent': 'Mozilla/5.0'})
    d = json.load(urllib.request.urlopen(r, timeout=40))
    desc = html.unescape(re.sub(r'<[^>]+>', ' ', d.get('description') or '')); desc = re.sub(r'\s+', ' ', desc).strip()
    imgs = [(d.get('imageServer') or '') + x.replace('\\', '/') for x in (d.get('imageUrlString') or '').split(';') if x]
    return d, desc, imgs

def detail(item_id):
    """Title, current bid, bids, end, weight, shipping, cleaned description and every full-size photo URL."""
    d, desc, imgs = _detail(item_id)
    print(f"{d['title']}\nbid ${d['currentPrice']} ({d['numberOfBids']} bids), ends {d['endTime']} PT, weight {d.get('displayWeight')}, "
          f"pickup-only {d.get('pickupOnly')}, seller {d.get('sellerCompanyName')}\n{desc[:2500]}\nPHOTOS:\n" + '\n'.join(imgs))

KNOWN = ('sterling', '925', '14k', '10k', '18k', '9k', '22k', '24k', 'karat', 'gold filled', 'platinum')

def markpool(run, n, out):
    """Markings run (Oct 16 2026): the n soonest-ending rows of /tmp/eye/<run>/pool.json (>=90 min left) whose titles
    don't already name the metal, with full description + every photo -> <out> as hallmark_panels.py input."""
    import time, datetime as dt
    pool = json.load(open(f'/tmp/eye/{run}/pool.json'))
    pt = dt.timezone(dt.timedelta(hours=-7))                      # API times are US Pacific (PDT in Oct)
    end = lambda r: dt.datetime.fromisoformat(r['ends'].replace(' PT', '')).replace(tzinfo=pt)
    soon = dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=90)
    rows = sorted([r for r in pool if r.get('ends') and end(r) > soon and not any(k in r['title'].lower() for k in KNOWN)], key=end)[:n]
    res = {}
    for i, r in enumerate(rows):
        for t in range(3):
            try:
                d, desc, imgs = _detail(r['pid']); break
            except Exception:
                time.sleep(2 + 3 * t); d = None
        if not d: continue
        res[r['pid']] = {'title': d['title'], 'imgs': imgs, 'bid': d['currentPrice'], 'bids': d['numberOfBids'],
                         'end': d['endTime'] + ' PT', 'url': r['url'], 'desc': desc[:1500], 'weight': d.get('displayWeight')}
        if i % 100 == 99: print(i + 1, 'details'); json.dump(res, open(out, 'w'))
    json.dump(res, open(out, 'w')); print(len(res), 'of', len(rows), 'details ->', out)

def sold(q, days=30):
    d = search(searchText=q, searchClosedAuctions='true', closedAuctionDaysBack=str(days), sortDescending='true')
    it = d['searchResults']['items']; ps = sorted(i['currentPrice'] for i in it if i['currentPrice'])
    print(q, '| n', len(ps), '| median', ps[len(ps) // 2] if ps else None)
    for i in it[:10]: print(f"  ${i['currentPrice']} {i['numBids']} bids  {i['title'][:70]}")

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == 'harvest': harvest(float(a[1]), '--first' in a)
    elif a[0] == 'sold': sold(a[1])
    elif a[0] == 'markpool': markpool(a[1], int(a[2]), a[3])
    elif a[0] == 'detail':
        for x in a[1:]: detail(x); print('-' * 40)
