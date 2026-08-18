# The build documents — how the Vectus website gets made

*Written August 2026. This folder is the buildable blueprint for the entire Vectus website: the game engine, the play surfaces, accounts, authoring, the rules explainer, the database, the hosting — all of it. The test these documents must pass, set by Dylan: **any Claude session, starting cold, should be able to pick up this folder and construct a fully working website from it.** If a session cannot, the missing information is a bug in these documents — fix the document, then build.*

---

## What is being built, in one paragraph

**Vectus** is a tabletop RPG that is its own platform — the rules live in software because nobody can run the vector arithmetic by hand. What gets built is a website: people log in, make characters, play campaigns live or across a week, GMs create the content of their worlds, and a public section teaches the whole system down to the nitty-gritty, because TTRPG people love the nitty-gritty. **Everything right now is playtest**: every surface is 100% transparent, every provisional number is a hard-labeled PLAYTEST tunable changeable on the fly, and every log lands in the database for analysis. This is not "the beta page plus a site around it" — the site *is* the product growing up in public with its developers inside it.

## The documents, in reading order

| Doc | What it settles |
|---|---|
| `README.md` | This file — the map, the bootstrap procedure, the definition of done |
| `stack-and-hosting.md` | The exact stack (already decided in `../architecture.md` §10 — restated operationally), the vendors at the ~$25/month budget, environments, CI, backups |
| `site-map.md` | Every page and surface of the website, who sees it, and what it does |
| `auth-and-roles.md` | Magic-link auth, the role model, and the playtest transparency rule |
| `database.md` | The full schema — every table, with DDL. The `records` event store comes verbatim from `../architecture.md` §10.3 |
| `engine-spec.md` | The pure `/ruleset` package: modules, the Fold contract, canonical serialization + hashing, the PRNG, the integer policy, and the fixture harness |
| `api-and-protocol.md` | The HTTP surface and the owned WebSocket protocol, including reconnect/resync |
| `authoring-pipeline.md` | How every asset gets made — by GMs in the site, and by Dylan + Claude through the *same* pipeline with super-admin access. Components and Settings functionality |
| `rules-explainer.md` | The public "How Vectus Works" section — the full nitty-gritty, powered by the real engine |
| `build-order.md` | The milestones, M0 → M9, each with acceptance criteria. **Build in this order** |
| `claude-md-template.md` | The `CLAUDE.md` that goes at the root of the code repo — the working rules for every session that writes code |

**The design corpus is upstream of all of this.** `../CLAUDE.md` (the working rules), `../dictionary.md` (the vocabulary — used exactly, everywhere, including in code identifiers), `../beta-spec.md` (the three laws and the tunables registry), `../architecture.md` (the reasoning), `../brand-identity.md` (the look and the play-register words). Where a build doc and the corpus disagree, **the corpus wins** — and the disagreement is a finding to report, not to silently resolve.

## Where the code lives

**A new, private GitHub repository: `vectus`** (Dylan's account). The design corpus stays in the public `game-platform` repo; the code repo pins the corpus commit it was built against in its README. Layout comes from `../architecture.md` §11:

```
/ruleset       Tier 1. Pure. No I/O, no imports outside itself. The game.
/components    One directory per Component
/settings      Reference Settings
/adventures    Reference Adventures
/server        Tier 2. Transport, persistence, auth. Thin.
/client        Tier 2. React 19 SPA on Vite.
/authoring     The asset editor surfaces. Structurally cannot author types.
/ops           Admin CLI
/tools         Determinism harness, fixtures, export/import
/spec          Prose specs written BEFORE implementation
/docs          Pointer back to game-platform/docs + the pinned commit
```

## The bootstrap procedure — for any Claude session starting cold

1. **Read, in order:** this file → `claude-md-template.md` (it becomes your working rules) → `build-order.md` (find the current milestone — the repo's `PROGRESS.md` says where things stand) → the specific build docs that milestone cites.
2. **Read the corpus minimum:** `../CLAUDE.md`, `../START-HERE.md`, `../beta-spec.md`. Skim `../dictionary.md` Parts 2A–2C; return to it constantly — **vocabulary is law, in code as in prose.**
3. **Spec first.** Every non-trivial unit gets a short prose spec in `/spec` before implementation (`../CLAUDE.md` demands it; the template repeats it). The build docs are the outer specs; `/spec` holds the inner ones.
4. **Build the current milestone to its acceptance criteria.** Do not skip ahead; the order is a dependency order.
5. **Every session ends with:** tests green, the determinism fixtures green, `PROGRESS.md` updated with what was done and what is next, committed and pushed.

## The three laws (from `../beta-spec.md`) — restated because every surface obeys them

1. **Everything is visible.** No hidden bars, no hidden state, every resolution expandable to every slot. Hidden information is a release-era feature, not a playtest one.
2. **Everything provisional is a hard-labeled PLAYTEST tunable.** Changeable on the fly from the tuning console, logged on change, visibly marked wherever its value surfaces.
3. **Every log lands in the database.** The Ledger for the game; the playtest event log for everything around it.

## Definition of done, for the whole build

The website is *done for the playtest era* when: a stranger Dylan invites can log in with an email link, make a character, join a campaign, and play a session where every resolution is fully expandable; a GM can create a creature, an item, an ability and a Threshold from inside the site and use them the same session; Dylan can bulk-inject Claude-drafted assets through the same validated pipeline with super-admin access; anyone — logged in or not — can read the complete rules in the explainer with live widgets running the real arithmetic; every tunable from `../beta-spec.md` is changeable mid-session; and the analysis queries in `database.md` §Measurements answer A9, A11, A1 and Q3.5 from real logs.
