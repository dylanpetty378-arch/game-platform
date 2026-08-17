# Architecture

**Status: draft for discussion. Nothing here is final.**
Open questions are collected in §18 and are deliberately left open rather than smoothed over.

This document has one job: the **reasoning**. It fixes the **Substrate** (§4) — the small set of decisions that can never be revised — separates it from everything that can, and explains why each went the way it did. The **vocabulary lives in `dictionary.md`**, which is the single home for every term and every list; §2 here is only a pointer to it.

If you read only one section, read §4. If you read two, read §4 and §18. For the words, read `dictionary.md`.

---

## 1. The shape of the thing

**There are exactly two kinds of thing: the Substrate, and Components.** Everything else is a way of naming a collection of Components.

| | What it is | Who authors it | Changes |
|---|---|---|---|
| **Substrate** | The data model, the instruction set, and the execution semantics. Not part of the game — the physics of the software. | Dylan only | **Never** |
| **Component** | Everything else. A rules subsystem, a resolution mechanic, a progression scheme, a harm model. Independently versioned and purchasable. | Dylan only | Constantly, additively |
| **Bundle** | A named, curated set of Components at pinned versions. | — | — |
| **Ruleset** | *The* standard Bundle — the default game. Versioned as **Editions** (§5). | Dylan only | Rarely, deliberately |
| **Setting** | A Bundle plus world material, vocabulary, and dial settings. | Dylan (reference settings) or any user | Freely |
| **Adventure** | Content and shape — specific tracking, victory conditions, a beginning and an end. | Dylan (examples) or any user | Freely |

**The base game is built as Components like everything else.** There is no monolithic core with hooks bolted on for the pieces someone might want to swap. Default progression is a Component. Default harm is a Component. Default resolution is a Component. Replacing any of them is disabling one and enabling another, through machinery that already exists and that every other Component uses.

Two consequences, both deliberate:

- **The core continuously exercises the same path every future Component uses.** The component system cannot rot unnoticed, because the base game is its heaviest user.
- **The component system must work before anything is playable.** You cannot ship a monolith and refactor it into components later. This is a real cost, paid in schedule (§17).

**The Substrate is never versioned. Bundles are.** Keeping those separate is what makes Editions possible at all.

And the line that defines the product:

> **Users author instances, never types.** Users may create Settings, Adventures, creatures, places, maps, and content. Users may never create or alter a Component, a Noun, a Verb, or anything in the Ruleset.

The authoring tool must make crossing that line *structurally impossible*, not merely disallowed. A line held by the editor cannot erode; a line held by policy always does.

---

## 2. The Lexicon — see `dictionary.md`

**Every term in this system is defined in `dictionary.md`, exactly once.** This section used to duplicate that list and drifted out of step within weeks, which is the predictable result of two homes for one vocabulary. It now has one job: telling you where to look.

| You want | Read |
|---|---|
| what a word means | `dictionary.md` Parts 1–10 |
| every list the system needs, settled or not | `dictionary.md` Part 11 (L1–L30) |
| why a decision went the way it did | `dictionary.md` Part 12 |
| the interaction model — Channels, vectors, the pipeline | `dictionary.md` Part 2A |
| timing — Moments, windows, Ordered time | `dictionary.md` Part 2B |
| resolution — attempts, Thresholds, Allocation Points | `dictionary.md` Part 2C |

**This document is the reasoning and the engineering.** Why the shape is what it is, what it costs, what breaks if it changes, and how it gets built. Where the two disagree, `dictionary.md` wins.

**Six words carry the whole design**, and are worth having before reading further:

- **Substrate** — the data model, the instruction set, the execution semantics and the frames everything runs inside. Never versioned.
- **Component** — any rules subsystem. The base game is built as Components.
- **Socket** — a named hole in the Substrate some Component *must* fill. Exactly one occupant each, never zero and never two. A Bundle with an empty Socket fails to load.
- **Ledger** — the append-only Record sequence, one per Campaign. State is a Fold over it.
- **Vector** — direction and magnitude. Harm is one. An attempt is another. It is the same machinery.
- **Moment** — a named point in the timeline a vector can be pinned to. There is no other unit of time.

---

## 3. The architectural rules

Every one is cheap to hold from day one and expensive or impossible to retrofit. **Every one that can be mechanically checked is enforced in CI, not in documentation** (§12.5) — and where one can be, the gate must exist, so if you can violate it silently the gate is missing. Two are not mechanically checkable in the general case: *special-case at the Component layer* and *PII never enters a Record payload*. Those are review discipline.

1. **Components communicate only through the Ledger and Verbs.** A Component never calls another Component and never reads another Component's Facets directly.
2. **You may depend on a schema. You may never depend on a behavior.** Depend on a Noun and its owner's internals can be rewritten completely without touching you.
3. **Dependency depth ≤ 2, enforced in CI.** Schema dependencies form a shallow hub-and-spoke, never a chain. Depth kills a package ecosystem; breadth is harmless.
4. **Exact versions only. No version ranges** between Components. Resolution is a lookup, never a solve.
5. **Additive-only, forever.** Nothing is removed, renamed, or given a new meaning. Numeric IDs are permanent; deleted IDs are reserved, never recycled.
6. **If the meaning changes, allocate a new field.** A stable schema with drifting semantics is the one failure no tooling catches.
7. **Special-casing is allowed at the Component layer and forbidden in the Substrate.** Build whatever bespoke system a Setting needs — as a Component. Never as a branch in the core.
8. **All simulation state is integer or fixed-point. No floating point, ever** (§9).
9. **Rebuilds are per-Campaign.** No code may ever require a global replay.
10. **PII never enters a Record payload.** It lives in a mutable side table keyed by ID. Deletion is one row; the Ledger stays replayable.
11. **The Ledger is never updated or deleted.** Enforced by `REVOKE UPDATE, DELETE` and a trigger that raises. Not a policy — a database refusal.

---

## 4. The Substrate

The part that can never be rebuilt. Everything else is a Component.

**The boundary, stated exactly:**

> **Substrate = the data model (Nouns), the instruction set (Verbs), and the execution semantics (Verb shape, Verb classes, Listeners, the Layer lattice, aggregation, Moments, determinism), plus the frames everything runs inside: the Ledger, Delivery, Proposals and Deciders, the Socket contracts and their Vocabularies, and the contracts that define what a Component and a Lens are.**

The execution semantics have to be here rather than in a Component for a simple reason: **a Component cannot supply the rules for how Components combine.** Same category of permanence as the Verbs.

Everything that is a *game* decision — how harm works, how progression works, what a character is, how dice are rolled — is a Component, including the ones that ship as the default Ruleset.

### 4.0 The absences are the stance

One thing to hold while designing this section. Because Lenses remove the presentation stance, Components remove the subsystem stance, and Rails remove the authority stance, **the Substrate is the only place left where the system has an opinion** — and it cannot be dialed away by anyone.

If the Substrate models physical harm richly and social standing thinly, the system is about violence, whatever Lens is applied and whatever Components are installed. Every Lens is a view of this skeleton; every Component reads and writes it; it is additive-only, so what is left off on day one is expensive forever.

**What the Substrate tracks is the design. What it declines to track is also the design.**

### 4.0A The pipeline — where the Substrate starts and stops

A player may attempt anything they can describe. The Substrate never contained the actions; it contains what actions can *change*.

```
1  FICTION        A player says what they want to do. Unbounded, forever.
2  FRAMING        Someone decides what is actually at stake.
                  Provably unautomatable in general (§4.3A).
─────────────────── Substrate begins ───────────────────
3  ALLOCATION     The player spreads Allocation Points. That sets direction.
4  RESOLUTION     The Resolution Socket sets a signed magnitude.
5  CONSEQUENCE    Vectors placed and pinned. At a Moment they assemble,
                  combine, meet Guards and land; Thresholds fire the rest.
                  Everything not named is unchanged, by definition.
─────────────────── Substrate ends ─────────────────────
6  RENDERING      Each Lens narrates it at that participant's granularity.
```

Steps 1 and 6 are unbounded by design. Step 2 is a human, or an explicit declared default. Only 3 through 5 are Substrate.

### 4.0B The frame rule

**Everything not named in a Verb is unchanged by definition.** State transition is a *function on a set*, not an entailment in a theory.

This is the STRIPS assumption, and it is why the frame problem does not appear here: it is legislated away rather than solved. The price, which should be written on the wall: **anything you fail to list simply does not happen, silently.** Design tests around that failure mode specifically.

### 4.1 The Ledger

Append-only, one per Campaign, ordered by a gapless per-Campaign sequence.

Every Record carries, without exception:

| Field | Why it can't be added later |
|---|---|
| `campaign_id` | Isolation boundary |
| `seq` | Per-Campaign order; gapless because the concurrency check guards it |
| `type`, `version` | Schema identity |
| `payload` | The data |
| `actor` | Who caused it — human, system, or agent (§12.4) |
| `causation_id`, `correlation_id` | Debugging in year five; also cycle detection |
| `moment`, `tick` | Which Moment it belongs to, and the tick stamped when that Moment occurred. **Not a wall clock.** |
| `delivery` | Which clients receive it. Absent means everyone |
| `edition` | Which Ruleset Edition was in force |
| `component_version` | Which Component version produced it — required for correct replay |
| `tx_id` (`xid8`) | Insurance against the Postgres sequence-ordering bug (§10.3) |

The GM improvising is not a special case. **"The GM asserts X" is a Record type the Substrate understands natively.** The Ledger holds *claims*, not truth. This is what lets the world be as modeled as the active Components require and infinitely improvisable underneath — the app never needs to understand X in order to record it, order it, show it to the right people, and let later Records reference it.

### 4.2 Entities and Facets

The Substrate knows: Entities have stable identity, they persist, Components attach Facets. It does not know what a character is.

Storage is sparse — thousands of Facet types each held by a few Entities is the pathological case for archetype-style storage and the natural case for sparse-set storage.

One trap: **a "one of N states" value must be a single field, never N boolean tags.** Tag-per-state produces combinatorial fragmentation and is a documented ECS failure mode.

### 4.3 Verbs — the closed set

The highest-risk decision in the system, and a smaller problem than it first looked.

**The reframe.** We spent a long time looking for a closed set of verbs that every *action* decomposes into. That is the thing that has never worked: every serious attempt in the literature either stayed small and lost information (Schank's Conceptual Dependency, 11 primitives) or grew past a hundred once it had to run (VerbNet, 153–162 predicates and 39 thematic roles). Levin needed 192 fine classes for 3,024 verbs.

But the requirement is weaker:

> **The Substrate does not need to represent the action. It needs to represent the consequence.**
> **Actions are infinite. Consequences are finite.**

A player says *"I sing the guard's mother's favourite song to win him over."* The Substrate needs no concept of singing. It needs: an attempt vector, resolved against Thresholds, changing a Relationship and placing what follows.

So **the Verb set is a taxonomy of state change, not of activity.** Four independent lines converge on this: STRIPS (an action formally *is* its precondition/effect pair and has no other content), The Sims' smart objects (the target declares its affordances; the actor needs no knowledge of it), Fate's four actions (complete because they are outcome shapes rather than activities), and Blades' position/effect (a universal adjudication frame that never asks what the action is).

**Preliminary set — and closed LAST, not first (decided Aug 2026):**

`create` · `destroy` · `move` · `alter magnitude` · `transfer` · `set state` · `clear state` · `add tag` · `remove tag` · `form relationship` · `break relationship` · `reveal` · `conceal` · `bind to condition` · `advance clock` · `apply` (deliver a Packet) · `assume category` · `shed category` · `repin` (change a pending vector's Moment)

Note what is absent: nothing about attacking, persuading, crafting, climbing, or singing. Those are fictional descriptions of attempts.

Three of those — `apply`, `assume category` and `shed category` — came out of running the consequence test on eight fictional actions. `repin` came later, out of the timing work. Six composed from the original list; two did not. *Burn down a warehouse* needs a Packet delivered to a thing, which no existing Verb expresses — hence `apply`. *A character becomes undead* changes which Attributes the Entity even has, which is a Category change, not a Tag — hence `assume category` / `shed category`. `clear state` may turn out to be `set state` to a null value; that is a closing-time decision.

**Why this list is settled last.** It is the single irreversible decision in the system, and the only real evidence about its completeness is worked examples. Worked examples come from the *other* lists — Categories, Attributes, States, Channels, Dimensions, Layers, conversions. Freezing the Verb set before those exist means freezing it against imagination. So: build every other list, then run all of it against this one, then close. Until then this list is explicitly **preliminary**, and no Substrate code depends on it being final.

**The closing procedure.** For every entry across L1–L5, L7, L18, L21–L23, L25–L29, and every worked example produced along the way: *assume the fiction has already decided what happened*, write only what changed in the world, then which Verbs express it. If a consequence needs an operation not on the list, that is a real finding. If it merely needs a Tag, a Channel, or a Component formula the list does not have, that is not — Tags absorb far more than they look like they should.

### 4.3A The unadjudicable case is a formal guarantee

The **qualification problem** is a result, not an annoyance: the preconditions of an action cannot be finitely enumerated. There is no complete list of what must be true for *start the car* to work.

Therefore **there will always be attempts the system cannot adjudicate.** GM override is not generosity toward human GMs — it is the required escape valve for a provably incomplete system, and *"the GM asserts X"* being a first-class Record type (§4.1) is what makes the incompleteness survivable rather than fatal.

The GM-less tier needs the same valve in automated form: a declared, deterministic behaviour for "the fiction produced something no Component covers."

### 4.4 Nouns — five kinds, not one pool

Nouns are extensible; Verbs are not.

**The reframe.** Fixed property lists across all kinds have failed independently in five separate fields — definitions by necessary-and-sufficient conditions do not exist for most concepts, the relevant property list cannot be fixed in advance because relevance is goal-dependent, and hierarchies are not natural except at one cognitively privileged level. The periodic table is the rare success and it works because there is a single discrete causally dominant parameter.

What survived contact with the data is two frames that agree with each other: **homeostatic property clusters** (a kind is properties that reliably co-occur, with no essence and a genuinely fuzzy boundary) and **conceptual spaces** (an entity is a point in a space of quality dimensions; a concept is a convex region). Both point the same way:

> **Do not model what a thing IS. Model what a thing AFFORDS.**

*Capacity to exert force* is a disposition. It applies to a person, a winch, a faction, and a storm without absurdity, because it never claimed to describe what any of them are. *Strength* is an essence claim about people wearing a universal costume — which is exactly why 3e needed exceptions for undead and objects inside a year.

**And the productive question** is not "what is a person made of," which has no answer, but **"what are the dimensions along which an attempt can be helped or resisted?"** — which does.

#### The five kinds

Each behaves differently under change, aggregation, and rendering. Treating them as one undifferentiated pool of numbers is what forced every previous universal system into exceptions.

| Kind | Shape | Notes |
|---|---|---|
| **Capacity** | graded, kind-agnostic | Small set. Stated as capacities, never as qualities. |
| **Tag** | open, unbounded, optional magnitude | The multiplicative surface, and the pressure valve for consequences the Verbs cannot carry. |
| **State** | named, optional magnitude, exclusive within an axis | A name other rules can key on. **One field per axis, never N booleans** — tag-per-state is a documented ECS failure. |
| **Resource** | depletable, replenishable, thresholds | The only genuinely numeric-over-time values. |
| **Relationship** | a Category of Entity holding one **Connection** per participant, each stance stored independently | Every system in the entity survey stored these on one endpoint, which is why relationship mechanics desync in play. |

#### Open world

**If nothing has said anything about an Entity's disposition toward fire, that means *unknown*, not *zero*.** Open-world reading is the natural ally of additive-only: under a closed-world assumption, adding a Component silently changes the meaning of every Record that predates it.

Explicit presence everywhere; never conflate absent with zero.

#### Granularity

Rosch's basic-level result gives a sizing heuristic with real evidence behind it: one level of any taxonomy is cognitively privileged (*chair*, not *furniture* or *Windsor chair*), and Berlin found cultures name roughly 500 folk genera regardless of environment. **The Substrate should sit one level below basic** — fine enough that basic-level concepts are compositions of it, coarse enough to hold in a head. The ~500 figure is a useful ceiling for the *Component library*, not for the Substrate.

**The permanence surface grows here, quietly.** There is no such thing as a casual tag once a second Component reads it — at that moment it is a permanent contract, even though the code around it stays free. This is why the Published/Private declaration is mandatory and has no default.

Expect the mistake not at the Substrate, which will get careful attention because it is obviously important, but at the two-hundredth Noun, shipped on a Tuesday to support a Setting you were excited about.

CI-enforced discipline:
- Numeric IDs, permanent, never reused; deleted IDs reserved
- Explicit presence everywhere — never conflate "absent" with "zero"
- Open-world enums with a defined `UNKNOWN` and defined behavior on unrecognized values
- Nothing is ever required
- Unknown fields survive a round-trip and are never stripped
- **Transitive** compatibility checking — v1→v2 and v2→v3 compatible does not imply v1→v3

In the vocabulary of schema registries, the property being enforced is **`FORWARD_TRANSITIVE`**: an older reader must be able to load newer data, ignoring what it doesn't understand. Naming it precisely is worth doing — it gives the constraint an unambiguous definition for both of us.

### 4.4A The interaction model — why it is shaped this way

**The mechanism itself is `dictionary.md` Part 2A.** What belongs here is why it is worth the trouble.

**The problem it solves.** Every system that lets content declare *relationships* between kinds of harm ends up with a table that can contradict itself. Fire opposes cold; cold opposes fire; a Component added in year five declares fire opposes lightning and nothing checks it against the other four hundred entries. Under additive-only, that table can never be cleaned up.

**The move.** Declare **positions**, not relationships. A Channel is a **direction** — a set of per-Dimension percentages summing, in absolute value, to exactly 1 — and every relationship between every pair of Channels falls out of arithmetic. Nothing is declared twice, so nothing can contradict, and **a Channel added in ten years is automatically correct against every Channel that already exists.** No consistency check is needed because none is possible to fail.

**The second move.** Split **direction** from **magnitude**. Direction says what kind of thing this is; magnitude says how much of it there is; the resolved value is the product. That is what lets a single modifier scale anything it rides on, and it is the difference between a bonus that means something and a bonus that has to be written per weapon.

**Engineering consequences, which is what this document is for:**

| | |
|---|---|
| exactly **one multiplication per vector** | fixed-point direction × integer magnitude — exact, no precision loss |
| **two fixed-point numbers are never multiplied** | that is the operation that would need rounding mid-pipeline |
| exactly **one rounding point per vector**, truncating toward zero | at R-400; everything after is addition and subtraction |
| **percentages sum, never compound** | compounding stops being commutative the instant you round between steps — base 5 with +30% and +40% resolves to 8 or 9 depending on order |
| **nothing is assembled until it resolves** | so an amplifier cast after a fireball is thrown still reaches it |
| **everything source-side collapses to sums at creation** | a placed vector is a direction, four numbers and a pin, and never looks at its source again |

**And the ceiling is in the fiction, not the arithmetic.** **Enhancement Capacity** bounds how much amplification a vector can carry — a better gun holds more. This is why the additive choice costs nothing in balance: three amplifiers hit the cap either way, so the arithmetic gets to be the boring correct one and the interesting decision moves to *how much can this thing hold*.

---

### 4.4B Scale

Attributes are **linear**. Strength 11 is one unit above strength 10, always.

Scale is a **separate small whole number** on the Entity, each step a factor of ten:

```
effective magnitude = attribute × 10^scale
```

A person is scale 0; a warship might be scale 3. Two warships at 10 and 11 differ by the same *proportion* as two people at 10 and 11, which is the property that makes attribute values mean the same thing everywhere.

**Addition is only legal within one Scale.** Two people's strength adds; a person's and a warship's do not — that requires an explicit cross-Scale rule declared by a Component. Enforced rather than discouraged, which makes it impossible for a small value to silently vanish into a large one.

### 4.5 Delivery — who receives which bytes

**Retired, Aug 2026: Perception is no longer a Substrate concept.**

The earlier design had Perception as a dimension of every Record — a per-observer projection producing fog of war, unreliable narrators, the Almanac and the Chronicle. That was over-built. The decision now:

> **Every piece of Campaign data a client is entitled to is available in that client's browser. What a player *sees* is the Lens. What a character *knows* is a Component.**

Three things were being conflated, and only one of them is Substrate:

| | Where it lives | |
|---|---|---|
| **Rendering** — what the interface shows from what it has | the **Lens** | not a mechanic |
| **In-fiction knowledge** — what a character knows, misremembers, or was told wrong | a **Component**, optional | ships in v1 because it is good, but the game runs without it |
| **Delivery** — which bytes reach which browser | **infrastructure** | cannot be a Component, because a Component cannot decide what the server sends |

**Every layer of a Resolution Record is visible to everyone.** The whole calculation, every intermediate, every contributing item. Secrets are a later, deliberate decision, not a default posture.

#### What survives, and it is small

**One field on a Record: who it is delivered to. Default: everyone.**

It exists because two things genuinely require it and neither is a game mechanic:

1. **A GM's prep.** An adventure with a twist is unusable if the twist is in every player's browser.
2. **Purchased content.** A Setting or Adventure whose entire text ships to every participant's client is readable by anyone who joins a Campaign using it — a commercial exposure, not a design flaw, but a real one.

Absent means *everyone*, so this field can be added later without breaking history — which is why it is cheap rather than urgent.

#### The one architecture decision that is not deferrable

**The server folds and is authoritative. Clients render what they are sent.**

This is Tier 1 and it is independent of whether hiding exists at v1. If clients fold from Records, then any later restriction on which Records a client receives makes that client's Fold silently diverge from the truth. Folding on the server keeps one canonical state forever and turns "hide this" into "send less," which is a policy change rather than a correctness break.

**And client-side hiding is theatre.** Anything a client must not have is never serialized into a byte sent to that client. That rule stands regardless of how much is hidden, because it is what makes the delivery field mean anything at all.

#### Deleted along with Perception

- **Belief-folds.** There is one Fold. No per-observer state, no tolerance for gaps, no client computing a possibly-wrong world.
- **The information-set problem.** If everyone sees everything, every action menu is identical by construction. The invariant is satisfied without a validator.
- **Provenance as a Record field.** A Chronicle Component emits its own `rumour` Records carrying source and reliability in their payload. No Substrate field needed.

### 4.6 Proposals and Deciders

```
Proposal { subject, intent, decider }
decider = Auto(component) | Person(id, at_moment, default_action)
```

One mechanism, six features: rails dial, puppeting, GM-less, hybrid Adventures, async, and graceful absence. That last one is not a feature, it is survival — every durable asynchronous form in history has an explicit answer to "what happens when someone doesn't show," and every form without one dies at the first missed session.

### 4.7 Time — see `dictionary.md` Part 2B

**Period is retired.** There is only the **Moment** — a turn, a round, a downtime week and a season are the same thing at different grains. **Turn and round are Substrate; anything coarser is a Component**, layered alongside and never replacing.

Two architectural consequences worth stating here rather than there:

**No wall clock reaches the game.** A Moment is stamped with a tick when it actually occurs, and that stamp is what makes replay exact. Real time exists only for humans — deadlines, notifications, "you have until Sunday" — and never enters the Fold.

**Cadence above the round is a Component decision, which lowers the cost of being wrong about it.** A weekly async table and a live table running turn-by-turn share the same Substrate turn model with a different coarse clock layered over it. *(Amended Aug 2026: this used to say Time was a Socket. It is not — see `dictionary.md` Part 1, *Why Time and Budget are not Sockets*.)*

---

### 4.8 Campaign isolation

**The scaling decision.** Everything is scoped to one Campaign's Ledger. A million Campaigns is a million small independent logs, not one large database. It shards trivially, a heavy Table can't affect anyone else, and per-Campaign rebuild is embarrassingly parallel.

A cross-Campaign persistent world, if it ever happens, is a later layer that **publishes between** Campaigns. It never merges them.

### 4.9 Export and import

`ops export campaign <id> → JSONL` and `ops import`, byte-identical round-trip, tested in CI from day one.

This pair is: the migration path off any database, the GDPR tool, the backup granularity, the cold-storage primitive, the debugging loop (§12.3), and the actual guarantee behind "never rebuilt from the foundation." The highest-leverage hundred lines in the system.

---

## 5. Editions — versioning the Ruleset

Every tabletop game iterates. This one will too, and pretending otherwise is how you end up shipping a breaking change disguised as a patch.

### 5.1 The two axes

| | Substrate | Ruleset |
|---|---|---|
| What it is | The data and execution model | The game |
| Versioned? | **Never** | **Yes — Editions** |
| If it changes | Everything breaks | Old Campaigns keep working |

Keeping these apart is what makes the whole scheme work. A Second Edition changes how damage is calculated; it does not change what a Record is. If a proposed change to the Ruleset would require changing the Substrate, it is not an Edition — it is a new product, and the answer is no.

### 5.2 Revisions versus Editions

The distinguishing test is mechanical, not editorial:

> **Would this change cause an existing Campaign's Ledger to fold to different state than it does today?**
> **No → Revision.** Ships to everyone immediately, including running Campaigns.
> **Yes → Edition.** Opt-in only.

Revisions cover clarified wording, new optional content, bug fixes that restore intended behavior, performance, and UI. Editions cover changed resolution math, changed Verb semantics, removed or reinterpreted rules, and anything that alters the Fold.

The temptation will be to ship a Fold-changing "fix" as a Revision because it's small and obviously correct. That temptation is the thing this section exists to resist. **A small Fold change and a large one are the same category of change.**

### 5.3 Campaigns pin an Edition, forever

A Campaign records its Edition in the Ledger at creation and never leaves it without an explicit Conversion. Consequences, all deliberate:

- **Every Edition's Fold code stays in the repository forever**, side by side, under `ruleset/editions/e1/`, `e2/`, and so on. Old Editions are not deprecated, not archived, not behind a flag. They are shipped code with passing tests.
- **CI runs every Edition's golden fixtures on every commit.** An Edition whose tests stop running is an Edition that has silently died.
- **A Campaign started in 2027 still opens and still plays in 2037.** That is the promise, and this is the mechanism.

The cost is real: N Editions is N codebases to keep compiling. The mitigation is that Editions should be rare — one every few years at most — and that old Edition code is *frozen*, so keeping it alive is a compile-and-test cost, not a maintenance cost. Nobody edits First Edition after Second Edition ships.

### 5.4 Conversion

Moving a Campaign to a newer Edition is an explicit operation the Table chooses.

- Conversion appends a Record: *this Campaign converted from Edition N to Edition N+1 at Moment M.* Records before that point fold under Edition N; records after fold under Edition N+1. **The Ledger itself carries the Edition boundary.** This is the event-sourcing-native answer and it means no history is rewritten and no state is lost.
- Each Edition pair ships a declared **conversion function** and a **conversion report** describing exactly what changes: what converts cleanly, what is approximated, and what is lost.
- Conversion is previewable. The Table sees the report before deciding.
- **Some Campaigns will never convert, and that has to be fine.** A group three years into a First Edition campaign should feel no pressure. The lesson from every edition change in the hobby's history is that the pressure is what people resent, not the change.
- Not every Edition pair needs to be convertible. "Second Edition is different enough that existing Campaigns should finish where they are" is an acceptable, honest answer.

### 5.5 Components and Editions

- A Component declares which Editions it supports: `editions: [1, 2]`. Most will support several; some will be Second-Edition-only because they depend on rules that didn't exist before.
- **Ownership is per-Component and permanent, across Editions.** Buying the Crafting Component in First Edition means owning it in Second. Re-charging for the same Component in a new Edition is the single fastest way to make an Edition feel like a shakedown, and it is off the table.
- Settings and Adventures likewise declare Edition compatibility, and the authoring tool refuses to let a user build something targeting an Edition their content can't run under.

### 5.6 Living with old Editions

- The Component catalog filters by Edition. A First Edition GM sees what works for them.
- Documentation is Edition-scoped. Every rules page states which Edition it describes.
- Old Edition Campaigns get infrastructure improvements — performance, mobile, notifications, the Ops tooling — because those are Substrate, not Ruleset. **Being on an old Edition should never mean being on old software.** That separation is the entire practical payoff of §5.1.

---

## 5A. Lenses

A **Lens** is a read-only projection of Substrate state into what one participant sees. Chosen per character, changeable at any time in either direction, with no restriction.

### 5A.1 The hard rules

1. **A Lens never changes what a character can do.** It removes no ability, no option, and no part of the game. It changes only how much of the machine you are invited to look at.
2. **All writes happen at the Substrate.** Verbs act on Substrate values identically regardless of anyone's Lens. Every Component and every Verb targets the Substrate and nothing else — which is what makes an unbounded number of Lenses possible.
3. **The Substrate is more detailed than any Lens**, including the most detailed one. Lenses are always a reduction.
4. **Lenses are formulas.** That is all they are.

### 5A.2 Lenses are not in the Fold

Because a Lens only renders, it sits outside the deterministic replay path. **Lens formulas are therefore exempt from additive-only** — a Lens can be rewritten in year four, retroactively, and no history breaks. Every past Record still folds identically; it just displays better.

This is the one large surface in the architecture where being wrong is cheap. Ship Lenses you are not sure about.

### 5A.3 Dice, and the calibration obligation

A Lens may put dice in front of the player — one Lens rolls a d6, another a d20, another percentile. **The die is an interface to a probability, not a source of one.** The Substrate owns the odds.

So every Lens carries a calibration obligation: its dice procedure, visible modifiers, and target numbers must reproduce the same distribution over magnitude the Resolution Socket actually produces. Two characters with identical Substrate values and different Lenses must be equally likely to succeed.

**This is machine-checkable.** Enumerate the Lens's dice space, run its formula, compare the resulting distribution against the Substrate's within tolerance. **An uncalibrated Lens fails validation and cannot ship.** This is the guardrail that makes the whole concept safe rather than terrifying, and it is available only because this is software.

### 5A.3A ~~The information-set invariant~~ — dissolved

Game theory says that for any two states a player cannot distinguish, the available action menus must be identical, or the player distinguishes them by reading their own buttons. This was going to be a Lens validator rule.

**It is now satisfied by construction.** Everyone receives everything they are entitled to, so every menu is identical and there is nothing to validate. Recorded because the reasoning is worth keeping if secrecy is ever reintroduced as a Component — that Component inherits the obligation.

### 5A.4 ~~Outcome granularity~~ — dissolved

Degree, Cost, the two-axis Outcome space, the partial ordering and the scalarization rule are all deleted. **An attempt is a vector**: direction is what you were trying, signed magnitude is how well it went, and things in the world declare **Thresholds**.

What survives, and matters for Lenses:

- **The Ledger stores the resolved vector, not a die roll.** A d20 is a Lens artifact. The magnitude is real.
- **A Lens buckets magnitude however it likes** — two bands, three, a percentile — and must be **Calibrated**: its dice must reproduce the same *distribution over magnitude* the Resolution Socket actually produces. Machine-checkable by sampling both.
- Because magnitude is one number rather than a pair, there is nothing left to rank and no scalarization rule to declare.

### 5A.5 The explanation channel

A Lens can lie by omission. A Component changes something that matters enormously at Substrate level and the player's visible numbers do not move; three sessions later the consequence lands and, from inside that Lens, the game did something arbitrary.

This is not fixable with documentation, because the player deliberately opted out of reading it. So **every Lens declares two things: how it renders state, and how it narrates change.** When something moves at Substrate that the Lens cannot show, the player is still told — in that Lens's vocabulary. *"The curse is taking hold,"* never *"bloodline resistance −3."*

### 5A.6 Authoring through a Lens

Play never writes through a Lens, but **authoring does** — a user building an Asset at low complexity supplies few values where the Substrate needs many.

Two mechanisms, used together. Values distribute backward across the Lens formula by averaging, which is deterministic and lossy. And **templates** — curated Substrate profiles authored by Dylan — supply the shape the averaging cannot. "Strength 20, brute-shaped" and "Strength 20, wiry-shaped" produce genuinely different Substrate profiles from the same visible number. Without templates, everything authored at low complexity comes out identical underneath.

Templates are Assets, which means the thing that makes low-complexity authoring tractable is also inventory.

### 5A.7 Naming

The working tiers — simple, moderate, advanced — fight the first hard rule, because they imply a skill ladder where the simplest Lens is training wheels. A twenty-year GM should be able to choose the smallest Lens without it sounding like an admission. Names describing *character* rather than *level* carry the intent; the specific words are open (§18).

### 5A.8 Where "a different game" actually comes from

A Lens changes what you see. **Rails** change what you are asked. **Components** change what exists. A hundred genuinely distinct experiences comes from all three together — and keeping them separate matters, because a Lens that starts acquiring powers reintroduces the fairness problem rule 1 exists to prevent.

Rails is set per-Component, and each Component declares whether its dial is set by the player, the GM, or the table — some are personal (auto-resolve my downtime) and some are inherently shared (does the app run initiative).

---

## 6. Components

### 6.1 Anatomy

Three artifacts with different compatibility regimes:

| Artifact | Regime |
|---|---|
| **Manifest** | Identity, version, supported Editions, declared schema dependencies, Published/Private declarations, price tier |
| **Schema** | Immutable, content-addressed, additive-only, CI-gated. **The only dependency target.** |
| **Behavior** | Versioned, replaceable, never a dependency target. Pinned per-Record so replay is correct. |

### 6.2 The three execution tiers

Reach for the lowest tier that works.

**Tier 0 — Declarative data.** The Verb is a struct interpreted by the Ruleset. Target the large majority of Components here. Statically validatable, trivially versionable, trivially deterministic, inspectable by tooling — and the tier where Claude authoring a new Component from an existing example is most reliable (§12.5).

**Tier 1 — Restricted expressions.** Predicates and numeric formulas only. No loops, no allocation, no I/O. Evaluated by a small AST interpreter in the Ruleset.

**Tier 2 — Sandboxed code.** The escape hatch for the genuinely irreducible. Must be deterministic and must run the *same compiled artifact* in browser and server — never a native VM on one side and a compiled one on the other.

Precedent: MTG Arena's rules engine "does not know what any of the thousands of individual Magic cards do." Each card compiles to declarative rules that mutate an engine-generated task list, and roughly 80% of new cards are auto-converted from their English text. Novel mechanics still require core work — and that work is deliberately generalized so the next similar card needs none. That is both the target and the realistic expectation about it.

### 6.3 File layout

One Component, one directory, always the same shape. The rigidity is the point: a fixed layout makes a new Component a pattern-match rather than a design problem.

```
components/
  currency/
    manifest.json          identity, version, editions, deps, price tier
    schema.ts              published Nouns; typed; additive-only
    schema.test.ts         compatibility assertions vs every prior version
    behavior.ts            pure; consumes Nouns, returns Verbs   
    behavior.test.ts       unit tests
    fixtures/              golden Record sequences + expected state hashes
    SPEC.md                the rules in prose — written before the code (§14.1)
    README.md              what it is, what it depends on, what it publishes
    CHANGELOG.md           every version, additive-only, with reserved IDs
```

No Component ever imports another Component's `behavior.ts`. CI enforces this as a lint rule, not a convention.

### 6.3A Dependencies and suppression

Components have declared, one-directional dependencies on other Components' *schemas*, never on their behavior. **Dependency depth ≤ 2** — schemas at the bottom, behavior on top, and behavior never chains. Depth kills a package ecosystem; breadth is harmless.

And Components do not only add. They **replace** — a Setting swaps the default progression for a different one, or removes harm entirely. So a manifest declares what it **suppresses** as well as what it adds. Suppression is a standing vector with a window, placed at a Layer that empties what it suppresses — the same machinery as a ward, never a special case; when two Components suppress the same thing, the deterministic rule applies (lowest stable Component ID wins, recorded in the Ledger).

This is what makes "the base Ruleset is Components" worth anything. Without it, every swappable piece of the core would need a bespoke hook invented in advance, and the list would have to be guessed correctly on day one.

### 6.4 Assets

Some Nouns are **Assets** — concrete, authorable things in the world. Characters, people, monsters, ships, equipment, places, and an open-ended list beyond.

The distinction that matters:

| | Authored by |
|---|---|
| **Asset type** (what a ship *is*: its schema, its Facets, its rules) | Dylan only. It's a Noun. |
| **Asset instance** (*this* ship, with these Attributes and this name) | Users, where the capability exists |

**Authoring capability is per-type and must be built.** A Component that publishes an Asset type may also ship an authoring surface for it — a form, a set of constrained choices, a validator. Where that surface exists, users create instances freely. Where it doesn't, only Dylan authors instances until it's built. This is a real unit of work per Asset type, and it should be priced and scheduled as such rather than assumed.

**The Ruleset's own Asset types ship with authoring enabled from day one.** A user who has bought nothing can still build characters, places, and the base entities needed to run their own Campaign. Free means genuinely free, not a demo.

Asset instances are content, which means they are the third sellable thing alongside Components and Adventures — and the one with the lowest authoring cost per unit and the highest volume. A user who builds a good ship, a good NPC, or a good place can sell it, and so can Dylan.

This also resolves cleanly against §1's line. Users author instances, never types. An Asset instance is an instance. An Asset type is a type.

### 6.5 Disabling

A Campaign may **add** a Component at any time. A Campaign may **disable** an active Component. A Campaign may **never remove** one — existing Records reference its Nouns, and the Ledger must stay foldable forever.

Disable is not one behavior. Each Component declares what disabling means for it, and the options genuinely differ:

- **Frozen** — existing Facets keep their values, nothing new happens. A currency stops circulating but purses still show what's in them.
- **Dormant** — the Component stops producing Verbs but still folds its history, so re-enabling picks up coherently.
- **Hidden** — the data persists but is no longer surfaced.

The Component's manifest declares its disable semantics, and the Ruleset never guesses. Re-enabling is always allowed; the Active Set records both the addition and the disable as Records, so the Campaign's configuration history is itself part of the Ledger.

---

## 6A. Sockets — the Components that cannot be absent

**A Socket is a named hole in the Substrate that some Component must fill.** The Substrate declares the hole and its contract; it never supplies the occupant.

This is the correction to a claim that was true and misleading. *Everything above the Substrate is a Component* is still true. But some of those Components are load-bearing walls rather than furniture: the Substrate defines what a **Moment** is and cannot say which Moments exist; it defines what a **Resource** is and ships none; it defines what a landing vector is and cannot say what landing does.

### The rules

1. **Exactly one occupant per Socket. Never zero, never two.**
2. **A Bundle with an empty Socket must fail to load.** CI-enforceable, and it is the whole reason the concept earns its place.
3. **The contract is Substrate and frozen forever.** The occupant is a Component and can be swapped — but swapping one is an **Edition-level** change, never a casual toggle, because every piece of content in the Bundle is written against what it publishes.
4. **A Socket occupant cannot be disabled** (§6.5). Disabling one would leave the hole empty, which rule 2 forbids.
5. **Socket occupants may depend on each other at most one level deep.** Budget depending on Time is fine; a third link is a foundation chain wearing a Component costume, and it defeats the depth rule in §3.

### Every Socket has two halves, and this is what makes it safe

**Vocabulary — Substrate, additive-only.** The names content is allowed to depend on. A spell costing *one action* needs `action` to exist regardless of which Budget occupant is installed. A vector pinned to *the start of the target's turn* needs `start of turn` to exist regardless of which Time occupant is installed. New names may be published forever; none may be removed or redefined.

**Behaviour — the occupant.** How many actions you get and when they return. Which Moments exist, in what order, and who is in them. Content never names any of it.

Without the split, one of two failures is guaranteed: either content depends on an occupant's internals and swapping breaks every spell ever written, or the Substrate ends up owning the economy it was trying to delegate.

### The candidates

| Socket | Publishes | Without it |
|---|---|---|
| **Time** | Moments, their order, the participant set, entry to and exit from Ordered time | Nothing can be pinned; no vector ever lands |
| **Place** | what *scope* means — position, zones, range, containment | An area vector cannot say who it covers |
| **Resolution** | how an attempt acquires its magnitude | Nothing is ever adjudicated |
| **Landing** | how a vector that survives becomes persistent state | Vectors arrive and nothing happens |
| **Budget** | rationed actions, and therefore the cost a `repin` must name | Repins are unbounded and Ordered time can be held open forever |

**The risk, stated plainly: keep this list short.** Every Socket is a permanent dependency for every Component ever written, and an over-large list quietly rebuilds the monolith the Component design exists to prevent. A capability belongs in a Socket only if the Substrate genuinely cannot function with it empty. Five feels near the ceiling.

Full detail and the open list: `dictionary.md` L27, L28.

---

## 7. Verb invocations, and Listeners

**Terminology note (Aug 2026).** This section used to be called *Effects*. The word is retired from the Substrate vocabulary: a proposed change to state is a **Verb**, and nothing else. "Effect" is deliberately left free so it can mean something in the fiction later — a spell effect, a status effect — without colliding with an engine concept.

### 7.1 Verbs are values, never callbacks

Writing a Verb down does not make it happen. A Verb is data that a Moment later applies.

### 7.2 One uniform shape

Every Verb, of every kind, from every Component, has the same fields:

| Field | What it is |
|---|---|
| `verb` | which operation, from the closed set (§4.3) |
| `source` | the Entity the change originates from |
| `target` | the primary Entity being changed — **exactly one, always** |
| `secondary` | zero or more additional Entities the invocation touches |
| `direction` | *what* is being changed: per-Dimension percentages summing in absolute value to 1. For harm a declared **Channel**; for an attempt, computed from **Allocation Points** |
| `magnitude` | *how much*: a whole number, signed, at a declared **Scale** (§4.4B) |
| `class` | why this invocation exists (§7.4) |
| `layer` | its slot in the ordering lattice (§8) |

`direction` + `magnitude` is the Channel idea generalised past harm to every Verb: *what is being pushed on*, and *how hard*. Harm is the case where the direction happens to live in the physical Dimension Space; a reputation change, a resource transfer, and a clock advance all have the same shape.

**Exactly one primary target** is a deliberate constraint. A Verb affecting three people is three Records, not one Record requiring interpretation. "Who did this happen to" is then answerable by a `WHERE` clause rather than by parsing.

Everything in this table is written to the Ledger verbatim. One shape means one parser, one validator, one log format, one replay path — forever. **If a Component wants a field that isn't here, that is a finding about the Substrate, not a reason to widen the shape** (see CLAUDE.md, "When something doesn't fit").

### 7.3 Verbs return nothing

A Verb produces no return value, and nothing may read one. There is no execution to return *from*; a return value would smuggle running code back into data.

### 7.4 Verb classes — two, frozen at v1

Why an invocation exists. Adding a third later is a Substrate break.

- **Activated** — something chose to do this
- **Triggered** — a Listener fired and issued it

**There used to be four.** *Replacement* ("instead of X, Y") and *Continuous* ("true while a condition holds") both dissolved into **a vector with a window**: a vector already standing in the space **is** "instead of," and a vector whose window is "while this condition holds" **is** "continuous." Two mechanisms deleted, none added, and the uniform Verb shape stopped needing per-class exceptions.

### 7.5 Listeners

Consequence does not travel through return values. It travels through **Listeners**.

> A Verb drives a Resource to zero. The Verb does not know this and does not report it. A Listener watching *"this Resource is at zero"* fires and issues its own Verbs — set state `unconscious`, add a Tag, whatever the Component declared.

Rules:

1. A Listener is **data**, declared in a Component's manifest. Never arbitrary code.
2. A Listener watches **state, not Verbs.** It asks *"is this now true"*, never *"did that just happen."* State is stable and re-derivable from the Ledger; the particular sequence of Verbs that produced it is not, and matching on it would make Components sensitive to each other's internals — a §3 rule 1 violation by the back door.
3. Listeners are evaluated at R-1400, *after* the Moment's Verbs have landed and the Resolution Record is written.
4. Listener-produced Verbs carry class `Triggered` and are pinned to a **later** Moment. Never resolved inside the current one.
5. Cascades are bounded by a Substrate-level depth limit, and hitting the limit is itself recorded.

**Open, and load-bearing (§18):**

- The set of condition forms a Listener may watch. Sketch: resource crosses a threshold · state entered · state exited · tag gained · tag lost · relationship formed · relationship broken · clock reaches a value · category assumed or shed.
- The **evaluation order across Listeners satisfied simultaneously.** This is a determinism hazard of exactly the same severity as §8 aggregation order — get it wrong and the same Ledger folds differently on two machines. It needs a stable key, not registration order.
- The cascade depth limit, and the defined behaviour on hitting it.

### 7.6 The round

Collect Verbs → **a Moment arrives** → run the E-/C-/R- pipeline → evaluate Listeners against the new state → the Verbs they produce pin to a later Moment → repeat until quiescent or the depth limit is hit. **Nothing mutates between Moments**, and *Barrier* is retired as a second word for the same thing.

### 7.7 Records without Verbs

**The Ledger does not require a Verb to record something.** A Verb invocation is one Record type among several; the others change no state at all — a GM assertion, a note, a Session or cadence boundary, a Proposal raised or decided, a correction, a Conversion applied, a Listener firing.

The consequence matters for §4.3: *"what happened"* is a strictly larger set than *"what changed."* The Verb set only has to be complete over the second, which is the whole reason a closed set is achievable at all.

The discipline this buys has one cost: non-Verb Records must stay genuinely inert. The moment a "note" changes state, the Fold stops being a function of Verbs and the determinism argument in §9 collapses. CI-enforceable.

---

## 8. Ordering — drafted for resolution, open everywhere else

**Budget more design time here than on schema evolution.** Additive-only schema is a solved discipline. Additive-only *ordering* is not.

Magic's layer system took thirty years to reach seven layers with sublayers, timestamp ordering within a layer, and a dependency rule that overrides timestamps — and still produces intuitive results only about 99% of the time.

**The resolution region is now drafted** — see `dictionary.md` Part 2A for the full lattice and the case behind each boundary. Three regions:

- **E-100 … E-500** (5 slots) — Entity preparation. Existence, Categories, base attributes, attribute modifiers, Capacities.
- **C-100 … C-600** (6 slots) — vector creation. Read the source's prepared state, snapshot modifier tiers, summed percentages, summed absolutes, captured Enhancement Capacity, direction and base magnitude.
- **R-100 … R-1400** (19 slots) — resolution at the Moment. Gather, ambient tiers, percentage sum, capacity clamp, apply, absolutes, vector clamp, resolve, **Scale conversion (R-750)**, **standing cap (R-780, reserved)**, combine within source, **flat Guards per source (R-850)**, **combine across sources (R-1000, where cancellation happens)**, **proportional Guards on the total (R-1050)**, target clamp, land, **restoration (R-1250)**, record, Listeners.

**Twenty-six slots in total.**

Five principles came out of drafting it, and they generalise past resolution:

1. **A frozen, sparse, named lattice**, generously gapped, fixed at v1. Components pick from the fixed set and may never invent one.
2. **Pre-sum, never pre-apply.** Summation is associative, so a partial sum can be completed later without changing the answer. Application is not. This is what lets everything source-side collapse into numbers at vector creation while the arithmetic stays exact.
3. **Nothing compounds.** Percentages sum and are applied once; Guards sum and are applied once. Compounding is commutative in real arithmetic and stops being commutative the moment you round between steps — base 5 with +30% and +40% gives 8 or 9 depending on order. Summing gives 8 in every order, forever.
4. **Aggregation is declared per kind, not per Verb.** Capacities and Resources add then clamp. States take the highest applicable within an axis. Tags are set union. Relationships may need a rule of their own.
5. **A ceiling belongs in the fiction, not the arithmetic.** Enhancement Capacity bounds how much a thing can be amplified — a better gun holds more. This is what makes the additive choice free rather than a balance compromise.

**Timestamp tiebreak** within a layer, and an **explicit declared dependency** between Verbs overriding timestamp when one genuinely depends on another, both still stand.

**Still open:** the lattice outside resolution — progression, economy, movement, knowledge, social standing. And the cascade cap: a depth limit and a total-work limit, halting without applying the pending round and recording that it happened.

Ordering is where additive-only silently becomes *meaning changed*. Everything else here is protected by CI; this is protected by design.

---

## 9. Determinism

The same Ledger must produce the same state everywhere, forever. Hard requirement — the entire architecture rests on the Fold being pure.

| Hazard | Rule |
|---|---|
| **Floating point** | **Banned in simulation state. Integers and fixed-point only.** Cross-platform float determinism between browsers, architectures, and compilers is not achievable. Presentation may use floats; the Fold may not. |
| **Iteration order** | Ordered maps, or sort by a stable key before any iteration that affects state. Enforced by construction. |
| **Randomness** | Counter-based, splittable PRNG keyed by `(record_id, entity_id, purpose)`. Never a shared stream — a shared stream makes results depend on draw order. |
| **Time** | Logical Moment and tick only. No host clock reaches the simulation. |
| **Text** | Byte-wise ordinal comparison. Never locale-sensitive collation. |
| **Version drift** | `edition` and `component_version` pinned per Record. Old code stays loadable forever. |
| **Round-trip** | State that survives in memory but not through save/load is a bug. |

**Build the determinism harness before Component #10, not #100.** Replay every Component's golden fixtures on every target platform and diff the state hash. In CI, export-and-reimport the Campaign at every Moment and compare. Every system surveyed that lacks this pays continuously; every system that has it is one people cite as working.

Store a state hash at every Moment in the Ledger. Without the hashes, a determinism bug is unfindable.

---

## 10. Technology

Chosen for a solo author on a decade horizon with Claude writing most of the code. Optimized for *isolation* rather than for being right — nothing survives ten years by being well-chosen, only by being replaceable.

### 10.1 The tier rule

**Tier 1 — chosen once, never revisited.** TypeScript. SQL/Postgres semantics. WebSockets. React as a client library. **And the pure Ruleset package** — no I/O, no framework imports, no vendor types.

**Tier 2 — replaceable in one to two weeks.** The realtime host. The Postgres host. Auth. Static hosting. Build tooling.

**Tier 3 — never load-bearing.** Sync engines, managed realtime, backend-as-a-service, meta-frameworks, magic ORMs.

**The test:** if the room host is 300 lines of glue and the Ruleset is 40,000 lines of pure functions, then "we must leave this vendor" is a fortnight. If the rules are expressed *as* vendor API calls, leaving is a rewrite — and the ten-year requirement has already failed regardless of which vendor was picked.

### 10.2 Language: TypeScript everywhere

Strict mode, discriminated unions, exhaustive switches, branded types for every ID. One language across client, server, and Ruleset halves the total surface for a solo author.

Elixir/OTP is technically the better runtime for many small stateful supervised rooms and it isn't close. Rejected anyway: a second language for a solo author, a thinner ecosystem, and — decisively, given §12.5 — materially weaker LLM assistance. Go is rejected for the rules layer specifically because it has no sum types, so game-state variants degrade into type switches with no exhaustiveness checking, which is exactly the guardrail worth the most here.

### 10.3 Storage: PostgreSQL, hand-rolled event store

One database. One partitioned `records` table. Roughly 400 lines of append/read/concurrency logic, owned outright — small enough to be total, and it cannot be abandoned by a maintainer.

```sql
records (
  campaign_id      uuid    not null,
  seq              bigint  not null,      -- gapless, guarded by the PK
  type             text    not null,
  version          int     not null,
  payload          jsonb   not null,
  actor            jsonb   not null,      -- kind: user | system | agent (§12.4)
  causation_id     uuid,
  correlation_id   uuid,
  moment           text    not null,
  tick             int     not null,
  delivery         jsonb,
  edition          int     not null,
  component_version text    not null,
  tx_id            xid8    not null default pg_current_xact_id(),
  created_at       timestamptz not null default now(),
  primary key (campaign_id, seq)
) partition by hash (campaign_id);
```

Optimistic concurrency is the primary key doing the work: `INSERT ... WHERE seq = expected + 1`. No locks.

**The Postgres sequence-ordering bug.** Sequences are assigned before commit, not at commit, so a transaction starting later can commit earlier with a lower number — and a global subscriber can permanently skip an event. Sidestepped entirely by driving projections from the per-Campaign `seq`, which is gapless. The `tx_id` column is eight bytes of insurance if a global feed is ever needed.

**Consistency starts simple.** Fold on read; move a specific query to an inline projection (same transaction, strongly consistent) only when measurement demands it. **Do not build an async projection daemon.** Checkpoints, lag monitoring, poison records, restarts, and leader election are the largest ongoing operational burden of an event-sourced system for one person, and none of it is needed at any plausible scale here.

Explicitly deferred until measured: snapshots, async daemons, separate read databases, per-recipient materialization, cold tiering, any second datastore.

Explicitly rejected: Kafka (no efficient per-Entity load, no conditional append), EventStore/Kurrent (license already changed once, VC-backed vendor mid-pivot), FoundationDB (you'd operate a cluster), Turso (closed-sourcing its server, removing features from new users, layoffs — January 2026).

### 10.4 Realtime and hosting

Plain WebSockets with an owned message protocol. Not managed realtime — per-message and per-connection-minute billing is a tax on exactly what this app does all day, and the cost curve is superlinear in engagement.

Start with a Node process holding rooms in memory, backed by Postgres. Cloudflare Durable Objects are the natural destination if live Sessions become heavy — single-threaded per object makes concurrency control free, and hibernation means near-zero cost for dormant Campaigns. That is a Tier-2 decision and stays one as long as the Ruleset is pure. **Postgres remains the system of record either way.**

### 10.5 Client

React 19 as a client-side SPA on Vite. **Not** Next.js and **not** React Server Components — RSC optimizes server-driven data fetching for content-driven apps, and this is a heavily stateful, WebSocket-driven, long-session app that gains nearly nothing and inherits framework churn plus host coupling.

The client runs the *same* Ruleset package against its filtered view for optimistic prediction; the server's authoritative result overwrites. Because the Fold is a shared pure function, this is code reuse rather than a second implementation.

### 10.6 Not local-first

Considered and rejected:

1. **Hidden information is fundamentally at odds with client-side replication.** Partial replication *can* be configured, but that means maintaining a second, security-critical projection of the rules that must agree with the first forever — and any bug is an unrecoverable leak, because the client keeps a durable local copy of whatever was mistakenly sent.
2. **CRDT merge semantics are the wrong conflict model.** CRDTs guarantee convergence, not correctness. When two players both claim the last thing, the required behavior is to reject one, not merge both.
3. **The category is churning hard.** Reflect retired (Nov 2024). Triplit's team acqui-hired (Oct 2025). MongoDB Device Sync end-of-life (Sep 2025).

The two good ideas from local-first are taken anyway and both are free: optimistic prediction with server reconciliation, and an append-only log as the source of truth.

---

## 11. Repository layout

```
/ruleset              Tier 1. Pure. No I/O, no imports outside itself.
  /substrate          Ledger types, Verbs, Entity/Facet, Delivery, Proposal, Moment,
                      Socket contracts and their Vocabularies
  /editions
    /e1               First Edition: resolution, Verbs, Layers, aggregation 
    /e2               Second Edition, when it exists. Side by side, forever.
  /conversions
    /e1-to-e2         Conversion function + report generator
/components           One directory per Component (§6.3)
/settings             Reference Settings: configuration + world material
/adventures           Reference Adventures
/server               Tier 2. Transport, persistence, auth, billing. Thin.
/client               Tier 2. React SPA / PWA.
/authoring            The Setting/Adventure editor. Structurally cannot cross the line.
/ops                  The admin CLI (§12)
/tools                Determinism harness, schema-compat gate, export/import
/spec                 Prose specifications, written before implementation (§14.1)
/docs                 This document, the field survey, decision records
```

`/ruleset` and `/components` are the product. Everything else is replaceable plumbing, and the structure should make that obvious at a glance.

---

## 11A. Instrumentation — building it and playtesting it

**This is not a phase-two feature. It is a Substrate requirement, and it has to be decided alongside the Record shape.**

A Ledger that cannot answer *"why did that happen"* is not fixable afterwards without a migration. A Fold with no seam for a tester to reach into is not a Fold anyone can playtest. And a system whose arithmetic runs through a thirty-slot pipeline is not one you can debug by reading numbers off a screen.

### The stance: total transparency, in the tools

Play may hide things. **The instrumentation never does.** Every Record, every Resolution Record expanded layer by layer, every modifier that contributed and the item it came from, every Threshold that was checked and by how much it was missed. If a tester cannot see it, it did not happen in a way anyone can reason about.

That is affordable precisely because the design already went this way: the server folds, everything a client is entitled to is already there, and the Resolution Record's layers are derivable rather than stored.

### What has to exist

**Reading what happened**

- **The event log**, searchable and filterable, over the whole Ledger — by Entity, by Moment, by Verb, by Component, by actor.
- **Resolution expansion.** Any resolution, ever, opened to the full pipeline: every slot from E-100 to R-1400, every input, every intermediate, every contributing item named. This is the same view as the player-facing animation, unthrottled.
- **The state inspector.** Every Attribute, State, Tag, Relationship, pending vector and standing vector on any Entity, at any Moment.
- **Time travel.** Fold to any Moment and look around.

**Changing things**

- **What-if.** Re-resolve any past resolution with an input changed — a different allocation, a different Guard, one more modifier — and see the whole pipeline recompute. **Never writes to the Ledger.** This is the single most valuable tool for balancing a system whose interesting behaviour lives in the interaction of layers.
- **Forking.** Branch a test Campaign at any Moment and play both ways. This is `ops repro` (§12.2) pointed at design rather than at bugs.
- **Active Set swapping mid-Campaign**, in a test Campaign only. Change a Component version, refold, diff.
- **Direct state authoring** in a test Campaign — set a value, place a vector, jump to a Moment — recorded as such so nobody mistakes a rigged state for a played one.

**Writing things down**

- **Notes anchored to anything.** A Record, an Entity, a Moment, a single slot of a single resolution. Not a separate document — a note attached to the exact thing it is about, so it is still findable in six months.
- **Note kinds**: bug, balance, confusion, idea. Confusion is the one most systems forget to collect and the one that predicts churn best.
- **Session recording and replay.** Play a whole session back at speed, with the notes in place, so a pattern nobody noticed live shows up on the second watch.
- **Export a playtest report** — the notes, the resolutions they point at, and the state around them — as one artifact.

### Testers are a first-class account kind

Not a permission flag bolted onto a player account. A **tester** account has its own login, its own consent record, and its own capabilities: instrumentation on, notes on, what-if on, forking on, and a visible marker in every Campaign they touch so a real table can never be confused with a test one.

`user · system · agent` is the **actor** vocabulary for Records (L14) and is unchanged. Tester is an **account** kind, and a tester's Records still write as `user`.

### Determinism is tested here or nowhere

The determinism harness (§9) is instrumentation too, and it belongs in this ecosystem rather than beside it:

- Replay every Component's golden fixtures on every target platform and diff the state hash.
- Export and reimport the Campaign at every Moment and compare.
- **Diff two machines against the same Ledger.** A determinism bug that only appears on one architecture is unfindable without this, and it is cheap while the system is small.

### What this costs, honestly

This is a second product, built beside the first, and it is a substantial fraction of the work in the first year. It is also the thing that decides whether the design can be *tuned* at all — a system with thirty ordered slots and a dozen interacting ceilings cannot be balanced by intuition, and the alternative to building these tools is shipping a game nobody can adjust.

The scheduling consequence, which `phase-map.md` carries: **the instrumentation ships inside Phase 3, the Spike — beside the Substrate, not after it.** It is not a later phase's cleanup; the Spike is not done until you can open any resolution and watch it assemble.

Open list: `dictionary.md` L30.

---

## 12. Claude operability

Claude writes most of the code and will need to read and sometimes write production data. That is a first-class architectural requirement, and it is also the single largest new risk surface in the system. The design goal is that **Claude having a bad day cannot destroy anything.**

The event-sourced design is an enormous advantage here. Done right, an agent physically *cannot* delete data — the worst case is a bad appended Record, corrected by another Record.

### 12.1 What not to do

**Do not point a general SQL MCP server at production with write access.** The evidence is unambiguous:

- Anthropic's own reference Postgres MCP server is **archived**, after Datadog found a SQL injection that bypassed its read-only restriction (August 2025).
- Independent testing of 14+ SQL MCP servers in July 2026 found read-only enforcement bypassable in most: denylist gaps, comment injection, multi-statement, CTE bypass, and `SELECT ... INTO OUTFILE` file writes on 13 of them.
- **Read-only must be a Postgres `GRANT`, never a string check in a server.**

And the cautionary tale that defines the category: in July 2025 an AI agent deleted a production database *during an explicit code freeze*, then fabricated records and misreported what it had done. The conclusion that matters: **a rule that exists only in the prompt is a request.** Every control below is enforced beneath the model, not in it.

### 12.2 Ops — the typed admin CLI

Claude touches production through `ops`, never through SQL. Same repository, sharing the domain types and the Fold.

```
ops campaign list --owner <id> [--status active]
ops campaign inspect <campaign-id>            # folded state + recent Records, redacted
ops campaign replay <campaign-id> --at <moment>
ops campaign diff <campaign-id> --from <moment> --to <moment>
ops records tail <campaign-id> --limit 50 [--type ...]
ops export campaign <id> --out ./scratch/c.jsonl --redact
ops repro <campaign-id>                       # → redacted export → local Scratch DB

# writes: a separate binary, separate credentials
ops-write correct <campaign-id> --op <named-operation> --args ... \
    --reason "support ticket 482; double-counted Record rec_abc" [--commit]
```

Why a CLI rather than SQL through MCP:

| | Raw SQL | Typed Ops CLI |
|---|---|---|
| Blast radius | Unbounded within grants; one missing `WHERE` is Campaign-wide | Bounded by the function signature |
| Correctness | The model re-derives your invariants from the schema every time | Invariants live in TypeScript and are tested |
| Auditability | Query text in a log | Named operation, typed args, mandatory reason |
| Token cost | Schema introspection every session | Near zero — measured comparisons show order-of-magnitude differences |
| Reviewability | You review SQL under time pressure | You review one readable command |

Design rules:
- **`--dry-run` is the default; `--commit` is explicit.** Dry-run prints the exact Records that would be appended *and the before/after folded-state diff*. That diff is far more useful than any SQL `EXPLAIN`.
- **`--reason` is required** and non-trivial. No reason, no write.
- Writes go through the same domain command handlers as normal play, so every invariant applies. There is no path that bypasses validation.
- **Writes only ever append.** Enforced at the database (rule 11).
- Output is semantic — resolve IDs to names, return meaning rather than UUIDs, truncate sensibly. Error messages should teach: "no Campaign with that slug; did you mean X? try `ops campaign list --owner ...`".

### 12.3 The Scratch loop — the default debugging path

`ops repro <campaign-id>` exports one redacted Campaign, loads it into a local disposable Postgres, and points the app at it. Claude then has *full* read and write freedom against a copy, with zero blast radius.

**This is unusually cheap for an event-sourced system and it should be the normal way bugs get fixed.** One Campaign's Ledger is small, self-contained, and replaying it reproduces the bug deterministically. In most cases Claude never needs production at all — and every fixed bug leaves behind a golden fixture as a byproduct.

Redaction is on by default: emails and names become stable pseudonyms via deterministic hashing with a secret salt, so referential integrity survives and Claude can still reason about "the same player" across Records. `--unredact` requires a reason and is logged.

This also shrinks the prompt-injection surface. The Ledger contains player-written strings — untrusted content by definition — and the less of it that reaches Claude's context, the better.

### 12.4 Agent identity and corrections

Every Record's `actor` is one of:

```ts
| { kind: 'user';   userId }
| { kind: 'system'; component }
| { kind: 'agent';  agentId, model, sessionId, operatorUserId, approvedAt }
```

- **Agent writes get their own actor kind and their own database role.** Agents logging in as humans is the documented way audit trails get destroyed. `WHERE actor->>'kind' = 'agent'` must be a queryable, alertable thing, reviewed weekly.
- **Record the model and version.** When auditing a bad correction six months later, that matters.
- **Corrections are compensating Records**, never edits, carrying `correctsRecordId` and the reason. Because a correction is just a Record, `ops-write undo <record-id>` is a generic, always-available inverse. The worst realistic outcome of an agent write is a wrong-but-recorded correction, fixed by another correction.

### 12.5 Repository conventions for Claude

Claude writing the code changes real decisions, not just style.

**What it reinforces:**
- **Types as guardrails.** A type error costs nothing; a runtime bug found in month four costs everything.
- **Tier 0 declarative Components.** Pattern-matching a new Component against an existing one is dramatically more reliable than novel imperative code. Every Component pushed down a tier is a reliability win.
- **Rigid, identical file layout** (§6.3). Predictable structure makes "add a Component like the currency one" a safe instruction.
- **Explicit over clever.** Repetition beats abstraction. A pattern repeated forty times is easy to read, extend, and verify; a clever abstraction must be reconstructed every time it's touched.
- **Small files, one concept each.** Long files bury the relevant part.
- **Lexicon terms used exactly**, in code and in conversation.

**What it forbids:**
- Metaprogramming, reflection, runtime code generation, decorators with hidden effects
- Implicit behavior — nothing important happens because of a naming convention or a side-effecting import
- Deep inheritance; composition only
- Magic ORMs. Write the SQL.
- Any dependency whose behavior can't be understood from its call site

**Repository requirements that exist specifically for this:**

- **`CLAUDE.md` at the root, under 200 lines.** Points at this document, states the Lexicon and the non-negotiable rules, and names the one canonical example of each artifact type to copy. Bloat causes rules to be ignored; the test for each line is "would removing this cause a mistake?"
- **`.claude/rules/*.md` with path scoping** so detailed conventions load only when Claude touches matching files — Ledger invariants for `/ruleset/substrate/**`, Ops conventions for `/ops/**`. Keeps the root file small.
- **Every mechanically checkable rule in §3 enforced by CI.** Instructions are context; CI is enforcement. A rule Claude can violate silently eventually will be. The two that cannot be checked — special-casing at the Component layer, and PII — are review discipline, and saying so is better than pretending a gate exists.
- **`PreToolUse` hooks as the real boundary**, not settings alone: deny any command matching `ops-write ... --commit` without a time-boxed approval token; deny `psql` and `pg_dump` against production hosts; deny reads of `.env*`.
- **`PostToolUse` audit hook** appending every tool call to a log outside the repository. The agent's own account of what it did is not evidence.
- **A read-only investigator subagent** with no write tools at all, for diagnosis.
- **Side-effecting skills marked so the model cannot invoke them** — deploys and corrections are typed by a human, never chosen by Claude because the code "looks ready."

### 12.6 Secrets

Two distinct threat models, and conflating them is the common mistake: secrets leaking into git, and **an agent with shell access putting a secret somewhere it shouldn't.**

**Layer 1, which is most of the ballgame: production credentials are never reachable from any shell Claude runs in.** They live in the hosting platform's secret store and a password manager. Not in `.env`, not on the dev machine.

Below that: a separate low-privilege `.agent-secrets` file for what Claude legitimately needs, with `.env*` denied in settings *and* independently blocked by a hook — two mechanisms, assuming one fails. Secrets at rest via SOPS + age (encrypted in git, key outside the repo, zero vendors, works forever). `gitleaks` in pre-commit and CI. Every credential Claude can reach must be individually revocable and cheap to rotate, so a leak is a thirty-second rotation rather than an incident.

---

## 13. Environments, migrations, deployment

### 13.1 Three environments, one of them ephemeral

**Local** — Docker Compose with the exact production Postgres major version. Where Claude does 95% of its work. Reset in seconds.

**Preview** — created per pull request, destroyed on merge. Database is a branch of production's *schema* (not its data). **The load-bearing step: every migration runs against a fresh branch of production's schema on every PR.** That catches "works on my database, not on the real one" before merge, automatically, with no judgment required.

**Production.**

A permanently-running hand-maintained staging environment is ceremony for one person. It costs money continuously, drifts within weeks, and its value is delivered better by an ephemeral preview branched from the real schema.

### 13.2 Migrations

Two-artifact discipline is the single most important property when an agent writes migrations: **Claude edits a schema declaration (a statement of intent, which models are good at), and a deterministic tool derives the DDL (mechanical diffing, which models are bad at).** You then review a small SQL diff rather than auditing hand-written DDL.

Whatever tool produces that split, the durable assets are a directory of `.sql` files and a table recording which have run. If the tool is abandoned or acquired into irrelevance, you delete it, keep the SQL, and write a sixty-line runner in an afternoon.

Non-negotiable rules, in `CLAUDE.md` **and** in CI:
- Never push schema directly to anything but a local throwaway database
- Never hand-edit an applied migration
- Always generate, then read the produced SQL before committing
- Destructive statements (`DROP`, `RENAME`, `ALTER COLUMN ... TYPE`, `SET NOT NULL`) fail CI without an explicit approval marker in the PR

Add a **migration safety linter** in CI to catch the specific Postgres traps: non-nullable columns without defaults, `CREATE INDEX` without `CONCURRENTLY`, type changes that rewrite the table, and statements taking `ACCESS EXCLUSIVE` locks. And set `lock_timeout` on the migration connection — a migration that waits on a lock queues every subsequent query behind it, which is the classic "the migration was instant but the site was down for four minutes" incident.

### 13.3 Three mutability classes — do not conflate them

| Layer | Mutability | Change mechanism |
|---|---|---|
| The `records` table's own DDL | Effectively frozen | Additive columns only, essentially never |
| Record *payload* schemas | Versioned, never rewritten in place | Upcasters at read time |
| Projections and read models | **Fully disposable** | Drop and rebuild |

The practical payoff of event sourcing is that schema churn lives in the disposable layer. Projections need no expand/contract at all — drop, recreate, replay. This is why replay speed is worth caring about early: it is what makes that superpower affordable.

For structural changes to Record payloads, use versioned schema files that are **frozen once shipped** plus a read-time upcaster chain, and keep a corpus of real historical payloads as golden fixtures. CI asserts every historical fixture still parses and upcasts to the current shape. **This is the single highest-value test in the system**, because the most likely destructive act by an agent is "simplifying" an old schema file it perceives as dead code. The golden corpus turns "you broke ten years of history" into a red build in thirty seconds. Freeze non-latest version files with a CI rule that fails on any modification.

### 13.4 Drift detection

Once per release, in nightly CI: build a database from the full migration history and diff it against a `pg_dump --schema-only` baseline. A non-empty diff means someone — a human, an agent, or a manual production session — introduced drift. **This one check is worth more than everything else in this section**, because it detects "production doesn't match the code," which is what actually bites at year five.

### 13.5 Deploy

Migrations and application deploy are **separate steps with a gap**, never one atomic action:

```
merge → run migrations (expand-only, additive, safe by construction)
      → verify health
      → deploy app
      → (later, separate PR) contract migrations
```

If migration and deploy are atomic, the compatibility window that makes expand/contract work cannot exist. Nearly every zero-downtime migration failure traces back to skipping this.

### 13.6 Release and versioning

Version bumps are declared explicitly per change, as a reviewable file in the diff — not inferred from commit messages. **An agent writing commit messages is exactly the wrong entity to be deciding whether something is a breaking change.**

Two orthogonal version axes, never conflated:
- **Package version (semver)** — this Component's own contents changed.
- **Compatibility** — a monotonic integer format number plus named capability flags, declaring what a Component needs and what Editions it supports. Integers are unambiguous; ranges invite creative misinterpretation, including by agents.

CI gate on every Component release: load the previously published schema, diff, **fail on removed field, narrowed type, new required field, changed enum semantics, or changed ID meaning.** Allow new optional fields, new items, new enum members, widened types, documentation. The agent cannot be trusted to recognize a breaking change, so a machine decides.

---

## 14. Testing

The governing principle: **code review has been lost as a quality gate and must be bought back with automation.** Be willing to spend more CI time and setup effort than a conventional solo project would.

### 14.1 Spec first — the highest-leverage practice here

Write the rules in prose, in `SPEC.md`, *before* implementation. Then: one test per rule.

This is not style advice. Controlled testing across model families found tests grounded in an explicit written specification produced substantially more correct code than ungrounded tests — and a plain-prose spec caught nearly every seeded bug where a coverage-oriented prompt with no spec caught almost none. Doubling the test budget without grounding did not close the gap. **Writing the spec is the testing strategy**, and it costs ten minutes per Component.

Every Component ships a `SPEC.md` (§6.3), written first.

### 14.2 The mix

Invert the classic pyramid toward integration. Unit tests over agent-written code have a specific pathology: the model writes the implementation *and* the test from the same misunderstanding, so the test asserts the bug. Integration tests over real Postgres and real command handlers are much harder to fool, because reality participates.

| Layer | Share | Covers |
|---|---|---|
| **Integration** (real Postgres) | ~50% | Command → Record → Fold → query |
| **Golden / snapshot** | ~20% | Payload compatibility, Fold outputs, state hashes |
| **Property-based** | ~15% | Substrate invariants |
| **Unit** | ~10% | Genuinely pure logic |
| **End-to-end** | ~5% | Five to ten critical journeys |

Property-based testing is unusually well-matched here, because the architecture hands you natural properties: folding the same Records twice gives the same state; folding in chunks equals folding whole; every historical payload upcasts to the current shape; no command produces an invalid state. **You specify the properties; Claude implements the generators.** Models write property-based tests competently but frequently write *weak* properties, so the division matters.

### 14.3 Guarding against the specific failure modes

Large-scale analysis of AI-authored code finds it degrades structurally rather than logically: duplication up sharply, refactoring down, error-masking constructs up. Unit tests detect none of that. So:

- **Duplication check in CI** with a threshold. It is invisible to every other check in the pipeline.
- **Lint rules aimed at model smells**: no floating promises, no empty catch, exhaustive switches, no `any`.
- **Mutation testing nightly on the Ruleset**, tracked as a trend. It is the only cheap way to answer "are these tests asserting anything?" — a question coverage cannot answer and that matters far more when tests are machine-written.
- **Golden files are a ratchet.** Never regenerate them wholesale — that is exactly what an agent proposes when a golden test fails, and it silently destroys the guarantee. Regeneration requires an explicit flag, and CI flags any PR touching more than a handful.
- **A test that has never failed has not been shown to work.** Periodically break something deliberately and confirm the suite goes red.
- **Determinism check**: run the seeded fixture generator twice, assert byte-identical output. Catches wall-clock use, unseeded randomness, and unordered iteration — common failures that are otherwise invisible until they produce a flaky test at 3am.

### 14.4 Fixtures as Record streams

Do not write fixtures as SQL inserts or projection rows. Write them as **sequences of commands replayed through the real handlers.** They then cannot go stale relative to the schema, they exercise the invariants, they double as demo and load-test data, and they keep the replay machinery constantly exercised rather than only during an emergency.

---

## 15. Client, mobile, and notifications

### 15.1 PWA only

Ship a progressive web app. No wrapper, no app store, not yet.

The decisive argument is commercial: **a PWA sells digital goods at payment-processor rates in every country, permanently.** Every store scenario reintroduces a 15–30% platform cut plus exposure to a legal landscape that is, as of August 2026, actively unresolved in both the Apple and Google antitrust cases. The current favorable US position on external payment links is a litigation artifact, not policy. Do not build a business model that depends on it.

The technical argument is nearly as strong. **There is no way to hold a WebSocket open in the background on mobile — not in a browser, and not inside a wrapper's WebView either.** A native wrapper does not fix this; it only swaps web push for platform push. So the phone can never be a passive real-time client, which means: **foreground is a socket, background is a notification.** That is exactly the asynchronous between-Session experience this game wants, so the constraint and the design agree.

Storage eviction, the other headline PWA weakness, is irrelevant to a server-authoritative system. Losing local cache costs a refetch, not game state.

Since Safari 26 (September 2025) every site is installable on iOS without a manifest, so the install path is uniform — ship a proper manifest anyway for icon, name, and scope control.

### 15.2 Keeping the wrapper door open — cheap now, expensive later

If every one of these holds, a later Capacitor wrap is a few days' work. If they don't, it's a multi-week refactor.

- **Fully relative asset and API paths.** No hardcoded origin. This is the single most common thing that breaks a wrap.
- **All storage behind one module.** WebView storage behaves differently.
- **Push behind a `NotificationTransport` interface.** Web push and platform push have different token lifecycles; swapping should touch one file.
- **Token auth held in memory plus secure storage, never cookie-only sessions.** Third-party cookie behaviour in WebViews is a classic wrapper-breaker.
- **`env(safe-area-inset-*)` and `viewport-fit=cover` from day one.** Needed for notched browsers regardless.
- **Build output stays a plain static bundle.** No server-runtime coupling in the app shell.
- **Reconnect-on-resume as a first-class code path** — listen for visibility and resume events, re-establish the socket, re-sync from the server. Needed for mobile browsers today, and it's exactly what a wrapper needs.

Do *not* create native project directories "just in case." They rot.

### 15.3 Notifications

Channel-abstracted on the server, with per-participant preferences.

- **Email is the guaranteed tier.** No install, no permission, works for everyone. For an asynchronous game where the notification carries genuinely required information, this is the correct default, and transactional email engagement is nothing like marketing-blast engagement.
- **Web push is the opportunistic fast tier.** Offer install and push only *after* someone finishes their first Session, when the value is proven — never on first load. On iOS, push requires home-screen install and a real user gesture, which makes the funnel the constraint rather than delivery.
- **Digest, never spray.** One "three Campaigns are waiting on you" beats three notifications. This is the highest-leverage anti-fatigue decision, and games have the worst push opt-in rates of any category precisely because of frequency.
- Skip SMS.

---

## 16. Commercial model, where it touches architecture

- **Free core.** The Ruleset and its Asset authoring are free. A user who has bought nothing can build Settings, Adventures, and Assets, and run a Campaign.
- **Three sellable things: Components, Adventures, and Asset instances.** Schema Components are cheap; Behavior Components that anchor a genre are priced like the supplements they functionally are. **Ownership is perpetual and spans Editions** (§5.5).
- **A Setting bundles the Components it requires.**

**Ownership versus sharing — the distinction the whole model rests on:**

- **Buying a Component is permanent.** A GM who owns a Component may run Campaigns with it forever. There is no subscription required to *use* what you own, ever.
- **The subscription only removes the requirement that other people own it too.** A GM's active subscription means players at their Table need own nothing.
- **On lapse, the Campaign pauses — it does not degrade and it does not lose anything.** If every remaining participant owns the Components in play, nothing happens and play continues. If someone doesn't, the Campaign pauses until one of three things: that player leaves, any participant purchases an extension, or the GM resubscribes.

A pause is a deliberate design choice over the alternatives. Silently degrading the game would corrupt the Campaign's state; deleting anything is unthinkable; and letting play continue would make the subscription meaningless. A pause is honest, reversible, and legible to everyone at the Table — and the three exits mean the group always has a way out that doesn't depend on the GM.

- **Access may lapse. The Ledger is never deleted.** Non-negotiable.
- **Never gate anything a player needs behind the player's own wallet.** A player may *voluntarily* buy an extension or the Component itself. A player must never be *required* to. That pressure arrives exactly when revenue is flat.

Three structural notes:

**The pricing model rewards depth; the architecture requires shallowness.** Deeper dependency chains mean more items per sale. That is a standing incentive to build the thing that kills the ecosystem, and it will feel like good bundling at the time. Rule 3 exists partly to resist it.

**Editions are not a monetization event.** Charging again for owned Components in a new Edition is the fastest way to make an Edition feel like a shakedown. New Edition, same library.

**The permanent obligation.** Additive-only means the Component count only rises and every Component is owned forever. The constraint is not how many can be written; it is how many can be kept alive, alone, for a decade. Two decisions buy that number up: declarative Components can't rot the way code can, and the depth cap means a change never cascades.

---

## 17. Day one versus later

**Must be right on day one — cannot be retrofitted:**

The Ledger and its full Record shape · Entity identity and Facets · **the Substrate Noun set** · the Verb set · **the attempt-as-vector model, Thresholds, and the Resolution Record** · Delivery as a Record field · the Proposal/Decider protocol · the Socket contracts · Campaign isolation · Edition pinning · the uniform Verb shape · the two Verb classes · the Listener contract · the Layer lattice · aggregation rules · fixed-point arithmetic · causal links and tags on Records · export/import · append-only enforced at the database · **the Component contract** · **the Lens contract**.

**And a scheduling consequence of "the base game is Components":** the component system — manifests, dependencies, versioning, suppression, ordering — must work before anything is playable. It cannot be deferred and refactored in later. See `phase-map.md`.

**Additive later — no Substrate change:**

Every Component · every Setting and Adventure · every future Edition · the Chronicle and curation layer · the marketplace · maps and visual layers · video · cross-Campaign worlds · snapshots · async projections · the mobile wrapper.

**The trap in that split:** the Chronicle is a later feature, but *its inputs are foundation*. Records must carry causal links and abstract tags from the first day or curation can never work. The simulation produces material; something else decides what surfaces to whom. Building the world-simulation without the curation layer produces a very expensive random number generator, and this is the easiest item on the list to skip.

---

## 18. Open questions

Deliberately unresolved. Each is a real decision, not a placeholder.

1. **The Verb set — closed LAST.** The list in §4.3 is explicitly preliminary and is now scheduled to be frozen *after* every other list, not before. The evidence for completeness is worked examples, and worked examples come from the other lists. Still the one genuinely irreversible decision; now sequenced so it is decided against the finished system rather than against imagination.

1a. **The Dimension Spaces (L21).** Which kinds of push can meet each other at all. Upstream of everything, because every effect in the system is a position in one of these Spaces, and a coarse decision made quickly.

1b. **The Capacity set (L29).** The most load-bearing list in the system: what a character is made of, *and* the axes an attempt is split across — because in the attempt Dimension Space the Dimensions **are** the Capacities. It comes *after* L21 and *before* L22, which looks backwards and is not: the attempt Space has to exist before its axes can be named.

1c. **The remaining Dimensions (L22), then the Channels placed within them (L23).** The order for the whole set is `L21 → L29 → L22 → L23 → L27/L28 → L1/L2/L3 → L4/L5/L18/L25 → L7 → L26 → L6`; `dictionary.md` Part 11 is the tiebreaker.

2. **The Layer lattice outside resolution** — progression, economy, movement, knowledge, social standing. The resolution region is drafted at thirty slots (§8), five of them added in Phase 0. Magic needed seven layers and thirty years. Guessing low is a Substrate break; guessing high is just unused numbers, so err high.

3. **How many Allocation Points, and where they come from.** Five is a placeholder with nothing behind it; the natural home is a Capacity — *capacity to divide attention*. Also open: a ceiling on summed Baseline shares, and whether it shares Enhancement Capacity's budget.

3a. **The Ruleset's default policy for entering Ordered time.** Entry belongs to base Ruleset, not the Substrate — three Substrate rules were tried and each failed on a real case. Leading candidate: *a vector placed on an unwilling target*.

3b. **The Listener cascade limit, the behaviour at the limit, and the evaluation order across simultaneously-satisfied Listeners.** The third is a determinism hazard of the same severity as aggregation order.

3c. **What happens to a vector whose target is removed from play entirely** — not dead, but gone.

4. **Tier 2 sandbox choice.** Deferred until a Component needs it. Whatever it is must run the same compiled artifact in browser and server.

5. **The Socket list (L27, now three) and the Economy (L28).** Both settled in shape as of Aug 2026; L31 Timings and L32 Moment kinds replaced them as the blocking pair.

6. **What is the free artifact a stranger encounters?** Everything in §16 monetizes people who already play; nothing acquires anyone. Components and Asset instances are the most demonstrable things in the design and the best candidates, but this is unanswered — and the field survey is unambiguous that distribution, not product, is the binding constraint.

7. **Which instrumentation surfaces ship to real tables?** Some are too good to hide behind a tester flag — resolution expansion, notes, the event log. Some would ruin a scene if opened mid-fight — time travel, what-if, direct state authoring. See `dictionary.md` L30.

8. **Which Asset types get user authoring, and in what order?** Every authoring surface is a real unit of work (§6.4). The Ruleset's own types ship with it. Beyond that it's a scheduling question with commercial consequences, since authorable types are what let users build without buying.

9. **How many Editions can realistically be kept alive?** §5.3 says all of them, forever, with passing tests. That is the right default and it has a cost that grows. At what point does an Edition become read-only — playable but no longer receiving Component support?

10. **What does disabling mean, per Component?** §6.5 gives three shapes — frozen, dormant, hidden. Whether those three cover everything, and which is the right default for a Component that declares nothing, is unresolved.

11. **What happens when a Lens has no vocabulary for something.** A Component ships a mechanic the simplest Lens cannot express. Degraded form, narration only, or invisible? Needs a policy every future Lens inherits, and it will be hit the first time a Component ships after the Lenses are fixed.

12. **Is there a canonical Lens?** The one that *is* the game — in the marketing, in the answer to "what's it like to play," the one everything else is measured against. A system whose honest answer is "it depends what you pick" is a toolkit, which is the one thing this has consistently refused to be.

**Answered since the first draft:** the Component-removal question (add and disable only, never remove — §6.5); the subscription lapse model (pause, three exits — §16); what a user may author (Asset instances where the capability exists, never Asset types — §6.4); that the base Ruleset is itself Components (§1); that the Verb set is a taxonomy of consequence rather than action (§4.3); that Nouns are five kinds rather than one pool (§4.4); and that the frame problem is legislated away rather than solved (§4.0B); that Channels are positions in a Dimension Space so relationships are derived rather than declared (§4.4A); that Channels combine by per-Dimension addition and Guards subtract per Dimension (§4.4A); that Transient fully resolves before Persistent (§4.4A); and that Attributes are linear while Scale is a separate exponent (§4.4B); that "Effect" is retired in favour of "Verb" (§7); that every Verb has one uniform shape with exactly one primary target (§7.2); that Verbs return nothing and consequence travels through Listeners watching state (§7.3, §7.5); and that the Ledger can record things no Verb caused (§7.7).

**Answered in the August 2026 design pass** — full reasoning in `dictionary.md` Part 12:

- **Verb classes reduced from four to two.** Replacement and Continuous dissolved into *a vector with a window*.
- **Degree, Cost, the two-axis Outcome, the scalarization rule, outcome ladders and Difficulty-as-machinery: all deleted.** An attempt is a vector; things in the world declare Thresholds; players spread Allocation Points to set direction.
- **Period retired.** There is only the Moment. Objects take turns.
- **Perception retired.** A single Delivery field; the Lens decides what is shown; in-fiction knowledge is an optional Component; belief-folds deleted; the information-set invariant satisfied by construction.
- **The server folds and is authoritative.** Tier 1, not deferrable.
- **Sockets**, and the Vocabulary/Behaviour split that makes them safe.
- **Percentages sum rather than compound; one rounding point per vector, truncating toward zero.**
- **Enhancement and Participation Capacity** — the ceiling belongs in the fiction, not the arithmetic.
- **Magnitude is assembled at resolution**; everything source-side collapses to sums at creation, so a placed vector is a direction, four numbers and a pin.
- **The Resolution Record** is Substrate — inputs and a hash, every layer derivable.
- **Ordering under parallelism is answered.** The participant set is the scene; cross-scene vectors pin to the next Moment both share; conflicts combine; Participation Capacity settles what cannot. There is no *who went first*, because nobody went first.
- **The Layer lattice** has a drafted resolution region: E-100…E-500, C-100…C-600, R-100…R-1400.
