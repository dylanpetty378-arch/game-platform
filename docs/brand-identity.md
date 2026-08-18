# Vectus — brand identity, the base design principles

*Adopted August 2026 from Dylan's brand board. This document is the canonical transcription and interpretation of that board: everything on it, documented, mapped onto the system, and flagged where it touches a settled decision. The board itself is the visual source of truth — the master file belongs at `docs/brand/vectus-brand-board.png` (to be committed; the values below marked ⚠ should be re-sampled from the master before they are tokenized into CSS).*

**The name is VECTUS.** The system and the platform, one name, exactly as Q5.4 decided. From *vector* — the word the whole design stands on. **Clearance has not been run**: before attachment hardens further, the knockout searches (USPTO classes 009/041/042, domains, handles, the existing Vectus-named companies in other industries) and the intent-to-use filing. That is the only thing between this board and the letterhead.

---

## The words, verbatim

| Element | Text |
|---|---|
| **Name** | VECTUS |
| **Tagline** | Your Story. Your World. Your Way. |
| **Brand essence** | FOCUS ON PLAY. FREEDOM TO CREATE. STORIES THAT MOVE. |
| **System line** | THE VECTUS SYSTEM — Actions are vectors. Stories are results. |
| **Learning line** | Simple to learn. Deep to master. Play your way. |
| **Worlds line** | One platform. Infinite worlds. · Create any world. Any tone. Any style. It's yours. |
| **Category badge** | VTTRPG · Virtual Tabletop RPG · Play together. Anywhere. |
| **Who we are** | "Vectus is a virtual tabletop RPG platform built for players first. Jump into rich worlds or build your own in minutes. Deep when you want it. Simple when you don't. Every action is a vector. Every choice matters. Every story is yours." |
| **The heart of Vectus** | "At the core of every story is you and your choices. Vectors represent your actions, intent, and influence — shaping the world and everyone in it." |
| **Iconography line** | Clean. Clear. Functional. The system at a glance. |
| **Dynamic signal line** | The platform adapts to your world's identity. You set the signal. |

**The four pillars:** **PLAYER FIRST** — built for players, fast to start, easy to play · **ENDLESS WORLDS** — create a setting, any genre, any style · **PLAY YOUR WAY** — rules that flex, depth on tap, you're in control · **ALWAYS READY** — jump in solo, no prep needed, start playing.

**The footer promises:** Built for players, not game masters · Start playing in minutes · Play solo or together — your choice · Go deep or stay simple — your pace · Your world, your rules — your story.

---

## The mark

A **stick figure with vectors radiating from its limbs** — five to six thin arrows leaving the head, hands and feet at different angles, each tipped in a different signal color, the figure standing on **concentric ripple ellipses** (the world responding). It is the whole thesis drawn: a person whose choices push on the world in every direction, and a world that ripples back. A second lockup shows the figure standing above the **layer stack** (tilted translucent planes), tying the mark to the lattice.

Usage seen on the board: mark + wordmark on Void (primary); mark alone on merchandise (dice bag, dice); wordmark VECTUS in wide-tracked caps. The mark reads at favicon size because it is line art — keep it line art.

## Color

**Platform palette** (fixed — the platform itself is neutral, near-monochrome, dark-first):

| Token | Hex (as printed) | Role |
|---|---|---|
| `void` | `#0B0D11` ⚠ *(tiny label — verify against master; reads as 0B0D11 or 080D11)* | The background. Everything sits on Void |
| `paper` | `#F3F2EE` | Primary text on Void; light surfaces |
| `graphite` | `#21242A` | Cards, panels, elevated surfaces |
| `steel` | `#394148` ⚠ *(verify)* | Borders, secondary text, disabled states |
| `signal` | `#22D3EE` | The platform's own accent — links, actives, the cyan in the system diagrams |

**Dynamic Signal (by world):** the platform stays neutral and **each world sets its own signal color** — the board shows seven: orange, red, magenta, purple, blue, teal, green *(no hexes printed; sample from master — they read close to `#F59E0B` `#EF4444` `#EC4899` `#8B5CF6` `#3B82F6` `#14B8A6` `#22C55E` ⚠)*. This is the identity system's best idea: **one brand, per-world accents** — a Setting's entire UI tint changes with its signal while the platform chrome stays Void/Paper/Graphite. It maps directly onto the settled visual-identity strategy (typography-and-layout-led, procedural, per-Setting) and should become a per-Setting field the authoring tools expose.

**Vector colors in the diagrams** follow the signal family: each vector in an illustration gets one signal color, on Void, as a thin line with a small arrowhead and a dot at origin.

## Typography

| Face | Role | Note |
|---|---|---|
| **Aeonik Bold** | Display, headings, the wordmark's world | ⚠ **Commercial font — license required before shipping.** If unlicensed, the closest open stand-ins for the beta era are Space Grotesk or Archivo; decide before any public page |
| **Inter Regular** | Body, UI, numbers | Free (OFL), ships everywhere, already the de-facto UI face |

Display type is set in caps with wide tracking for labels (the board does this everywhere: THE VECTUS SYSTEM, BRAND ESSENCE), sentence case for body.

## Iconography

Thin-line, geometric, single-weight, no fill — drawn from the same pen as the mark. The board's set: the vector burst, the layer stack, party/people, polyhedral dice, fire, sword, shield, hourglass, flask, book, crown, skull. Rule from the board: *clean, clear, functional — the system at a glance.* Icons are UI, not illustration; the illustrated genre panels are the only place rich art lives.

## The Vectus System — the eight steps, and what they are underneath

The board's centerpiece: the pipeline explained to a player in eight steps of plain language. **This is the play-register vocabulary the jargon research demanded** (Q5.6) — the words a player meets, with the engine vocabulary staying documentation-side. The mapping is exact, which is why it works:

| # | Step | Board copy (verbatim) | What it is in the engine |
|---|---|---|---|
| 1 | **INTENT** | "You decide what to do. That's your vector." | Declaring an attempt / creating a vector |
| 2 | **DIRECTION** | "You aim it. Direction gives it purpose." | Attempt Points allocation; a Channel's position — direction is the proportion spent |
| 3 | **FORCE** | "You commit. Magnitude gives it strength." | Magnitude — the Attempt roll |
| 4 | **INTERACTION** | "It meets the world. Forces collide, assist, or resist." | Cancellation, Enhancement, Participation, Guards |
| 5 | **LAYERS** | "Everything exists on layers. Position changes outcomes." | The 41-slot lattice — E/M/C/R/X |
| 6 | **RESOLUTION** | "The system calculates. Conflicts resolve. Results emerge." | The R-region pipeline, server-folded |
| 7 | **OUTCOME** | "The world changes. Consequences become reality." | Landing — Tracks pushed, bands crossed, Records written |
| 8 | **YOUR STORY** | "You keep going. Every choice writes your story." | The append-only Ledger; the Chronicle |

Vocabulary rule that falls out: **player-facing surfaces use the eight step-words plus *vector*, *magnitude*, *direction*, *layer*, *chance*; the engine register (Substrate, Fold, Facet, Verb, Moment, Channel…) never appears on a player screen.** The board's own UI mock keeps this discipline.

## UI language (from the board's mock)

The action card pattern — the product's atomic readout:

```
Action: Strike          Vector ID: A-17
Magnitude   7/10        Direction   52°
Layer       3/5         Chance      68%
Status: In Progress                [Continue]
```

Plus: a party rail (portraits with each member's current vector as a small arrow), and a **color-coded event log** ("Kian strikes / Lyra assists / Bandit defends / Result: Success") — the log is a first-class UI element, which matches the Ledger being the product's heart. The **Chance %** readout is the Resolution Socket's published distribution surfacing in the UI, exactly as rule 19 requires. *(Note: "Magnitude 7/10", "Direction 52°", "Layer 3/5" are brand-mock notations, not settled mechanics — direction-as-degrees is an illustration of the idea, not the fifteen-Dimension reality. The pattern to keep is the card, the four-stat readout, the status line and the log — the exact fields get decided when the release UI is designed.)*

**The beta deliberately ignores all of this.** `beta-spec.md` stands: the developer build is ugly on purpose. This identity applies from the first public-facing surface onward (Phase 7 UI, the website, the posters).

## One platform, infinite worlds — the genre range

Ten illustrated panels, each in a genuinely different art style, each with its two-line pitch: **Mythic Fantasy** (swords, magic, and ancient legends) · **Cyberpunk** (neon dreams, corporate nightmares) · **Space Opera** (stars to explore, factions collide) · **Western** (dust, danger, and hard choices) · **Noir** (shadows, secrets, and nothing is clean) · **Anime** (epic journeys, unbreakable bonds) · **Comic Book** (bigger than life, make your mark) · **Pixel Art** (retro worlds, timeless adventure) · **Abstract** (strange, beautiful, beyond words) · **Horror** (fear, dread, and the unknown).

This is the *horizon*, not the roadmap — `phase-map.md` still ships **one** Setting deep enough to run a real campaign, then six free at v1. The panels' job is to prove the Substrate's claim visually: one engine, any genre, any tone, and the art style changes with the world while the chrome does not. Per the no-AI rule, the shipped versions of any such panels are commissioned human art or procedural-from-code — the board's panels are direction, not assets.

## Brand applications (seen on the board)

Web hero (essence statement + PLAY NOW on Void) · mobile app (the mark as icon) · **physical merchandise: a dice bag and custom dice** carrying the mark — which fits Dylan's stated plan (posters and physical promo, no physical shop). Physical dice for a game whose rolls are digital is the right kind of merch: an emblem, not a component.

---

## Flags — where the board touches settled positions

Documented rather than silently resolved; each is Dylan's call, with a recommended reconciliation:

1. **"Virtual tabletop RPG platform" and the VTTRPG badge** sit directly against the settled positioning rule *refuse the VTT frame* (`branding-research.md`; `the-game.md`: "It isn't a virtual tabletop"). The reconciliation that keeps both: **VTTRPG is a coined category, not a membership claim** — Vectus is not a virtual tabletop that hosts other people's games; it is a *virtual tabletop RPG*, a game that **is** its own platform. The body copy already says this ("built for players first… every action is a vector"). If the badge stays, the category story must be told that way everywhere, or the comparison shopping lands us next to Roll20 and Foundry, which is the exact frame the research says loses. **Recommended: keep the badge, own the coinage, never say "VTT" unmodified.**
2. **"Built for players, not game masters"** — a sharp positioning line, and the game *has* GMs (the GM names the Domain; GM tools are half the beta). Read it as "no GM homework required," which the design genuinely delivers (authored Thresholds, standing orders, async reports). Keep the line; never let the product make it a lie for the person running the table.
3. **"Jump in solo" / "Play solo or together"** — a **new product promise**. The corpus never scoped solo play. Standing orders + async + authored content make a solo mode plausible, but somebody has to build the GM-less loop. Logged as **Q4.5** in `open-questions.md`; the brand should not outrun the roadmap on this one until it is scoped.
4. **"Build your own in minutes"** — consistent with the settled authoring line (*users author instances, never types*), and "minutes" becomes a real UX budget for the authoring tools. Noted in the Q4.4 territory.
5. **Aeonik requires a license** (flag 1 under Typography). Budget it or pick the stand-in before anything public.
6. **Vectus clearance** — the gating item, unchanged.

---

*Supersedes the candidate-generation section of `brand-drafts.md` (kept as the record of the search). The no-AI statement and first-post drafts there stand, and should be re-voiced with the Vectus name once clearance passes.*
