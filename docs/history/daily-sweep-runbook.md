# Daily deal sweep – runbook

> **Oct 12, 2026 – READ THIS FIRST.** The identification step is now **Google Lens in Dylan's Chrome**, not thumbnail review by agents. The complete step-by-step procedure — every command, what to expect, what to do when it breaks — is in **`claude/lens-pipeline-runbook.md`**. Follow that file for the harvest → Lens → Stage 2 → sold comps → PDF flow. This file keeps Dylan's rules, scope, tiers and the other sources (Facebook, OfferUp, estate sales, HiBid).

**How to run it:** open a new Cowork chat in the Refurbish project with Chrome (Claude in Chrome) running and Facebook logged in, then say **"run the daily sweep."** Claude should read this file, `lens-pipeline-runbook.md`, `site-access-methods.md`, `shipped-sweep-methods.md`, `encyclopedia/index.md`, `sweep_tools.py`, `build_deal_sheet.py` and the latest entry in `sweep-log.md`, then do everything below without asking questions.

## Scope (Dylan, Oct 12, 2026)

- **Search everywhere.** Any US listing, any site, whether or not it says it ships. When something is found in another city we message the seller and ask for shipping and pay for it. Do **not** filter to "shipping" listings – that filter only returns resellers and eBay-syndicated items (see `shipped-sweep-methods.md`).
- Local pickup (Keller / North Fort Worth, fits in a Honda Civic) is still fine and still the best source of uninformed sellers.
- **Research everything – the encyclopedia method** (Dylan, Oct 12): look at the pictures, work out what each thing is, research it, write the research down per item type in `encyclopedia/` so later runs and other models can reuse it, decide whether it's valuable, move on. When a type already has an entry, use it for speed. The encyclopedia is never a filter: an item type with no entry gets researched, not skipped. Don't go in with a list of "things we look for."

## Deliverable rule (Dylan, Sept 22)

- **Give Dylan exactly one document per run: the full-list PDF** (`DFW-Resale-Finds-Full-List-YYYY-MM-DD.pdf`, built by `claude/build_master_pdf.py`; the nationwide run uses `claude/build_run12.py`). It always contains everything still live, not just today's finds. Built for printing (Oct 8): no clickable links, he works from the paper copy.
- Update everything else (master workbook, logs, runbook, tools, encyclopedia) quietly. Don't send those files unless he asks.
- If he logs buys, keep the Buys & Sales data in the master workbook, which stays internal.

## Buy rules (Dylan's rules, updated Sept 21, 2026 – sweep 5)

1. **Seller doesn't know the value.** Search generic words, never brand names. Find value from the photos.
2. **Max cost $200 per item**, including shipping in.
3. **Profit must be at least the price paid, with a $50 floor:** profit ≥ MAX($50, price). A $20 item needs $50 profit; a $150 item needs $150. Profit is after fees and shipping out. Gas and time aren't counted, but flag long drives. The sheet checks this at the offer price and at the full listed price.
4. **Fits in a car or ships.** No truck yet.
   - **Small furniture** that fits in the car is OK if profit ≥ 2× the price and it gets relisted within a week (updated Sept 21).
   - Bigger furniture only if its brand or make could profit **$750+**, since that pays for hired pickup.
5. **Price drops:** if an item was listed higher and is now low because it isn't selling, include it only if there's a specific reason we could sell it that the seller isn't using (a better channel, the right keywords, the right audience).
6. **List every item that meets the rules.** Don't stop at a target count.
7. **Out of scope:** repair, refinishing, untested electronics, and anything whose value depends on authentication (designer goods, gold/silver claims) unless it can be verified from the photos.
8. **Trips:** group pickups by area. A trip should add up to at least **$150 profit** (Trips tab). A lone small item isn't worth its own drive.

## Priority tiers (column B) – scaled to price

Multiple = profit ÷ needed profit (needed = MAX($50, price)).

| Tier | Rule of thumb |
|---|---|
| **Stop Everything And Get This** | Multiple ≥ 4× **and** profit ≥ $300, high confidence |
| **Great Deal** | Multiple ≥ 2.5× |
| **Good Deal** | Multiple ≥ 1.5× |
| **Just Barely Over The Threshold** | Multiple 1–1.5×, or low confidence, or a long drive |
| **Lead – need price/photos** | One missing fact (price placeholder, unreadable marks, one photo). Message the seller |

## The encyclopedia method (the core of every run)

Brand, model and maker marks are in the photos, not the text. So:

1. **Harvest wide** (Craigslist nationwide via `cl_nat.py`; Facebook/OfferUp/estate sales as below).
2. **Every listing gets identified by machine first** – Google Lens on its first photo (`lens-pipeline-runbook.md`, Steps 2–5). The old method (agents reading 130-px contact sheets) found 9 in 9,600; Lens identifies brand/model on ~73% and flags 25–40% for human review. Facebook/OfferUp photos can go through the same Lens loop: the queue string is just `imageUrlOrId,price;…` – for non-Craigslist photos edit `lensOne` in `lens_gentle.js` to take a full URL.
3. **Look the type up in `encyclopedia/index.md`.** If there's an entry, apply its tells and buy rule. If there isn't – or the item may be a variant the entry doesn't cover – **research it** (sold prices, price guides, collector references), then write or extend the entry (`encyclopedia/README.md` has the template). Passes get recorded too ("Seen in sweeps"); that's what makes the next run faster.
4. **Open the flagged listing's full photos**, read the description only after the photos, identify the exact model, then compare the sold comps to the price. Never the other way round. Lens often matches the *category* (any oak rocker) – the photo review is what separates "a rocker" from "a Temple Stuart rocker".
5. **Verify finalists with Terapeak / eBay sold** (sold, not asking) before they go on the sheet.
6. Skip items whose value depends on authentication you can't see in the photos, anything "needs work" / "not working", and current retail products (if Lowe's or Amazon sells it new, pass).

## Steps

1. **Window.** Read the last run's timestamp in `sweep-log.md`. The window is from that time to now, plus 12 hours of overlap. If there's no log, use 7 days.
2. **Craigslist nationwide → Lens.** Exactly as in `lens-pipeline-runbook.md` Steps 1–9. Local DFW (`sweep_cat`, area 21, 30 mi) still runs every time with all 27 categories and goes through the same Lens queue.
3. **OfferUp.** Browser only since Oct 12 (container 403). Local feed as before; no shipping search on the web.
4. **Facebook (Chrome).** Category feeds (`FBSEO`) for antiques, toys, instruments, hobbies, entertainment, home-improvements, sports, free, newest first, *without* the shipping-only flags (local radius, plus a few other metro `buyLocation`s if budget allows), then the generic query list below. Review on the light tab (facebook.com/robots.txt) – see site-access-methods.md. Drop eBay-syndicated items on sight ("See item on eBay").
5. **Estate sales (container, Tuesday–Wednesday runs, before Thursday openings).** `esn.sales()` → `esn.window()` → `esn.all_pictures()` → Lens or contact sheets → verify → Terapeak comps → **Estate readout workbook** (`claude/build_estate_readout.py`). Also run `gsalr.sweep()` for garage sales and keyword-screen them.
5b. **HiBid (browser, any day):** GraphQL harvest of lots closing in the next 48 h within 40 miles, drop store-return sellers, grid-review photos, and give Dylan max bids only for items with solid Terapeak comps.
6. **New-source slot (15 min every run).** Build the next source from Tier 1 of the source directory in `site-access-methods.md`, and record what worked.
7. **Liveness + seller check.** Run `live.py` on every Craigslist/OfferUp link and the Facebook `LC` checker on every FB link. Drop anything sold. Use the exact seller title it shows for the "Seller knew?" column – never guess.
8. **Comps.** For every shortlist item, get at least 2 real **sold** prices – **before** it goes on the sheet. Use **Terapeak** first (see site-access-methods.md; always set minPrice). Ignore asking prices and parts listings.
9. **Sheet / PDF.** The deliverable is the printable finds PDF: every live item found so far – carry forward yesterday's rows, update each row's live status, strike through sold ones, and add today's finds (marked with the date first seen). For out-of-town items the row carries "ask seller to ship" and the estimated shipping cost in. Save to the conversation and to the project.
10. **Encyclopedia.** Push every new or changed `encyclopedia/*.md` to the project and update `encyclopedia/index.md`.
11. **Log.** Append to `sweep-log.md`: run time and window, counts per site, Lens done/flagged, deals found (tier, link), encyclopedia entries added, dead ends, any new technique.

## Generic query list (Facebook)

- **Round A (broad):** estate, antique, old, vintage, lot, collection, box of, grandma, grandpa, storage unit, misc, garage sale, moving sale, tools, camera, art, painting, pottery, glass, jewelry, silver, brass, lamp, chair, stool, radio, record, toy, game, knife, sign
- **Round B (rotate 10 per day):** watch, pen, clock, sewing, china, figurine, vase, book, comic, cards, coins, stamps, keyboard, guitar, speaker, amp, rug, mirror, frame, print, sculpture, mid century, retro, old school, military, western, indian, turquoise, sterling, carved, signed, handmade, tackle, reel, lure, dolls, trains, tin, cast iron, copper, bronze, crystal, lot of, bundle, estate jewelry, junk drawer, attic, barn find, basement, inherited, "don't know much about", "no idea"
- The last three phrases catch sellers who say outright that they don't know what they have.

## Fakes and lookalikes to skip (keep adding to the encyclopedia)

- "Navajo" rugs with warp fringe (real Navajo rugs have none)
- slip-cast "Native American" pottery
- "14k" that's plated (read the description)
- silver-tone squash blossoms
- Indian reproduction brass sextants/telescopes (Kelvin & Hughes etc.)
- "Blaeu"/old-master maps on bright white paper (reproductions)
