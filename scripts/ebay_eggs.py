#!/usr/bin/env python3
"""eBay auctions as a golden-egg source (Oct 13 2026). Runs in GitHub Actions (api.ebay.com is blocked from Claude's
container); needs the EBAY_CLIENT_ID / EBAY_CLIENT_SECRET repo secrets Dylan added.

The classic shipped arbitrage: casual sellers (low feedback) listing auctions with poor titles in art / antiques /
pottery / jewelry / cameras, ending soon with 0–2 bids. Everyone on eBay can see them, but the seller's title and a
single dark photo hide what it is, and few bidders open it.

  python3 scripts/ebay_eggs.py pool [hours=24]   # -> research/pools/ebay-latest.json (compact rows), committed by the workflow
Then in a Claude session: python3 scripts/ebay_eggs.py sheetpool  → /tmp/eye/ebay-<ts>/pool.json → eye_screen.py sheets
"""
import os, sys, json, time, datetime, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
# eBay US leaf/top categories where eggs live (top-level ids; Browse searches include children)
CATS = {'550': 'Art', '20081': 'Antiques', '870': 'Pottery & Glass', '281': 'Jewelry & Watches', '625': 'Cameras & Photo',
        '1': 'Collectibles', '619': 'Musical Instruments', '13877': 'Militaria', '64482': 'Sports Mem'}
OUT = os.path.join(ROOT, 'research', 'pools', 'ebay-latest.json')

def pool(hours=24):
    import ebay_api
    end = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=hours)).strftime('%Y-%m-%dT%H:%M:%SZ')
    rows, seen = [], set()
    for cid, name in CATS.items():
        for off in range(0, 10000, 200):
            d = ebay_api._get('browse', '/buy/browse/v1/item_summary/search', {
                'category_ids': cid, 'limit': 200, 'offset': off, 'sort': 'endingSoonest',
                'filter': f'buyingOptions:{{AUCTION}},price:[..200],priceCurrency:USD,itemEndDate:[..{end}],itemLocationCountry:US'})
            items = (d or {}).get('itemSummaries') or []
            for it in items:
                iid = it.get('itemId')
                if iid in seen: continue
                seen.add(iid)
                fb = (it.get('seller') or {}).get('feedbackScore')
                bids = it.get('bidCount') or 0
                if fb is None or fb > 150 or bids > 3: continue          # casual sellers, few bidders
                img = (it.get('image') or {}).get('imageUrl') or ''
                rows.append({'id': iid, 't': it.get('title', '')[:90], 'p': float(((it.get('currentBidPrice') or it.get('price') or {}).get('value')) or 0),
                             'b': bids, 'fb': fb, 'end': it.get('itemEndDate'), 'img': img, 'url': it.get('itemWebUrl', '').split('?')[0], 'c': name})
            if len(items) < 200: break
            time.sleep(0.5)
        print(name, len(rows))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump({'made': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'hours': hours, 'rows': rows}, open(OUT, 'w'), separators=(',', ':'))
    print('ebay pool', len(rows), 'auctions (feedback <=150, <=3 bids, <=$200, ending within', hours, 'h)')

def sheetpool():
    P = json.load(open(OUT)); run = 'ebay-' + P['made'][:16].replace(':', '').replace('-', '').replace('T', '-')
    out = [{'pid': 'ebay' + r['id'].split('|')[1] if '|' in r['id'] else 'ebay' + r['id'], 'source': 'ebay', 'price': r['p'], 'title': r['t'],
            'thumb': r['img'].replace('s-l1600', 's-l225'), 'imgs': [r['img']], 'url': r['url'], 'cat': r['c'], 'area': f"fb {r['fb']}",
            'region': 'eBay', 'posted': 0, 'ends': r['end'], 'bids': r['b']} for r in P['rows'] if r['img']]
    d = f'/tmp/eye/{run}'; os.makedirs(d + '/th', exist_ok=True); json.dump(out, open(d + '/pool.json', 'w'))
    print(run, len(out))

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == 'pool': pool(float(a[1]) if len(a) > 1 else 24)
    elif a[0] == 'sheetpool': sheetpool()
