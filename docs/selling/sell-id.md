# Photo or description in → selling plan out (Oct 27 2026)

Mirror of `docs/photo-id.md` for the selling side. Dylan sends a picture or a line about something he's selling; the
chat answers with exactly how to sell it. Knowledge: `docs/selling/playbook.md`. Research: `research/selling/`.

## Procedure (per item)
1. **Identify it exactly** — same as buying: maker, line, model, material, year, size. `enc.py find`, label hunt, the
   Sept 2026 household sell list in the Refurbish project (claude/sell-list.md) if it's one of those pieces. The
   name is what buyers search for and what justifies the price. Then open the knowledge for it: a small shippable
   thing → `enc.py sell <slug>` (the entry's "Selling it" section); a bulky household thing → the family's section in
   `docs/selling/household-families.md`.
2. **Condition, honestly, in buyer words.** Name each flaw and where it is. Smoke/pet status. What's included.
3. **Value — three numbers:** what the same thing is *asking* locally right now (FB search in Chrome, Craigslist DFW,
   OfferUp), what it *sold* for if any channel shows sold data (eBay sold for shippable things), and new-replacement
   price (IKEA/Wayfair/Amazon for commodity pieces). List = at/just under local asks, padded 10–15%. Floor = where
   donating/hauling beats waiting.
4. **Channel** from the family table (playbook §3): local vs shipped vs consignment/dealer/auction/donate. For local:
   FB Marketplace + the free cross-posts (OfferUp, Craigslist, Nextdoor) + 8–12 groups via "List in more places."
5. **Haul plan** (no truck, no delivery): what vehicle it fits, weight, "we'll help load," rental-truck hint,
   split-the-set option if a piece opens the SUV pool.
6. **Write the listing**: title (brand + line + type + material/colour + size + condition word), first line with
   dimensions, body in the order of §2 of the playbook, photo shot list (first photo rule), price + "firm"/"OBO" call.
7. **Clock**: when to check stats (24–48 h), what the numbers mean (playbook §1), day-7/14/21/30 actions, and the
   exit (channel change, lot, consign, donate, haul).
8. **Log it**: a row in `db/selling/items.jsonl` (with `family`), then `scripts/sell.py check <id> clicks saves msgs`
   at each check and `sell.py sold <id> <price>` at the end. `sell.py stats` is the feedback loop: days-to-sell,
   % of list achieved and click→message rate by family replace the playbook's anecdotal numbers as rows accumulate.
9. **Answer the buyers** with `docs/selling/buyer-messages.md`: scripts for the ten standard messages, the scam
   tells, no-show prevention, pickup logistics for a seller who can't deliver, and the negotiation table by day.

## The card Dylan gets back
**Item** · **List on** (channels, in order) · **Price** list / accept / floor · **Title** (paste) · **Body** (paste) ·
**Photos** (shot list) · **Haul** (what it fits, what to say) · **Clock** (day 2 / 7 / 14 / 30 actions) · **If it
doesn't move** (next channel, named, with a phone number where there is one).

## When the photo isn't enough
Ask for the one thing that changes the plan — the label/stamp, a measurement, "is there a stain under the cushion" —
and say what each answer changes. Never "take it to an appraiser."
