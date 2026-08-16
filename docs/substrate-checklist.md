# Substrate Checklist

**Revised August 2026.** The workbook for filling the lists is `substrate-lists.xlsx`; the guide is `work-lists.md`; the reasoning is in `dictionary.md` Part 12.

**The Substrate is the data model, the instruction set, the execution semantics, and the frames everything runs inside.** Everything else is a Component, including the base Ruleset. Nothing here can be revised once a Campaign exists.

⬤ **Design** — a real decision with real alternatives.
○ **Specify** — the shape is settled; write it down precisely.

---

## What changed in v2

Two of the four blocking decisions were framed wrongly.

**Nobody has ever built a small closed set of action primitives.** Every attempt either stayed small and lost information (Schank: 11 primitives) or grew past a hundred once it had to run (VerbNet: 153–162 predicates, 39 thematic roles). But the requirement is weaker than we assumed: **the Substrate does not need to represent the action, only the consequence.** Actions are infinite; consequences are finite. The Verb set is a taxonomy of state change, not of doing.

**Fixed property lists across all kinds have failed independently in five fields.** What survived is homeostatic property clusters and conceptual spaces, and both say the same thing: **do not model what a thing is, model what it affords.** A capacity is kind-agnostic because it never claimed to describe an essence.

**And Nouns split into five kinds** — Capacity, Tag, State, Resource, Relationship — which behave differently under change, aggregation, and rendering.

## The pipeline

```
1  FICTION       Unbounded, natural language, forever.
2  FRAMING       What is actually at stake. Provably unautomatable in general.
──── Substrate ────
3  ALLOCATION    The player spreads Allocation Points; that sets direction.
4  RESOLUTION    The Resolution Socket sets a signed magnitude.
5  CONSEQUENCE   Vectors placed and pinned; at a Moment they assemble,
                 combine, meet Guards, and land. Thresholds fire the rest.
                 Then Listeners.
───────────────────
6  RENDERING     Each Lens narrates at its own granularity.
```

---

# A. What exists

**Section A is answered.** Decisions and reasoning are in `dictionary.md`; the outstanding work is the lists, not the shape. Kept here for reference.

**New from Section A:** every interaction in the system is a **Channel** — a position in a **Dimension Space**. Channels combine by adding their Dimension values; **Guards** subtract per Dimension; **Transient** Channels fully resolve before touching **Persistent** ones. Relationships between Channels are therefore *derived from positions*, never declared, so they can never contradict and a new Channel is automatically correct against every existing one. See `dictionary.md` Part 2A.


**A1 ○ Entity.** Anything that persists and has identity. What qualifies as an Entity rather than a value on one? The test is whether something else needs to refer to it later.

**A2 ○ Facet.** One Component's data attached to one Entity. A Component reads and writes only its own.

**A3 ⬤⬤ The Capacity set (L29)** — *the largest single decision.*
Graded, kind-agnostic dispositions. What an attempt is assisted or resisted by. Should be **small**.
*The test per candidate:* state it as a capacity rather than a quality, then check it applies without absurdity to a person, a ship, a faction, and a storm. *Capacity to exert force* passes. *Strength* does not.
*And the half that is easy to skip:* what you deliberately leave off. Nothing above the Substrate can put it back, and this is where the stance lives.

**A4 ⬤ Tags.** Cluster membership — open, unbounded, no defining property, **optional magnitude**. Identified by ID and not by name; never imply other Tags. Decide the **shape**, not the list, since the list grows with Components: bare symbol or valued? Namespaced? Can a tag imply another? Who may mint one? Then the seed vocabulary the base Ruleset ships with, which is what Components may rely on existing.
*Tags are the multiplicative surface* — the thing that makes a dozen Verbs interesting — and the pressure valve for consequences the Verbs cannot quite carry. They absorb more than they look like they should.

**A5 ⬤ States.** Named conditions, optional magnitude, exclusive within an axis. What other rules key on *by name* — "advantage against a prone target" cannot be written against a −2. What are the axes? Do states stack or does only the highest apply (`max()` removes a bug class)? How does a state end?
*A one-of-N state is a single field, never N booleans.*

**A6 ⬤ Resources.** Depletable, replenishable, with named thresholds. The only genuinely numeric-over-time values. Which are Substrate and which belong to Components?

**A7 ○ Relationships — ANSWERED.** A **Relationship is a Category of Entity**, holding one **Connection** per participant, each stance stored **independently** — *A loves B while B tolerates A* is the normal case, not an exception. Every system in the entity survey stored these on one endpoint, which is exactly why relationship mechanics desync in play.

**A8 ⬤ Kind and labels.** Does an Entity carry a kind tag, and does kind change which values apply or only what they are *called*? Traveller's precedent: one set of slots, per-kind labels.

**A9 ○ Scale — SETTLED.** `effective magnitude = attribute × 10^scale`. Attributes stay linear so 10 versus 11 means the same thing at every Scale, and **addition is only legal within one Scale** — enforced, not merely discouraged, so silent loss of small values is impossible rather than unlikely.

**A10 ⬤ The significance scalar.** Every generalizing system converges on one — Hit Dice, level, CR, Tier. Does one exist, stored or derived?

**A11 ⬤ Asset types.** Which structures describe concrete authorable things, and which get user authoring first.

**A12 ○ Fixed-point scale — SETTLED.** One global scale, **four decimal places**: store `125000`, meaning 12.5. Plus log-integers wherever values are compared across Scales.

**A13 ○ Open world — SETTLED.** Absent means *unknown*, never zero, with explicit presence on every field. Under closed-world, adding a Component would silently change the meaning of every prior Record. A **declared soft default** treats an unspecified value as absent for resolution convenience, without ever recording it as absent — so a later Component can fill in the truth without rewriting history.

---

# B. What can change

**Section B is answered.** Decisions and reasoning are in `dictionary.md` Part 3 and `architecture.md` §7. Kept here for reference.

**New from Section B:** "Effect" is retired — a proposed change is a **Verb**, full stop, and "Effect" is reserved for a future in-fiction meaning. Every Verb has **one uniform shape**. Verbs **return nothing**; consequence propagates through **Listeners** that watch *state*. The **Verb list is closed last**, not first. And the **Ledger does not require a Verb** to record something.

**B1 ⬤⬤ The Verb set — PRELIMINARY, closed LAST.**

Preliminary: `create · destroy · move · alter magnitude · transfer · set state · clear state · add tag · remove tag · form relationship · break relationship · reveal · conceal · bind to condition · advance clock · apply · assume category · shed category · repin`

Three of those — `apply`, `assume category`, `shed category` — came from running the consequence test on eight fictional actions; `repin` came later, out of the timing work. Note the absences: nothing about attacking, persuading, crafting, or singing. Those are fictional descriptions of attempts; the Substrate sees only what changed.

*Decided:* this list is **not** settled now. Every other list produces the worked examples that are the only real evidence of completeness, so freezing Verbs first means freezing them against imagination. Build L1–L5, L7, L18, L21–L23 and L25–L29, then run all of it against this list, then freeze. See `dictionary.md` L6.

**B2 ○ Verb shape — SETTLED. One shape for all.**

`verb · source · target (exactly one) · secondary (zero or more) · direction · magnitude · class · layer`

`direction` is *what* is being changed — per-Dimension percentages summing in absolute value to 1; a declared **Channel** for harm, computed from **Allocation Points** for an attempt. `magnitude` is *how much* — a whole number, signed, at a declared **Scale**. This is the Channel idea generalised past harm to every Verb. Written to the Ledger verbatim.

Exactly one primary target: a Verb affecting three people is three Records, so "who did this happen to" is never ambiguous.

**A Verb returns nothing.** There is no execution to return from.

**B3 ⬤ Listeners — NEW, and partly open.**

A declared watch on a *state* condition. Evaluated at R-1400, after the Moment's Verbs have landed and the Resolution Record is written; produces Verbs pinned to a **later** Moment, class `Triggered`. Data in a Component's manifest, never code. Watches **state, not Verbs** — "is this now true," never "did that just happen."

*Open:* the closed set of condition forms (L26); the **evaluation order when several fire at once** — a determinism hazard of the same severity as C4 aggregation; the cascade depth limit and the behaviour on hitting it.

**B4 ○ Records without Verbs — SETTLED.** A Verb invocation is one Record type among several. GM assertions, notes, Moment and Session boundaries, Proposals, compensations, supersessions, Listener firings, cascade-limit records and Edition conversions change no state and are still permanent history. *"What happened" is strictly larger than "what changed"* — which is the reason a closed Verb set is achievable at all. The discipline: non-Verb Records must stay genuinely inert, CI-enforced.

---

# C. How changes combine

**Section C is answered.** Full detail in `dictionary.md` Part 2A. Kept here for reference.

**What Section C turned into.** It stopped being a set of abstract combination rules and became a concrete, ordered pipeline, because every question in it was answered by working a real case — two pyromancers buffing one fireball, a fire elemental with a fire aura, a flamethrower that can only take so much enhancement.

**C1 ○ The frame rule — SETTLED.** Everything not named in a Verb is unchanged **by definition**. The cost goes on the wall: *anything you fail to list simply does not happen, silently.* Mitigation: every Component's tests must include at least one "and this did **not** change" assertion.

**C2 ⬤ Verb classes — SETTLED at two.** `Activated` and `Triggered`. Replacement and Continuous both dissolved into *a vector with a window*: a vector already standing in the space **is** "instead of," and a condition-scoped vector **is** "while true." Two mechanisms deleted, none added.

**C3 ⬤⬤ The Layer lattice — DRAFTED for resolution, thirty slots.** Three regions: entity preparation (E-100…E-500, 5), vector creation (C-100…C-600, 6), resolution at the Moment (R-100…R-1400, 19). Phase 0 added **R-750** (Scale conversion), **R-780** (standing-vector cap, reserved), **R-850** (flat Guards, once per contributing source) and split the combine into **R-800** within a source and **R-1000** across sources, which is where cancellation now happens. Every boundary is forced by a worked case rather than guessed. Outside resolution — progression, economy, movement, knowledge, social standing — the lattice is still empty. See L7.

**C4 ⬤ Aggregation — SETTLED for the resolution path.** **Everything adds by default.** Percentages sum and are applied once; absolutes add afterwards; Guards sum proportionally, then subtract flatly. Nothing compounds anywhere, because compounding stops being commutative the moment you round between steps. Aggregation for the other Noun kinds — Tags as set union, States with an optional max — is settled in shape and comes with those lists.

**C4a ⬤ Capacity — NEW, and the most consequential thing in Section C.** A ceiling on how much enhancement a vector can carry, captured from its source at creation. It moves the stacking problem out of the arithmetic and into the fiction: a better gun holds more, upcasting raises it, Resources can buy it. It also makes the sum-versus-compound choice free, since three buffs hit the cap either way. Bounds enhancement only, never reduction.

**C5 ○ Moments, rounds, and the cascade cap — OPEN.** Two caps needed: a depth cap on Moments within one cascade, and a total-work cap. On hitting either: **halt without applying the pending round** and write a `cascade limit reached` Record, so the world sits at the last complete Moment. Same question as B3's Listener cascade limit — answer once. **The numbers are still blank.**

**C6 ○ Replacement conflict rule — MOOT.** Replacement is no longer a class. Two standing vectors simply combine.

**C7 ○ Determinism rules — SETTLED, with three additions from Sections B and C.** No floating point. No wall clock. Ordered iteration or stable-key sort. Byte-wise string comparison. Counter-based PRNG keyed by `(record, entity, purpose)`. Edition and Component version pinned per Record. **Plus:** rounding is truncate-toward-zero, applied once per vector at R-400; Listeners satisfied simultaneously sort by `(layer, component_id, listener_id, target_entity_id)`; and **pre-sum, never pre-apply** — source-side contributions collapse to sums at vector creation, and nothing is ever applied early.

---

# D. Resolution

**Section D is answered, and mostly by deletion.** Full detail in `dictionary.md` Part 2C.

**What happened.** An attempt turned out to be a **vector**: direction is what you are trying to do, signed magnitude is how well it went, and a failure is the same direction with a negative magnitude. Things in the world declare **Thresholds**, and whatever bars are crossed, happens. That one move deleted five concepts and added none.

**D1 ⬤⬤ The Outcome space — DELETED.** *Degree* is the magnitude. *Cost* is consequences at other Thresholds on other Dimensions. There is no two-axis space and no ladder of named steps — the **Substrate declares no steps at all**; each object declares its own bars. L8 and L9 are retired.

**D2 ⬤ The scalarization rule — DELETED.** There is no pair of scalars left to rank.

**D3 ⬤ Difficulty — DELETED as separate machinery.** It is a Threshold, set by the GM or by an Adventure's script, in canonical magnitude units. What survives is a different obligation: **every Ruleset declares a magnitude reference** — *a competent attempt at an ordinary task is about 5* — so content and CI have something to check against instead of a silent mismatch.

**D4 ⬤ The unadjudicable case — OPEN, and narrowed.** The qualification problem is a formal guarantee: preconditions cannot be finitely enumerated, so there will always be attempts nothing can resolve. *The GM asserts X* as a first-class Record type is what makes that survivable. The GM-less answer: it becomes a **Proposal** with a `Person` Decider, and with no GM the Moment arrives and the declared default fires. **The default is chosen per Campaign at setup; the recommended one is "no change."**

**D5 ○ The resolution interface — ANSWERED.** A resolution hands back three things: the **direction** (from the declaration), the **signed magnitude** (from the Resolution Socket), and the **per-slot intermediates** (derivable, for the animation and the explanation channel). Calibration is now *the same distribution over magnitude*, machine-checkable by sampling.

**New in D, and the real remaining work:**

- **Allocation Points.** A player spreads whole points; direction is the proportion spent. **Points buy precision, not power** — one point all-in is 100%, same as five — so this progression axis can never inflate damage. *Open: how many, and where they come from.*
- **What a point may be placed on.** Settled in shape: **in the attempt Dimension Space, the Dimensions are the Capacities.** The contents are L29, blocking.
- **Shaping.** Gear changes the shape of an attempt, in **points**, in two forms: **Bonus Points** (adds points to a Dimension and to the total — redistributive, cannot inflate) and **Baseline** (a Dimension counts as at least N points without raising the total — genuinely raises total effect, clamped by Enhancement Capacity). Order is Bonus Points → Baseline. *Demand was retired in the Phase 0 re-attack.*
- **Settled and worth not re-litigating:** shaping is snapshot only, never ambient; a Threshold may be declared on total magnitude as well as on one Dimension; an attempt runs the whole assembly pipeline; **gear contributes its modifiers automatically and visibly.**

---

# E. Time

**Section E is answered, and mostly by deletion.** Full detail in `dictionary.md` Part 2B.

**E1 ⬤ Period — DELETED.** There is only the **Moment**. A turn, a round, a downtime week and a season are the same thing at different grains, published by the **Time Socket**. Every question E1 asked — fixed or variable, who closes one early — belongs to the occupant.

**E2 ○ Tick — ANSWERED, restated.** The stamp on a Moment when it *actually occurs*. Logical only. It is what makes replay exact while the pending side of the world stays symbolic.

**E3 ⬤ Budget — A SOCKET.** How actions are rationed, what replenishes when, whether reactions exist: all occupant. **The Vocabulary is Substrate** — the Economy Unit *names* (L28) that content depends on, and that a `repin` must name. Rarely swapped in practice, because swapping it means playtesting a whole economy from scratch.

**E4 ⬤⬤ The parallelism rule — ANSWERED, and differently than proposed.** **The participant set is the scene.** A vector whose scope reaches outside it is pinned to **the next Moment both share** — an ordinary pin, no synchronisation machinery. **Conflicts need no tiebreak**: they combine, exactly as two fire vectors do, and where they genuinely cannot, **Participation Capacity** settles it. There is no *who went first*, because nobody went first.

*Socket contract clause:* the Time Socket must guarantee any two participant sets eventually share a Moment.
*The cost, deliberately accepted:* scenes are **simultaneous** until their shared Moment arrives. A table wanting sequence puts a shared Moment between them.

**E5 ○ Session — UNCHANGED.** A marker for a live gathering; carries no rules.

**E6 ○ Crossing between grains — ANSWERED.** **Windows freeze; they never convert.** A ward with three rounds left keeps three rounds left, and resumes exactly there if Ordered time restarts. **Pending arrivals cannot survive the transition**, and nothing extra is needed to guarantee it — Ordered time cannot end while anything is anchored to another Entity's Moment. *Knowable consequence:* a party can raise wards, end the fight, and carry them indefinitely. Where content does not want that, a window declares a coarse expiry alongside its fine one.

**Also settled here:** a Moment is a **reference, not a tick**; **objects take turns**, which is what makes cooperation work with no help action; a **repin must name a cost**; there is **no special case for death**. *Open:* what happens to a vector whose target is removed from play entirely, and names for the four standing-vector kinds.

---

# F. Knowledge

**Section F is answered by deletion.** Full detail in `architecture.md` §4.5.

**F1 ⬤ Perception — RETIRED.** Three things were being conflated and only one is Substrate:

| | |
|---|---|
| what a player **sees** from what they have | the **Lens** |
| what a character **knows** — misremembers, was told wrong | a **Component**, optional; ships in v1 because it is good |
| which **bytes reach which browser** | infrastructure |

**Every piece of Campaign data a client is entitled to is in that client's browser**, and **every layer of a Resolution Record is visible to everyone by default.** Secrets are a later deliberate decision, never the default posture.

**F2 ⬤ The visibility descriptor — REPLACED by Delivery.** One field on a Record: who receives it, default everyone. It exists for exactly two reasons a Component cannot serve — **a GM's prep**, and **purchased content** whose full text would otherwise ship to every participant. Absent means everyone, so it can be added later without breaking history.

**F3 ⬤ Provenance — A COMPONENT.** A Chronicle Component emits its own `rumour` Records carrying source and reliability in the payload. No Substrate field, and therefore no permanent hole in early history.

**F4 ○ The one thing that is not deferrable.** **The server folds and is authoritative; clients render.** Tier 1. If clients folded from Records, the first withheld Record would silently diverge that client's Fold. Folding on the server keeps one canonical state forever and turns *hide this* into *send less*. And client-side hiding is theatre: anything a client must not have is never serialised into a byte sent to it.

**Deleted along with Perception:** belief-folds; the requirement that a Fold tolerate gaps; the information-set invariant and its validator; write-time visibility descriptors and the current-membership-versus-membership-at-the-time question.

---

# G. Decision

**Section G is answered.** Full detail in `dictionary.md` Part 5.

**G1 ○ Proposal — ANSWERED and extended.** A **pending Entity**, using the same pinning machinery as a vector: repinnable, cancellable, queued, visible. *"Give me another day"* is a `repin`, and it costs something.

**G2 ⬤ Decider — TWO KINDS, not three.** `Auto` (a Component decides) and `Person` — **always carrying a Moment and a default.** A human decider with no fallback is never legal: one quiet person behind an open-ended decision stops everything behind them, which is the most common way a months-long asynchronous game dies. A live table is served by a very long deadline, which costs nothing. **A table vote is `Auto`** — adding a `Vote` kind would freeze one voting rule into the Substrate forever.

**G3 ⬤ Rails — OPEN (L12), with two additions.** Socket occupants are Components and therefore have rails too — *does the app run initiative* is a Time Socket dial. And **Threshold visibility is a built-in GM setting**, not a per-Component rail: same content, two very different games.

**G4 ⬤ Default actions — ANSWERED in shape.** A default is a **Standing Order**, which **is a Listener** — no new machinery. The Component publishes the Listener template; **the player fills in the parameters**, so the authoring line holds. Critically, a default must include a **default allocation**, not just a default verb, because direction is half of every attempt. This is what makes absence survivable: a player away for two weeks leaves standing orders instead of a hole.

---

# H. The Ledger

**Section H is answered.** Full detail in `dictionary.md` Part 9 and `architecture.md` §4.1.

**H1 ○ Record shape — the test, then the list.** A field belongs from the first Record if **its absence cannot be given a safe default**, because absent means *unknown*, not zero.

`campaign · seq · type · version · payload · actor · causation · correlation · ` **`moment`** ` · tick · edition · component_version · tx_id · created` — all required. **`delivery`** is the exception: absent means everyone, so it can be added later.

*Changed:* **`moment` replaces `period`** (tick orders, Moment groups — the animation and the Resolution Record both key off the grouping). **`delivery` replaces `visibility`.** `created` is a wall clock for humans and is **never folded**.

**H2 ⬤ What is stored — CHANGED.** **Store inputs and a state hash; derive the layers.** The Fold is deterministic, so every intermediate is recomputable against the pinned Component version — storing them stores what can always be recreated, and the hash makes recomputation self-checking. Storage drops sharply in exactly the case that would have hurt: a long fight with many participants.

**H3 ○ Fold contract — strengthened.** Pure, total, deterministic, no I/O. Plus: **the server folds and is authoritative**, there is exactly one Fold, and **snapshots are a rebuildable cache** verified against the Moment hash, never a source of truth.

**H4 ⬤⬤ Correction semantics — the hard one.** Two mechanisms, and they are not equivalent:

- **Compensation** — add an opposite. The Fold stays a simple left-fold and history reads as a story that includes its own mistakes. **This is the default.**
- **Supersession** — a Record declaring that an earlier one should be read differently. Necessary for the non-invertible cases (a Category change, a revealed secret) and **it is where event-sourced systems rot**: once any Record can be retroactively neutralised, nothing can be trusted without scanning forward.

**Supersession goes through `ops-write` only** — `--dry-run` by default, `--reason` required, human-approved. A mis-click gets compensation. A bug that wrote garbage gets supersession, with a name attached.

**H5 ⬤ Causal tags — DOWNGRADED from blocking (L19).** Provenance moved into Component payloads, and thematic tagging can follow it as an optional additive field. Records written before it exists have no tags, permanently — but the Chronicle is a later feature, so those Records predate it anyway, and a Component can derive tags retroactively from Verb patterns. **`causation` stays Substrate** and is a different thing: engine-level lineage, not in-fiction provenance.

**H6 ○ Export / import.** Byte-identical round-trip, tested from day one — because `ops repro` depends on it, and because a Campaign a user can export and reimport elsewhere is a trust feature and not only a debugging tool.

**H7 ○ Concurrency.** `seq` is server-assigned and monotonic **per Campaign**; `tx_id` makes retries safe. The Campaign is both the isolation unit and the concurrency unit, so scale is many independent small serial streams rather than one large contended one.

---

# I. Contracts

**Section I is answered in shape**, with the open parts marked. Full detail in `architecture.md` §6 and §6A.

**I1 ⬤ The Component contract — writable now.** A manifest declares: identity and exact version · Categories it attaches Facets to · Nouns it publishes, **Published or Private with no default** · Nouns it depends on at exact versions · Verbs it uses · **Layers it writes at**, from the fixed lattice · **Listeners it declares**, plus any **Listener templates** it exposes for Standing Orders · **Dimensions or Channels it adds** · **Economy Units it uses** · **which Socket it fills, if any** · what it **suppresses** · disable semantics — frozen, dormant or hidden, **and the default for a Component that declares nothing** · execution tier.

*Depth ≤ 2 survives* because a Socket is a hub rather than a chain — but **Socket occupants may depend on each other at most one level deep.**

**I2 ⬤⬤ The Socket contract — NEW.** An occupant declares its **Vocabulary** (the additive list of names content may depend on — Moment kinds, Economy Units, persistent-state names) separately from its **Behaviour** (everything else, which content never names). Swapping an occupant is always Edition-level. **A Bundle is valid only if every Socket is filled — exactly one occupant each, never zero, never two — and a Bundle with an empty Socket must fail to load.** CI-enforceable.

**I3 ⬤ The Lens contract — SIMPLIFIED.** Two clauses died: *what a Lens may read* (it reads everything) and the information-set invariant (satisfied by construction). **Calibration sharpened**: a Lens's dice must produce **the same distribution over magnitude** the Resolution Socket produces — one number rather than named bands, and machine-checkable by sampling both. Unchanged: a Lens never changes what a character can do, never writes, and is **not part of the Fold**, so its formulas are exempt from additive-only and may be rewritten retroactively. **New:** the per-slot pipeline must be *available* to a Lens; rendering it is optional, and shaping must appear as its own named step attributed to the item that caused it.

**I4 ○ Active Set.** Bundle, Components, versions, Edition, **and which Component occupies each Socket**. Hashed and recorded. Add and disable only, never remove — and a Socket occupant cannot be disabled.

**I5 ⬤ Template contract — OPEN, and concrete now.** A Template sets Capacities, Allocation Points, Enhancement and Participation Capacities, and default Thresholds. Full profile, partial overlay, or weightings — undecided.

**I6 ⬤⬤ The content contract — NEW, and it is the commercial surface.** *Users author instances, never types* is now specific enough to write down.

**A Setting or Adventure author may declare:** Entities, their Categories and Attribute values · **Thresholds** on objects · **Enhancement and Participation Capacities** · **Guards**, polarised or not, proportional or flat · Standing Order parameters. **Placing a new Channel is not on this list** — a Channel's position is permanent once shipped, which makes it a type.

**They may never declare:** a Verb · a Dimension · a Layer · an Economy Unit · a Listener template. And the authoring tool must make that **structurally impossible**, not merely disallowed.

This list decides how much a user can build without buying anything, which makes it a commercial decision as much as a technical one.

---

# J. Instrumentation

**New, and it ships inside Phase 3 — the Spike — beside the Substrate rather than after it.** The Spike is not done until any resolution can be opened and watched assemble. Full detail in `architecture.md` §11A, open list in `dictionary.md` L30.

**The stance.** Play may hide things; **the instrumentation never does.** Every Record, every resolution expanded slot by slot, every modifier and the item it came from, every Threshold checked and by how much it was missed.

**J1 ○ Reading.** A searchable event log over the whole Ledger · full resolution expansion for any resolution ever · a state inspector at any Moment · time travel to any Moment.

**J2 ⬤ Changing.** **What-if** — re-resolve any past resolution with an input changed and watch the whole pipeline recompute, **never writing to the Ledger**. Forking a test Campaign at any Moment. Active Set swapping mid-Campaign, test Campaigns only. Direct state authoring, recorded as such.

**J3 ⬤ Recording.** Notes anchored to a Record, an Entity, a Moment, or **a single slot of a single resolution** — not a separate document. Note kinds: bug, balance, **confusion**, idea. Session recording and replay. A playtest report exported as one artifact.

**J4 ○ Testers are a first-class account kind** — their own login, their own consent record, instrumentation and what-if and forking enabled, and a visible marker in every Campaign they touch so a real table is never confused with a test one. *(Tester is an **account** kind; `user · system · agent` remains the **actor** vocabulary on Records, and a tester's Records still write as `user`.)*

**J5 ○ The determinism harness lives here.** Golden fixtures replayed on every target platform with state hashes diffed; export-and-reimport at every Moment; **two machines diffed against the same Ledger.** A determinism bug that appears on one architecture only is unfindable without it, and it is cheap while the system is small.

**What it costs.** A second product built beside the first, and a substantial fraction of the first year. It is also what decides whether the design can be **tuned** at all: thirty ordered slots and a dozen interacting ceilings cannot be balanced by intuition.

---

# Order of work

On paper, before any code. These cannot be revised and cannot be discovered later.

1. **L21 — the Dimension Spaces.** Which kinds of push can meet each other at all. Coarse, and upstream of everything, because every interaction in the system is a position in one of these Spaces. Doing this first is what makes L29 answerable.
2. **L29 — the Capacity set.** Small, kind-agnostic, each entry stated as a capacity and checked against a person, a ship, a faction and a storm. **And what you deliberately leave off.** Doubly load-bearing: what a character is made of, *and* the Dimensions of the attempt Space.
3. **L22 → L23** — the Dimensions inside the remaining Spaces, then the Channels placed in them.
4. **L27 and L28** — the Socket list and the Economy Units. Both block the Component contract, and L28 blocks every spell and ability ever written.
5. **L1 → L2 → L3** — Categories, Universal Attributes, Category Attributes. All three blocking, and the three character sheets get written here.
6. **L4, L5, L18** — Tag shape and seed vocabulary, State axes, and the aggregation operators for the non-resolution Noun kinds.
7. **L25** — the transient-to-persistent conversions the Landing Socket performs.
8. **L7's remaining regions** — the Layer lattice outside resolution: progression, economy, movement, knowledge, social standing. The resolution region is drafted.
9. **L26** — the Listener condition forms, plus the cascade limit, the behaviour at the limit, and the evaluation order.
10. **L6 — the Verb set, LAST.** Not third, and not an afternoon. Every list above produces the worked examples that are the only real evidence of completeness; freezing the Verb set before them means freezing it against imagination. When they are done, run every entry and every worked example through the closing procedure, then freeze.

**Then, and only then, code** — starting with the Ledger, the Fold, and **the instrumentation**, which is what makes everything after it possible to tune.

**The forcing function.** Write the character sheet first, at the most detailed Lens you can imagine. What is printed on it is what has to exist underneath. Then do the same for a ship and a faction. The values all three need are the Capacity set; the ones only a person needs tell you whether the Substrate is genuinely kind-agnostic or a person schema wearing a costume.

**The warning.** A distinction that never reaches a **Lens** does not exist for players — and it is pure cost forever, because it is additive-only. Ultima Online built a full ecology, players killed everything faster than it respawned, nobody ever noticed, and it was quietly removed.
