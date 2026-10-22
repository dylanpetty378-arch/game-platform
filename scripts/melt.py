#!/usr/bin/env python3
"""Melt floor (Oct 22 2026): the price a refiner pays for the metal alone — the one value that needs no expertise.

A stated weight + a stated (or photographed) purity gives a floor: grams × purity × spot × payout. If the listing
price is far enough under that floor, the item is a lead whatever it is, and anything it is beyond metal is upside.

  python3 scripts/melt.py "<title or text>" [price]     # test the parser on one listing

Spot prices live in research/spot.json (update weekly; the workflow warns when older than 10 days).
Payout: refiners pay ~85% of melt for gold and ~70% for sterling after fees — deliberately conservative.
Excluded on purpose: plated / filled / tone / vermeil gold, silverplate, nickel / German / Tibetan "silver",
weighted sterling (cement-filled candlesticks), gauges (body jewelry "14g"), platinum (no spot kept).
Stones inflate gram weight: with stone words present only 80% of the weight is counted as metal.
"""
import os, re, json, sys, datetime as dt
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPOT = os.path.join(ROOT, 'research', 'spot.json')
TROY = 31.1035
PAYOUT = {'gold': 0.85, 'silver': 0.70}
SHIP = 5                      # small padded envelope

GOLD = [(re.compile(r'\b24 ?k(?:t|arat)?\b|\b999\.?9?\b(?=.*gold)', re.I), 0.999, '24k'),
        (re.compile(r'\b22 ?k(?:t|arat)?\b|\b916\b', re.I), 0.916, '22k'),
        (re.compile(r'\b18 ?k(?:t|arat)?\b|\b750\b', re.I), 0.750, '18k'),
        (re.compile(r'\b14 ?k(?:t|arat|p)?\b|\b585\b', re.I), 0.585, '14k'),
        (re.compile(r'\b10 ?k(?:t|arat)?\b|\b417\b', re.I), 0.417, '10k'),
        (re.compile(r'\b9 ?k(?:t|arat)?\b|\b375\b', re.I), 0.375, '9k')]
SILVER = [(re.compile(r'\b(?:fine silver|\.?999 silver|silver \.?999)\b', re.I), 0.999, '999'),
          (re.compile(r'\b(?:sterling|925|\.925|ster)\b', re.I), 0.925, 'sterling'),
          (re.compile(r'\b(?:coin silver|900 silver|silver 900)\b', re.I), 0.900, '900'),
          (re.compile(r'\b(?:800 silver|silver 800|835|830)\b', re.I), 0.800, '800')]
NOT_GOLD = re.compile(r'\b(plated?|plating|gold ?tone|filled|gf|g\.f\.|1/20|1/10|rolled gold|rgp|hge|hgp|gep|vermeil|'
                      r'over (?:sterling|silver|925)|electroplated?|clad|wash|layered|bonded|gold color|goldtone|ep)\b', re.I)
NOT_SILVER = re.compile(r'\b(silver ?plated?|silverplate|silver ?tone|epns|ep ?ns|nickel silver|german silver|alpaca|'
                        r'tibet(?:an)? silver|tibet silver|plated|silver color|silvertone|mexican silver plate|'
                        r'weighted|reinforced|cement)\b', re.I)
SKIP = re.compile(r'\b(gauge|barbell|septum|nose ring|tragus|helix|belly ring|labret|ctw?\b.*\bg\b)', re.I)
STONES = re.compile(r'\b(diamonds?|turquoise|stones?|cz|cubic|opal|pearls?|jade|garnet|amethyst|onyx|coral|sapphire|ruby|'
                    r'emerald|topaz|crystal|gem|cabochon|inlay|lapis|malachite|beads?)\b', re.I)
WEIGHT = re.compile(r'(?<![\w.])(\d{1,4}(?:\.\d{1,2})?)\s*(grams?|gr|gms?|g|dwt|ozt|troy ?oz|oz)(?![a-z])', re.I)

def spot():
    try: s = json.load(open(SPOT))
    except Exception: return None
    s['gold_g'] = s['gold'] / TROY; s['silver_g'] = s['silver'] / TROY
    return s

def stale_days():
    s = spot()
    if not s: return 999
    return (dt.date.today() - dt.date.fromisoformat(s['date'])).days

def grams(text):
    for m in WEIGHT.finditer(text):
        v, u = float(m.group(1)), m.group(2).lower()
        if v <= 0: continue
        if u.startswith('dwt'): return round(v * 1.555, 2)
        if u.startswith('ozt') or u.startswith('troy'): return round(v * TROY, 2)
        if u == 'oz': return round(v * 28.35, 2)       # avoirdupois — conservative vs troy
        return v
    return None

def purity(text):
    """(metal, purity, label) or None. Gold only if nothing says plated/filled; the LOWEST karat named wins."""
    gold = [(p, l) for rx, p, l in GOLD if rx.search(text)]
    if gold and not NOT_GOLD.search(text):
        p, l = min(gold); return ('gold', p, l)
    if NOT_SILVER.search(text): return None
    sil = [(p, l) for rx, p, l in SILVER if rx.search(text)]
    if sil: p, l = min(sil); return ('silver', p, l)
    return None

def floor(text, price, extra_purity_text=''):
    """Melt floor for a listing. text = title (+ description/aspects); extra_purity_text = OCR of the marks.
    Returns dict(metal, label, g, melt, net, max_bid, ok) or None."""
    s = spot()
    if not s or SKIP.search(text): return None
    pu = purity(text) or (purity(extra_purity_text) if extra_purity_text else None)
    g = grams(text)
    if not pu or not g: return None
    metal, p, label = pu
    if metal == 'silver' and g > 3000: return None
    if metal == 'gold' and g > 300: return None       # parse error, or not a casual listing
    gm = g * (0.8 if STONES.search(text) else 1.0)
    melt = gm * p * s[metal + '_g']; net = melt * PAYOUT[metal] - SHIP
    # profit rule (Dylan): profit >= $50 when price < $50, profit >= price above that -> max bid = min(net-50, net/2)
    mx = int(max(0, min(net - 50, net / 2)))
    return {'metal': metal, 'label': label, 'g': g, 'melt': round(melt), 'net': round(net), 'max_bid': mx,
            'ok': mx >= max(price, 1) and net >= 100, 'spot_date': s['date']}

if __name__ == '__main__':
    t = sys.argv[1] if len(sys.argv) > 1 else ''
    print(floor(t, float(sys.argv[2]) if len(sys.argv) > 2 else 0))
