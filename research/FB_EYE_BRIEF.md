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
Flag it when **resale minus a realistic offer is ≥ $50 AND resale is ≥ ~3× the listed price** (free / $0 / $1 / OBO
always pass the price part). Resale may be eBay/Poshmark/Mercari (minus ~13–20% + shipping) or local Facebook (no
fees) — whichever is better. Named items count: a seller who named it can still be dumping it (prewar Lionel $50).

**Dylan (Oct 23 2026): cover ALL kinds of goods, not just cards and collectibles — and anything brand-name, whatever
the item.** Give the everyday categories the same attention as antiques:
- **Clothes, shoes, bags:** brand-name lots and singles — Lululemon, Patagonia, Arc'teryx, North Face (Nuptse/Summit),
  Carhartt/Filson, Levi's vintage (big E, orange tab, 501XX), Nike/Jordan/Yeezy/New Balance, Dr. Martens, Frye, Lucchese
  and other good boots, Coach/Kate Spade/Tory Burch/Michael Kors (real), designer, vintage band and sports tees (single
  stitch), letterman/leather jackets, NWT bundles, a box of name-brand kids' clothes (Hanna Andersson, Janie & Jack,
  Patagonia kids) sold as a lot.
- **Children's toys and baby gear:** Magna-Tiles/Picasso Tiles, LEGO by the tub or pound, Calico Critters, American Girl,
  Melissa & Doug sets, Little Tikes/Step2 outdoor pieces, Power Wheels, Plan Toys/Hape/Grimm's wooden toys, vintage toys
  (Fisher-Price, Star Wars, He-Man, Barbie), Nintendo/console bundles; baby gear: UPPAbaby, Nuna, Doona, Bugaboo,
  Babyletto/4moms/SNOO, Ergobaby, high-end car seats (check expiry).
- **Books:** sets and runs (leather/antique volumes, Easton/Franklin Mint, Folio Society), signed or first editions,
  vintage children's books, cookbooks of note, comics/manga runs, textbooks of the current edition, a box of books that
  shows any of these on the spines.
- **Kitchen and home:** Le Creuset/Staub, cast iron (Griswold/Wagner/Lodge vintage), All-Clad, Vitamix/Blendtec,
  KitchenAid stand mixers, Breville/espresso machines, Ninja/Instant Pot only if new-in-box, vintage Pyrex/Corningware/
  Fiesta/Fire-King, Dansk/Catherineholm, good knives (Wüsthof/Shun), sterling flatware, crystal (Waterford), YETI/Stanley,
  Dyson, iRobot.
- **Also:** power tools and tool lots (Milwaukee/DeWalt/Makita/Snap-on), outdoor/sports gear (YETI, Traeger, Weber,
  golf clubs, bikes by brand), audio/electronics by brand, furniture with a name or mid-century design, art, antiques,
  cards, records, instruments — as before.
- **Garage / estate / moving-sale posts:** flag if the PHOTO shows brand-name or valuable things on the tables.
- **Big things** (furniture, appliances, ride-ons): flag only if branded/valuable; note "SIZE: truck".

## Skip
Replica/homage luxury (a "luxury automatic watch" that looks like an Omega/Rolex for $160, logo handbags at $50 —
real ones are never dumped at that price without a receipt/box story); items only ~2× the price above $100 asks;
services, food, rentals, loans, "we buy", internet/phone plans, new mass-retail items at retail price, cheap fashion
jewelry, kids' clothes, dealer/store ads (display cases, many identical items, shop names, $1 placeholder on a store
item), and things whose real resale is under $100.

## Be generous at this stage
A deeper review checks every flag with sold prices. Missing a $600 book set costs far more than one extra flag.
Expect roughly 2–8 flags per 25-cell sheet in a household pool, across all kinds of goods — not mostly cards. If a cell's photo is too small or unclear but
*could* be something good, flag it with "CHECK PHOTOS".

## Output
For each sheet in your batch: read `sheet_NN.md` (cell → title, price, city/miles), then view `sheet_NN.jpg`
(yellow tag = cell number). Write one line per flag to your flags file, tab-separated:
`<sheet number>\t<cell number>\tLEAD — <what the photo shows / what it really is, est. resale $, why>`
Create the file even if empty. Reply with only the flag count and flags per sheet.
