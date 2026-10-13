"""Seller-ignorance score for a Craigslist listing title (shared by lens_prep.py and cloud_cycle.py).

Higher = more likely the seller does not know what the item is (the whole point of the project).
-99 = drop (junk category, out of price range, wanted ads, services, …).
Change the rules here only, and log the change + the reason in docs/improvements.md.
"""
import re
JUNK=re.compile(r'\b(firewood|tires?|rims?|mattress|couch|sofa|sectional|recliner|treadmill|elliptical|refrigerator|washer|dryer|dishwasher|stove|microwave|patio set|hot tub|trailer|mower|snow ?blower|generator|ladder|lumber|pallets?|bricks?|gravel|mulch|dirt|puppies|kittens|chickens|goats|horse|hay|car seat|stroller|crib|free|wanted|iso|looking for|services?|repair|install|cash app|zelle|venmo)\b',re.I)
RESELLER=re.compile(r'\b(authentic|rare|collectible|collectable|nib|nwt|mint|sealed|htf|discontinued|retails?|msrp|worth|value|ebay|firm|no ?lowball|wholesale|bulk|inventory)\b',re.I)
HELPER=re.compile(r"\b(estate|grandma|grandmother|grandpa|mom's|dad's|inherited|attic|basement|garage|clean ?out|cleanout|moving|downsizing|old|vintage|antique|box of|misc|miscellaneous|stuff|things|assorted|unknown|not sure|don't know|dont know)\b",re.I)
MODEL=re.compile(r'\b[A-Z]{1,4}-?\d{2,5}[A-Z]?\b|\b\d{3,5}[A-Z]{1,3}\b')
# Category priors (from Runs 4-14: finds came from antiques, collectibles, jewelry, cameras, instruments, art, vintage
# tools/fishing; furniture rarely clears Dylan's $750 furniture bar). cloud_cycle.py adds a LEARNED adjustment on top
# from review outcomes (see learned_weights) — the priors only matter until there is data.
CAT_PRIOR = {'ata': 2, 'atq': 2, 'cba': 1.5, 'jwa': 1.5, 'art': 1.5, 'pha': 1.5, 'msa': 1.5, 'tag': 1, 'emd': .5,
             'vga': .5, 'spo': .5, 'tls': .5, 'gms': .5, 'clo': 0, 'clt': 0, 'hab': 0, 'ele': 0, 'for': 0, 'hsd': 0,
             'hsh': -.5, 'sys': -.5, 'fua': -1.5, 'bik': -1, 'mpo': -1, 'mob': -1, 'boo': -1.5, 'bop': -1, 'rvs': -2, 'wan': -2}
LEARNED = {}   # filled by cloud_cycle.learned_weights() before scoring

def learned_weights(events, listings_by_pid, k=60):
    """Per-category adjustment from REVIEW outcomes (not Lens medians, which proved to be noise — Oct 13): share of
    reviewed listings that became a lead (decided ask/find, or comps pass) vs the overall share; shrunk toward 0 until a
    category has ~k reviewed listings."""
    cur = {}
    for e in events:
        if e.get('stage') in ('photo_review', 'comps', 'decided'):
            p = str(e['pid']); o = cur.get(p)
            if o is None or (e.get('ts') or '') >= (o.get('ts') or ''): cur[p] = e
    tot = {}; hit = {}
    for p, e in cur.items():
        c = (listings_by_pid.get(p) or {}).get('cat')
        if not c: continue
        tot[c] = tot.get(c, 0) + 1
        good = (e['stage'] == 'decided' and e.get('status') in ('ask', 'find')) or (e['stage'] == 'comps' and e.get('status') == 'pass')
        if good: hit[c] = hit.get(c, 0) + 1
    n_all = sum(tot.values()); r_all = (sum(hit.values()) / n_all) if n_all else 0
    out = {}
    for c, n in tot.items():
        if not r_all: break
        rel = (hit.get(c, 0) / n) / r_all
        adj = max(-2.0, min(2.0, 2.0 * (rel - 1.0)))
        out[c] = round(adj * n / (n + k), 2)
    return out

# SIZE RULE (Dylan, Oct 12 2026): only items that fit in a car's passenger seat (a little bigger at most). Anything bigger
# is not worth the time — excluded outright. Labels agree: furniture words = 120+ kills, 0 keeps in the first 432 reviews.
BULKY=re.compile(r'\b(desk|table(?! ?(lamp|top clock|clock))|chairs?|cabinet|mirror|trunk|chest|dresser|rocker|rocking|bench|bookcase|bookshelf|shelf|shelves|armoire|wardrobe|hutch|buffet|sideboard|credenza|nightstand|headboard|bed ?frame|vanity|stool|ottoman|sewing machine|piano|organ|loveseat|futon|couch|daybed|bunk|wagon wheel|anvil|wood ?stove|pot ?belly|safe|jukebox|arcade|pinball|slot machine|grandfather clock|tall case|hall tree|coat rack|church pew|pew|bathtub|clawfoot|sink|doors?(?! ?(knob|knocker|hardware|stop|plate|bell|handle|pull))|windows?(?! ?(sticker|decal|light))|mantel(?! clock)|fireplace|area rug|rugs? \d+ ?x|\d+ ?x ?\d+ rug|canoe|kayak|boat|motorcycle|scooter|mower|tractor|plow|carriage|buggy|sleigh|crib|cradle|highchair|high chair|rocking horse|room divider|folding screen|china cabinet|curio|display case|showcase|workbench|tool chest|toolbox on wheels|rolling tool|two[- ]man saw|crosscut saw|chandelier|milk can|(?:10|ten)[- ]gallon|pitcher and bowl|wash ?bowl|carpet sweeper|gone with the wind|parlor lamp|banquet lamp|floor lamp|torchiere|miter box|grandmother clock|wall unit|bookshelf|room size|full size|tricycles?|bicycles?|bikes?|sleds?|skis|wheel lot|mannequin|parking meter|butter churn|neon signs?|yield sign|stop sign|street sign|highway sign|floor lamp|pole lamp|swag (?:light|lamp)|coolers?|wood heaters?|heaters?|armchair|nightstands|sewing machines|crocks? jugs?|\d+[- ]gal(?:lon)?|autoharp|parts? bin|computer|amplifier|receiver(?! ?hitch)|turntable|speakers)\b',re.I)

# Small things whose titles contain a bulky word (doll trunk, hand mirror, bench vise, motorcycle jacket, desk lamp…)
SMALL=re.compile(r'\b(hand mirror|compact|vanity (mirror|set|tray|box)|dresser (set|box|tray|jar)|dolls?|doll ?house|dollhouse|miniature|mini|toy|salesman|sample|model|bench (vise|vice|grinder|plane)|vise|vice|helmet|jacket|patch|pin|desk (accessor\w*|lamp|clock|set|organizer|pen|top|calendar)|lap desk|writing (slope|box)|remote|opener|key|keys|knob|hinge|ski rack|rack|jewelry|music box|tea caddy|trinket|box|figurine|ornament|book|books|catalog|manual|brochure|sign|poster|photo|print|postcard|flags?|bells?|machine head|picture|sticker|decal|emblem|badge|plate|spoon|cup|mug|glass|lamp|clock|radio|camera|lens|watch|ring|necklace|bracelet|brooch|earrings)\b',re.I)
# eBay-banned / policy-risk items (research Oct 13: offensive-imagery listings get pulled; ivory banned outright)
POLICY=re.compile(r'\b(blackamoor|mammy|golliwog|golly|sambo|pickaninny|ivory|whale ?bone|scrimshaw|tortoise ?shell|bear claws?|eagle feathers?|coral reef|sea turtle|butterfly knife|balisong|nazi|swastika|ss dagger)\b',re.I)

# Always bulky/heavy even when a SMALL word (sign, lamp, radio…) appears in the title (Oct 13: 95 size-kills slipped through)
HEAVY=re.compile(r'\b(stop sign|yield sign|street sign|highway sign|neon signs?|tricycles?|bicycles?|bikes?|sleds?|floor lamp|pole lamp|computer|amplifier|turntable|speakers|sewing machines?|mannequin|parking meter)\b',re.I)
def is_bulky(t):
    t=t or ''
    return bool(HEAVY.search(t)) or (bool(BULKY.search(t)) and not SMALL.search(t))

# Research tells (Oct 13): hunter-case / jewelled pocket watches and small gold-tone pieces are where solid gold hides
# under "gold tone" titles; owners rarely look inside the case back. Small, cheap to ship, Terapeak-supported.
TELL=re.compile(r'\b(collection|lot|set of \d+|\d+ (?:pieces|pcs)|full bee|goebel|pocket ?watch|hunter case|hunting case|\d{2} jewels?|jewel(?:l)?ed|railroad watch|elgin|waltham|hampden|illinois watch|straight razors?|sterling|\.?925|14k|10k|18k|hallmark(?:ed)?|signed)\b',re.I)

def score(r):
    t=r.get('title') or ''; s=0.0
    if JUNK.search(t) or is_bulky(t) or POLICY.search(t): return -99   # junk, or bigger than a passenger seat
    p=r.get('price')
    if p is None or p<=0 or p>500: return -99   # $200–500 tier needs profit ≥ 10× price (Dylan, Oct 13)
    if not r.get('imgs'): return -99
    w=len(t.split())
    s+= 3 if w<=4 else 2 if w<=7 else 0            # short generic titles
    s+= 2 if HELPER.search(t) else 0                # seller doesn't know what it is
    s-= 3 if RESELLER.search(t) else 0              # seller does know
    s-= 2 if MODEL.search(t) else 0                 # model number = seller already identified it
    s+= 2 if TELL.search(t) else 0                  # value tells worth a Lens look
    s+= 1 if 10<=p<=100 else 0
    s+= 1 if len(r['imgs'])>=3 else 0
    c=r.get('cat'); s+= CAT_PRIOR.get(c,0) + LEARNED.get(c,0)
    try:
        import type_model; s+= type_model.adjustment(t)   # encyclopedia economics of the predicted type
    except Exception: pass
    return s


# --- The arbitrage detector (Oct 13 rethink): Lens names a maker/model the seller's title doesn't. ---------------------
# research/makers.json = maker/brand/model names harvested from the encyclopedia's Makers sections (enc.py sync rebuilds it).
_MK=None
def _makers():
    global _MK
    if _MK is None:
        import json, os
        p=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'research','makers.json')
        try: names=json.load(open(p))
        except Exception: names=[]
        _MK=[(m,re.compile(r'(?<![A-Za-z])'+re.escape(m)+r'(?![A-Za-z])')) for m in names]
    return _MK
def mismatch(title, ai, best):
    """Maker names that appear (case-sensitively, whole-word) in the Lens identification but not in the seller's title."""
    txt=(ai or '')+' '+(best or ''); tl=(title or '').lower(); out=[]
    for m,pat in _makers():
        if pat.search(txt) and m.lower() not in tl and not any(m.lower() in o.lower() or o.lower() in m.lower() for o in out): out.append(m)
    return out[:4]
