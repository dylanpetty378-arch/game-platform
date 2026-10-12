# Identification Routing — Looks Like X, Look It Up Here

The purpose of this document is speed. When a photo comes in, the question is
never "what could this be" — it's "where does this category hide its mark, and
which database answers it." This is that routing table.

---

## 0. Universal first moves

These work on anything and should be the reflex before category-specific work.

**Sold comps — the workhorse.** Asking prices are fiction; sold prices are data.
eBay's sold filter is the fastest real number available and works on a phone:

```
https://www.ebay.com/sch/i.html?_nkw=SEARCH+TERMS&LH_Sold=1&LH_Complete=1
```

Add `&_sop=13` to sort newest-first (recency matters — comps decay). Swap spaces
for `+`. This single URL pattern answers more questions than every other resource
in this document combined.

**Reverse image.** Google Lens on the item, and separately on the *mark itself*.
Lens is often better at reading a backstamp than at recognizing the object.

**Search the mark as text, in quotes.** Any string of letters and numbers on the
item — model number, pattern name, mold number — in quotes, plus the category
word. `"SX-780" receiver` beats describing the object.

**Search misspellings.** Sellers who can't identify an item often can't spell it
either. Deliberately searching common misspellings of a brand surfaces listings
no one else is finding. This is one of the cleanest edges available and costs
nothing.

**Absence of a mark photo is itself the signal.** A listing with eight photos and
none of the label is a listing where the seller never looked. Those are the ones
worth a message asking for a photo of the underside.

---

## 1. Furniture and wood

**Where the mark hides — check in this order:**

1. Inside the top drawer — bottom, sides, and the back of the drawer face
2. Back panel, upper corners
3. Underside of the tabletop, seat, or chassis
4. Under seat rails on chairs; inside the apron
5. Paper labels inside cabinet doors (fragile, often partial, still readable)

**Fast era brackets without any mark:**

- **Dovetails:** irregular, slightly uneven, varying widths = hand-cut, older or high-end. Perfectly uniform and evenly spaced = machine-cut, 20th century production.
- **Screws:** all slotted, no Phillips anywhere = likely pre-1940s. Phillips heads went mainstream in the 1930s–40s.
- **"Made in [country]" stamps:** a country-of-origin requirement brackets the era and often the value. "Made in Denmark," "Made in Yugoslavia," "Made in Occupied Japan" (1945–52) are each strong signals.
- **Plywood/particleboard in a carcass:** caps the ceiling. Solid hardwood and veneer over hardwood are where the money is.

**Names that carry a premium — flag immediately:**

Lane (especially the *Acclaim* line), Broyhill (*Brasilia*, *Sculptra*), Heywood-Wakefield,
Drexel (*Declaration*), Dillingham, Founders, Kroehler, American of Martinsville,
Thomasville (mid-century lines only), Bassett (mid-century only), Herman Miller,
Knoll, Baker, Henredon, Stickley, Ethan Allen (older solid-wood lines).

Danish and Scandinavian: look for a stamped "Danish Furniture Makers Control"
mark or "Made in Denmark." Teak with that stamp is worth stopping for.

**Lane cedar chests** carry a serial number, and the date of manufacture is
conventionally read by reversing the serial digits. Worth checking — it dates the
piece instantly and gives the listing a concrete claim.

**Where to look it up:** brand + line name into eBay sold. For mid-century pieces
with no name, search the *form* — "walnut lowboy dresser tapered legs mid century"
— and match visually against sold results.

**What drives value:** mid-century modern walnut and teak >> everything else.
Solid wood over veneer. Original hardware intact. Complete sets. Scale — large
credenzas and long dressers outperform small case pieces.

### Upholstered furniture with no brand name anywhere

The hardest case in the category, and it has a reliable solution. Every piece of
upholstered furniture sold in the US carries a legally required law tag, and it is
almost never removed.

```
LAW TAG → FACTORY NAME → CUSTOMS RECORDS → US IMPORTER
        → IMPORTER ADDRESS → RETAILER → COLLECTION NAME
```

1. **Find the law tag** — underside of the deck, or sewn into the back of the frame. Photograph it readably.
2. **Read what's actually on it.** The tag names the *factory*, not the brand. It also carries a CA registry number, a **date of delivery** that dates the piece precisely, and the full material breakdown. Unlike a copyright date on a toy, that delivery date is the real manufacture window.
3. **Run the factory name through customs records.** Import databases (ImportGenius, Panjiva) publish shipper-to-consignee records, which returns the factory's US customers by name.
4. **Match the importer's address to a retailer.** Importers are often shell names that mean nothing alone — the address is what identifies the retailer.
5. **Search the distinctive piece, not the main one.** A sofa is generic. A round tufted ottoman in matching fabric is a collection fingerprint. When a set won't ID, search the odd piece.
6. **Decode the SKU.** Private-label retailers use readable patterns — piece type + collection + colorway — which lets you derive sibling SKUs you've never seen listed.

Two things that generalize beyond furniture:

- **Scraped product copy is a gift.** Drop-shippers and competitors repost original manufacturer descriptions verbatim, brand references included. Searching a distinctive phrase from a product description *in quotes* leaks the original brand constantly.
- **Replatformed sites lose their history.** A retailer that migrated e-commerce platforms has usually dropped its old catalog; indexed URLs redirect to current collection pages. Don't mine the live site — call the retailer's phone system and ask for the old invoice.

*Worked example: `2026-09-13-hollywood-set-adagio-rug.md` in this project, which ran this
chain from a Vietnamese factory name to a discontinued Home Zone collection.*

**What each step of the chain is worth.** The chain doesn't have to reach a retail
collection name to pay. Each stage adds specificity you can put in a listing, and
specificity is what separates a researched listing from a guess:

| Stage reached | What the listing can honestly say |
|---|---|
| Law tag / manufacturer label found | "Made in Malaysia, manufactured November 2012" — a real date beats "a few years old" |
| Factory identified | "Built by Chuanheng, a Muar, Malaysia furniture maker founded 1990" — real provenance |
| Factory's catalog found | "From their espresso bedroom line" — ties the piece to a documented product family |
| US importer list obtained | Narrows the retailer to a handful, and geography usually picks the winner |
| Retail collection named | The full prize — the buyer can Google it and see the original price |

Even a partial chain earns its time. **Run it before pricing anything**, and let what you
find set the ceiling rather than deciding the ceiling first and skipping the work.

**The one genuine stopping point** is the material, and it's a ceiling, not a reason to
skip the research: particleboard or MDF anywhere structural means the piece will not
command solid-wood money whatever its name turns out to be. Identify it anyway — you
still need the name, the date and the original price to write a listing that holds its
asking price — but calibrate expectations before you spend an afternoon on it.

*Worked example both ways: `sell-list.md` item 06. A Malaysian factory label led to a
real manufacturer with a documented 2012 espresso bedroom line and a shortlist of three
US retailers that could have sold it — genuinely useful listing material. The chain
dead-ended only at shipment-level customs records, which are paywalled, and one question
to the original buyer about which store it came from likely finishes it for free.*

---

## 2. Clothing

Clothing has the best public identification infrastructure of any category.

**Where the mark hides:** neck tag, side seam tag, inner waistband, under the
care label (often a second tag behind the first).

**The RN number.** US garments carry a Registered Identification Number — "RN"
followed by digits. The FTC maintains a public RN lookup that returns the company
that registered it. This identifies the manufacturer *even when the brand name on
the tag means nothing to you*, which is exactly the case we're hunting. Search
"FTC RN lookup" to reach it. **WPL** numbers are the older equivalent and
themselves indicate a pre-1960s garment.

**The Vintage Fashion Guild label resource** —
https://vintagefashionguild.org/resources/vintage-label-resource/ — is a curated,
image-based archive of clothing labels with date ranges. It is the single best
free resource for dating a garment from its tag. Use it whenever a tag design is
unfamiliar.

**Fast era brackets from construction:**

- **No care instruction tag at all** — US care labeling became required in the early 1970s. A garment with no care tag is likely pre-1972.
- **Single-stitch hems** on a t-shirt (one row of stitching at sleeve and bottom hem, not two) — generally pre-mid-1990s. This alone separates a $8 shirt from an $80 shirt.
- **Metal zipper** — pre-1960s leaning; nylon coil zippers took over after. Zipper makers (Talon, Conmar, Scovill) are themselves datable.
- **Union labels** (ILGWU and others) — the label *design* changed over time and dates the garment to a range. VFG has the chart.
- **"Made in USA" on a mainstream brand** — nearly always older than the same brand today.
- **Selvedge edge** on denim (visible clean-finished seam inside the outseam, often with a colored line) — older or premium repro.

**Names that carry a premium:** Levi's (Big E tab = pre-1971, significant),
Pendleton, Filson, Woolrich, Carhartt (older), Harley-Davidson, band and tour
tees, college and sports tees with single stitch, Patagonia (older), L.L.Bean
(Made in USA era), Brooks Brothers (older), Burberry, leather outerwear of any
quality, western wear, workwear of any era.

**What drives value:** graphics and licensing beat blank garments. Condition on
knits is unforgiving — holes and pit stains kill value. Size matters: larger
sizes in vintage menswear sell for more, and vintage sizing runs small.

**Where to sell:** Poshmark, Depop, Mercari, eBay. eBay for anything where the
brand is the story; Depop for streetwear and youth-facing vintage.

---

## 3. Toys

**Where the mark hides:** underside of the base or feet, back of the head, inside
the neck, the small-of-the-back on figures, inside a battery hatch.

**What you'll find there:** a copyright date, a company name, a country of
manufacture, and often a mold number. All four matter. Note that the **copyright
date is the date of the design, not the date of manufacture** — a figure stamped
1977 may have been made in 1995. Use it as a floor, not a date.

**Category-specific:**

- **LEGO** — Bricklink is the authoritative database for both sets and individual parts, with real sold price history. Identify the set number if the box is present; if not, distinctive parts and minifigures carry the value, and Bricklink's part catalog IDs them.
- **Hot Wheels** — the base carries the year and country. "Redlines" (a red stripe on the tire, 1968–1977) are the premium era.
- **Barbie and fashion dolls** — markings on the buttocks and the back of the head give year and country.
- **Star Wars (vintage 1977–1985)** — country-of-origin stamp on the figure and the condition of any accessories drive value enormously.
- **Fisher-Price** — Little People and pull toys from the wood-and-litho era outperform later plastic.
- **Funko Pop** — the number on the box plus "vaulted" status; most are worth little, a few are worth a great deal.
- **Model kits and board games** — completeness is everything. Sealed or complete-with-all-pieces versus not is a 5× swing.

**What drives value:** completeness, the box, and sets over singles. A single
loose figure is usually a pass; a complete set of them is not.

---

## 4. Pottery, glass, china, and housewares

This is the richest category for the specific arbitrage we're running, because
value is almost entirely locked in marks and pattern names that sellers don't
read.

**Where the mark hides:** the base, always. Turn it over — that's the whole game.
Also the inside of lids, and the underside of handles on hollowware.

**The key resources:**

- **Replacements.com** — an enormous searchable database of dinnerware, crystal, and silver patterns, searchable by manufacturer and browsable by pattern image. If you can read the backstamp, this names the pattern; if you can only see the pattern, you can often match it visually. It also lists per-piece retail values, which are high but directionally useful.
- **Kovels** — antique marks and price guide, partially free.
- **WorthPoint** — a deep archive of sold prices across auction and marketplace history. Paywalled, but the search previews often reveal enough.
- **LiveAuctioneers / Invaluable** — realized auction prices, free to search.

**Fast reads:**

- **Pontil mark** (a rough scar on the base of glass) = hand-blown, older.
- **Seams** running up the side of glass = machine-molded, later.
- **Pyrex** — pattern name is everything. Certain patterns sell for many multiples of others in identical condition. Vintage US pieces are marked "PYREX" in capitals; the lowercase "pyrex" mark indicates a different era/origin. Promotional and short-run patterns are the prizes.
- **Fire-King, CorningWare, Corelle** — each has collectible patterns and worthless ones; the pattern name decides.
- **Fiesta (Homer Laughlin)** — color determines value more than form. Discontinued colors carry large premiums.
- **Cast iron** — Griswold and Wagner are the names. Check the logo style and the presence of a heat ring on the base. A cleaned, flat, crack-free vintage skillet is reliably sellable.
- **Silver** — "925" or "Sterling" is real silver and has a floor at melt value. "Silverplate," "EPNS," "quadruple plate" generally does not. Read the mark before getting excited.
- **Roseville, McCoy, Weller** — beautiful, valuable, and **heavily reproduced**. Treat an unverified piece as speculative. Repros typically have softer detail and a different base finish.

**What drives value:** pattern name, color, completeness of a set, and the
absence of chips. One chip on the rim of a display piece removes most of the
premium.

---

## 5. Electronics and audio (working only)

**Where the mark hides:** rear panel plate, underside, inside the battery door.
The **model number** is the entire ballgame — within a single brand and year, the
spread between a low model and a flagship is often 20×.

**Resources:**

- **HiFi Engine** and **Audiokarma** — specification databases and community knowledge for vintage audio, indexed by exact model number.
- eBay sold, searched on the bare model number in quotes.

**Names worth stopping for:** Marantz, Pioneer (SX series receivers especially),
Sansui, Technics (SL turntables), McIntosh, Kenwood (older silver-face), Luxman,
Thorens, Harman Kardon (older), Klipsch, JBL, Advent, Bose (older only).

Silver-faced receivers from the 1970s are the sweet spot. Also: vintage film
cameras (check KEH for pricing), older synthesizers and drum machines, and
professional audio gear.

**Our constraint applies hard here:** it must already work. Test before buying if
at all possible — plug it in, confirm it powers on, confirm every channel. A
non-working flagship receiver is a repair project, and repair is out of scope
regardless of how good the numbers look on paper.

---

## 6. Art, prints, books, and paper

- **Art** — photograph the signature and search it on **askART** and **Artnet**; check **LiveAuctioneers** for realized prices. Distinguish an original from a print: look at the surface under raking light for brushstroke texture, and look for a regular dot pattern under magnification (a print).
- **Books** — the ISBN if present; otherwise the title page and the copyright page. First editions are identified by "points" that vary by publisher — the number line on the copyright page is the usual tell. **AbeBooks** sold listings for pricing.
- **Prints, posters, maps** — edition numbering in pencil in the margin indicates a limited edition. Original vintage posters (linen-backed, period printing) versus modern reproductions is the key distinction.

---

## 7. Jewelry (costume and signed)

Out of scope for fine jewelry requiring gem authentication. **In scope** for
signed costume jewelry, which is a genuine information-arbitrage category.

**Where the mark hides:** the clasp, the back of the pendant or brooch, the inner
band of a ring, the underside of a clip earring.

**Names that carry a premium:** Trifari, Weiss, Coro, Sherman, Eisenberg,
Schiaparelli, Miriam Haskell, Juliana (unsigned but identifiable by construction),
Bakelite (test carefully), Native American silver with a hallmark.

**Precious metal marks** — 925, 800, 14K, 10K, 18K — establish a floor at melt
value and are worth reading on every piece.

---

## The shoot list

When Dylan is in a store and the item can't be identified from the shelf photo,
the fastest possible loop is a second photo of the right thing. By category:

| Category | Shoot this |
|---|---|
| Furniture | Inside the top drawer (bottom + sides), back panel corners, a dovetail close-up |
| Clothing | Neck tag, care tag, any second tag behind the first, sleeve/bottom hem stitching |
| Toys | The underside of the base or feet; the back of the head on figures |
| Pottery/glass/china | The base. Just the base, in focus, filling the frame |
| Electronics | The rear panel model plate |
| Art | The signature, and the lower margin of the paper |
| Jewelry | The clasp or the back, close enough to read |

A blurry mark photo is worthless — it has to be readable. Better to take three of
the base than one of the whole shelf.
