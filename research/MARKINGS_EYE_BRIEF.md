# Markings eye brief: read every small mark sellers ignore

Dylan (Oct 16 2026): look for ANY marking in a photo that the average person wouldn't think twice about but that shows value,
brand, maker, period, first edition or rarity. Start with the catalog:
/home/claude/gp/docs/encyclopedia/entries/markings-catalog-index.md. It tells you, per object type, where marks sit and which
entry decodes them. Read it first, then open only the entries that apply to what you're looking at.

Each panel is ONE listing: every photo the seller posted, tiled, numbered, with the title and current bid on top. Look at every
tile: backs of paintings (canvas stamps, gallery/framer/exhibition labels, customs stamps), print margins (blindstamps, chops,
edition numbers, plate marks), bases and undersides (pottery/porcelain/glass marks, country-of-origin wording, patent and Rd
numbers), copyright pages and jackets, deadwax, labels inside clothing, toy bases and feet, serial plates, tang stamps, case
backs, clasps, seals and box inscriptions. Zoom into any tile with a mark: PIL crop/resize from the source image in img/.

## Flag when a mark changes what the item is
- The mark identifies a maker, edition, period or material worth clearly more (≥3×) than the title implies, and the title
  doesn't already say it. Examples: a "decor oil" with a pre-1882 Winsor & Newton stamp and a gallery label; a "vintage vase"
  with a Grueby or Rookwood mark; a "print" with a Tamarind chop and pencil edition; "old book" with a true first-edition
  statement; "toy car" with a redline Hong Kong base; "camera" with a black-paint Leica serial; "knife" with a Case Tested XX
  tang; a "cup" with Meissen crossed swords and a period form; a "pin" with a 14K stamp.
- Estimate realistic value from the catalog entry. Golden eggs ($1,000+) are the goal, but also flag ≥$150 profit leads.

## Do NOT flag
- Marks the title already names (the seller knows). Common marks that don't add value (Made in China, plain Japan, decorator
  "Bavaria", modern "Lalique France" crystal, Royal Vienna-style beehives on modern pieces, pseudo-hallmarks on plate).
- Authentication items (designer bags, signed sports, Rolex), untested electronics, anything bigger than a passenger seat,
  Nazi items, ivory.
- Unreadable marks with no other evidence.

## Output: one line per flag, appended to your flags file
`<panel number>\t<mark read and where (tile n)>\t<what it means, est. value, why the title misses it>`
Precision over volume: most listings have nothing.
