# Facebook Marketplace eye brief (Oct 23 2026, Dylan's rules — replaces the Facebook section of LOWUSE_EYE_BRIEF.md)

Facebook Marketplace is a different ballgame from eBay/ShopGoodwill. Read this whole file; ignore the eBay rules.

## How Facebook works (Dylan, Oct 23 2026)
- Local pickup around Keller TX. People sell cheap because that is how Marketplace works: they want it **gone fast**.
  Moving, clearing a garage, grandma's estate, kids' old stuff. Price is a starting point — "best offer", "$1",
  "free", "make an offer", "need gone" all mean the real price is whatever Dylan offers.
- **Dylan's proof:** a 14-volume antique book set listed best-offer; he offered $50, picked it up next day, worth
  ~$600. It was recognised **from the pictures** — the title and text did not say what it was.
- So: **judge the PHOTO, not the title.** Titles are vague, wrong, or Spanish. The listed price is a ceiling, not the cost.

## What to flag
Look at every cell's photo and ask: *what is this really, and what does it sell for (sold, used, as-is)?*
Flag it when **typical resale is ≥ $100 AND at least ~3× the listed price** (free / $0 / $1 / OBO always pass the
price part). Resale may be eBay (minus ~13% + shipping) or local Facebook (no fees) — whichever is better.
Named items count: a seller who named it can still be dumping it (prewar Lionel set for $50).

Things that typically clear this on Facebook (not a filter — anything can):
- Sets and runs: multi-volume antique/leather books, encyclopedias of note, complete card sets, full china/silver sets.
- Bulk lots: LEGO by the tub/pound (~$8–10/lb), Pokémon/sports card binders and boxes, vintage toys, tools, records.
- Brand-name things people underprice: power tools (DeWalt/Milwaukee/Makita/Snap-on), KitchenAid/Vitamix/Le Creuset,
  Pyrex/Fiesta, sterling, Coach/Dooney/Louis Vuitton, Apple, game consoles + games, cameras/lenses, audio gear.
- Antiques & vintage: signs, cast iron (Griswold/Wagner), crocks, mid-century lamps/furniture pieces, art pottery,
  quilts, militaria, fishing tackle, typewriters, Native/Mexican silver & turquoise, gold jewelry in a junk lot.
- Garage / estate / moving-sale posts: flag if the PHOTO shows something valuable on the tables (note what and where).
- Furniture & appliances: flag only if the brand/design is valuable (mid-century, Ethan Allen-quality solid wood,
  name designers, Weber grills) — note "SIZE: truck" so Dylan can decide. Plain free couches/fridges: skip.

## Skip
Replica/homage luxury (a "luxury automatic watch" that looks like an Omega/Rolex for $160, logo handbags at $50 —
real ones are never dumped at that price without a receipt/box story); items only ~2× the price above $100 asks;
services, food, rentals, loans, "we buy", internet/phone plans, new mass-retail items at retail price, cheap fashion
jewelry, kids' clothes, dealer/store ads (display cases, many identical items, shop names, $1 placeholder on a store
item), and things whose real resale is under $100.

## Be generous at this stage
A deeper review checks every flag with sold prices. Missing a $600 book set costs far more than one extra flag.
Expect roughly 2–8 flags per 25-cell sheet in a household pool. If a cell's photo is too small or unclear but
*could* be something good, flag it with "CHECK PHOTOS".

## Output
For each sheet in your batch: read `sheet_NN.md` (cell → title, price, city/miles), then view `sheet_NN.jpg`
(yellow tag = cell number). Write one line per flag to your flags file, tab-separated:
`<sheet number>\t<cell number>\tLEAD — <what the photo shows / what it really is, est. resale $, why>`
Create the file even if empty. Reply with only the flag count and flags per sheet.
