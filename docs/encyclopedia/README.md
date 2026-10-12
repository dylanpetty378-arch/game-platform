# Resale encyclopedia – how it works

Dylan's instruction (Oct 12, 2026): research everything we see, write it down per item type so later runs and other models can reuse the work, and judge value from that research. The encyclopedia is for **speed on repeat types, never a filter** – a listing whose type has no entry gets researched, not skipped.

## Files
- In the project, entries are bundled alphabetically into `encyclopedia/encyclopedia-<letters>.md` volumes (one slug per `# ` heading); in the container they are one file per slug under `/home/claude/sweep/encyclopedia/`.
- `index.md` – one row per entry: type, slug, one-line value summary, buy rule, last updated. Read this first.
- `<slug>.md` – one entry per item type (e.g. `cast-iron-skillets.md`, `film-slr-cameras.md`, `fly-reels.md`). Slugs are plural nouns, lowercase, hyphenated.

## Entry template
```
# <Type name>
Updated: YYYY-MM-DD · Sources: <where the research came from>

## What it is / how to recognise it in a photo
Shapes, silhouettes, badges, stamps, logos, where the maker's mark sits, how to tell the valuable makers/models apart from the common ones. Include the words sellers typically use in titles.

## Value ladder (sold prices, not asking)
| Tier | Examples | Typical sold price | Notes |
|---|---|---|---|
| Junk / common | … | $5–20 | most listings |
| Decent | … | … | |
| Collectible | … | … | the ones worth buying |
| Top | … | … | rare; verify before paying |

## Comps (sold, dated)
- YYYY-MM-DD – <item> – $xx (eBay sold / Terapeak / auction)
- …

## What sellers usually miss
The brand/model/variant tells that raise the price and that the untrained seller leaves out of the title.

## Shipping / handling
Weight class, packing risk, typical shipping cost in, platform to resell on, expected fees.

## Buy rule
Buy when: <condition on price vs. tier>. Pass when: <…>. Profit must be ≥ max($50, price) after fees and shipping both ways (Dylan's rule).

## Seen in sweeps
- YYYY-MM-DD – <site> – <title> – $price – verdict (bought / passed / lead) – why
```

## Process for a review agent
1. For **every** cell on a contact sheet, name the item type (coarse) and a best guess at maker/model from the photo.
2. If `index.md` has the type: apply its buy rule and tells. Flag the listing if the photo shows a valuable variant or the price is below the "buy when" line.
3. If it does not, or the item looks like a notable variant the entry doesn't cover: research it (web search for sold prices, price guides, collector sites; note the sources), then **write or extend the entry** and add the row to `index.md`.
4. Report flags as: `idx | price | identification | entry slug | why it clears or might clear | confidence`.
5. Append a "Seen in sweeps" line to the entry for anything researched, cleared or not. The passes are part of the knowledge.

Entries are written in the container under `/home/claude/sweep/encyclopedia/` and pushed to the project (`encyclopedia/<slug>.md`) at the end of each run.
