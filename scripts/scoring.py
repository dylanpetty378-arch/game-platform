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
    return s
