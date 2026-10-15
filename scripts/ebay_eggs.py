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
# All eBay US top-level categories, for listing one seller's items (Browse search needs a category or keyword).
SELLER_CATS = ['20081', '550', '2984', '267', '12576', '625', '15032', '11450', '11116', '1', '58058', '293', '14339', '237',
               '45100', '26395', '11700', '281', '11232', '11233', '619', '1281', '870', '888', '64482', '260', '220', '3252',
               '1249', '99', '6000']

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

def detail():
    """Full description + every photo for research/pools/ebay-flagged.json (Browse getItem) -> ebay-detail.json."""
    import ebay_api, re, html
    F = json.load(open(os.path.join(ROOT, 'research', 'pools', 'ebay-flagged.json'))); out = {}
    for r in F:
        d = ebay_api._get('browse', f"/buy/browse/v1/item/v1|{r['id']}|0", {}) or {}
        desc = html.unescape(re.sub(r'<[^>]+>', ' ', d.get('description') or '')); desc = re.sub(r'\s+', ' ', desc).strip()[:3000]
        imgs = [(d.get('image') or {}).get('imageUrl')] + [i.get('imageUrl') for i in d.get('additionalImages') or []]
        out[r['id']] = {'title': d.get('title'), 'desc': desc, 'imgs': [i for i in imgs if i], 'bid': (d.get('currentBidPrice') or {}).get('value'),
                        'bids': d.get('bidCount'), 'end': d.get('itemEndDate'), 'ship': [(o.get('shippingCost') or {}).get('value') for o in d.get('shippingOptions') or []],
                        'loc': (d.get('itemLocation') or {}).get('stateOrProvince'), 'cond': d.get('condition'), 'err': d.get('error')}
        time.sleep(0.4)
    # Seller's other listings (Oct 15 2026): ids in research/pools/ebay-seller-req.json -> out['_seller_items'][id].
    # Stored inside ebay-detail.json because the workflow only commits that file. The seller username is used only
    # in the API filter and never written (public repo).
    rq = os.path.join(ROOT, 'research', 'pools', 'ebay-seller-req.json')
    if os.path.exists(rq):
        out['_seller_items'] = {}
        for iid in json.load(open(rq)):
            d = ebay_api._get('browse', f"/buy/browse/v1/item/v1|{iid}|0", {}) or {}
            user = (d.get('seller') or {}).get('username')
            if not user: out['_seller_items'][iid] = {'err': d.get('error') or 'no seller'}; continue
            rows, seen = [], set()
            for cid in SELLER_CATS:
                r = ebay_api._get('browse', '/buy/browse/v1/item_summary/search',
                                  {'category_ids': cid, 'limit': 200, 'filter': f'sellers:{{{user}}}'}) or {}
                for it in r.get('itemSummaries') or []:
                    if it['itemId'] in seen: continue
                    seen.add(it['itemId'])
                    rows.append({'id': it['itemId'].split('|')[1] if '|' in it['itemId'] else it['itemId'], 't': it.get('title'),
                                 'p': ((it.get('currentBidPrice') or it.get('price') or {}).get('value')), 'b': it.get('bidCount'),
                                 'opt': it.get('buyingOptions'), 'end': it.get('itemEndDate'), 'cat': cid,
                                 'img': (it.get('image') or {}).get('imageUrl'), 'url': (it.get('itemWebUrl') or '').split('?')[0]})
                time.sleep(0.3)
            out['_seller_items'][iid] = {'fb': (d.get('seller') or {}).get('feedbackScore'), 'n': len(rows), 'rows': rows}
            print('seller of', iid, len(rows), 'active items')
    json.dump(out, open(os.path.join(ROOT, 'research', 'pools', 'ebay-detail.json'), 'w'), indent=0)
    print('details', len(out))

def flags(run):
    """/tmp/eye/<run>/flags_*.tsv (eye agents) -> research/pools/ebay-flagged.json for the detail run."""
    import glob, re
    d = f'/tmp/eye/{run}'; idx = json.load(open(d + '/index.json')); rows = []
    for f in sorted(glob.glob(d + '/flags_*.tsv')):
        for l in open(f):
            m = re.match(r'^(\d+)\t([A-Ja-j]\d+)\t?(.*)$', l.rstrip('\n'))
            r = m and idx.get(f'{int(m.group(1))}:{m.group(2).upper()}')
            if r: rows.append({'id': r['pid'][4:], 'title': r['title'], 'bid': r['price'], 'bids': r['bids'], 'ends': r['ends'],
                               'url': r['url'], 'img': r['imgs'][0], 'eye': m.group(3), 'fb': r['area']})
    json.dump(rows, open(os.path.join(ROOT, 'research', 'pools', 'ebay-flagged.json'), 'w'), indent=0)
    print(len(rows), 'flags -> research/pools/ebay-flagged.json')

def sheetpool():
    P = json.load(open(OUT)); run = 'ebay-' + P['made'][:16].replace(':', '').replace('-', '').replace('T', '-')
    out = [{'pid': 'ebay' + r['id'].split('|')[1] if '|' in r['id'] else 'ebay' + r['id'], 'source': 'ebay', 'price': r['p'], 'title': r['t'],
            'thumb': r['img'].replace('s-l1600', 's-l225'), 'imgs': [r['img']], 'url': r['url'], 'cat': r['c'], 'area': f"fb {r['fb']}",
            'region': 'eBay', 'posted': 0, 'ends': r['end'], 'bids': r['b']} for r in P['rows'] if r['img'] and r['c'] != 'Sports Mem']
    # Skip auctions already screened in an earlier run (pools overlap; ids kept until their auction ends).
    sp = os.path.join(ROOT, 'research', 'pools', 'ebay-screened.json')
    seen = json.load(open(sp)) if os.path.exists(sp) else {}
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    seen = {k: v for k, v in seen.items() if (v or '') > now[:19]}
    out = [r for r in out if r['pid'] not in seen]
    # Drop auctions already ended or ending within 30 min — nothing can be done with them (Oct 15: a stale pool
    # screened 3,573 auctions that had all ended).
    soon = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)).isoformat()[:19]
    out = [r for r in out if (r.get('ends') or '9')[:19] > soon]
    for r in out: seen[r['pid']] = (r.get('ends') or '')[:19]
    json.dump(seen, open(sp, 'w'), separators=(',', ':'))
    d = f'/tmp/eye/{run}'; os.makedirs(d + '/th', exist_ok=True); json.dump(out, open(d + '/pool.json', 'w'))
    print(run, len(out), 'new to screen (research/pools/ebay-screened.json updated — commit it)')

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == 'pool': pool(float(a[1]) if len(a) > 1 else 24)
    elif a[0] == 'sheetpool': sheetpool()
    elif a[0] == 'detail': detail()
    elif a[0] == 'flags': flags(a[1])
    elif a[0] == 'flags': flags(a[1])
