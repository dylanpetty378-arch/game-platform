# The rules explainer — "How Vectus Works"

*The public `/learn` section. TTRPG people love the nitty-gritty, so this section goes all the way down — from the one-paragraph pitch to the 41-slot lattice — and because it is the playtest era, it wears its provisionality proudly: every tunable number on every page carries the PLAYTEST chip, and a standing banner says the honest thing: "You are reading a game that is being built. These numbers move. Here is the log of when they moved."*

## The two principles

1. **The widgets run the real engine.** `/learn` imports the same `/ruleset` package the server folds with. When a page demonstrates cancellation, the reader drags a fire magnitude against an ice magnitude and the actual pipeline computes it, expansion and all. Nothing is a mock; nothing can drift from the shipped rules, because it *is* the shipped rules. This is the site's single best trust move and the whole reason the explainer is buildable at all.
2. **Two registers, strictly.** Pages speak the play register — the eight steps, *vector, magnitude, direction, layer, chance* (`../brand-identity.md`) — and each page ends with a collapsible **"The nitty-gritty"** block that opens the engine register (Channels, Tracks, Guards, the lattice) for the readers who want it. The deep-dive chapters live entirely in that second register and say so. The jargon budget is enforced editorially: a play-register page introduces at most two new words.

## Structure

```
/learn                       The hub: what Vectus is, the eight steps as cards, reading paths
/learn/start                 "The game, in plain terms" — the-game.md, adapted, with the lock
                             demo LIVE: 4 points, three bars, drag your split, see the story change
/learn/steps/1..8            One page per step (Intent → … → Your Story), each with copy from
                             the brand board, a live widget, and its nitty-gritty block:
                               2 DIRECTION  → allocation playground (Attempt Points across Dimensions)
                               3 FORCE      → the dice lab: swap the roll expression, see the
                                              published distribution redraw (the Socket contract, visible)
                               4 INTERACTION→ fire-vs-ice cancellation slider; assists and Guards
                               5 LAYERS     → the lattice, drawn; hover any slot for what it does
                               6 RESOLUTION → a full worked resolution, every slot expandable
                               7 OUTCOME    → Tracks and bands; push a Track, watch "prone" happen
                               8 YOUR STORY → a tiny ledger; scrub time, watch state refold
/learn/deep/*                The nitty-gritty chapters (engine register, proudly):
   /channels                 all 88, auto-generated from the engine's data, filter by Space/Dimension,
                             each channel's position chart; the four help/harm trades called out
   /tracks                   the 14 Tracks, bands, bipolar axes, absence-is-immunity (the vase!)
   /attempts                 Domains, the 15 Dimensions, Specialisations, all-in and downside bars
   /time                     Moments, rounds, Ordered vs Loose, entering Ordered time, Repin
   /economy                  doubloons, cost/timing/cap, the turn allowance (PLAYTEST chip)
   /consequence              Listeners, the 7 forms, cascades, the Brush
   /pipeline                 the full 41-slot reference — the honest whole thing
   /verbs                    the seven, with the "column list of the Entity model" argument
/learn/design                The design log: why-it-is-this-way, linking into the public
                             game-platform docs; the changelog of tunable changes (from the
                             tunable_changes table via a public read endpoint) — build-in-public, in-product
/learn/glossary              every term, one line each, linking to its page; sourced from dictionary.md
```

## How content is built and maintained

- Pages are **MDX-lite**: markdown files in `/client/src/learn/`, compiled at build time, with a small registry of interactive components (`<AllocationPlayground/>`, `<CancellationDemo/>`, `<DiceLab/>`, `<LatticeMap/>`, `<TrackDemo/>`, `<LedgerScrubber/>`, `<ChannelTable/>`) — each ≤200 lines over the engine package.
- **Data-driven pages are generated, never transcribed**: the Channel table, Track/band tables, the lattice map, and the glossary skeleton are rendered from the engine's own exported data. When a Part 12 decision changes a list, the site is right on the next deploy with zero editing.
- Prose is adapted from the corpus (`the-game.md`, dictionary Parts 2A–2C, `worked-builds.md` examples) — **by a human pass**: Claude may draft the adaptation, Dylan approves every player-facing page, same rule as assets.
- Each page footer: "Something confusing? Tell us" → opens a `note` of kind `confusion` anchored to the route (the churn-predicting note kind, collected from readers too).

## Acceptance (this is M7's checklist)

A logged-out visitor can go from `/learn` to understanding the lock example interactively in under two minutes; every deep-dive number matches the engine's data by construction; the dice lab shows the current `attempt_roll` default with its PLAYTEST chip and its real distribution; the pipeline reference lists all 41 slots; and the design-log page shows live tunable history.
