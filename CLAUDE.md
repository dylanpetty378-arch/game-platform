# CLAUDE.md

Working rules for this repository. **Vocabulary lives in `dictionary.md`; the reasoning behind every decision is in its Part 12.** This file is the short version you actually follow.

**Status: draft. No code exists yet.**

## Vocabulary

Use these words exactly, in code and in conversation. Full definitions in `dictionary.md`.

**Substrate** the data model, the instruction set, the execution semantics and the frames everything runs inside; never versioned · **Component** any rules subsystem; the base game is built as Components · **Ledger** append-only Record sequence, one per Campaign · **Record** one immutable entry · **Fold** pure function deriving state from Records; **the server folds, clients render** · **Entity** anything with identity — including a pending vector and a Proposal · **Facet** one Component's data on an Entity · **Noun** a published schema, of five kinds · **Verb** one of the closed set of Substrate operations · **Verb invocation** a proposed change, as data, in one uniform shape · **Vector** direction and magnitude; harm and attempts are the same machinery · **Channel** a named direction over **every** Dimension, in whole hundredths summing in absolute value to 100; never confined to one Space · **Dimension** an axis; **negative always means less of the target's property**, except the two bipolar axes `temperature` and `working` · **Modifier** acts per vector at R-300, before combining; **snapshot** (captured at placement) or **ambient** (present at resolution) · **Guard** target-side, acts on the combined total · **Threshold** a bar declared by a thing in the world, on a Dimension, a Domain or the total, reading contributors as **sum**, **highest** or **each** · **Domain** a label on a set of attempt Dimensions; it stores no number · **Capacity** the three ceiling forms: **Enhancement** (how far one vector may be amplified) · **Attempt** (how much total attention a task absorbs, as a percentage) · **Participant** (how many distinct sources may contribute) · **Allocation Points** whole points a player spreads across attempt **Dimensions**; the GM names the Domain and at least one point must be spent inside it · **Specialisation** a scoped narrowing of one Dimension granting Bonus Points, strictly narrower and never a substitute for it · **Listener** a declared watch on a state condition, the only way consequence propagates · **Moment** a named point a vector is pinned to; the only unit of time · **Tick** the stamp when a Moment occurs · **Layer** ordering slot, in the E-/C-/R- regions · **Resolution Record** inputs and a hash, per target per Moment; every slot derivable · **Socket** a hole the Substrate cannot fill itself; exactly one occupant, never zero; **three of them — Place, Resolution, Landing — and occupants are frozen per Setting** · **Delivery** which clients receive a Record; default everyone · **Lens** a read-only projection for one participant, exempt from additive-only · **Edition** a version of the Ruleset · **Bundle** a named set of Components, valid only if every Socket is filled · **Conversion** moving a Campaign between Editions · **Campaign** the unit of isolation, and the unit of concurrency · **Session** a live gathering · **Doubloon** the atomic Economy Unit; Substrate, integer, no denominations · **Cost** at least three fields — `cost` (doubloons) · `timing` (a named member of the closed set) · `cap` (optional) · **Timing** *when* you may pay — one of four frozen words (`own` · `any` · `respond` · `interrupt`), each a shorthand expanding to a defined predicate · **Trigger** an optional condition opening a window; required for `respond` and `interrupt`; permission, never a Listener · **Budget** how many doubloons you get and when they refresh; base Ruleset, not Substrate · **Proposal** a pending Entity awaiting a decision · **Decider** `Auto`, or `Person` with a Moment and a default · **Standing Order** a player-parameterised Listener · **Almanac** per-character knowledge index · **Dispatch** the personal report at a cadence Moment · **Chronicle** the curated in-world digest · **Ops** the admin CLI · **Scratch** a local disposable copy of one Campaign.

Nouns are five kinds, and they behave differently: **Capacity** (graded, kind-agnostic disposition) · **Tag** (open cluster membership, **optional magnitude**, identified by ID not name, never implies another Tag) · **State** (named condition, exclusive within an axis, optional max, ended only by a Verb) · **Resource** (depletable, with thresholds; the Substrate defines them and ships none) · **Relationship** (a Category of Entity holding one **Connection** per participant, each stance stored independently — **never an edge**).

Do not invent synonyms:

| Don't say | Say |
|---|---|
| Event | Record |
| Module | Adventure |
| Plugin | Component |
| Stat | Attribute |
| Class, race | Category, or Tags |
| Buff, debuff | Modifier, or State |
| Roll | Resolution — the magnitude is the real thing |
| Barrier | Moment |
| **Effect** | **Verb** — "Effect" is retired from engine vocabulary and reserved for a future in-fiction meaning |

**"Attribute"** is any named value on an Entity; say **Capacity** when you mean the graded, kind-agnostic sort. **"Damage"** is fine as plain English and is never a Substrate term — there is no `damage` field.

## Framings worth holding

**Verbs are a taxonomy of state change, not of activity.** The Substrate never represents the action — only the consequence. Actions are infinite; consequences are finite. Nothing in the Verb set is about attacking, persuading, or crafting.

**Every Verb has the same shape.** verb · source · target (exactly one) · secondary · direction (what is changed) · magnitude (how much) · class · layer. Verbs return nothing. Consequence propagates through **Listeners**, which watch *state* — never "did that Verb just happen." A Verb needing a field outside this shape is a Substrate finding, not a reason to widen the shape.

**Model what a thing affords, not what it is.** *Capacity to exert force*, never *Strength*. A capacity is kind-agnostic because it never claimed to describe an essence.

## The line

**If it is only true in some Settings, it is a Component. If it is true in all of them, it is base Ruleset. If the Substrate cannot function without it, it is a Socket.** One question, three tiers.

**Users author instances, never types.** Users create Settings, Adventures, creatures, places, and content. Users never create or alter a Component, a Noun, a Verb, or anything in the Ruleset. The authoring tool must make this structurally impossible, not merely disallowed.

## Non-negotiable rules

1. Components communicate only through the Ledger and Verbs. Never call another Component. Never read another Component's Facets.
2. Depend on schemas, never on behavior.
3. Dependency depth ≤ 2. Shallow hub-and-spoke, never chains.
4. Exact versions between Components. No ranges.
5. Additive-only, forever. Numeric IDs are permanent and never reused.
6. If the meaning changes, allocate a new field. Never redefine an existing one.
7. Special-case at the Component layer. Never in the Substrate.
8. **No floating point in simulation state.** Integers and fixed-point only. One multiplication inside a vector's own assembly. **Never take a square root**; compare squared values.
8c. **Exactly three rounding sites, all truncating toward zero: R-400, R-750, R-1050.** CI fails on a fourth. Every truncation is a visible step in the resolution expansion — rounding never happens off-screen.
8d. **An attempt's resolved value is `⌊points × magnitude ÷ total points⌋`** — one integer operation. A share is never stored as a decimal. Working the share out first and then multiplying is a different, wrong answer.
8a. **Everything not named in a Verb is unchanged, by definition.** State transition is a function on a set. The cost: anything you fail to list silently does not happen — test for that.
8b. **Absent is not zero.** Open-world reading everywhere; explicit presence on every field.
9. Rebuilds are per-Campaign. Never write code requiring a global replay.
10. PII never enters a Record payload.
11. **The Ledger is never updated or deleted.** Corrections are **compensating** Records by default; **supersession only through the audited `ops-write` path.**
12. **Exactly one Component per Socket, never zero and never two.** A Bundle with an empty Socket must fail to load.
13. **Percentages sum and apply once, before absolutes**, truncating toward zero. Nothing compounds anywhere. Content writes *+100%*, never *double*.
14. **Immunity is a clamp at R-600, never a −100% modifier.**
15. **A modifier may only affect modifiers at a strictly lower tier.** Acyclicity, not a ceiling.
16. **A `repin` must name a cost**, and that cost is in doubloons.
16a. **Time and Budget are Substrate, not Sockets.** Turn, round and **turn ownership** are frozen; how turn order is *produced* is base Ruleset; anything coarser than a round is a Component, added alongside and never replacing.
16b. **One Economy Unit, integer, no denominations, and nothing ever divides.** Costs are authored and folded in doubloons. A Lens may render a fraction of a turn for display; the Fold never does. If a second unit is ever added it is **never convertible** with the first.
16c. **Cost and timing are orthogonal, and frequency is neither.** A 10-doubloon reaction and a 40-doubloon reaction are both reactions. "Once per turn" is `cap`, never part of a timing's name.
17. **A Channel's direction is never modified.** All modification is to magnitude.
17a. **A Channel positions over every Dimension.** Spaces partition Dimensions, not Channels. A Channel's components must all land on the same target; two targets means two vectors.
17b. **No two Channels may share a position** — identical coordinates are the same Channel. CI rejects it. **Every Dimension must be used on both signs**, or the axis dies.
17c. **Conditions are not Channels.** Silence, invisibility, aging, knockback and size are States, Tags, Place and Scale.
18. **Addition is only legal within one Scale.** Enforced, not merely discouraged. Cross-Scale conversion is `× 10^(source − target)`, truncated toward zero, at R-750. **Scale belongs to the part as well as the whole** — a Scale-4 ship has Scale-1 doors, and the Scale that applies is the Scale of the thing actually targeted.
18a. **Log-integers are never added** — compare and multiply only. Table-based log addition is lossy and therefore not associative. Sums happen in ordinary integers within one Scale.
18b. **A universal flat Guard subtracts from the packet total, then redistributes** by integer apportionment (floor, then remainder largest-first, ties by Dimension index). A Dimension-named flat Guard acts on that Dimension alone. Named acts before universal. **A Guard reduces toward zero and never past it**, and a universal flat Guard may never be negative.
18c. **A flat Guard acts once per contributing source at R-850. A proportional Guard acts once on the combined total at R-1050.** Cancellation happens between them, at R-1000. Armour meets each blow; what you are made of meets the remainder.
18d. **Restoration is an ordinary vector with a negative magnitude, resolving at R-1250** — after harm has landed. Not an exception: because it resolves after R-850 and R-1050, no Guard can reach it and it cannot cancel incoming harm. Both fall out of the layer choice rather than being written as rules.
18i. **Landing receives the contributor breakdown, not only the combined totals.** Otherwise a Threshold at R-1200 could never read `highest` or `each`, and critical hits would be inexpressible. The Landing Component is therefore order-sensitive and must state its sort key in its SPEC.
18h. **Anything may attempt.** No Category gates it; an Entity with no points in any attempt Dimension simply cannot, and *absent is not zero* already said so.
18e. **A consequence is graded by distance from the bar**, never by an absolute value below zero. An attempt with no points spent anywhere is not legal.
18f. **An absolute modifier may not exceed the declared fraction of the Ruleset's magnitude reference.** CI-checked. Percentages are the bounded lever; absolutes only stay a minor one while they stay small.
18g. **Shaping is expressed in points, never percentages**, and has exactly two forms: **Bonus Points** (adds points, and to the total — cannot inflate) and **Baseline** (a Dimension counts as at least N points, without raising the total — can inflate, and is clamped by Enhancement Capacity). Demand is retired.
19. **A Lens is a view of the data.** Only a Lens that expresses a **likelihood** must be Calibrated — the same distribution over magnitude the Resolution Socket produces. Knock-on: **the Resolution occupant must publish its distribution.**
20. **Agents never write as humans.** An agent Record carries the model, the session, and the approving human.
21. **A human Decider always carries a Moment and a default.** One without a fallback is never legal.
22b. **An interrupt never cancels anything.** Its state change is visible to the prompting vector's gather at R-100, so the prompting vector resolves normally against whatever is left. Nothing in this design cancels a Verb.
22a. **A Moment kind says *when*; a Listener says *whether*.** Never add a Moment kind to express a condition — the Moment list is a frozen coordinate system, and the Listener condition set is the open one.
22. **Listener-produced Verbs are class `Triggered` and pin to a later Moment**, never resolved inside the current one.

Most of these are CI-enforceable, and where one is, the gate must exist — **if you can violate it silently, the gate is missing, so say so.** Two are not mechanically checkable in the general case: rule 7 (special-case at the Component layer) and rule 10 (PII). Those are review discipline.

## Determinism

The same Ledger must fold to the same state everywhere, forever.

- No floating point. No wall clock — logical Moment and Tick only.
- Ordered maps, or sort by a stable key before any iteration affecting state. **Required for arithmetic correctness, not tidiness** — changing the order of additions changes results.
- Listeners satisfied at the same Moment sort by `(layer, component_id, listener_id, target_entity_id)`.
- **Pre-sum, never pre-apply.** Source-side contributions collapse to sums at vector creation; nothing is applied early.
- Randomness is a counter-based PRNG keyed by `(record_id, entity_id, purpose)`. Never a shared stream.
- Byte-wise ordinal string comparison. Never locale collation.
- **Integer apportionment, everywhere a whole is split:** floor each share, then hand the remainder out largest-first, ties broken by index. One function, used by Allocation Points and by flat-Guard redistribution.
- **Shaping order is Bonus Points → Baseline**, permanently. They do not commute.
- `edition` and `component_version` are pinned per Record.

## Git and GitHub — read this before touching git

**Remote:** `git@github.com:dylanpetty378-arch/game-platform.git` · **local:** `~/Documents/GitHub/game-platform` · **branch:** `main`.

**The invariant: every session that changes a file ends with a commit AND a push.** No exceptions. The documents are the project; work that never reaches GitHub did not happen, and the next session starts from stale files. A session is finished only when `git status -sb` reads `## main...origin/main` with nothing after it.

**Pull before starting.** `git pull --ff-only origin main`. Another machine or session may have pushed.

**Run every git command through `osascript` → `do shell script`. Never through the folder bridge.** The bridge mounts read-write but forbids deletion, and git's lock protocol depends on deletion — so git through the bridge leaves stale locks, and working around them destroys the staged content and produces a **commit with an empty tree that reports success**. That has happened once. `osascript` runs as the user on the real filesystem and behaves normally.

- File contents → cloud workspace → `SendUserFile` → `device_commit_files`.
- Every git operation, and every deletion on the Mac → `osascript`.

**One command does it all:**

```
osascript: do shell script "cd ~/Documents/GitHub/game-platform && bash sync.command 'what changed'"
```

**After committing, verify the tree is not empty:** `git ls-tree -r HEAD --name-only | wc -l`.

**Never** hand-edit `design-docs.html` (it is generated by `build_reader.py`) · **never** force-push · **never** authenticate as Dylan or change his account settings — adding SSH keys and creating repos are his, always.

Full detail, including bootstrapping a machine that has never seen the repo: `docs/repo-and-sync.md`.

## Writing code here

**Spec first.** Write `SPEC.md` in prose before implementing. Then one test per rule. This is not style advice — grounded tests produce substantially more correct code than ungrounded ones, and it costs ten minutes.

**Prefer, in order:** Tier 0 declarative data → Tier 1 restricted expressions → Tier 2 sandboxed code. Every Component pushed down a tier is a reliability win.

**Do:**
- Strict TypeScript. Discriminated unions. Exhaustive switches. Branded types for every ID.
- Explicit over clever. Repetition beats abstraction.
- Small files, one concept each.
- Colocate tests and golden fixtures with the code.
- Copy the canonical example (see below) rather than inventing a structure.

**Do not:**
- Metaprogramming, reflection, runtime code generation, decorators with hidden effects
- Implicit behavior — nothing important happens via naming convention or side-effecting import
- Deep inheritance. Composition only.
- Magic ORMs. Write the SQL.
- Add a dependency whose behavior isn't clear from its call site

## Component layout

One Component, one directory, always these files:

```
manifest.json  schema.ts  schema.test.ts  behavior.ts  behavior.test.ts
fixtures/  SPEC.md  README.md  CHANGELOG.md
```

Canonical example to copy: *(none yet — the first Component built becomes this, and gets named here.)*

Never import another Component's `behavior.ts`.

## Testing

Integration over unit. The model that writes the implementation also writes the unit test, from the same misunderstanding — real Postgres and real command handlers are harder to fool.

Rough mix: integration 50% · golden 20% · property-based 15% · unit 10% · end-to-end 5%.

**Golden fixtures are a ratchet.** Never regenerate them wholesale to make a test pass. If a golden test fails, the change is wrong until proven otherwise. Regeneration requires an explicit flag and flags the PR.

You specify generators; Dylan specifies the properties.

## Migrations

- Never push schema directly to anything but a local throwaway database.
- Never hand-edit an applied migration.
- Always generate, then read the produced SQL before committing.
- `DROP`, `RENAME`, `ALTER COLUMN ... TYPE`, `SET NOT NULL` fail CI without explicit approval.
- Migrations and app deploy are separate steps with a gap between them.

## Production data

**Never touch production directly.** No `psql`, no `pg_dump`, no SQL against a production host.

The debugging loop is `ops repro <campaign-id>` — it exports one redacted Campaign into a local Scratch database where you have full freedom and zero blast radius. Use it. Most bugs never require production at all, and every fix leaves a golden fixture behind.

Writes to production go through `ops-write` only: `--dry-run` by default, `--reason` required, appends only, human-approved. Never propose a "quick data fix migration." The database will refuse it, and it should.

## The authoring loop is the test

**Every asset built is a test of the Substrate.** From Phase 2 on, content is authored in bulk and each piece is checked against the structure — mechanically, because at the volume that makes it meaningful it cannot be done by hand. A structure that survives five hand-picked examples has proved nothing.

**A misfit is a finding, never a workaround.** No special cases, no clever encodings, no "close enough."

**Report which kind of finding it is, because they are nothing alike.** *Additive* — a new Channel, Tag, State axis, Listener form, Moment kind — is cheap, breaks nothing, and stays open for Components forever. *Structural* — a different Verb shape, a split Dimension Space, a redefined field — is an Edition break at best, and the window closes permanently at public launch. Full practice in `phase-map.md`.

## When something doesn't fit

If a Component you want can't be expressed cleanly with the current Verbs, the **two** Verb classes, Listener conditions, the Layer slots, a Socket's Vocabulary, the Dimension Spaces, or Thresholds — **stop and say so.** A Verb needing a field outside the uniform shape is the same signal. Do not work around it. That's a signal the Substrate is wrong, and the Substrate can't be changed later, so finding it early is worth more than the feature.
