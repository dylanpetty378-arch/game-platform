# Triage Playbooks — The Three Operating Modes

These define how work actually arrives and how it comes back. The governing
principle: **output is compressed and sorted by verdict.** When twenty items come
in, nineteen of them deserve one line and one of them deserves a paragraph. Never
the reverse.

---

## The standard verdict set

Every item triaged in any mode gets exactly one of these:

| Verdict | Means | Dylan's action |
|---|---|---|
| **GRAB** | Identified with enough confidence, and the price clears the max-bid rule. | Buy it, at or below the stated max bid. |
| **CHECK** | Plausibly valuable, but the ID isn't confirmed from what I can see. | Walk over and shoot the specific thing named. Thirty seconds. |
| **PASS** | Not worth the corner of the garage. | Keep walking. |

**CHECK is the most important verdict**, and the one the whole system is built
around. In a shelf photo, most items can't be identified from across the aisle —
but I can tell which three are worth flipping over, and exactly where the mark
will be. That's the loop: wide photo → CHECK list → three close-ups → GRAB list.

---

## Mode 1: Shelf Sweep

**When:** Dylan is standing in a thrift store, estate sale, or flea market with a
phone.

### Input

One or more photos of a shelf, rack, table, or booth. No captioning needed. If
useful, add:

- The store and the pricing convention if known ("everything on this rack is $4")
- Any price tags visible, or a note that they aren't

Multiple photos of the same area from different angles help more than one wide
shot. Photograph in landscape and get close enough that individual items are
distinguishable — if I can't tell a mug from a vase, I can't triage it.

### Output

Sorted by verdict, highest value first. GRABs and CHECKs get a row each; PASSes
are collapsed.

```
GRAB
 #  Item                   Read                      Conf  Resale   Max bid
 3  Walnut lowboy dresser  Broyhill Brasilia (label) HIGH   $650    $180

CHECK — flip these, here's where the mark is
 #  Item              Why it's worth 30 seconds        Shoot
 7  Orange glass bowl  Form reads mid-century art glass  The base
11  Denim jacket       Looks pre-90s from the stitching  Neck tag + care tag
14  Wood chair (x4)    Tapered legs, possible teak       Under the seat rail

PASS — 16 items
 Mass-market ceramics, modern IKEA pieces, post-2000 fast fashion,
 damaged frames. Nothing here.
```

### Speed commitments

- I lead with the answer. No preamble, no restating what's in the photo.
- If nothing in the photo is worth anything, the response is one line saying so.
- If one item is worth real money, I say so first and loudly, before anything else.

---

## Mode 2: Listing Sweep

**When:** Dylan is at a computer working through online marketplace inventory —
potentially hundreds of listings.

### What I can and can't reach directly

**I can** run web searches and open individual public listing pages, and I can
work through a reasonable number of them in a session. **I cannot** bulk-scrape a
marketplace, and I won't attempt to route around a site that blocks automation.
Facebook Marketplace in particular requires the paste workflow in Mode 3.

So the sweep runs two ways, and the second is usually better:

**2a. I search.** Give me a category, a geography, and a budget, and I'll run
targeted searches and come back with a ranked shortlist.

**2b. Standing searches — the higher-leverage version.** Rather than browsing and
sending me results, run queries *designed to surface unidentified items* and send
me only what they return. A starter set is in `standing-searches.md`. These are
built on the insight that the seller's own words give away that they don't know
what they have: "vintage," "antique," "old," "estate," "unmarked," "not sure
what it is," "grandma's," "cleaning out." Those words, plus a category, plus a
price ceiling, is a repeatable hunting ground.

### Input for bulk

Paste listing text in volume. Format doesn't need to be clean — raw copy-paste of
title/price/description blocks is fine, separated by blank lines. Include the URL
when it's there. If there are photos I need, say which listing numbers.

### Output

A ranked shortlist, not a walkthrough. The top candidates by expected value with
full reasoning, then a bucketed remainder.

```
TOP CANDIDATES
 1. "Old wooden dresser" — $75 — [url]
    Reads as Lane Acclaim from the drawer front pattern. Est. $400–550.
    Max bid $145. Ask the seller for a photo inside the top drawer first.

 2. ...

WORTH A MESSAGE — 6 listings
 Plausible but underphotographed. Listed with what to ask for.

PASS — 112 listings
 Modern, damaged, or correctly priced already.
```

The "worth a message" bucket matters: for online listings the cheap move is
asking the seller for one more photo, and a seller who hasn't identified their
item is usually happy to oblige.

---

## Mode 3: Pasted Posts (Facebook Marketplace and anywhere else automation is off-limits)

**When:** Facebook Marketplace, local buy/sell groups, Craigslist, auction house
listings, anywhere Dylan is browsing by hand.

### Input

Paste whatever comes out of the copy. Screenshots work equally well and are often
faster — a screenshot of a Marketplace post carries the photo, title, price, and
location in one object.

Batch them. Ten posts in one message is far more efficient than ten messages,
and lets me rank across the whole set instead of judging each in isolation.

Include if available: asking price, location/distance, how long it's been listed,
and anything the seller said about why they're selling. "Moving, must go this
weekend" is pricing information.

### Output

Same ranked format as Mode 2, with two Marketplace-specific additions:

- **A drafted message to the seller** where one is worth sending — asking for the
  photo that would confirm the ID, or making an offer. Ready to paste.
- **A distance/time note** — Facebook items are local pickup, so the drive is a
  real cost. An item 45 minutes away needs to clear a higher bar than one on the
  way home from Weatherford.

### The Marketplace-specific edge

Facebook sellers are the least sophisticated of any channel — most are households
clearing a room, not resellers. The listing quality is correspondingly poor:
one dark photo, a three-word title, no brand. That's precisely our target
condition. Marketplace is likely the single best hunting ground for this business,
and it's the one that requires the most manual feeding. Worth the friction.

Local pickup also means **zero platform fees on the buy side**, and if we resell
locally, zero on the sell side too. For furniture especially — where shipping
destroys margin — Facebook-to-Facebook is often the highest-margin path available.

---

## What I need to do this well

A few things that make every mode faster:

1. **Tell me the ceiling.** "Nothing over $50 today" changes every verdict and saves us both time.
2. **Tell me the store type.** Goodwill pricing, estate sale pricing, and antique-mall pricing are different games with different max bids.
3. **Say when you're in a hurry.** "Two minutes, I'm in line" gets a three-word answer. "Working through this tonight" gets the full analysis.
4. **Send the outcome.** What you bought, what you paid, and later what it sold for. That closes the loop and it's the only way the brand reference and my calibration improve. See `data-collections.md`.
