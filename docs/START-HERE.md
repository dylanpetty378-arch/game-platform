# Start here

*Written August 2026, at the close of Phase 1. If you are a new session — human or otherwise — read this before anything else. It is the whole project in one document.*

---

## What this is

**An original tabletop RPG, played through a purpose-built web app.** Not a virtual tabletop for other people's games — the rules live in the software, and the software is the reason the rules can be what they are.

**Dylan Petty is building it solo, nights and weekends.** That constraint shapes every plan in this repo: nothing here assumes a team, and scope is cut on purpose rather than by accident.

**No AI-generated prose or art will ever ship.** AI is used freely for code, research and analysis. The words a player reads and the pictures they see are Dylan's or a paid human's. This is not negotiable and it is not a phase.

**Version 1 of the website ships everything free.** The first six Settings and every Component built for them are in the free tier; paid Components come after. So every addition is shipped content, not just a row in a table — which is why the vocabulary is kept deliberately small.

---

## Where it stands

| Phase | | |
|---|---|---|
| **0 · Repair** | **CLOSED** Aug 2026 | 8 foundation decisions + 10 re-attack findings, all covered by numeric tests in `phase-0-checks.py` |
| **1 · The Lists** | **CLOSED** Aug 2026 | every blocking list settled except **L6 · Verbs**, which is drafted and closes in Phase 2 |
| **2 · Paper** | **NEXT** | play it with index cards and people who will tell the truth |

**The gate for Phase 2 is one sentence: a group asks to play again without being asked.**

Not "they were polite." Not "it was fine once I explained it." Someone asked.

**What kills this phase is not doing it.** Building the engine first is the most common way a project like this dies — years of machinery for a game nobody confirmed was fun.

---

## The model, in one page

**Everything with identity is an Entity** — a person, a ship, a rumour, a lock, a storm, a faction, a relationship, a pending vector, a pending decision.

### Every Entity has eight fields

```
id          permanent numeric, never reused, derived from the creating Record
category    zero or more; they COMPOSE — a sentient sword is Item + Creature
tags        zero or more, magnitude declared per Tag, never implies another Tag
links       (relation, target) pairs stored on the holder
scale       optional integer; Substrate, because R-750 reads it
facets      per-Component data — the escape hatch
capacities  Capacity ID → value; the fifteen attempt Dimensions live here
tracks      Track ID → current, bounded by a max
```

### Four Noun kinds

**Capacity** is what you *bring* to an attempt. **Tag** is open cluster membership. **Track** is a bounded value with a max, a current and named bands — what can be *pushed*. **Relationship** is a Category of Entity holding one Connection per participant, each stance independent, **never an edge**.

### Nine Categories

**Substrate, shape-enforced:** `Vector` · `Proposal` · `Relationship`
**Base Ruleset:** `Creature` · `Item` · `Place` · `Group` · `Notion` · `Phenomenon`

**`Creature` means *can act*, not *is alive*.** A haunted anchor, a sentient storm and a scheming guild are all Creatures, because all three do things.

### How anything affects anything

A **Channel** is a named direction — `fire`, `impact`, `dread` — positioned in whole hundredths across **all fourteen** non-attempt Dimensions, absolute values summing to exactly 100. Eighty-eight of them.

A **vector** is a Channel plus a magnitude, aimed at exactly one target and pinned to a **Moment**. It travels the **R-region** of the lattice — modifiers, clamps, Scale conversion, Guards, cancellation — and lands by **pushing the Track the Dimension names**.

**Every Dimension pushes at least one Track.** That is a CI invariant: a Dimension with nothing to land on is a dead axis.

**Named conditions are bands, not things.** There is no `prone` State — there is a `mobility` Track and a word for a range of it. Prone, blinded, stunned, charmed, exhausted, sealed, hollowed: all bands.

**Most immunity is absence.** A vase has no `composure`, so a fear vector resolves perfectly normally and lands on nothing. You never write *"vases are immune to fear."*

### Time and cost

**Turn, round and turn ownership are Substrate.** Nine Moment kinds, every reference carrying a round. Anything coarser than a round is a Component, layered alongside.

**One Economy Unit — the doubloon.** Integer, no denominations, nothing divides. A cost is three fields: `cost` (doubloons) · `timing` (one of `own`, `any`, `respond`, `interrupt`) · `cap` (optional). **Cost and timing are orthogonal** — a 10-doubloon reaction and a 40-doubloon reaction are both reactions.

### Consequence

**Verbs return nothing.** Nothing follows from anything except a **Listener** watching *state* — never "did that just happen." Seven condition forms, composing with and/or/not, each carrying a required `once`/`while` discipline. Cascade depth 32; at the limit, halt and write a Record.

### Two Sockets

**Place** and **Resolution**. Time and Budget became Substrate; Landing was retired when the Track merge removed its job. Occupants are **frozen per Setting**.

---

## What is genuinely still open

1. **How magnitude is produced.** *"A combination of modifiers and a dice roll."* The Resolution Socket's business. Its *contract* is decided — the occupant must publish its distribution — but the formula waits for real numbers. **This blocks worked arithmetic, not content.**
2. **L6 · Verbs.** Seven drafted: `Push` · `Set` · `Place` · `Repin` · `Link` · `Create` · `Decide`. Closes in Phase 2 against content. **No Substrate code should depend on it being final.**
3. **The turn allowance** — how many doubloons a turn holds. A playtest number.
4. **L4 Tags** — 22 provisional. The full field survey is in `tags-tabletop.md` and `tags-digital.md`.
5. **Character creation**, and therefore the character sheet. What a sheet shows is downstream of how a character is made.
6. Everything in `open-questions.md` Parts 3–5.

---

## How to work here

**Read `CLAUDE.md` first — it is the working rules, and it is short.** Vocabulary must be used exactly; the reasoning behind every word is in `dictionary.md` Part 12.

**Three habits that earned their place:**

**Attack a list when you think it is done.** Not review it — attack it. That is what found the four foundation findings in Phase 0 and the sign-convention error in L22.

**Try to write a list's entries out of the pieces that already exist, before accepting it is a list.** Three proposed lists died this way in one week — the denomination ladder, most of L31, and the entire Landing Socket. All three would have been permanent.

**A misfit is a finding, never a workaround.** And **say which kind**: *additive* (a new Channel, Tag, Track, Moment kind) is cheap and stays open for Components forever; *structural* (a different Verb shape, a split Dimension Space, a redefined field) is an Edition break and the window **closes permanently at public launch**.

---

## Reading order

| | |
|---|---|
| `CLAUDE.md` | the working rules. Short, and binding |
| `the-game.md` | plain terms — what it is and how it plays |
| `dictionary.md` | **the source of truth.** Every term, every list, every decision. Part 12 is the decision log |
| `phase-map.md` | every phase to release, what gets done, and the gates |
| `work-lists.md` | the Phase 1 record — what each list decided |
| `list-log.md` | **the argument** behind each list, not just the answer |
| `open-questions.md` | everything undecided, by when it has to be answered |
| `repo-and-sync.md` | **read before touching git.** The folder bridge breaks git; use `osascript` |

`orientation.md` and `architecture.md` are the long-form versions. `lists-research.md` and the `research-*.md` files are what the field does. `substrate-lists.xlsx` is the workbook, one tab per list.

**`design-docs.html` is generated by `build_reader.py`. Never hand-edit it.**

---

## The one thing to remember about git

**Every session that changes a file ends with a commit AND a push.** The documents are the project. Run git through `osascript`, never the folder bridge — the bridge cannot delete, git's locks depend on deletion, and working around that once produced a commit with an empty tree that reported success.

```
osascript: do shell script "cd ~/Documents/GitHub/game-platform && bash sync.command 'what changed'"
```

A session is finished when `git status -sb` reads `## main...origin/main` with nothing after it.
