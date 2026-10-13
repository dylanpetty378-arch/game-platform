# Review procedure — from "flagged by Lens" to "find" (Stages 2–4)

Input: listings whose latest stage is `flagged` (`python3 scripts/db.py worklist flagged`, or STATUS.md).
Order: highest ratio first, but give collector-site matches (`collect=1`) and AI-value sentences a look regardless.
Log every decision as an event **as you make it**.

## Stage 2 — look at the actual object (cheap, fast)

1. Photos: `https://images.craigslist.org/<imgId>_1200x900.jpg` for each id in the listing's `imgs`
   (`db.py show <pid>`). In the container, build a sheet: `python3 scripts/lens_export.py --photos stage2.json sheets/`
   (needs a stage2.json; or just Read the 1200px images directly). The listing page: `url` field.
2. Decide what it is. Lens `best` is a *hint*: it often matches the category (any oak roll-top → $2,200 antique,
   any Persian-style rug → $2,880 antique) — those false flags are the norm.
3. Read the encyclopedia entry for that type (`docs/encyclopedia/index.md`). Use its tells and sold ranges.
4. **Kill now** (event `photo_review --status kill --note <reason> --type <slug>`) if: mass-produced/reproduction
   (the photo shows it), bigger than a passenger seat (size rule) or unshippable, untested/broken electronics, needs
   authentication, reseller listing (model already in title, "retails for", lot pricing), obvious scam (stock photo +
   placeholder price), or the Lens match is a different object.
5. Survivors: `photo_review --status keep --type <slug> --note "<what it is, exact comp search string>"`.
   If a mark/label would settle it: `identified --status need_mark --note "ask for photo of underside stamp"`.

Typical yield: ~1 in 4 flagged survive; ~1 in 15–25 flagged becomes a find.

## Stage 3 — sold comps and the rule

1. eBay sold: Terapeak (Seller Hub → Research, Dylan's eBay is signed in on his Chrome) or
   `https://www.ebay.com/sch/i.html?_nkw=<exact name>&LH_Sold=1&LH_Complete=1`. Exact name, never the generic type.
   Exclude parts/for-repair/mismatched lots. Take the median of the last 10–20.
   Log the search: `db.py search --site ebay_sold --query "…" --purpose comps --results N`
   and the prices: `db.py comp --type <slug> --query "…" --source ebay_sold --prices a,b,c --pid <pid>`.
2. `net = median × 0.87 − ship_to_buyer − ship_to_Dylan` (estimate $15 small / $30 medium / $60+ large or fragile).
   `profit = net − price`. Pass if `profit ≥ max(50, price)`.
   Tiers: **A** profit ≥ 2× price · **B** passes · **C** within 20% — ask for mark/condition first.
3. Event: `comps --status pass|fail|close --data '{"median":…,"n":…,"profit":…}'`, then
   `decided --status find|ask|pass --note "Tier A, ~$215 profit, ask height + back casting"`.

## Stage 4 — deliver to Dylan
- Printable PDF, one page per find: photo, title, price, location, what it is, sold comps, profit math, tier, QR code
  to the listing, drafted seller message. Template: `scripts/legacy/build_run12.py`; format: `docs/history/report-format.md`.
- Seller contact: Craigslist relay address via the listing's Reply → email dropdown (Chrome, logged in). Put relay
  addresses/phones in the chat/PDF only — **not** in this public repo. Send nothing until Dylan OKs that message.
- After sending: `contacted --status sent`; on reply `contacted --status replied --note …`.

## Stage 5 — learn
- Encyclopedia: add/update the entry for every item type you looked at (README in `docs/encyclopedia/` has the
  format), and `db.py itemtype <slug> --name … --volume …`.
- `docs/improvements.md`: anything that would have made this faster or found more.
- Ideas for the scorer/flag rule go there too, with the evidence (pids) — then change `scoring.py` / the flag rule.
