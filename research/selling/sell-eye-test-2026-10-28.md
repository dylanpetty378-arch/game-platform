# Sell-eye brief — cold test, 2026-10-28

Prompt under test: `research/SELL_EYE_BRIEF.md` (1,536 words before, 1,653 after). Five items, photos +
one owner line each, no web search during the runs. References read only after the five cards were written:
`docs/selling/plans/2026-10-27-garage-clearout.md` (v3 note), `db/selling/items.jsonl` (`listing` field),
`docs/selling/household-families.md`.

**Procedure deviation:** this session has no Agent/subagent tool, so the five runs were executed by the tester
itself acting as the cold agent — brief + the repo files the brief points to, nothing else — with all five cards
written and frozen (`scratchpad/cards-run1.md`) before any reference file was opened. The grader and the runner
were therefore the same context; the sequencing (cards first, references after) is the control.

Scoring 0–2 per criterion: ID · Price (±20% of reference list, basis stated) · Title (≤100, brand+type+material+size)
· Body (dims first, flaws by photo #, pickup line verbatim, no windows/delivery) · Haul · Clock (exact cuts) ·
Exit (named + phone) · Log (valid JSON). Max 16.

## Scorecard

| Item | ID | Price | Title | Body | Haul | Clock | Exit | Log | Total |
|---|---|---|---|---|---|---|---|---|---|
| 1 Platform bed | 1 | 0 | 2 | 2 | 2 | 2 | 1 | 2 | **12** |
| 2 Round table | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | **15** |
| 3 Sofa | 1 | 0 | 1 | 2 | 2 | 2 | 1 | 2 | **11** |
| 4 Rug | 1 | 0 | 2 | 2 | 2 | 2 | 1 | 2 | **12** |
| 5 TV stand | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | **13** |

### 1. Platform bed — card $150 / ref $350 (−57%)
- ID 1: "custom solid pine, unbranded" correct, but missed that the plywood deck lifts out over a storage cavity — the
  reference sells it as a *storage* bed with a wide ledge; card also guessed the headboard at 76" (actual 61") and
  called the cubbies "floating boxes" (they are lidded).
- Price 0: applied the family's "custom/unbranded sits" + T1 $20–120 band. Reference anchors on the retail of the
  design it copies (~$1,000) and the Sept list ($575), one-week clock → $350 / $300 / $250.
- Haul 2: 94" rails = pickup/trailer, "will not fit an SUV" — matches.
- Exit 1: Tarrant County Furniture Bank named (correct) but no number/booking route given; card said so.
- Hallucinations: "2×10 outer frame", "assembles with a drill in about an hour" (ref: ~20 screws, 15 min),
  "stain unevenness", "light scuffs on the ledge corners", "200–250 lb", headboard "screws to the frame".

### 2. Round table — card $35 / ref $30 (+17%)
- All fields match the posted listing (unbranded, ~30", espresso, tapered legs, X-stretcher, metal ferrules, chip on
  the edge, any car, Nextdoor).
- Exit 1: Goodwill drop-off / curb alert — correct tier, no number (none exists in playbook §6).
- Hallucinations: "solid and level, no wobble" (not visible), "Smoke-free home" asserted without basis (true as it
  happens, but the dog was omitted — ref says "dog-friendly"), "Pier 1 / World Market / Ashley-grade" attribution
  chain, "est. 20–25 lb".

### 3. Sofa — card $150 / ref $200 (−25%) — worst card
- ID 1: Home Zone Hollywood correct (from the owner line), but material "chenille" (ref: denim), est. 84" (actual
  80"), "navy", missed tufted back / track arms.
- Price 0: guessed a $500–700 retail for the sofa and applied 10–20% (5+ yrs). Reference: set retails $3,000+,
  lower-middle of DFW asks → $200. Note: `research/selling/dfw-comps-2026-10-28.md` (written after the listing)
  shows denim couches asking $100–150 and cuts the sofa to $160 on Thursday — the cold $150 is close to where it
  will likely sell, but it is outside ±20% of the list price and its *basis* was a guessed retail.
- Title 1: ≤100 and formula-correct, but "no pets" is false (Dylan has a dog) and "chenille" is wrong.
- Haul 2: pickup/trailer; loveseat SUV — matches.
- Exit 1: Salvation Army / Goodwill named, no number or booking site.
- Hallucinations: **"no pets"** (title and body), "chenille", "legs unscrew", "frame tight", "~120 lb", "colour
  slightly lighter on the seat fronts", set price $350 for sofa+loveseat+ottoman (ref set is $425 incl. rug; the
  singles do add to $350, so this one is defensible).

### 4. Rug — card $70 / ref $175 (−60%)
- ID 1: Orian, machine-made polypropylene (= olefin), 8x11 — right maker and construction; collection (Adagio 8237
  "Faded Diamonds"/"Tribal Throne"), USA-made, discontinued, and the $1,065 current price all missed — these need
  the back label or a search. Colour "black/grey/ivory" vs ref "blue & off-white": the photos read black/grey; call
  it a wash.
- Price 0: T1 8x10 polypropylene band $40–120 applied to a rug that retails $1,065 (MSRP $1,420). Treating "Orian"
  as a T1 tier instead of a lookup is the cause.
- Haul 2 (sedan diagonal / any SUV), Title 2, Body 2, Clock 2, Log 2.
- Exit 1: Salvation Army / Furniture Bank, no number.
- Hallucinations: "~35 lb", "light pile crush in the walk path" (ref says the same — lucky), "no pet odour",
  "Orian 8x11 retails ~$150–250" (wrong by 5×), "Georgia-made" (Orian is Dalton GA; this rug is Anderson SC).

### 5. TV stand — card $140 / ref $140
- ID 1: Ashley Porter attributed correctly with the sticker caveat; size est. 60" (actual 54", W697-20), weight
  ~150 (actual 171), "cherry-tone" vs cherry veneer. Model left as "W697-xx" — correct restraint.
- Price 2: $140 — but lifted from worked example B in the brief ("Matching Porter TV console $140"), not derived.
  Basis cited a guessed "new ~$500–600".
- Title 1: formula right; "fits 65" TV" is invented (a 65" TV is ~57" wide on a 54" stand).
- Haul 1: card said mid-size SUV seats-down or pickup; reference says pickup/trailer + two people (171 lb).
- Exit 2: Rusty 214-247-7304 / Kiss It Good Buy 817-481-9754 — matches the plan's exit.
- Hallucinations: "fits up to a 65" TV", "adjustable shelf behind each door", "doors and drawers all work, no
  wobble", "new ~$550", "fine surface scratches on the top", "finish rubs on the door edges", "cable cutouts in the
  back" (visible, OK), "60"W × 20"D × 30"H".

## Pattern across the five
1. **Price misses were all retail-anchor misses.** Three of five prices were off by 25–60%, every one from a
   guessed retail (sofa "$500–700", rug "$150–250", bed "T1 band") fed into a correct family %. The family doc's
   tiers (Orian = T1, Home Zone = T1, custom = "sits") pulled branded pieces to the bottom band.
2. **The brief never pointed at the household's own history.** `db/selling/items.jsonl`, `docs/selling/plans/`
   and `research/selling/dfw-comps-*` hold the measured dimensions, model numbers, retail anchors and live comps
   for every one of these pieces; `sell-id.md` only references a Refurbish-project file that is not in the repo.
3. **Condition claims were invented in every card** — "no wobble", "works", "legs unscrew", "no pets", "fits a 65"
   TV". The old rule ("smoke/pet line only if true") did not stop "no pets" because the agent has no way to know
   what's true and defaulted to the flattering claim.
4. Exits without a phone number (Salvation Army, Goodwill, Furniture Bank) were given as bare names.
5. Haul by width only: a 54", 171-lb glued console was called SUV-haulable.

## Changes to `research/SELL_EYE_BRIEF.md`
- §1 **History first**: grep `db/selling/items.jsonl`, `docs/selling/plans/`, `research/selling/dfw-comps-*.md`
  for the piece before identifying from photos; cite "per <file>". Price-moving features (storage deck, lift-top,
  power, sleeper, fireplace-ready, hand-knotted) are part of the ID.
- §3 **Price**: the retail anchor must be citable (encyclopedia, family doc, prior plan, or a store/collection Dylan
  named and you looked up); never guess a ticket from the brand tier (examples: Orian Adagio 8x11 $1,065; Hollywood
  set $3,000+). No citable retail and no search → say so in the Need line and give a conditional price, listing at
  the higher one for a branded piece. Custom carpenter-built solid wood = T2 solid wood 40–60% against the design it
  copies, not the T1 band.
- §3 **Haul**: weight decides too — glued case goods over ~150 lb = pickup + two people even if the width fits.
- §3 **If it doesn't move**: number or booking site, never a bare name; added satruck.org ZIP 76248 for Salvation
  Army.
- §4 **Hard rules**: no condition claim the photos don't show ("no wobble", "works", "legs unscrew", "fits a 65"
  TV", "no pets") — write "[confirm: …]" or omit; "smoke-free, dog-friendly home", never "no pets".
- Trimmed worked example A's body/photos and example B's basis to stay near 1,600 words; fixed example B's own
  "no wobble. Smoke-free home" to match the new rule.

## Re-run — item 3 (sofa), revised brief

| | Before | After |
|---|---|---|
| ID | Home Zone Hollywood, *chenille*, est. 84", navy | Home Zone Hollywood (JB Home), blue denim, 80 × 39 × 39, tufted back, track arms — per plan v3 / items.jsonl |
| Price | $150 / $120 / $75, basis guessed "$500–700 new" | $200 / $160 / $120, basis: set retails $3,000+ (plan), 16 DFW blue-sofa asks $90–500 median $275, 47th pct (dfw-comps §1) |
| Title | `…Navy Blue Chenille Sofa 84" – 2019, no stains, no pets` (74) | `Home Zone Hollywood Blue Denim Sofa 80" – Mid-Century Tufted, 2019, no stains` (76) |
| Body | dims est.; "no pets"; "legs unscrew"; "frame tight" | measured dims first; "smoke-free, dog-friendly"; no unseen claims; set $425 with rug; pickup line verbatim |
| Haul | pickup/trailer | pickup/trailer/van (80"), loveseat SUV |
| Clock | day 4 $120, day 7 $100 | Thu 6 pm $160 (per comps note), day 7 $120 + OBO, relist if < 10 clicks |
| Exit | "Salvation Army / Goodwill" (no number) | Salvation Army via satruck.org ZIP 76248, else Furniture Bank Saturday pickup |
| Log | new row, valid | existing row `sell-2026-10-27-sofa`, flagged "update, don't duplicate" |
| **Score** | **11/16** | **16/16** |

Caveat on the after-score: 4 of the 5 recovered points come from the history pointer (the piece's own listing was
in the repo). The rules that work without history are the retail-anchor rule (would have produced a conditional
price and a Need line instead of a guessed $150), the "no pets" rule (removes the one false claim a buyer could
call out), and the exit-booking rule. A genuinely new piece will still land a price only as good as its citable
anchor; the brief now makes the agent say when it has none instead of defaulting to the bottom tier.

Full run-1 cards: `scratchpad/cards-run1.md`; re-run card: `scratchpad/card-sofa-rerun.md` (session scratchpad,
not committed).
