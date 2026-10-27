#!/usr/bin/env python3
"""Free shortlist (Oct 21 2026, low-usage mode). Runs in GitHub Actions — no Claude usage.

Turns the full eBay + ShopGoodwill pools (~30k listings a day) into a ranked shortlist of ~700 photos per run that a
Claude eye then looks at with the encyclopedia in hand. Everything here is free compute.

  python3 scripts/shortlist.py [--n 700] [--sgw-hours 14] [--ebay-hours 30] [--no-sgw] [--limit 0]

Pipeline
  1. POOLS   research/pools/ebay-latest.json (written by the ebay-eggs workflow) + a fresh ShopGoodwill harvest.
  2. DEDUPE  skip anything already shortlisted (research/pools/shown.json, kept 12 days).
  3. TEXT    hard drops: over the money rule, >3 bids, new / sealed / cards / ACEO / OOAK / AI art / licensed characters,
             and titles that already NAME a maker from research/makers.json (the seller knows — no arbitrage).
             Soft score `ign` = how little the title says (vague words, short title, cheap, 0 bids).
  4. IMAGE   CLIP ViT-B-32 on the first photo:
             egg  = collector-object look (clip_rank POSITIVE − NEGATIVE prompts)
             type = zero-shot match against all 663 encyclopedia types; tval = Σ p(type)·log10(top-tier $ of type)
  5. RANK    z(egg) + 0.8·z(tval) + 0.5·z(ign) + 0.7·z(dv); dv = labelled-down (title calls it the cheap version:
             copy, costume, plated, print, resin, souvenir…) × the matched type's log(top/low) spread. Keep the best --n,
             split across sources by pool size (min 25%), 30% of each reserved for labelled-down rows.
  6. DETAIL  every shortlisted row gets all photos + description (eBay getItem needs the EBAY_* secrets).
  7. WRITE   research/pools/shortlist.json — rows carry their top-3 encyclopedia types so the eye agent gets the
             right entries' money tells for each cell (scripts/lowuse.py).
"""
import os, sys, re, io, json, glob, math, time, argparse, datetime as dt, urllib.request, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
POOLS = os.path.join(ROOT, 'research', 'pools')
SHOWN = os.path.join(POOLS, 'shown.json')
OUT = os.path.join(POOLS, 'shortlist.json')

# Hard drops: modern retail, cards, mass-market art, licensed characters. NOT cheap-sounding labels — those are the hunt.
JUNK = re.compile(r'\b(new with tags|nwt|nib|brand new|sealed|factory sealed|funko|lego|psa|bgs|sgc|beckett|topps|panini|'
                  r'upper deck|rookie|trading card|aceo|ooak|original acrylic|acrylic painting|abstract|giclee|canvas art|'
                  r'wall art|wall decor|ai art|print on demand|poster print|dropship|wholesale|lot of \d{2,} new|'
                  r'stainless steel|toy story|disney|star wars|marvel|pokemon|nfl|nba|mlb)\b', re.I)
# Labelled DOWN (Dylan, Oct 21 2026): the seller calls it the cheaper version — copy, costume, plated, print, resin, tourist —
# while the photo may show the real, expensive one. Kept, boosted, and given a reserved share of the shortlist.
DOWN = re.compile(r'\b(reproductions?|repro|replica|copy|style of|in the style|inspired|imitation|faux|fake|knock ?off|'
                  r'costume|fashion jewelry|simulated|cz|cubic zirconia|rhinestones?|paste|glass beads?|plastic|resin|composition|'
                  r'silver ?tone|gold ?tone|silver ?plated?|gold ?plated?|plated|electroplate|epns|brass|pot metal|white metal|'
                  r'spelter|base metal|alloy|tin|print|poster|reprint|decor|decorator|decorative|souvenir|tourist|craft|'
                  r'homemade|home made|hobby|student|kitsch|unbranded|no name|generic|mass produced|made in (?:china|taiwan|'
                  r'hong kong|japan|occupied japan)|occupied japan|cheap|style)\b', re.I)   # 'style' (Oct 27 2026 misses: "vintage style" clarinet $251, "Palais Royal style" $300)
JEWELRY_SHARE = 0.35
JEWELRY = re.compile(r'(jewel|ring|necklace|bracelet|brooch|pendant|cufflink|earring|hallmark|-marks\b|precious-metal|silver|gold|'
                     r'watch|bead|scarab|cameo|charm|locket|chain)', re.I)
def is_jewelry(r):
    """True when the row's best CLIP type is in the jewelry/metal-marks family (title words count too)."""
    t = (r.get('types') or [[None]])[0]; s = t[0] if isinstance(t, (list, tuple)) else t
    return bool(s and JEWELRY.search(s)) or bool(re.search(r'\b(ring|necklace|bracelet|brooch|pendant|earrings?|cufflinks?|chain|bangle)\b', r['t'], re.I))
VAGUE = re.compile(r'\b(old|vintage|antique|unknown|unmarked|mystery|estate|signed|marked|hallmarked?|stamped|unsigned|'
                   r'hand ?made|handcrafted|primitive|folk|carved|bronze|brass|silver|sterling|gold|jade|bone|horn|ivory|'
                   r'painting|drawing|etching|engraving|lithograph|woodblock|watercolou?r|oil on|print|sketch|'
                   r'pottery|stoneware|porcelain|glass|vase|bowl|figure|figurine|statue|sculpture|box|lot|junk drawer|'
                   r'grandma|grandpa|attic|barn find|found|as is|untested|tribal|asian|chinese|japanese|native|ethnic|'
                   r'mid ?century|mcm|deco|nouveau|victorian|primitive|religious|icon|military|medal|pin|badge|coin|'
                   r'watch|pocket watch|camera|lens|knife|tool|instrument|scientific)\b', re.I)

def load_makers():
    """Maker names from research/makers.json (markdown fragments) -> regex of distinctive names (>=5 letters)."""
    try: raw = json.load(open(os.path.join(ROOT, 'research', 'makers.json')))
    except Exception: return None
    names = set()
    for m in raw:
        s = re.sub(r'[*"“”`]', '', str(m)).strip(' :-–.').lower()
        s = re.split(r'[(:,/]', s)[0].strip()
        if 5 <= len(s) <= 40 and re.fullmatch(r"[a-z][a-z .&'\-]+", s) and len(s.split()) <= 4: names.add(s)
    # common words that slipped in as "makers" would drop good titles; keep only names that are not plain English
    common = {'sterling', 'silver', 'vintage', 'antique', 'bronze', 'brass', 'glass', 'pottery', 'signed', 'marked', 'china',
              'japan', 'germany', 'england', 'france', 'italy', 'mexico', 'western', 'pacific', 'american', 'national',
              'royal', 'crown', 'union', 'eagle', 'standard', 'victoria', 'imperial', 'gold', 'made in', 'handmade', 'studio',
              'original', 'limited', 'company', 'stamped', 'pewter', 'enamel', 'knives', 'rooster', 'cloisonne', 'majolica', 'ironstone', 'jadeite', 'sheffield', 'bohemian', 'bohemia', 'native', 'navajo'}
    try:
        from wordfreq import zipf_frequency as zf      # drop plain English words that slipped into the maker list
        names = {n for n in names if not all(zf(w, 'en') >= 4.0 for w in n.split())}
    except ImportError: pass
    names = sorted((n for n in names if n not in common), key=len, reverse=True)
    return re.compile(r'\b(' + '|'.join(re.escape(n) for n in names) + r')\b', re.I) if names else None

def ign_score(t, p, b):
    s = 1.0 * len(VAGUE.findall(t))
    s += 1.5 if len(t) < 35 else 0.7 if len(t) < 55 else 0
    s += 1.0 if p <= 15 else 0.5 if p <= 40 else 0
    return s - 0.7 * b

def load_ebay(hours):
    p = os.path.join(POOLS, 'ebay-latest.json')
    if not os.path.exists(p): return []
    now = dt.datetime.now(dt.timezone.utc); lim = now + dt.timedelta(hours=hours)
    # newly listed auctions (any end date) are kept so each is screened on day 1; shown.json stops repeats
    out = []
    for x in json.load(open(p)).get('rows', []):
        try: end = dt.datetime.fromisoformat(x['end'].replace('Z', '+00:00'))
        except Exception: continue
        if end <= now or (end > lim and x.get('via') != 'newlyListed'): continue
        out.append({'src': 'ebay', 'id': 'eb' + x['id'].split('|')[1], 't': x['t'], 'p': x['p'], 'b': x['b'], 'end': x['end'],
                    'img': x['img'].replace('s-l225', 's-l500'), 'url': x['url'], 'c': x.get('c', ''), 'fb': x.get('fb')})
    return out

def load_sgw(hours):
    import sgw
    before = set(glob.glob('/tmp/eye/sgw-*'))
    sgw.harvest(hours, first=True)
    new = sorted(set(glob.glob('/tmp/eye/sgw-*')) - before) or sorted(glob.glob('/tmp/eye/sgw-*'))
    if not new: return []
    out = []
    for x in json.load(open(os.path.join(new[-1], 'pool.json'))):
        out.append({'src': 'sgw', 'id': x['pid'], 't': x['title'], 'p': x['price'], 'b': x['bids'], 'end': x['ends'],
                    'img': x['thumb'], 'url': x['url'], 'c': x.get('cat', '')})
    return out

def text_pass(rows, shown, makers):
    keep, why = [], {}
    for r in rows:
        k = None
        if r['id'] in shown: k = 'shown'
        elif r['p'] > 200 or r['b'] > 3: k = 'price/bids'
        elif r['c'] == 'Sports Mem' and re.search(r'\b(card|auto|autograph|jersey|signed)\b', r['t'], re.I): k = 'sports'
        elif r.get('melt', {}).get('ok'): k = None          # metal floor clears the money rule: keep whatever it is
        elif JUNK.search(r['t']): k = 'junk'
        elif makers and makers.search(r['t']): k = 'maker named'
        why[k] = why.get(k, 0) + 1
        if not k:
            r['ign'] = ign_score(r['t'], r['p'], r['b'])
            r['down'] = sorted(set(m.lower() for m in DOWN.findall(r['t'])))[:4]
            keep.append(r)
    return keep, why

class Clip:
    def __init__(self, digest):
        import torch, open_clip
        from clip_rank import POSITIVE, NEGATIVE
        self.torch = torch
        self.m, _, self.prep = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
        self.m.eval(); tok = open_clip.get_tokenizer('ViT-B-32')
        self.slugs = list(digest)
        self.logv = torch.tensor([math.log10(max(digest[s]['top'], 10)) for s in self.slugs])
        # spread = top tier / low tier: how far a type's money version sits above its common one (hard-to-tell types)
        self.logs = torch.tensor([math.log10(max(digest[s]['top'], 10) / max(digest[s]['low'] or 10, 1)) for s in self.slugs])
        with torch.no_grad():
            pn = self._txt(tok, POSITIVE + NEGATIVE); self.pos, self.neg = pn[:len(POSITIVE)], pn[len(POSITIVE):]
            # one embedding per type = mean of "a photo of <title>" and up to 3 aliases
            embs = []
            for s in self.slugs:
                e = digest[s]; ps = [f"a photo of {e['title']}"] + [f'a photo of {a}' for a in e['aliases'][:3] if a]
                v = self._txt(tok, ps).mean(0); embs.append(v / v.norm())
            self.types = torch.stack(embs)

    def _txt(self, tok, ps):
        t = self.m.encode_text(tok(ps)); return t / t.norm(dim=-1, keepdim=True)

    def text(self, prompts):
        import open_clip
        with self.torch.no_grad(): return self._txt(open_clip.get_tokenizer('ViT-B-32'), prompts)

    def embed_urls(self, urls, batch=64, threads=32):
        """Unit image embeddings (float16 tensors) for a list of image URLs; None where the download failed."""
        torch = self.torch
        def get(u):
            try:
                from PIL import Image
                b = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read()
                return self.prep(Image.open(io.BytesIO(b)).convert('RGB'))
            except Exception: return None
        out = [None] * len(urls)
        with cf.ThreadPoolExecutor(threads) as ex:
            for i in range(0, len(urls), batch * 4):
                ims = list(ex.map(get, urls[i:i + batch * 4]))
                ok = [(i + k, im) for k, im in enumerate(ims) if im is not None]
                for j in range(0, len(ok), batch):
                    part = ok[j:j + batch]
                    with torch.no_grad():
                        e = self.m.encode_image(torch.stack([im for _, im in part])); e = e / e.norm(dim=-1, keepdim=True)
                    for (k, _), v in zip(part, e): out[k] = v.half()
                if i % (batch * 40) == 0: print(f'  embed {min(i + batch * 4, len(urls))}/{len(urls)}', flush=True)
        return out

    def run(self, rows, batch=64, threads=32):
        torch = self.torch
        def get(r):
            try:
                from PIL import Image
                b = urllib.request.urlopen(urllib.request.Request(r['img'], headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read()
                return self.prep(Image.open(io.BytesIO(b)).convert('RGB'))
            except Exception: return None
        with cf.ThreadPoolExecutor(threads) as ex:
            for i in range(0, len(rows), batch * 4):
                chunk = rows[i:i + batch * 4]; ims = list(ex.map(get, chunk))
                ok = [(r, im) for r, im in zip(chunk, ims) if im is not None]
                for j in range(0, len(ok), batch):
                    part = ok[j:j + batch]
                    with torch.no_grad():
                        e = self.m.encode_image(torch.stack([im for _, im in part])); e = e / e.norm(dim=-1, keepdim=True)
                        pos = (e @ self.pos.T).topk(3, dim=1).values.mean(1); neg = (e @ self.neg.T).topk(3, dim=1).values.mean(1)
                        pt = (100 * e @ self.types.T).softmax(dim=1); top = pt.topk(3, dim=1)
                        tval = (pt * self.logv).sum(1); tspr = (pt * self.logs).sum(1)
                    for k, (r, _) in enumerate(part):
                        r['egg'] = round(float(pos[k] - neg[k]) * 100, 2); r['tval'] = round(float(tval[k]), 3)
                        r['spread'] = round(float(tspr[k]), 3)
                        r['types'] = [[self.slugs[int(top.indices[k, q])], round(float(top.values[k, q]), 3)] for q in range(3)]
                        r['_e'] = e[k].half()
                if i % (batch * 40) == 0: print(f'  clip {i + len(chunk)}/{len(rows)}', flush=True)
        return [r for r in rows if 'egg' in r]

def details(rows, threads=6):
    """Full photos + description for every shortlisted row (free: eBay Browse getItem / ShopGoodwill API), so a
    Claude session can zoom on a flag without dispatching another workflow. Stored on the row as r['det']."""
    import html
    def eb(r):
        import ebay_api
        d = ebay_api._get('browse', f"/buy/browse/v1/item/v1|{r['id'][2:]}|0", {}) or {}
        if d.get('error') or not d.get('itemId'): return None
        desc = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', d.get('description') or ''))).strip()[:1200]
        imgs = [(d.get('image') or {}).get('imageUrl')] + [i.get('imageUrl') for i in d.get('additionalImages') or []]
        asp = {a.get('name'): a.get('value') for a in d.get('localizedAspects') or [] if a.get('name')}
        return {'imgs': [i for i in imgs if i][:16], 'desc': desc, 'aspects': dict(list(asp.items())[:12]),
                'ship': [(o.get('shippingCost') or {}).get('value') for o in d.get('shippingOptions') or []][:2],
                'loc': (d.get('itemLocation') or {}).get('stateOrProvince'), 'cond': d.get('condition')}
    def sg(r):
        import sgw
        d, desc, imgs = sgw._detail(r['id'])
        return {'imgs': imgs[:16], 'desc': re.sub(r'\s+', ' ', desc)[:1200], 'weight': d.get('displayWeight'),
                'ship': d.get('shippingPrice')}
    def one(r):
        for t in range(3):
            try: return (eb if r['src'] == 'ebay' else sg)(r)
            except Exception: time.sleep(2 + 3 * t)
    have_eb = bool(os.environ.get('EBAY_CLIENT_ID'))
    todo = [r for r in rows if r['src'] == 'sgw' or have_eb]
    with cf.ThreadPoolExecutor(threads) as ex:
        for r, d in zip(todo, ex.map(one, todo)):
            if d: r['det'] = d
    for src in ('ebay', 'sgw'):
        n = sum(r['src'] == src for r in rows); k = sum(r['src'] == src and 'det' in r for r in rows)
        print(f'details {src} {k} of {n}', flush=True)
        if n and k < n // 2: print(f'::warning::{src} details only {k} of {n} (EBAY_* set: {have_eb})', flush=True)

def z(xs):
    m = sum(xs) / len(xs); sd = (sum((x - m) ** 2 for x in xs) / len(xs)) ** 0.5 or 1
    return [(x - m) / sd for x in xs]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=700); ap.add_argument('--sgw-hours', type=float, default=14)
    ap.add_argument('--ebay-hours', type=float, default=30); ap.add_argument('--no-sgw', action='store_true')
    ap.add_argument('--no-details', action='store_true'); ap.add_argument('--no-knn', action='store_true')
    ap.add_argument('--no-ocr', action='store_true')
    ap.add_argument('--limit', type=int, default=0, help='test: cap rows per source before CLIP')
    a = ap.parse_args(); t0 = time.time()
    from enc_digest import build
    digest = {k: v for k, v in build().items() if v['top']}
    shown = json.load(open(SHOWN)) if os.path.exists(SHOWN) else {}
    cut = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=12)).isoformat()   # eBay auctions run up to 10 days
    shown = {k: v for k, v in shown.items() if v >= cut}
    rows = load_ebay(a.ebay_hours) + ([] if a.no_sgw else load_sgw(a.sgw_hours))
    pool = {s: sum(r['src'] == s for r in rows) for s in ('ebay', 'sgw')}
    import melt
    if melt.stale_days() > 10: print(f'::warning::research/spot.json is {melt.stale_days()} days old — update spot prices', flush=True)
    for r in rows:
        m = melt.floor(r['t'], r['p'])
        if m: r['melt'] = m
    makers = load_makers()
    rows, why = text_pass(rows, shown, makers)
    print('melt floor clears the money rule (title only):', sum(1 for r in rows if r.get('melt', {}).get('ok')), flush=True)
    print('pool', pool, '| text drops', why, '| to CLIP', len(rows), flush=True)
    if a.limit:
        rows = [r for s in ('ebay', 'sgw') for r in sorted((r for r in rows if r['src'] == s), key=lambda r: -r['ign'])[:a.limit]]
    clip = Clip(digest)
    rows = clip.run(rows)
    if not rows: print('nothing scored'); return
    if not a.no_knn:
        import knn
        try: knn.add(clip); knn.query(rows)
        except Exception as ex: print('::warning::knn failed:', ex, flush=True)
    # similar-sold value: log10(look-alikes' median SGW final / price) — 0 when fewer than 3 close look-alikes
    for r in rows:
        k = r.get('knn'); r['kv'] = math.log10(max(k['p50'], 1) / max(r['p'], 5)) if k else 0
    # labelled-down value: cheap label × how big the type's money/common gap is (only counts when a cheap word is present)
    for r in rows: r['dv'] = (1 + 0.5 * (len(r['down']) - 1)) * r['spread'] if r['down'] else 0
    for r, ze, zt, zi, zd in zip(rows, z([r['egg'] for r in rows]), z([r['tval'] for r in rows]), z([r['ign'] for r in rows]),
                                 z([r['dv'] for r in rows])):
        # Oct 27 2026 re-fit on 2,107 rows with finals: CLIP 'egg' look is INVERTED (top quartile 7% of lots ≥ $100 vs 19%
        # in the bottom quartile), type value is the only photo signal that helps (19% vs 9%), labelled-down rows sold
        # for a median $15 vs $35 for the rest (5% vs 30% ≥ $100). So egg weight 0, type value up, down kept only as a flag.
        r['score'] = round(0.0 * ze + 1.2 * zt + 0.5 * zi + 0.3 * zd, 3)
    for r, zk in zip(rows, z([r['kv'] for r in rows])): r['score'] = round(r['score'] + 0.8 * zk, 3)
    tot = sum(pool.values()) or 1
    quota = {s: max(int(a.n * 0.25), int(a.n * pool[s] / tot)) for s in pool if pool[s]}
    pick = []
    # Oct 27 2026: the jewelry/marks family took 807 of 1,147 eye slots and every flag was a melt play the free melt
    # line had already found. Cap the family at JEWELRY_SHARE of each source's quota; melt-ok rows are a separate lane
    # (shortlist['melt']) and never spend eye slots.
    for s, q in quota.items():
        mine = sorted((r for r in rows if r['src'] == s and not r.get('melt', {}).get('ok')), key=lambda r: -r['score'])
        def take(cands, n):
            out, jew, cap = [], 0, int(n * JEWELRY_SHARE)
            for r in cands:
                if len(out) >= n: break
                j = is_jewelry(r)
                if j and jew >= cap: continue
                out.append(r); jew += j
            return out
        # reserve 30% of each source's quota for labelled-down rows (best by score), then fill by score
        down = take([r for r in mine if r['down']], int(q * 0.1)); ids = {r['id'] for r in down}   # was 0.3; see re-fit note above
        pick += down + take([r for r in mine if r['id'] not in ids], q - len(down))
    have = {r['id'] for r in pick}
    melt_rows = [r for r in rows if r.get('melt', {}).get('ok') and r['id'] not in have]   # melt lane: decided by free compute
    for r in melt_rows: r['lane'] = 'melt'
    pick += melt_rows
    if not a.no_details: details(pick)
    if not a.no_ocr and not a.no_details:
        import ocr
        try: ocr.run(pick, clip, makers)
        except Exception as ex: print('::warning::ocr failed:', ex, flush=True)
    for r in pick:                       # second melt pass: description, aspects and the photographed mark
        det = r.get('det') or {}
        txt = ' '.join([r['t'], det.get('desc') or '', ' '.join(f'{k} {v}' for k, v in (det.get('aspects') or {}).items())])
        m = melt.floor(txt, r['p'], (r.get('ocr') or {}).get('text', ''))
        # the full text (title + description + aspects + photographed mark) is a superset of the title, so its answer
        # always wins — including a downgrade (Oct 27 2026: "14K ... 14.6g" whose description said "vermeil over
        # sterling" kept the title's $758 gold floor and cost an eye flag + deep review)
        if m: r['melt'] = m
        else: r.pop('melt', None)
        o = r.get('ocr') or {}
        r['score'] = round(r['score'] + (1.5 if o.get('makers') else 0) + (0.5 if o.get('metal') and not melt.purity(r['t']) else 0)
                           + (3 if r.get('melt', {}).get('ok') else 0), 3)
        r.pop('_e', None)
    # the description pass can create or remove melt rows: re-split the lanes on the final answer
    for r in pick: r['lane'] = 'melt' if r.get('melt', {}).get('ok') else 'eye'
    pick.sort(key=lambda r: -r['score'])
    print('melt leads:', sum(1 for r in pick if r.get('melt', {}).get('ok')), '| photo maker not in title:',
          sum(1 for r in pick if (r.get('ocr') or {}).get('makers')), flush=True)
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    for r in pick: shown[r['id']] = now
    json.dump(shown, open(SHOWN, 'w'))
    eye_rows = [r for r in pick if r['lane'] == 'eye']; melt_lane = [r for r in pick if r['lane'] == 'melt']
    print('eye rows:', len(eye_rows), '(jewelry family', sum(is_jewelry(r) for r in eye_rows), ') | melt lane:', len(melt_lane), flush=True)
    json.dump({'made': now, 'pool': pool, 'text_drops': why, 'scored': len(rows), 'rows': eye_rows, 'melt': melt_lane}, open(OUT, 'w'), ensure_ascii=False)
    print(f'shortlist {len(pick)} ({quota}) -> {OUT} in {time.time() - t0:.0f}s')

if __name__ == '__main__':
    main()
