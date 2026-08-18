# The Phase Map

*Every phase from today to a public release. What gets done in each, what has to be true before the next one starts, and what kills it.*

No hours and no dates. The sequence is the useful part — it is a **dependency order**, and every arrow in it exists because doing the later thing first wastes the earlier one.

---

## The whole thing at a glance

```
   0  REPAIR            fix what the review found broken
   1  THE LISTS         decide everything that can never be revised
   2  PAPER             play it without software
   3  THE SPIKE         Substrate, Sockets, instrumentation
   4  THE RULESET       the base game, built as Components
   5  CLOSED PLAYTEST   real groups, real months
   6  CONTENT           the first thing a stranger can buy
   7  OPEN BETA         public, free, and onboarding
   8  RELEASE           paid, marketplace open

   BRAND & LEGAL   ─────────────────────────────────────▶  starts now, never stops
   AUDIENCE        ─────────────────────────────────────▶  starts now, never stops
```

**Two rules about this order.**

Everything in Phases 0 and 1 is **additive-only forever**. Once a Campaign exists, none of it can be revised — only added to. That is why they come first and why they are worth being slow about.

**Every phase produces something worth having even if the next one never happens.** A finished ruleset played on paper is a thing. A half-built engine is not. If the project stops, it should stop at a phase boundary.

---

# Phase 0 · Repair — **COMPLETE, August 2026**

**Fix what the adversarial review found before anything is built on top of it.**

**Four foundation findings — A1, A2, A3, A4 —** each move, add or remove a lattice slot, and all four become Edition breaks the moment a Campaign exists. (They are not the same set as the *four arithmetic findings* named at the end of `issues-and-ideas.md`, which are A2, A3, A4 and A7. Three overlap; A1 and A7 do not.) Full detail in `issues-and-ideas.md` Part A; the decision-by-decision worklist is `work-repair.md`.

### What gets done

- **A1 — Allocation Points.** Decide whether whole points stay, and if they do, what happens to the granularity waste and to the all-in dominant strategy.
- **A2 — Uncapped pre-Guard cancellation.** Decide what bounds standing self-scoped vectors. Nothing currently does.
- **A3 — Flat Guards versus mixed Channels.** Decide whether a Channel in the interior of a Dimension Space can ever be worth placing.
- **A4 — Enhancement Capacity's three holes.** Absolutes are added after the clamp; Baselines sit outside it; Capacity is captured from the source and is therefore shoppable.
- **The determinism set** — A6, A7, A10, A16. Apportionment when shares do not divide evenly; the fixed-point multiplication at R-900; the order of Shaping's three forms; log-integer addition and associativity.
- **Re-attack.** The findings above came from an adversarial pass, not from the design conversation, because the design conversation was collaborative. Make the adversarial pass a habit: settle something, then try to break it, then move on.

### The gate

Every Phase 0 finding — A1, A2, A3, A4, A6, A7, A10, A16 — **either fixed, or explicitly accepted in writing with the reasoning.** *Accepted* is a legitimate answer. *Not yet looked at* is not.

### What kills this phase

Reading the findings, agreeing with them, and moving on to the more interesting work. These are unglamorous fixes and this is the last cheap moment for them.

---

# Phase 1 · The Lists — **COMPLETE, August 2026**

**Decide everything that can never be revised.**

Thirty-two numbered lists, of which thirty are live and sixteen are blocking. The workbook is `substrate-lists.xlsx` — one tab per list, the right columns, an example row. The companion guide is `work-lists.md`: what each list is for, the test each entry has to pass, and how to know it is done.

### What gets done, in this order

The order is a dependency order, not a preference.

1. **L21 Dimension Spaces.** Which kinds of push can meet each other at all. Coarse, quick, and upstream of everything.
2. **L29 Capacities.** What a character is made of *and* the Dimensions of the attempt Space — which is why L21 comes first. Every candidate passes the four-way test: person, ship, faction, storm.
3. **L22 → L23.** The Dimensions inside the remaining Spaces, then the Channels placed in them.
4. **All of Phase 1 closed in August 2026** except L6, which is drafted (seven Verbs) and closes in Phase 2 against real content, and L4, which is provisional at twenty-four and also closes against content.
5. **L1 → L2 → L3.** Categories, Universal Attributes, Category Attributes.
6. **L5 Tracks, L18 Aggregation and L25 landing models settled; L4 Tags provisional at twenty-four.**
7. **L7's remaining regions.** The lattice outside resolution: progression, economy, movement, knowledge, standing.
8. **L26 Listener conditions**, plus the cascade limit and the evaluation order across simultaneous Listeners.
9. **L6 Verbs — last.** Every list above produces the worked examples that are the only real evidence of completeness. Freezing the Verb set before them means freezing it against imagination.

### Two things done alongside the lists

**The three character sheets — deferred into Phase 2, deliberately.** The plan was to write the character sheet first, at the most detailed Lens imaginable, then one for a ship and one for a faction: the values all three need are the Capacity set, and the ones only a person needs reveal whether the Substrate is genuinely kind-agnostic or a person schema in a costume. That test still runs — but sheet content is downstream of character creation, which is undesigned, so the sheets are written as the first pieces of the Phase 2 paper kit instead, where they must exist anyway.

**The jargon count.** Every invented word is a word a new player has to meet. Keep a running count and a first-contact budget — research on jargon says inline definitions do not repair the damage, so a glossary will not save it. Only meeting fewer words at once will.

### The gate — met August 2026, as renegotiated

Every blocking list filled — with L4 provisional at twenty-four, closing against content. The Verb set drafted at seven, closing **in Phase 2** by running every entry from every other list plus the played content through the closing procedure — closing it against imagination was the mistake the rule exists to prevent. The three character sheets deferred into the Phase 2 paper kit, where they are the first deliverable.

### What kills this phase

**Skipping to code.** This is the phase that feels least like progress and is the most irreversible.

**Making the lists too big.** Eight Capacities is a choice a player makes at a glance. Twenty is a spreadsheet. The instinct while filling a list is always to add one more.

---

# Phase 2 · Paper

**Play it without any software.**

Index cards, a shared spreadsheet, and people who will tell the truth. This is the only phase that tests whether the game is any good, and it is the cheapest one.

### What gets done

- **The paper kit**: the three deferred character sheets (person, ship, faction — the Phase 1 debt, discharged where it is naturally due), a resolution walkthrough, a page of Channels, a page of Thresholds a GM can reach for, a one-page cheat sheet, and a **paper approximation note** stating exactly which pipeline rules are suspended at the table, so a misfit found on paper can be classified as a design finding rather than an artifact of the shortcut.
- **Sessions with people who are not you.** At least one group with no stake in your feelings.
- **The questions this phase answers**, and nothing else can:
  - Does splitting attention feel like a decision or like homework?
  - Does a hit that lands two turns later create tension or confusion?
  - Can a GM invent an object's Thresholds in the ten seconds a table will wait?
  - How long does one resolution actually take?
  - Does anyone care about the fiction the mechanics produce?
- **The comprehension question, settled with evidence.** The review's A9 finding is that the surface — many axes, hidden bars, a long pipeline — is past every documented tolerance. That is true on paper if it is true at all, and finding out costs nothing here.

### The gate

**A group asks to play again without being asked.**

Not "they were polite." Not "it was fine once I explained it." Someone asked.

### What kills this phase

**Not doing it.** Building the engine first is the most common way a project like this dies — years of machinery for a game nobody confirmed was fun.

---

# Phase 3 · The Spike

**The first code. The Substrate, the Sockets, and the tools that make it tunable.**

### What gets done

**The Substrate.** Ledger, Fold, the uniform Verb shape, Delivery, Deciders, Moments, and the full E-/C-/R- resolution pipeline. **Server-authoritative folding from the first commit** — it is Tier 1 and retrofitting it is not possible.

**Two Socket occupants.** Place and Resolution — the only Sockets there are. Time and Budget became Substrate and Landing was retired into the Track push, so what was once "five occupants" is now two occupants plus the base Ruleset's turn order, budget refresh and landing spec. Nothing loads without the two, so "one or two Components" was never the real scope.

**The instrumentation, here and not later.** Event log with search. Any resolution expanded slot by slot. State inspector at any Moment. Time travel. **What-if** — re-resolve a past moment with one input changed, never writing to the Ledger. Notes anchored to a single slot of a single resolution. Tester accounts. And the determinism harness.

A pipeline with this many ordered slots and interacting ceilings cannot be tuned by reading numbers off a screen. **Build the measuring device before the thing being measured.**

**A deliberately ugly interface.** Ugly enough that you feel no attachment to it, because it gets thrown away.

### The gate

Three questions, answered with evidence rather than opinion:

1. **Does the Substrate express the rules without contortion?** Write three Components you actually want. If any needs a field outside the uniform Verb shape, the Substrate is wrong, and this is the last cheap moment to find out.
2. **Does the same Ledger fold identically on two machines?** Diff the state hash.
3. **Can you answer *why was it 17* in ten seconds, from the tools?**

### What kills this phase

**Building the pretty interface**, which is far more satisfying than the event store and worth nothing yet.

**Skipping the determinism harness** because everything seems to work. The bug it catches is the one that makes players stop trusting the numbers.

---

# Phase 4 · The Ruleset

**The base game, built as Components. This is where the architecture is proved or disproved.**

### What gets done

- **Fifteen to twenty Components**: harm, healing, movement, gear, progression, one magic system, one social system, one economy.
- **Two Lenses over the same Substrate.** A Lens claim is unfalsifiable until two of them disagree, and the calibration obligation — the same distribution over magnitude — is what makes the disagreement testable.
- **Golden fixtures**, colocated with each Component, passing on every target platform.
- **The structural check.** Depth ≤ 2, no cross-Component reads, and everything harm-shaped needing to know about everything else will pull toward one enormous harm Component that everything depends on. If that happens, the boundaries are wrong, and it is visible by Component #10.

### The gate

Fifteen Components, two calibrated Lenses, all fixtures green on all platforms, and **a Component you did not plan for at the start, written without touching the Substrate.**

### What kills this phase

Discovering the Substrate is wrong — which is what this phase is *for* — and working around it instead of going back. Work around it once and every Component after inherits the workaround.

---

# Phase 5 · Closed playtest

**Real groups, over real months, with the tools open.**

### What gets done

- **Tester accounts** with their own logins, total transparency, and a visible marker in every Campaign they touch so a real table is never confused with a test one.
- **Three to five groups**, at least one playing asynchronously — that mode is a business bet the design has never tested, and it is testable cheaply.
- **Notes collected by kind**, including **confusion**, which most systems forget to collect and which best predicts whether someone comes back.
- **The balance work**, done with what-if and session replay rather than intuition. The interacting ceilings cannot be tuned any other way.
- **Onboarding, iterated.** The jargon-load risk lands here first and it lands hardest on the first hour.

### The gate

**A group has played for three months with you not in the room.**

Everything before that is a demo.

### What kills this phase

Building the features testers ask for instead of fixing what they trip over. The notes that matter are the confusion ones, and those never arrive phrased as feature requests.

---

# Phase 6 · Content

**The first thing a stranger can buy.**

### What gets done

- **One Setting**, deep enough to run a real campaign in.
- **One Adventure.**
- **The authoring tools**, to the content contract: users may declare Entities and their Categories and Attribute values, Thresholds on objects, Enhancement and Participation Capacities, Guards, and Standing Order parameters — and **structurally never** a Verb, Dimension, Layer, doubloon cost shape, Timing, Listener template **or Channel**. A Channel's position is permanent once shipped, which makes it a type. The full contract is `substrate-checklist.md` I6. The tool makes the second list impossible rather than merely disallowed.
- **The visual identity**, resolved without AI art and without a large art budget. The systems that solved this problem solved it with **design** — typography and layout led, not illustration led. And this project has an option those did not: visuals **generated by code**, procedural and deterministic, drawn from the same vectors the game already computes.

### The gate

Someone who has never met you runs a full campaign in your Setting using only what shipped.

### What kills this phase

Content is bottomless and it is more fun than the engine. One Setting. Finish it.

---

# Phase 7 · Open beta

**Public, free, and the first exposure to people who owe you nothing.**

### What gets done

Accounts, payments plumbing, moderation, support, the marketplace, and **onboarding — which is the whole phase.** First contact is where this design is most fragile.

### The gate

**Do people come back for a third session?** Second sessions are curiosity. Third sessions are a game.

### What kills this phase

Launching to nobody — which is the audience track's job, and it started at Phase 0.

---

# Phase 8 · Release

**Paid tiers, marketplace open, launch.**

And the thing that matters more than the launch: **the plan for month two exists before month one happens.**

---

# The authoring loop is how the Substrate gets tested

*Standing practice from Phase 2 onward. Written August 2026.*

**Nothing verifies a Substrate except trying to build content on it.** The lists can be internally consistent, the CI gates can all pass, the arithmetic can be provably deterministic — and the whole thing can still be unable to express a spell anybody actually wants. The only test that finds that is writing the spell.

So from Phase 2 on, **every asset made is a test of the structure**, and the loop runs the same way every time:

```
author an asset  →  express it in Substrate terms  →  it fits?
                                                       ├─ yes  → keep going
                                                       └─ no   → that is a FINDING
```

**A misfit is never worked around.** Not with a special case, not with a clever encoding, not with "close enough." That is the rule that already governs Component design — *when something doesn't fit, stop and say so* — and it applies with more force here, because content is where misfits actually surface.

## Volume is the point, and it is why this is tractable

Assets get generated in bulk rather than one at a time — hundreds of creatures, items, abilities and hazards, drafted fast and then checked. **A structure that survives five hand-picked examples has proved nothing. One that survives four hundred generated ones has.**

The generation is cheap. The **verification** is the work, and it has to be mechanical or it will not happen at the volume that makes it meaningful. That is a real deliverable and it belongs in L30: **an expressibility check** — a tool that takes an authored asset and either produces the Verbs, vectors, Channels, Tags and Listeners it compiles to, or reports precisely what it could not express and why.

## Findings come in two kinds, and the difference is everything

| | What it needs | Cost | Window |
|---|---|---|---|
| **Additive** | a new Channel, Tag, State axis, Listener condition form, Moment kind, Domain, Specialisation | Cheap. Additive-only means nothing that already exists breaks | Open **forever** for Component-level items; open **until public** for Substrate-level ones |
| **Structural** | a different Verb shape, a split or merged Dimension Space, a redefined field, a fourth rounding site | Expensive. An Edition break, or worse | **Closes at public launch, permanently** |

**The expressibility check must report which kind a misfit is.** "This needs a new Channel" and "this needs a field the Verb shape doesn't have" look identical from the authoring side and are nothing alike underneath. The first is a Tuesday; the second is a foundation finding and stops other work until it is understood.

## The window, and why it is a hard edge

**Expanding the Substrate is cheap now, expensive during playtest, and impossible after launch.** Campaigns exist after launch; a Substrate change means a Conversion for every one of them, and the Substrate is explicitly never versioned.

So the schedule is not a preference:

- **Phases 2–4** — expand freely. A finding is good news. This is what the phase is *for*.
- **Phase 5–6, closed playtest and content** — expand deliberately, with a written reason. Findings are still expected and still welcome, but each one now costs a re-check of everything already authored.
- **Phase 7, open beta** — additive only, and only where it cannot wait.
- **Phase 8, release** — the Substrate is closed. Everything after this is Components, forever.

**Track both rates, for different reasons.**

**Structural findings** should be falling toward zero through Phases 5–7. If they are not, the Substrate is not ready no matter what the calendar says.

**Additive findings** never stop and should not — that is what additive-only is for — but they are not free either, and the reason is a product reason rather than an engineering one. **Everything shipped in version 1 of the website is free to users.** The first six Settings and every Component built for them are part of the free version; paid Components come after. So every additive item is not just a row in a table — it is shipped content in the free tier, a word a player may meet in their first hour, and a thing that has to earn its place.

That connects straight to the jargon budget: additive-only makes an addition *technically* safe, and says nothing about whether it should exist. **A rising additive rate late in playtest is a signal the vocabulary is sprawling, not a signal the system is flexible.** Watch it the same way, and ask of each one: is this important, or is it merely possible?

---

# The two parallel tracks

Both start now and never stop. Both are cheap per week and impossible to compress at the end.

## Brand and legal

**Name it early** — trademark timelines are months, and intent-to-use filing should happen as soon as the name is chosen.

**The structural advantage worth knowing:** a *title of a single creative work* cannot be registered as a trademark, but **software and games are explicitly exempt from that bar.** Filing as a platform rather than as a book title is registrable where a book title is not. That is a legal argument for the framing, not only a marketing one.

**State the no-AI-content position early**, while it is cheap to say and impossible to fake retroactively.

Details in `branding-research.md`; the startable worklist is in `work-tracks.md`.

## Audience

An audience takes years and cannot be bought at the end. Starting now, at whatever cadence holds, is worth more than a large push at Phase 7.

**Build in public.** The design process is the interesting thing that exists right now, long before there is a game — and it is genuinely unusual.

---

# What has to be true, and when

| End of | This is true |
|---|---|
| **0** | All eight Phase 0 findings fixed or explicitly accepted in writing |
| **1** | Every blocking list filled (L4 provisional); the Verb set drafted, closing last in Phase 2; the character sheets deferred into the Phase 2 kit |
| **2** | **A group asked to play again without being asked** |
| **3** | Two machines fold the same Ledger identically; *why was it 17* answers in ten seconds |
| **4** | An unplanned Component written without touching the Substrate |
| **5** | A group played three months with you not in the room |
| **6** | A stranger ran a full campaign on what shipped |
| **7** | People come back for a third session |
| **8** | Paid tiers live, the marketplace open, and month two planned before month one ends |

**Phase 2's gate is the one that matters.** Everything before it is design, which is cheap and reversible. Everything after it is construction, which is neither. Do not start Phase 3 until someone has asked to play again.

---

# Where scope can be cut, if it has to be

Better chosen deliberately than discovered late. Four places, in order of what they cost:

**Reduce the surface** — fewer Capacities, fewer Dimensions, fewer Channels. Saves work in *every* phase, compounding, and it is the only cut that also reduces the comprehension risk, which is the one thing no amount of code fixes. Costs expressiveness at launch.

**Cut the marketplace from v1** — one Ruleset, one Setting, nothing purchasable. Costs delayed revenue, and revenue is what buys art.

**Cut asynchronous play from v1** — live only, async in v2. Costs the differentiator, and the design is shaped the way it is because of it.

**Cut the Component system from v1** — a monolithic Ruleset, refactored later. This is the architecture. Cutting it makes the project an ordinary RPG with a website. Named for completeness, not recommended.

**If cuts are needed, take the first two together.** They are the only pair that shortens the path without removing what makes the project worth doing.
