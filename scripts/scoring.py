"""Seller-ignorance score for a Craigslist listing title (shared by lens_prep.py and cloud_cycle.py).

Higher = more likely the seller does not know what the item is (the whole point of the project).
-99 = drop (junk category, out of price range, wanted ads, services, …).
Change the rules here only, and log the change + the reason in docs/improvements.md.
"""
import re
JUNK=re.compile(r'\b(firewood|tires?|rims?|mattress|couch|sofa|sectional|recliner|treadmill|elliptical|refrigerator|washer|dryer|dishwasher|stove|microwave|patio set|hot tub|trailer|mower|snow ?blower|generator|ladder|lumber|pallets?|bricks?|gravel|mulch|dirt|puppies|kittens|chickens|goats|horse|hay|car seat|stroller|crib|free|wanted|iso|looking for|services?|repair|install|cash app|zelle|venmo)\b',re.I)
RESELLER=re.compile(r'\b(authentic|rare|collectible|collectable|nib|nwt|mint|sealed|htf|discontinued|retails?|msrp|worth|value|ebay|firm|obo|no ?lowball|lot of \d+|wholesale|bulk|inventory)\b',re.I)
HELPER=re.compile(r"\b(estate|grandma|grandmother|grandpa|mom's|dad's|inherited|attic|basement|garage|clean ?out|cleanout|moving|downsizing|old|vintage|antique|box of|misc|miscellaneous|stuff|things|assorted|unknown|not sure|don't know|dont know)\b",re.I)
MODEL=re.compile(r'\b[A-Z]{1,4}-?\d{2,5}[A-Z]?\b|\b\d{3,5}[A-Z]{1,3}\b')
# Category priors (from Runs 4-14: finds came from antiques, collectibles, jewelry, cameras, instruments, art, vintage
# tools/fishing; furniture rarely clears Dylan's $750 furniture bar). cloud_cycle.py adds a LEARNED adjustment on top
# from Lens results (see learned_weights) — the priors only matter until there is data.
CAT_PRIOR = {'ata': 2, 'atq': 2, 'cba': 1.5, 'jwa': 1.5, 'art': 1.5, 'pha': 1.5, 'msa': 1.5, 'tag': 1, 'emd': .5,
             'vga': .5, 'spo': .5, 'tls': .5, 'gms': .5, 'clo': 0, 'clt': 0, 'hab': 0, 'ele': 0, 'for': 0, 'hsd': 0,
             'hsh': -.5, 'sys': -.5, 'fua': -1.5, 'bik': -1, 'mpo': -1, 'mob': -1, 'boo': -1.5, 'bop': -1, 'rvs': -2, 'wan': -2}
LEARNED = {}   # filled by cloud_cycle.learned_weights() before scoring

def learned_weights(lens_rows, listings_by_pid, k=150):
    """Per-category adjustment from Lens outcomes: share of lensed listings with a strong signal (match median >= $150
    and >= 3x the asking price), compared with the overall share; shrunk toward 0 until a category has ~k results."""
    tot = {}; hit = {}
    for x in lens_rows:
        c = (listings_by_pid.get(str(x.get('pid'))) or {}).get('cat')
        if not c: continue
        tot[c] = tot.get(c, 0) + 1
        if (x.get('med') or 0) >= 150 and (x.get('ratio') or 0) >= 3: hit[c] = hit.get(c, 0) + 1
    n_all = sum(tot.values()); r_all = (sum(hit.values()) / n_all) if n_all else 0
    out = {}
    for c, n in tot.items():
        if not r_all: break
        rel = (hit.get(c, 0) / n) / r_all            # 1.0 = average category
        adj = max(-2.0, min(2.0, 2.0 * (rel - 1.0)))
        out[c] = round(adj * n / (n + k), 2)         # shrinkage
    return out

def score(r):
    t=r.get('title') or ''; s=0.0
    if JUNK.search(t): return -99
    p=r.get('price')
    if p is None or p<=0 or p>200: return -99
    if not r.get('imgs'): return -99
    w=len(t.split())
    s+= 3 if w<=4 else 2 if w<=7 else 0            # short generic titles
    s+= 2 if HELPER.search(t) else 0                # seller doesn't know what it is
    s-= 3 if RESELLER.search(t) else 0              # seller does know
    s-= 2 if MODEL.search(t) else 0                 # model number = seller already identified it
    s+= 1 if 10<=p<=100 else 0
    s+= 1 if len(r['imgs'])>=3 else 0
    c=r.get('cat'); s+= CAT_PRIOR.get(c,0) + LEARNED.get(c,0)
    return s
