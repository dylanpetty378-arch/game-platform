# Standing Searches — Hunting Grounds

These are repeatable queries built on one idea: **the seller's own words give away
that they don't know what they have.** Run them on a schedule, skim the new
results, send me anything that looks like something.

All eBay URLs below use these parameters:

| Parameter | Meaning |
|---|---|
| `_nkw=` | the search terms (spaces become `+`, quotes become `%22`) |
| `_sop=10` | sort by **newly listed** — this is the setting that matters for hunting; you want to be early |
| `_sop=1` | sort by ending soonest — use for auctions |
| `_udhi=` | maximum price |
| `LH_BIN=1` | Buy It Now only |
| `LH_Sold=1&LH_Complete=1` | **sold comps** — swap these in to check what something actually went for |

Change `_sop=10` to `LH_Sold=1&LH_Complete=1` on any query below to flip it from
"what's for sale" to "what it's worth."

---

## A. Seller-doesn't-know language

The purest version of the edge. These phrases appear in listings where the seller
has openly told you they haven't researched the item.

- [unmarked vintage](https://www.ebay.com/sch/i.html?_nkw=unmarked+vintage&_sop=10&_udhi=60)
- [no markings antique](https://www.ebay.com/sch/i.html?_nkw=no+markings+antique&_sop=10&_udhi=60)
- [not sure what it is](https://www.ebay.com/sch/i.html?_nkw=not+sure+what+it+is&_sop=10&_udhi=60)
- [unknown maker vintage](https://www.ebay.com/sch/i.html?_nkw=unknown+maker+vintage&_sop=10&_udhi=75)
- [estate find unmarked](https://www.ebay.com/sch/i.html?_nkw=estate+find+unmarked&_sop=10&_udhi=75)
- [grandmas estate lot](https://www.ebay.com/sch/i.html?_nkw=grandmas+estate+lot&_sop=10&_udhi=75)
- [attic find vintage lot](https://www.ebay.com/sch/i.html?_nkw=attic+find+vintage+lot&_sop=10&_udhi=75)
- [mystery lot vintage](https://www.ebay.com/sch/i.html?_nkw=mystery+lot+vintage&_sop=10&_udhi=60)
- [cleaning out house vintage](https://www.ebay.com/sch/i.html?_nkw=cleaning+out+house+vintage&_sop=10&_udhi=75)

## B. Misspellings

Sellers who can't identify an item frequently can't spell it either, and their
listings are invisible to every other buyer searching the correct spelling. These
are the highest-yield misspellings in our categories — all of them common enough
to return real results.

- [pendelton](https://www.ebay.com/sch/i.html?_nkw=pendelton&_sop=10) — *Pendleton*
- [haywood wakefield](https://www.ebay.com/sch/i.html?_nkw=haywood+wakefield&_sop=10) — *Heywood-Wakefield*
- [griswald cast iron](https://www.ebay.com/sch/i.html?_nkw=griswald+cast+iron&_sop=10) — *Griswold*
- [broyhil](https://www.ebay.com/sch/i.html?_nkw=broyhil&_sop=10) — *Broyhill*
- [rosevile pottery](https://www.ebay.com/sch/i.html?_nkw=rosevile+pottery&_sop=10) — *Roseville*
- [la creuset](https://www.ebay.com/sch/i.html?_nkw=la+creuset&_sop=10) — *Le Creuset*
- [maranz receiver](https://www.ebay.com/sch/i.html?_nkw=maranz+receiver&_sop=10) — *Marantz*
- [pirex](https://www.ebay.com/sch/i.html?_nkw=pirex&_sop=10) — *Pyrex*
- [danish moderne](https://www.ebay.com/sch/i.html?_nkw=danish+moderne&_sop=10) — *Danish Modern*
- [mid centry modern](https://www.ebay.com/sch/i.html?_nkw=mid+centry+modern&_sop=10) — *mid century*

Worth adding to this list every time you notice a new one in the wild. Log them
in `signals.csv`.

## C. Category + era, no brand named

Items described by material and look rather than by maker. Filter hard on price.

- [mid century dresser](https://www.ebay.com/sch/i.html?_nkw=mid+century+dresser&_sop=10&_udhi=150)
- [vintage teak](https://www.ebay.com/sch/i.html?_nkw=vintage+teak&_sop=10&_udhi=100)
- [walnut credenza](https://www.ebay.com/sch/i.html?_nkw=walnut+credenza&_sop=10&_udhi=200)
- [vintage art glass vase](https://www.ebay.com/sch/i.html?_nkw=vintage+art+glass+vase&_sop=10&_udhi=40)
- [vintage stoneware crock](https://www.ebay.com/sch/i.html?_nkw=vintage+stoneware+crock&_sop=10&_udhi=50)
- [single stitch tee](https://www.ebay.com/sch/i.html?_nkw=single+stitch+tee&_sop=10&_udhi=25)
- [vintage wool jacket made in usa](https://www.ebay.com/sch/i.html?_nkw=vintage+wool+jacket+made+in+usa&_sop=10&_udhi=40)
- [vintage receiver silver face](https://www.ebay.com/sch/i.html?_nkw=vintage+receiver+silver+face&_sop=10&_udhi=125)

## D. Lots — where one item carries the value

Lot listings are priced on the average and won on the outlier. A $30 box of
twelve items where one is worth $200 is a good trade even if the other eleven go
to the donation pile.

- [vintage pyrex lot](https://www.ebay.com/sch/i.html?_nkw=vintage+pyrex+lot&_sop=10&_udhi=75)
- [vintage jewelry lot signed](https://www.ebay.com/sch/i.html?_nkw=vintage+jewelry+lot+signed&_sop=10&_udhi=50)
- [vintage toy lot](https://www.ebay.com/sch/i.html?_nkw=vintage+toy+lot&_sop=10&_udhi=50)
- [vintage clothing lot](https://www.ebay.com/sch/i.html?_nkw=vintage+clothing+lot&_sop=10&_udhi=60)

---

## Facebook Marketplace — manual, and worth it

Marketplace can't be automated and shouldn't be. Run these by hand in the app;
they're the same logic adapted to how people write local listings.

Search terms worth saving: `vintage`, `antique`, `old dresser`, `estate`,
`moving must go`, `grandma`, `mcm`, `mid century`, `teak`, `walnut dresser`,
`record player`, `stereo receiver`, `pyrex`, `cast iron pan`.

Filters that matter: sort by **newest**, set a tight radius first (things close to
Keller or on the Weatherford commute), and set a price ceiling.

The tells in a Marketplace listing:

- A three-word title and one dark photo
- No brand named anywhere in the description
- "Moving," "must go," "this weekend," "curb by Sunday" — time pressure is price pressure
- Priced at a round number ($20, $50) rather than a researched one
- Posted by someone with no other listings — a household, not a reseller

Screenshot anything that hits two or more of those and send me the batch.

---

## Cadence

| Frequency | What |
|---|---|
| Daily, 5 min | Facebook Marketplace, newest, tight radius |
| 2–3× per week | Section A (seller-doesn't-know) and Section B (misspellings) |
| Weekly | Section C and D |
| When something sells | Log it, and check whether the search that found it deserves a permanent spot here |

Searches that stop producing get deleted. Searches that produce get sharpened.
This document is meant to change.
