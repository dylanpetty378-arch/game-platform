# Item dossiers — everything about one item we buy or sell

Dylan (Oct 12 2026): "I'll want all the information possible on all the items I buy/sell. I'll need it so I can reference
the information for the customer."

A dossier is started when an item reaches `decided` with Tier A or B, or as soon as Dylan says he is buying it. It is
finished when the item sells. There is one file per item: `docs/items/<pid>-<short-slug>.md`. The dossier is the
buyer-facing source of truth, so it holds facts only. Seller contact details and Dylan's personal details never go in it
(the repo is public); they live in the printable report and the claude.ai project.

## Template
````
# <What it is, in one line: maker · model/pattern · material · period>
pid: <craigslist pid> · type: [[<encyclopedia slug>]] · status: decided | contacted | bought | listed | sold
Listing: <url> (as found: "<original title>", $<ask>, <area>, posted <date>)

## Identification
Maker, model/pattern/line, date range (with the evidence: mark, serial, construction), material (tested? magnet,
weight, hallmark), size (measurements), weight. Each marking transcribed exactly, and where it is on the item.

## Condition (as received)
Grade + every flaw (chips, cracks, crazing, repairs, wear, missing parts), with photo refs. Works/tested? How.

## History & provenance
What the seller said (as stated), estate/original owner, anything documenting origin.

## Why it's valuable / what makes it desirable
The collector story: rarity, variant, demand, what buyers look for, comparable pieces in museums/books.

## Comps
Sold comps (dated, source), active competition, price reasoning.

## Economics
Paid $ · fees · shipping in/out · listed price · sold price · days to sell · net profit. (Fill as it happens.)

## Listing copy (ready to paste)
Title (80 chars, keyword-ordered) · item specifics · description paragraph(s) · measurements · condition statement ·
shipping/packing note.

## Buyer Q&A log
Questions buyers asked + answers given (reuse for the next one of this type).

## Rubric (item)
```json
{ ...item rubric fields from docs/rubric.md... }
```

## Lessons
What we'd do differently; feed back into the encyclopedia entry (`enc.py seen` + edit).
````

## Workflow
1. When an item reaches Tier A/B: create the dossier from the review notes, comps and the encyclopedia entry.
2. When it's bought: add condition as received, measurements, mark photos (Dylan's photos stay with him; describe them
   here), and update the economics.
3. When listing: generate the listing copy from the dossier.
4. When it sells: record the sold price and days to sell, then update the type's rubric (`sell_through`, `days_to_sell`,
   price), turning estimates into measured numbers.
