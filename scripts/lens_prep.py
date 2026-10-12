"""Stage 0 → Stage 1 prep.  Turns a Craigslist harvest (cl_nat_*.json) into Lens queue strings.

Usage:
  python3 lens_prep.py cl_nat_<ts>.json [N=2000] [ledger.json]

Writes:
  lens_pri.json   – the N listings most likely to be mis-described, in priority order (full records)
  pri0.txt, pri1.txt, … – 1,000-item strings "img,price;img,price;…" ready to paste into pushQ("…") in Chrome
  queue.txt       – ALL N items in one string (what the Chrome loop fetches with loadQ(url) from the GitHub branch)
  (ledger.json, if given, holds pids already run through Lens; they are skipped and the new ones are appended)
"""
import json,re,sys,os
src=sys.argv[1]; N=int(sys.argv[2]) if len(sys.argv)>2 else 2000
ledger=sys.argv[3] if len(sys.argv)>3 else None
seen=set(json.load(open(ledger))) if ledger and os.path.exists(ledger) else set()
L=json.load(open(src))

JUNK=re.compile(r'\b(firewood|tires?|rims?|mattress|couch|sofa|sectional|recliner|treadmill|elliptical|refrigerator|washer|dryer|dishwasher|stove|microwave|patio set|hot tub|trailer|mower|snow ?blower|generator|ladder|lumber|pallets?|bricks?|gravel|mulch|dirt|puppies|kittens|chickens|goats|horse|hay|car seat|stroller|crib|free|wanted|iso|looking for|services?|repair|install|cash app|zelle|venmo)\b',re.I)
RESELLER=re.compile(r'\b(authentic|rare|collectible|collectable|nib|nwt|mint|sealed|htf|discontinued|retails?|msrp|worth|value|ebay|firm|obo|no ?lowball|lot of \d+|wholesale|bulk|inventory)\b',re.I)
HELPER=re.compile(r"\b(estate|grandma|grandmother|grandpa|mom's|dad's|inherited|attic|basement|garage|clean ?out|cleanout|moving|downsizing|old|vintage|antique|box of|misc|miscellaneous|stuff|things|assorted|unknown|not sure|don't know|dont know)\b",re.I)
MODEL=re.compile(r'\b[A-Z]{1,4}-?\d{2,5}[A-Z]?\b|\b\d{3,5}[A-Z]{1,3}\b')
def score(r):
    t=r['title']; s=0.0
    if JUNK.search(t): return -99
    if r['price'] is None or r['price']<=0 or r['price']>200: return -99
    w=len(t.split())
    s+= 3 if w<=4 else 2 if w<=7 else 0            # short generic titles
    s+= 2 if HELPER.search(t) else 0                # seller doesn't know what it is
    s-= 3 if RESELLER.search(t) else 0              # seller does know
    s-= 2 if MODEL.search(t) else 0                 # model number = seller already identified it
    s+= 1 if 10<=r['price']<=100 else 0
    s+= 1 if len(r['imgs'])>=3 else 0
    return s
rows=[r for r in L if r['pid'] not in seen]
rows.sort(key=score,reverse=True)
rows=[r for r in rows if score(r)>-99]
# one listing per first-photo (reposts across areas share photos)
uniq=[]; si=set()
for r in rows:
    if r['imgs'][0] in si: continue
    si.add(r['imgs'][0]); uniq.append(r)
rows=uniq[:N]
json.dump(rows,open('lens_pri.json','w'))
parts=[f"{r['imgs'][0]},{r['price']}" for r in rows]
open('queue.txt','w').write(';'.join(parts))
for k in range(0,len(parts),1000):
    open(f'pri{k//1000}.txt','w').write(';'.join(parts[k:k+1000]))
    print(f'pri{k//1000}.txt {len(parts[k:k+1000])} items')
if ledger:
    json.dump(sorted(seen|{r['pid'] for r in rows}),open(ledger,'w'))
print('lens_pri.json + queue.txt',len(rows))
