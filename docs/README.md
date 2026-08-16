# Documentation

Design documents for the game platform. Nothing is built yet; these exist to make sure it gets built once.

## Read in this order

**Start here if you've never seen any of this: `the-game.md`** — what the game actually is, in plain terms, with no architecture and no jargon. Ten minutes.

---

**0. `dictionary.md`** — the permanent reference for anyone building it.

Every term in the system is defined here exactly once, every list the system needs appears here whether it is settled or not, and **Part 12 is the decisions log** — every decision with the reasoning that produced it. If another document disagrees with this one, this one wins.

Parts 2A, 2B and 2C are the core mechanism: how anything affects anything, when things land, and how an attempt resolves. Part 11 is the thirty numbered lists, twenty-eight of them live. Part 12 is where to look before reopening anything.

**1. `orientation.md`** — the same thing explained, at length, in plain language.

Written to be read straight through, for systems literacy rather than software-engineering background. Covers what is being built and why the design is shaped this way, the reasoning behind each piece, the assumptions made along the way that were never confirmed, and every open question.

**2. `architecture.md`** — the reasoning and the engineering.

Not the vocabulary — that moved to the dictionary, because two homes for one vocabulary drifted apart within weeks. This document is *why the shape is what it is, what it costs, what breaks if it changes, and how it gets built*: the Substrate boundary (§4), **Sockets** (§6A), Verbs and Listeners (§7), ordering (§8), determinism (§9), the technology stack and why (§10), **instrumentation and playtesting** (§11A), Claude's access to production (§12), testing (§14), mobile (§15), commercial (§16), and the open questions (§18).

**3. `substrate-checklist.md`** — the working list.

Everything that has to exist in the Substrate. **Sections A through I are answered**, each with a banner saying where the detail now lives; Section J (instrumentation) is new. What remains is the lists, and the *Order of work* at the end says which order they have to be done in — with the Verb set closing **last**, not first.

**4. `phase-map.md`** — today to a public release.

Every phase, what gets done in it, the gate that has to be met before the next one starts, and what kills each. **Deliberately no hours and no dates** — the sequence is the useful part, because it is a dependency order. Ends with the four places scope can be cut and what each costs.

**5. `open-questions.md`** — everything undecided, in one place.

Organised by *when the answer is needed*: repair decisions that are broken today, decisions made while filling the lists, decisions needed before any code, decisions needed before launch, and the questions only Dylan can answer. Each gives the options and their consequences.

**6. The working documents** — startable now.

- **`work-repair.md`** — the Phase 0 worklist. Ten items, each with the failing test to run before deciding and the passing test that confirms the fix.
- **`work-lists.md`** — the Phase 1 guide. Companion to `substrate-lists.xlsx`: what each list is deciding, the test each entry must pass, and the mistake that is easy to make.
- **`work-tracks.md`** — brand, legal and audience. Everything that has to start now because it cannot be compressed later.

**7. `issues-and-ideas.md`** — an adversarial review of the design, and what it makes possible.

Twenty-three ranked problems. **Four foundation findings (A1–A4) open Phase 0**; **four arithmetic findings (A2, A3, A4, A7)** are the ones demonstrable on paper today. Both sets are Edition breaks once a Campaign exists. Then twenty ideas that fall out of machinery that already exists. Read Part A before writing any code — it is the input to `work-repair.md`.

**8. `branding-research.md`** — naming, trademark, identity, positioning, community.

Grounded in current sources. The load-bearing finding: a book title is not registrable as a trademark, but software and games are exempt from that bar — so the platform framing is a legal advantage and not only a marketing one.



**9. `entity-catalog.md`** — what other games actually track, with real numbers. ~90 systems. Reference rather than argument.

**10. `categorization-and-action.md`** — what five literatures say about representing everything. The research that reframed two blocking decisions.

**11. `tabletop-history.md`** — the history of the hobby, as history. Social, cultural and business rather than mechanical.

**12. `field-survey.md`** — what the world looks like. Nine research passes; three load-bearing findings about cost-versus-value, charging for tabletop software, and distribution as the binding constraint.

## Reference

**`CLAUDE.md`** — the working rules for anyone (human or model) writing code here. Deliberately short. Points back at `dictionary.md` for the vocabulary and Part 12 for the reasoning.

## Status

| Document | Status |
|---|---|
| `the-game.md` | Plain-language explainer. Current. |
| `phase-map.md` | Current. The sequencing document, and authoritative on order. |
| `open-questions.md` | Current. Every undecided thing, by when it is needed. Part 1 is closed. |
| `work-repair.md` | **Phase 0 is closed.** The record of what was decided in Repair, and why. |
| `work-lists.md` | Current. **Phase 1 — startable now that Phase 0 is closed.** |
| `work-tracks.md` | Current. Brand, legal and audience — startable today. |
| `issues-and-ideas.md` | Review, August 2026. Both sets — the four foundation findings and the four arithmetic findings — are carried as decisions in `work-repair.md`. |
| `branding-research.md` | Research, August 2026. Sources cited; thin areas flagged. |
| `substrate-lists.xlsx` | The workbook, one tab per list. Fourteen blocking; L7's resolution region is drafted, the rest unstarted. |
| `dictionary.md` | **The reference.** Thirty numbered lists, of which twenty-eight are live and fourteen are blocking: L1–L5, L7, L18, L21–L23, L25, L27–L29. |
| `orientation.md` | Draft. Long-form explainer; consistent with the rest as of August 2026, but the least frequently updated. |
| `architecture.md` | Draft. Vocabulary deferred to `dictionary.md`. §18 lists the open questions and what has been answered since. |
| `entity-catalog.md` | Research, August 2026. ~90 systems. Uncertain numbers flagged with ⚠️. |
| `tabletop-history.md` | Research, August 2026. Contested accounts flagged in Chapter 15. |
| `substrate-checklist.md` | Working list. **A–I answered, J added.** Remaining work is the lists, in the order given at the end. |
| `categorization-and-action.md` | Research, August 2026. Five literatures; reframed two blocking decisions. |
| `field-survey.md` | Research, August 2026. Sources cited; uncertainty flagged inline. |
| `CLAUDE.md` | Draft — will need revision once code exists. |
| `phase-0-checks.py` | The Phase 0 numeric tests. Run with `python3 phase-0-checks.py`. Becomes golden fixtures when the engine exists — never regenerate to make a test pass. |
| `build_reader.py` | Generator. Rebuilds `design-docs.html` from the Markdown. |
| `design-docs.html` | **Generated — never edit by hand.** Single-file reader over every document above. Rebuild with `python3 build_reader.py`. |

## Conventions for these documents

- **Open questions stay open.** Anything unresolved is listed as unresolved, never smoothed over.
- **Uncertainty is flagged inline**, especially in the field survey, where several areas have no reliable public data.
- **Every term is used exactly** as defined in `dictionary.md`, here and in code. One home for the vocabulary, permanently.
- Decisions get recorded with their reasoning. A decision without a reason cannot be revisited intelligently.
