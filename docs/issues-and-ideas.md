# Issues and Ideas

*A critique of the design in `dictionary.md`, `the-game.md` and `architecture.md`, and a list of things the design makes possible that nobody has written down.*

**Written August 2026.** Everything cited has a URL inline. Everything numeric has been worked, and the arithmetic is reproducible from the numbers given.

Two halves:

- **Part A — Issues**, ranked. Each entry gives what it is, the evidence or the worked example, how bad it is, when it becomes unfixable, and the options.
- **Part B — Ideas**, generative. Each entry gives what it is, which existing machinery it uses, and what it costs.

The tone is deliberately blunt. Several of these say a piece of the design is wrong. Four of them say a piece of the design is arithmetically broken in a way that is demonstrable on paper today.

---

# Part A — Issues

## The ranking

Severity is *how much damage if unaddressed*. Cost-to-fix-later is *what it takes to change once Campaigns exist*, given additive-only and a frozen Substrate.

| # | Issue | Severity | Cost to fix later |
|---|---|---|---|
| A1 | Allocation Points collapse to all-in, and the granularity tax eats most of the roll | **Critical** | Cheap mechanically, catastrophic for the pitch |
| A2 | Uncapped pre-Guard cancellation — the fire-elemental build is a dominant, unbounded defence | **Critical** | Substrate: needs a clamp slot that does not exist |
| A3 | Flat per-Dimension Guards make pure Channels strictly dominant and delete the Dimension Space | **Critical** | Substrate: R-1000 semantics are frozen |
| A4 | Enhancement Capacity is trivially bypassed by absolute modifiers and by Baselines | **High** | Substrate: R-350 is before R-500, permanently |
| A5 | Cross-scene simultaneity permits a genuine double-spend on shared Resources | **High** | Substrate-adjacent; needs a rule that does not exist |
| A6 | The direction vector does not actually sum to 1 in fixed point; apportionment is unspecified | **High** | Determinism bug; cheap now, an Edition break later |
| A7 | "Two fixed-point numbers are never multiplied" is false at R-900 | **High** | Cheap now; a second rounding point is an Edition break later |
| A8 | Turn position, not tactics, decides how much damage a creature takes | **High** | Base Ruleset turn order — versionable, but every content piece is written against it |
| A9 | Comprehension load: 8 axes × hidden bars × a 26-slot pipeline is past every documented tolerance | **High** | Not fixable by code; fixable only by Lens design and by cutting |
| A10 | Shaping's three forms do not commute and no order is declared | **High** | Cheap now; a determinism hazard the moment two items exist |
| A11 | Threshold authoring burden: every improvised object needs 8 numbers, not one DC | **High** | Design-level, not code; but it is what kills crunchy systems |
| A12 | Hidden thresholds versus total transparency — the tension is self-destroying, and the Ledger accelerates it | **Medium-High** | Cheap now (Delivery), expensive to retrofit trust |
| A13 | Participation Capacity needs the tiebreak the design says it does not need | **Medium-High** | Cheap now |
| A14 | Percentages sum → the third pyromancer contributes exactly zero, visibly | **Medium** | Cheap: one default Component |
| A15 | Unpolarised Guards make you unhealable; content authors will hit this constantly | **Medium** | Cheap now, if polarity is mandatory rather than optional |
| A16 | Log-integer addition by lookup table is not associative — the commutativity claim is false | **Medium** | Cheap now; a determinism bug later |
| A17 | Scale-crossing needs a bespoke rule per Component and will be hit on day one | **Medium** | Design; grows with the content library |
| A18 | The 26-slot lattice plus unbounded modifier tiers plus dependency-overrides-timestamp | **Medium** | Substrate. Permanent |
| A19 | Depth ≤ 2 plus no cross-Component reads will produce one monolithic harm Component | **Medium** | Structural; visible by Component #10 |
| A20 | Event sourcing operational reality: replay cost, versioning, determinism debugging | **Medium** | Manageable, but it is a continuous tax |
| A21 | PWA-only + async play depends on iOS notification behaviour that is genuinely constrained | **Medium** | Tier 2, but a wrapper is months of work |
| A22 | The time budget does not close, and the comparables are worse than the plan assumes | **Critical (business)** | Not fixable by architecture |
| A23 | Async play is a real gap but the evidence for the *product* is thinner than the evidence for the *need* | **High (business)** | Testable cheaply, and is not being tested |

---

## A1 · Allocation Points collapse to all-in, and the granularity tax eats most of the roll

**RESOLVED — Phase 0, Aug 2026.** The granularity half is closed by making the resolved value one integer operation, `⌊points × magnitude ÷ total points⌋`; nothing is lost and the truncation that remains is the intended penalty for spreading. The all-in half is **accepted and answered by authoring rather than arithmetic**: the authoring tool requires a downside bar on every Threshold set, the GM tool offers one by default, and instrumentation counts tasks that ship without one so playtesting measures it. The point count itself is still open and belongs to L29 and paper play.

**What it is.** The headline mechanic — spread whole points, direction is the proportion spent, magnitude is carved up by it — has two properties the design does not appear to have worked out.

**The clean result first.** Let a task declare thresholds `t₁ … t_k` on `k` Dimensions, and let the attempt resolve at magnitude `M`. Shares sum to 1, so dimension *i* clears iff `sᵢ · M ≥ tᵢ`, i.e. `sᵢ ≥ tᵢ/M`. Therefore:

> **You can clear exactly those subsets S for which `Σ_{i∈S} tᵢ ≤ M`.**

The allocation game *is* a 0/1 knapsack with hidden weights. That is a genuinely elegant thing to have fallen out — and it is also the problem, because a knapsack with hidden weights has no gradient. There is nothing to learn from a failure except the identity of that one lock.

**Now the integrality.** Points are whole. With `n` points, every share is a multiple of `1/n`, so to clear `tᵢ` you must commit `⌈tᵢ · n / M⌉` points. The real condition is:

> **`Σ_{i∈S} ⌈tᵢ · n / M⌉ ≤ n`**

Run the design's own worked example — lock at manipulation 5, needle at perception 4, corridor at stealth 1, magnitude 12:

| Points `n` | Largest set clearable | All three? |
|---|---|---|
| 1 | 1 | no |
| 2 | 2 | no |
| 3 | 2 | no |
| **4** (the book example) | **2** | **no** |
| 5 | 2 | no |
| **6** | **3** | **yes** |
| 12 | 3 | yes |

`5 + 4 + 1 = 10 ≤ 12`, so in continuous shares all three are clearable. **With four points they are not, and with five they are still not.** The design's own three worked splits all fail at least one bar, and the document reads that as a feature ("in-but-stung", "stopped-but-safe"). It is not a feature; it is the rounding. The player who wanted 5/12, 4/12, 1/12 = 42%/33%/8% cannot express it with quarters.

**The granularity tax, stated generally.** Committing `⌈tᵢn/M⌉` points delivers up to `M/n` more magnitude than the bar needed, on every dimension. Across `k` dimensions the wasted magnitude is up to `k·M/n`. **With 4 points across 3 axes that is up to 75% of the roll thrown away.** Against the eight-ish Capacity list L29 contemplates, four or five points is not a coarse instrument, it is a broken one.

**And then all-in.** Because shares sum to 1, allocating anywhere is *strictly subtractive* from everywhere else. There is no cost to concentration except the bars you neglect. So:

- If a task's only bars are `≥` bars, **all-in on one Dimension is strictly optimal**, always. One point, 100%, maximum magnitude on the axis you care about.
- Spreading is forced *only* by downside bars — the corridor's *"stealth 1 or below wakes the guard."* An unallocated dimension resolves at 0, which is below any `≤` bar.

So the entire tension of the headline mechanic rests on GMs and content authors reliably placing **penalty bars on every axis a player might neglect**. That is not a light requirement; it is authoring burden A11 restated as a load-bearing rule. Where authors do not do it — and improvising GMs will not, weekly, across eight axes — the mechanic collapses to "put everything on the thing you're doing", which is exactly the system it was designed to replace.

**Cross-check against precedent.** Effort-splitting is not new and its history is not encouraging. *The Riddle of Steel* splits a Combat Pool between offence and defence per exchange ([TRoS wiki](http://tros.thewestwinds.net/index.php?title=Combat)); it is admired and almost unplayed. Exalted 2e's dice-splitting and tick economy is the standard worked example of a system whose optimisation surface swallowed the game ([The Gaming Den's "Anatomy of Failed Design"](http://www.tgdmb.com/phpBB3/viewtopic.php?t=50260)). The One Roll Engine's "declare several actions and read one roll" is the closest structural analogue in print and is consistently described as the part groups drop ([RPGnet thread](https://forum.rpg.net/index.php?threads/godlike-wild-talents-ore-how-do-the-rules-really-play.475252/)). The pattern across all three: **the split is interesting for the designer and expensive for the table.**

**Game-theoretically**, blind allocation across contested positions is a Colonel Blotto game. The literature is unambiguous that these have no pure-strategy equilibrium above trivial sizes and that optimal play is a randomised mixture — at S=13 over three fields, the optimum is a 1/3 mix of (3,5,5), (3,3,7) and (1,5,7) ([Blotto game](https://en.wikipedia.org/wiki/Blotto_game)). "The optimal strategy is to randomise" is a fine property for a wargame and a poor one for a roleplaying game whose pitch is *you decide what to pay attention to*.

**How bad.** This is the pitch. `the-game.md` opens with it. If it degenerates, the design's differentiator is the vector-cancellation model alone, which is A2 and A3.

**When it becomes expensive.** The mechanic itself is cheap to change — it lives in the Resolution Socket and in the interface. What is expensive is that the *Allocation Point count* is bound to the Capacity list (L29), the Capacity list is bound to the Dimensions of the attempt Space, and Dimensions are additive-only forever. Choosing eight Capacities and five points bakes in an unfixable granularity tax.

**Options.**

1. **Far more points than five.** Twelve to twenty. The pitch survives; the interface becomes a slider or a budget bar rather than a pile of tokens; the granularity tax falls to `k·M/n` with a big `n`. This is the cheapest fix and probably the right one. It costs the "whole points, hand-countable" aesthetic.
2. **Allocate in fractions of the magnitude directly, with a `min` grain.** Same thing, honest about it.
3. **Let unallocated dimensions resolve at a floor rather than zero** — e.g. every Dimension gets `M/(2k)` free. This makes spreading a real choice rather than the only defence against downside bars, and it removes the dependence on GMs authoring penalty bars.
4. **Reduce `k` hard.** Three or four attempt Dimensions, not eight. `k·M/n` is linear in `k`. This contradicts the current lean of L29 and is worth the fight.
5. **Accept all-in and design around it** — make the interesting decision *which* axis rather than *how much*, and put the tension in the Channel/Threshold interaction instead. This is a real option and it deletes a lot of machinery.

**Do the paper playtest before choosing.** This is `phase-map.md` Phase 2, whose gate is the one the phase map says matters most.

---

## A2 · Uncapped pre-Guard cancellation: the fire-elemental build is a dominant, unbounded defence

**RESOLVED — Phase 0, Aug 2026. Accepted as content, with insurance.** An Entity that keeps an aura on itself is a large ability and gets priced per creature; this is a balance question, not a Substrate hole. **R-780 is reserved** as a ceiling on standing self-scoped cancellation and left unbounded in v1, because reserving a slot is free and needing one after Campaigns exist is an Edition break.

**What it is.** The rule *"damage cancels out before it reaches the target"* combined with *"Capacity bounds enhancement only, never reduction"* creates an unbounded defensive stack that the design explicitly believes cannot exist.

**The design's own showcase is the exploit.** From Part 2A:

```
a cold bolt arrives, magnitude 8              temperature −8
its own fire aura is present, magnitude 5     temperature +5
R-800 combine                                 temperature −3
R-900 guard: 100% temperature-POSITIVE            does not apply
                                              takes 3 cold
```

The elemental is a **standing durable fire aura** plus a **polarised 100% Guard on temperature-positive**. Two ordinary objects. Note what each does: the Guard makes the aura harmless to its owner, and the aura provides 5 points of free cancellation on the temperature axis, **every Moment, forever, before Guards, unmetered**.

**Generalise it.** Nothing in the Substrate stops a character carrying one such pair per Dimension. With the L21/L22 physical Space at, say, six Dimensions:

- six standing auras at magnitude 5, one per Dimension, each polarised in the direction its paired Guard covers;
- six polarised Guards at 100% covering exactly those directions.

Result: **you cancel 5 of every incoming Dimension every Moment before anything is checked, and you are immune to the direction your own auras point in.** Enhancement Capacity does not touch this — it bounds a vector's magnitude assembly, not the number of vectors standing on an Entity. Participation Capacity does not touch it — it bounds how many *sources* contribute to one thing, and these are all one source: you. Proportional Guards are clamped at 100%, which is precisely what makes the polarised half safe to max out.

**Why the design believes this cannot happen.** From the decisions log: *"Amplification compounds toward absurdity; reduction converges on zero. Only one of those needs a wall."* That is true of *reduction*. Cancellation is not reduction — it is a **positive vector on the same axis**, and the ceiling logic that governs vectors (Enhancement Capacity) governs the *magnitude of one vector*, not the count of standing vectors scoped to an Entity. There is no slot in the lattice at which "total standing self-scoped cancellation" is clamped, and R-800 is defined as a plain sum.

**How bad.** This is the arithmetic hole with the largest blast radius, because it is invisible until someone builds it and then it is unanswerable — the rules say it works, and the transparent breakdown will show exactly why. Worse, it is *the design's own worked example scaled up*, so it will be discovered by the first player who reads Part 2A.

**When it becomes expensive.** Now. There is no lattice slot for a cancellation ceiling, and adding a slot to the R-region is an Edition break — every Campaign folds differently.

**Options.**

1. **A Capacity for it.** *Capacity to sustain standing vectors* — a count and/or a summed-magnitude ceiling on self-scoped standing vectors, evaluated at E-500 and clamped at a new slot around **R-750**, between resolve and combine. Reserve the slot now even if the number is left at "unbounded" for v1. Reserving a slot costs nothing; needing one later costs an Edition.
2. **Forbid self-scoped standing vectors from participating in R-800 combination**, and route them through a Guard-shaped slot instead. Cleaner, and it costs the fire elemental its elegance.
3. **Make the polarised-Guard-plus-aura pair a single authored preset** with its own bookkeeping, so the pair cannot be replicated across Dimensions. Weakest option; it is a special case at the Substrate layer, which CLAUDE.md rule 7 forbids.
4. **Charge for it in doubloons** — a standing vector keeps doubloons `committed` while it stands. This is the most in-keeping fix (bound by economy, not by an engine limit — the same move as `repin`), and it is cheap. Probably the right answer.

---

## A3 · Flat per-Dimension Guards make pure Channels strictly dominant, and delete the Dimension Space

**RESOLVED — Phase 0, Aug 2026.** A **universal** flat Guard now subtracts from the packet total and is redistributed across Dimensions by integer apportionment, signs preserved, reducing toward zero and never past it. Every direction now lands the same total against the same armour. A **Dimension-named** flat Guard still acts on that Dimension alone, which is what specific resistance should do. Verified in `phase-0-checks.py`.

**What it is.** R-1000 subtracts flat Guards **per Dimension, floored at zero**. Channels' direction values sum in absolute value to 1. Therefore a Channel spread across `d` Dimensions pays the flat Guard `d` times, for the same total magnitude.

**Worked, against armour rated 3 on every Dimension:**

| Channel | Direction | Magnitude | Per-Dimension after flat Guard 3 | Total |
|---|---|---|---|---|
| `fire` | temperature 1.0 | 10 | 10−3 = 7 | **7** |
| `lightning` | temperature 0.3 / integrity 0.7 | 10 | 0 and 4 | **4** |
| a 3-way even Channel | 1/3 each | 10 | 0.33 each | **1** |

Same magnitude. Fire delivers **7×** what an evenly-spread Channel delivers. Lightning delivers 57% of fire.

**This is not a tuning problem; it is structural.** Two facts make it worse:

- The design correctly notes that *"a Guard that covers all Dimensions covers new ones too"*, and encourages universal Guards for exactly that forward-compatibility reason. Universal flat Guards are the case that punishes mixed Channels hardest.
- The compensating advantage of a mixed Channel — harder to cancel, harder to resist with a named Guard — only materialises against opponents who have *specific* counters. Armour is ubiquitous; specific counters are rare.

**Consequence.** Every Channel an author ever places will be pushed toward a Dimension axis. The Dimension Space collapses back into a list of damage types, and the central claim — *"creating a new damage type means placing it in the Space; its relationship to every existing type is then already determined"* — survives on paper and dies in play, because nobody will place anything off-axis.

**How bad.** It removes the reason the Dimension Space exists. Both `the-game.md`'s "fire and ice actually cancel" and the L22/L23 design programme assume authors will use the interior of the space.

**When it becomes expensive.** R-1000's semantics (subtract per Dimension, floor at zero) are Substrate and frozen. After that, the only fix is content discipline — i.e. never shipping universal flat Guards, which contradicts the forward-compatibility argument.

**Options.**

1. **Make flat Guards act on the Packet's total, not per Dimension**, allocated back across Dimensions proportionally to the resolved values. One subtraction, order-free, deterministic. Kills the dominance entirely. Costs: "over-penetration falls out of the arithmetic with no special rule" becomes "over-penetration is a proportional allocation", which is slightly less pretty and just as deterministic.
2. **Keep per-Dimension flat Guards but scale them by the Channel's share on that Dimension.** A Guard of 3 against a 0.3-temperature Channel removes 0.9. Restores neutrality; requires a fixed × fixed multiply (see A7 — which already exists anyway).
3. **Ban universal flat Guards; make flat Guards always Dimension-named.** Cheapest, and it is a content rule not an engine rule, but it fights the additive-only argument in the decisions log.
4. **Accept it and make it the design.** Pure Channels are "focused" and cheap; mixed Channels are "broad" and used for coverage against named resistances. State it explicitly so authors know what they are buying. This is defensible but it means the interior of the Dimension Space is decorative.

---

## A4 · Enhancement Capacity is trivially bypassed

**RESOLVED — Phase 0, Aug 2026.** Hole 1 is **accepted deliberately**: the ceiling clamps percentages, not absolutes, because absolutes grow linearly in the number of contributors and **Participation Capacity is already the wall for that**. Hole 2 is closed — a Baseline is a percentage, so the same ceiling covers it, with no second number on any item. Hole 3 is closed — **Enhancement Capacity belongs to the task or target, never the source**, so it cannot be shopped.

**What it is.** Three separate holes in the ceiling that the whole "the ceiling belongs in the fiction" argument rests on.

**Hole 1 — absolutes bypass the clamp entirely.** The R-region is explicit:

```
R-300   percentages         SUM
R-350   Enhancement cap     CLAMP the summed percentage
R-400   apply
R-500   absolutes           add
R-600   vector clamp
```

Enhancement Capacity clamps **percentages only**. Every absolute modifier is added *after* the clamp. So a lock at Enhancement Capacity 100% — *"cannot be helped by anything"* — is helped by any ambient `+5`. Content authors will write flat bonuses constantly, because flat bonuses are how you make low-magnitude things matter. **The wall has a door in it and the door is the more commonly used one.**

**Hole 2 — Shaping Baselines sit outside the system entirely.** Part 2C says so: a Baseline raises the summed shares above 1, *"a real increase in total effect"*, and the ceiling for it is marked **PENDING**. Two Baselines at 75% on different Dimensions give summed shares of 1.75+ before a vector even exists, because Shaping acts at allocation time. So the single most powerful item class in the game is the one with no ceiling, and the ceiling that does exist (Enhancement Capacity) never sees it.

**Hole 3 — Capacity is captured from the source, so it is shoppable.** *"A vector's Capacity is captured when the vector is created, from its source."* The dominant party composition is therefore: whoever has the highest Enhancement Capacity creates every vector, and everyone else amplifies. Capacity becomes a party resource to be routed around rather than a per-object property. That is not fatal — it is arguably interesting — but it means Capacity must be balanced on *every entity that can create a vector*, which is an enormous and permanent balancing surface for a solo designer.

**Precedent for why the additive choice needs the ceiling to actually work.** The design's argument is that with a ceiling in place, sum-versus-compound stops mattering for balance. That is right, and it is exactly the lesson of Path of Exile's `increased` (additive) versus `more` (multiplicative) split: additive stacking gives "great returns for relatively low investment... [with] diminished returns", so builds are forced to diversify into multiplicative sources ([maxroll damage scaling guide](https://maxroll.gg/poe2/getting-started/damage-scaling)). Here there *are* no multiplicative sources — which is good — but only if the ceiling is airtight. It is not.

**How bad.** High. The ceiling is load-bearing for three separate arguments (why summing is free, why stacking is solved, why progression can raise ceilings instead of numbers). All three weaken.

**When it becomes expensive.** The R-350/R-400/R-500 order is frozen Substrate. Adding a second clamp after R-500 is an Edition break.

**Options.**

1. **Reserve a second clamp slot now** — call it R-550, "Enhancement cap, absolutes" — even if v1 sets it to unbounded. Slots are free; missing slots are not. `architecture.md` §8 already says *err high* on the lattice; this is the concrete case.
2. **Convert absolutes into percentages at authoring time** for anything that could be an amplifier. A content rule, CI-checkable ("an ambient modifier may not be absolute"), cheap, and it preserves the frozen order.
3. **Give Baselines a ceiling and decide now whether it shares Enhancement Capacity's budget.** It should be a separate Capacity — *capacity to be shaped* — because it applies at a different time to a different object. Leaving this PENDING past v1 means shipping the game's strongest item class with no bound.
4. Accept holes 1 and 2 as content-discipline problems and write the CI gate. Given CLAUDE.md's *"if you can violate it silently, the CI gate is missing — say so"*: **this gate is missing.**

---

## A5 · Cross-scene simultaneity permits a genuine double-spend

**What it is.** The scene model says: the participant set is the scene; a vector reaching outside pins to the next Moment both share; *"conflicts need no tiebreak — two scenes sending something at the same faction combine there, exactly as two fire vectors do"*; and where they genuinely cannot combine, *"Participation Capacity settles it."*

That is fine for vectors landing on a target. It is wrong for **shared depletable Resources**.

**Worked.** The party has a shared Resource `coin = 10`. Group A plays Tuesday and spends 10. Group B plays Thursday and spends 10. Neither scene has seen the other. Both pin to Friday's shared Moment. At Friday:

- The two Verbs combine: `alter magnitude, coin, −10` and `alter magnitude, coin, −10` → `−20`.
- Resource aggregation is *"add then clamp"* (L18's known constraint). Clamped at zero.
- Both groups received what they bought. The Ledger records that 20 was spent from a pool of 10.

Participation Capacity does not settle this, because Participation Capacity bounds *how many sources may contribute vectors to one thing* — it is a cooperation bound, not a transactional one. Two spends are not competing for a contribution slot; they are competing for stock.

**And the design already rejected this exact failure once.** `architecture.md` §10.6, on why not local-first: *"CRDT merge semantics are the wrong conflict model. CRDTs guarantee convergence, not correctness. When two players both claim the last thing, the required behavior is to reject one, not merge both."* The scene model reintroduces convergence-without-correctness at the fiction layer, having removed it at the storage layer.

**The narrative version is acknowledged and the transactional version is not.** The document is honest about the duke: *"he is alive on Thursday and dies for everyone when their shared Moment arrives."* That is a stated cost and it is defensible. The double-spend is not a narrative oddity; it is a rules break.

**How bad.** High, and it will surface the first time two sub-groups share an inventory — which is week one of async play, because sharing an inventory is what a party is.

**When it becomes expensive.** Immediately. This needs a rule and the rule has to be in the Substrate, because a Component cannot see across scenes.

**Options.**

1. **Reservation at declaration.** Spending a shared Resource takes a reservation at the moment of *declaration*, not at the Moment of resolution — the resource is decremented into an escrow Entity and released if the action fizzles. This is the correct answer and it is a Verb (`transfer`) plus an Entity, so it needs no new machinery.
2. **Declare shared Resources Participation-Capacity-1** and give Participation Capacity a real, deterministic tiebreak (see A13). Blunt, and it prevents legitimate simultaneous small spends.
3. **Forbid cross-scene shared Resources** — every scene carries its own purse and reconciliation is a fiction problem. Honest, restrictive, and it removes a lot of the appeal of shared-world play.
4. **Make over-spend legal and consequential** — the pool goes negative and the shortfall is a debt with a Threshold. Genuinely in the spirit of the system, but only if chosen deliberately.

---

## A6 · The direction vector does not sum to 1 in fixed point

**RESOLVED — Phase 0, Aug 2026. Dissolved rather than fixed.** An attempt's direction is never materialised as fixed point; it is stored as whole point counts plus a total and resolved in one integer operation. There is no apportionment method to choose and therefore **no Alabama paradox** — verified exhaustively in `phase-0-checks.py`.

**What it is.** *"The sum-to-1 rule is enforced by construction. A player never types a decimal and can never produce an invalid direction."* That is true in rationals and false in the 4-decimal-place fixed point that Part 7 mandates.

**Worked.** Three points, one each on three Dimensions. Shares are 1/3. At four decimal places, `3333 + 3333 + 3333 = 9999`. The direction sums to 0.9999, not 1. Magnitude 12 resolves to 3.9996 on each axis instead of 4.

The design's own Bonus Points example is worse-looking and, by luck, exact: 4/7, 2/7, 1/7 → `5714 + 2857 + 1429 = 10000`. That it happens to come out right is coincidence, not construction.

**The general problem has a name.** Dividing a fixed total into whole units is *apportionment*, and it is one of the few areas of applied mathematics with a genuine impossibility theorem: Balinski and Young proved that **any method that respects the quota rule produces paradoxes once there are four or more parties**, and no method avoids the Alabama and population paradoxes simultaneously ([apportionment paradox](https://en.wikipedia.org/wiki/Apportionment_paradox)). Concretely, largest-remainder — the obvious fix — has the Alabama paradox: *adding an Allocation Point can reduce a Dimension's share.* A player who spends an extra point on perception and watches perception go **down** will report it as a bug, and it will not be one.

**How bad.** The magnitude of the error is tiny. The consequences are not: (a) an invariant the design states as guaranteed is not guaranteed, and invariants that are almost true are how determinism bugs get in; (b) the paradox is player-visible on the exact screen the design promises will show every step.

**When it becomes expensive.** Choosing an apportionment rule is a Substrate decision, because it changes every fold. Cheap today, an Edition break the moment a Campaign exists.

**Options.**

1. **Name the rule and write it down.** Largest remainder with a deterministic tiebreak on Dimension ID, byte-wise. Deterministic, documented, and accept the Alabama paradox — but *test for it* and make sure the interface never lets a player see it (e.g. by showing shares, not resolved values, at allocation time).
2. **Do not divide.** Keep the allocation as integers all the way through: resolved value on Dimension *i* = `⌊pᵢ · M / P⌋` computed as one integer operation, with the remainder assigned by a stated rule. Same problem, but only one rounding site and it is inspectable.
3. **Increase fixed-point precision for direction specifically.** Doesn't remove the paradox, only shrinks it. Not a fix.
4. **Raise the point count** (see A1) so shares are naturally finer. Helps, does not solve.

---

## A7 · "Two fixed-point numbers are never multiplied together" is false

**RESOLVED — Phase 0, Aug 2026.** The false claim is retired. There are **exactly three rounding sites, all truncating toward zero: R-400, R-750, R-1050** (the proportional-Guard slot, renumbered from R-900 when the re-attack split the combine in two), and CI fails on a fourth. Every truncation is a visible step in the resolution expansion.

**What it is.** Part 2A states, twice, that rounding happens once per vector at R-400 and that *"everything after is exact"* and *"two fixed-point numbers are never multiplied together. That is the operation that would need rounding in the middle of the pipeline, and it does not occur."*

It occurs at **R-900**.

**The chain.** R-700 resolves `direction × magnitude`. Direction is fixed-point (the table in Part 2A says so), magnitude is an integer, and the design's own examples produce non-integers: `0.5714 × 12 = 6.9`. R-800 sums those — still fixed-point. R-900 applies **proportional Guards**, which the table lists as *"a percentage"*, to that fixed-point total: `6.9 × 50% = 3.45`. That is fixed × fixed, and it needs a rounding step, in the middle of the pipeline, exactly as the document says never happens.

**It gets slightly worse.** R-1200 Landing is claimed to need no rounding *"because persistent state is stored in fixed-point"* — true, but the reasoning is offered as evidence that there is only one rounding point, and there are at least two.

**How bad.** High as a specification defect, moderate as an arithmetic defect. The fix is trivial (declare a rounding mode at R-900, truncate toward zero, same as R-400). The reason it matters is that the *claim* is being used as an argument that the pipeline is exact, and a determinism argument built on a false premise is the kind of thing that survives until the first cross-machine diff.

**When it becomes expensive.** Now. Adding or moving a rounding site changes every fold.

**Options.** Declare it. `R-900: SUM the proportional Guard percentages, clamp at 100%, apply once, truncate toward zero.` Then update Part 2A's two claims to *"rounding happens twice per target: once per vector at R-400, once at R-900."* Add a property test that the pipeline has exactly two rounding sites and CI-fail on a third.

---

## A8 · Turn position, not tactics, decides how much damage a creature takes

**What it is.** Two rules interact badly:

- *"Anything targeting a creature lands at the start of that creature's turn."*
- Flat Guards subtract **once per resolution**, floored at zero (R-1000).

Therefore all damage aimed at a creature accumulates until its turn start and is then resolved as **one combined Packet against one application of the flat Guard**. A creature late in the order absorbs a whole round of attacks in a single packet; a creature early in the order eats its Guard more often for the same incoming total.

**Worked.** Four allies each hit for 6. Target's flat Guard is 3.

- **Late in the order** — all four land at one turn start: `24 − 3 = 21`.
- **Early in the order** — the same four attacks straddle two of its turn starts, 12 and 12: `(12−3) + (12−3) = 18`.

A **17% defensive swing that is purely a function of where you sit in initiative**, with no player decision involved. It compounds with Guard size: at Guard 6 the numbers are 18 versus 12, a 50% swing.

**And the incentives are inverted.** Part 2B: *"Landing sooner costs more... Landing later is what you get for spending less, or the price of something powerful."* But landing later is *mechanically better for the attacker* — it merges your hit into the combined packet so the Guard is amortised across everyone's damage instead of eating yours alone. So the system **pays you to do the thing it charges you less for**. Coordinated late-landing alpha strikes are strictly dominant over spread pressure, and they are the cheap option.

**Worked, the attacker side.** Five hits of magnitude 4 against Guard 3: `5 × (4−3) = 5`. One combined hit of magnitude 20 against the same Guard: `20 − 3 = 17`. **The same total magnitude does 3.4× the damage when it arrives together.**

**Precedent.** This is the shot-counter problem in a new coat. Feng Shui's sequence produces exactly this class of "when does it land" optimisation, and even a sympathetic treatment concedes it *"requires more fiddly bookkeeping from everyone at the table, which can be a drag on pace"* ([The Alexandrian, *Feng Shui — Filling the Shot*](https://thealexandrian.net/wordpress/43096/roleplaying-games/feng-shui-filling-the-shot)). Exalted 2e's tick system is the canonical case of an initiative economy that became the whole game.

**How bad.** High. It makes turn order a bigger lever than any tactical decision, and it does so invisibly — a player will feel it long before anyone can name it.

**When it becomes expensive.** The default anchor is base Ruleset behaviour and therefore versionable in principle. In practice every spell, ability and monster will be written against it, so swapping is Edition-level.

**Options.**

1. **Make flat Guards per-vector rather than per-combined-total** — move them to the C/R vector region. This inverts the incentive (spreading becomes better) and breaks *"damage cancels before it reaches the target"*, which is a rule the design cares about a lot. Probably not.
2. **Make flat Guards a per-Moment budget rather than a per-resolution subtraction** — the Guard has a pool that refreshes per round, spent as damage arrives. Removes the ordering dependence, adds a pool, and is exactly the "depleting reactive standing vector" the design already names.
3. **Make flat Guards proportional-only** and put all flat reduction into R-900 percentages. Simplest; removes the whole class of problem; costs the "plate armour: integrity 3" idiom.
4. **Own it.** Declare that concentrating fire is supposed to be strong and that turn position is supposed to matter defensively, and ship base-Ruleset turn orders that randomise or rotate. This is the cheapest and it needs to be *said*, loudly, in the design docs, or it will be discovered as a bug.

---

## A9 · Comprehension load is past every documented tolerance

**What it is.** The design asks a player, per attempt, to:

1. choose a Dimension subset from ~8 Capacities,
2. apportion whole points across it against **hidden** bars,
3. understand that two different item behaviours (Bonus Points, Baseline) reshape the split in different directions,
4. reason about a signed magnitude where failure inverts the meaning of their allocation,
5. and, in combat, additionally choose a Moment to pin to, knowing the arithmetic rewards arriving with others.

The GM meanwhile authors bars on 8 axes per object, and the engine runs 25 ordered slots plus unbounded modifier tiers.

**What the evidence says about that.** Working memory holds roughly 3–5 (some say up to 7) chunks, and once players reach cognitive-load capacity they *"stop engaging with the game"* ([Cognitive Load Theory in Roleplaying Games](https://thebardicinquiry.com/2022/08/21/cognitive-load-theory-in-roleplaying-games/)). Analysis paralysis arises when *"decisions are too complex, choices are too numerous, or the consequences that may result from decisions are too difficult to evaluate"* ([League of Gamemakers](https://www.leagueofgamemakers.com/designing-games-to-prevent-analysis-paralysis-part-1/)) — the allocation decision hits all three at once, and the third especially, because the bars are hidden.

Comparable systems bear this out. Mythras's special-effect menu is small by comparison and the community's response was to build mind-map decision aids, with players saying *"immediately went looking for a print out for special effects, sorted in a useful way that make it easier to grasp"* ([Notes from Pavis](https://notesfrompavis.blog/2020/07/21/tactics-of-selecting-combat-special-effects-in-mythras-a-result-based-visualisation/)). Burning Wheel's scripted Fight! is the most-skipped subsystem in a game its fans love. The lesson is consistent: **subsystems that require simultaneous multi-axis commitment get dropped, even by groups that like the game.**

**Two mitigations already in the design, and they are good.** The layer-by-layer animation and the Lens tiers are genuinely the right answers — see B-ideas 10, 11 and 30. But note what they do: they reduce the load of *understanding a result*. They do not reduce the load of *making the decision*, which is where the paralysis is.

**How bad.** High, and it is the failure mode that shows up as "we tried it for two sessions" rather than as a bug report. `dictionary.md` L30 rightly names **confusion** as a note kind and observes it *"predicts churn best"* — that instinct is correct and should be given a budget.

**Options.**

1. **Ship a default allocation.** Every attempt has a suggested split derived from the character's Capacities and gear, one click to accept, one click to change. Most attempts should never be allocated by hand. This is by far the highest-leverage fix and it costs a Component.
2. **Cut `k`.** Four attempt Dimensions in v1. Add later; additive-only permits it.
3. **Reveal the bars by default.** The design already makes threshold visibility a GM setting; make *shown* the default, not the exception, and make hidden a deliberate spice. See A12 — the arguments for showing DCs are strong: it speeds play, increases perceived fairness, and stops players blaming the GM ([*Always Tell Me the Odds*](https://drolleries.substack.com/p/always-tell-me-the-odds)).
4. **Keep the Shaping forms unmistakable.** *(Partly answered: Demand was retired in the Phase 0 re-attack, which removed the pair that read identically in English. Two forms remain, and they now differ in what they touch — Bonus Points changes the total, a Baseline does not.)*

---

## A10 · Shaping's three forms do not commute, and no order is declared

**RESOLVED — Phase 0, then simplified in the re-attack.** **Demand is retired**, so Shaping has two forms and the order is **Bonus Points → Baseline**. They still do not commute — Bonus-first gives 6/3/1 on the standing lock, Baseline-first gives 10/3/1 — so the order is declared and permanent.

**What it is.** Bonus Points renormalise, Baselines take a max and let the sum exceed 1, Demands force a floor and squeeze everything else into what remains. No order among the three is specified. They do not commute.

**Worked.** Raw allocation 1 manipulation / 2 perception / 1 stealth = 25/50/25. Apply a Demand of 75% on manipulation and a Baseline of 60% on perception.

- **Demand first:** manipulation 0.75; the remaining 0.25 splits 2:1 → **0.75 / 0.167 / 0.083**. Then Baseline perception 60% → `max(0.167, 0.60)` → **0.75 / 0.60 / 0.083**, summing to 1.433.
- **Baseline first:** perception → `max(0.50, 0.60)` = 0.60 → **0.25 / 0.60 / 0.25**, summing to 1.10. Then Demand manipulation 75%, squeezing the rest into what remains → **0.75 / 0.177 / 0.074**, summing to 1.0.

Perception is either **0.60 or 0.177** — a 3.4× difference — purely on which item's Shaping was applied first. And the *second* case exposes a further undefined question: when a Demand squeezes "everything else", does it squeeze into `1 − demand` or into `(current sum) − demand`? Both readings are consistent with the text.

**How bad.** High as a determinism hazard the moment a character carries two shaping items — which is character one, session one. It is also the exact class of bug the design's own §8 warns about: *"Ordering is where additive-only silently becomes meaning changed."*

**When it becomes expensive.** Now. Shaping is snapshot-only and fixes the direction at C-600, so its order is part of vector creation and therefore Substrate.

**Options.** Declare slots inside the C-region: e.g. **C-520 Demands** (floors, applied highest-first, renormalise), **C-540 Bonus Points** (renormalise), **C-560 Baselines** (max, may exceed 1). Any fixed order works; none is obviously right; the point is that it must be *fixed and numbered* like everything else. Also declare the squeeze denominator explicitly.

---

## A11 · Threshold authoring burden

**What it is.** *"The GM knows what the bars are; you do not."* For the allocation game to be meaningful, an object must declare bars on more than one Dimension — and, per A1, must declare **downside bars on the Dimensions a player might neglect**, or all-in wins.

So "there's a crowbar by the door" is cheap, but "the door" now needs: a manipulation bar, a force bar, a perception bar for what's hidden in it, a stealth downside bar, and probably two more. Improvised, live, weekly, by one person, across an entire campaign.

**Compare.** D&D's improvised object costs one number (a DC) and most GMs get it right by feel. GURPS and Rolemaster ask for more and are famous for the prep cost. This design asks for `k` numbers per object, where `k` is however many attempt Dimensions exist, and it *requires* several of them to be non-trivial or the core mechanic degenerates.

**In async play this is worse, not better.** The asynchronous mode's entire premise is that scenes happen without the GM present in real time. That means bars must be authored **in advance**, for objects the GM has not yet imagined players interacting with. There is no "I'll wing it" path.

**How bad.** High. This is the most reliable killer of crunchy systems and it lands on the one person with 6–12 hours a week.

**Options.**

1. **Threshold presets, aggressively.** L24 already contemplates Guard presets. Do the same for Thresholds: named difficulty profiles (`ordinary door`, `good lock`, `warded vault`) that stamp a full bar-set from one choice. This should be a day-one Component, not a convenience.
2. **Derive bars from the Challenge Profile.** L10 already defines a per-axis rated profile. Make the Threshold set a *projection* of the Challenge Profile with an explicit formula, so authoring one shape authors all the bars.
3. **Default bars per Category.** L1/L3 gives every Category its Attributes; give every Category a default bar-set too, so an Entity created mid-sentence is immediately interactable.
4. **Let the GM author one bar and have the system fill the rest** from the magnitude reference (*"a competent attempt at an ordinary task produces about 5"*). Explicitly permitted by the design's own safeguard; not currently planned as a feature.

---

## A12 · Hidden Thresholds versus total transparency — the tension is self-destroying

**What it is.** Two of the design's stated pillars are in direct opposition.

- *"You allocate against bars you cannot see. Which is what makes information worth having."*
- *"Every layer of a Resolution Record is visible to everyone, by default."* And every Threshold checked is in the instrumentation, *"and by how much it was missed."*

If a player can see how much a bar was missed by, the bar is public after one attempt. If they cannot, the promise of total transparency has an asterisk on the most interesting number in the system.

**And the Ledger makes it worse, quickly.** The client runs the same Ruleset package for optimistic prediction (§10.5), the Fold is pure, and every Campaign is exportable. Therefore:

- An optimal-allocation solver is a weekend project for one motivated player. In asynchronous play — where the whole point is that you have days to decide — there is no time pressure preventing its use.
- A community threshold database is trivially assembled from exports. Every shipped Adventure's bars become public knowledge within days of release.

The tension the mechanic depends on has a shelf life measured in weeks after the first Adventure ships.

**Contrast with how commercial games handle this.** Nobody who displays probabilities displays true probabilities. XCOM's designers built a "bad streak breaker" that on Normal and Easy overrides the shown number entirely — *"if you miss three times in a row you're not going to miss your fourth shot. It can be a 1% chance to hit and you're not going to miss that shot"* ([PCGamesN](https://www.pcgamesn.com/secret-dice-rolls-xcom-enemy-within)). *Dispatch* auto-succeeded anything above 76% ([PC Gamer](https://www.pcgamer.com/games/strategy/just-like-xcom-superhero-comedy-dispatch-cheats-random-percentages-of-success-in-the-players-favor-anything-that-had-over-a-76-percent-success-chance-would-automatically-succeed/)). The reason is always the same: true randomness with visible odds reads as unfair. **A fully transparent, deterministic, auditable engine forfeits every one of those levers permanently.** That is a deliberate and defensible choice, but it should be a stated one — the design currently treats transparency as a pure win.

**How bad.** Medium-high. It does not break anything; it means one of the two pillars will quietly win and the design has not chosen which.

**Options.**

1. **Choose transparency and drop hidden bars.** Show every Threshold. The game becomes a knapsack you can see — which is a real, good game (it is most of *Into the Breach*'s appeal) and it repairs A1's learnability problem and A9's load problem simultaneously. Strong recommendation.
2. **Choose hidden bars and use Delivery.** Bars are withheld per-recipient; the Resolution Record's threshold section is elided for players. This works — Delivery is exactly the mechanism — but it costs "all the maths is visible", which is the one thing `the-game.md` says software does that paper cannot.
3. **Hybrid: reveal after the fact.** Bars are hidden at declaration and revealed in the post-resolution breakdown. The player learns, the tension survives inside a single decision, and the solver only helps on repeat encounters. **This is the answer** and it needs to be written down as policy, not left to the GM dial.

---

## A13 · Participation Capacity needs the tiebreak the design says it doesn't need

**What it is.** *"There is no 'who went first,' because nobody went first"* and *"conflicts need no tiebreak"* — followed immediately by *"where they genuinely cannot combine — both groups stealing the same unique object — Participation Capacity settles it."*

Participation Capacity is a **count**. Deciding which contributors occupy the slots when more than `n` want them *is* a tiebreak, and it needs a stable key or the same Ledger folds differently on two machines.

**And in async play it is worse than an ordering problem — it is a race.** A lock at Participation Capacity 2 is claimed by the first two players who declare. The player who plays Thursday finds the slots gone. That is precisely the fairness failure `orientation.md` §11.2 worries about (*"the guy with time is winning"*), arriving through a mechanism nobody flagged.

**How bad.** Medium-high. A determinism hazard *and* a fairness hazard, in the mode that is supposed to be the differentiator.

**Options.**

1. **A stable key**, in the same shape as the Listener ordering key: `(declaration seq, component_id, entity_id)`. Deterministic, and first-come — which is honest about being a race.
2. **Auction the slots.** Contributors submit a Budget bid with their declaration; the Decider is `Auto` and resolves at the object's Moment. Removes the race, gives absent players a way to participate, and needs only Proposal + Decider machinery that already exists. See idea B15.
3. **Highest-magnitude wins the slots.** Deterministic, and it makes Participation Capacity read as "only the best two efforts count", which is a better fiction than "only the fastest two typists".
4. **Combine anyway and clamp.** Excess contributors are recorded as overflow, and a Component decides what happens. Consistent with how Enhancement overflow is handled, and it means nobody's turn is wasted.

---

## A14 · The third pyromancer contributes exactly zero, visibly

**What it is.** Percentages sum and Enhancement Capacity clamps the sum. Take the design's own example: base 8, Flametongue `+50%` snapshot, *Amplify Flame* `+100%` ambient, and a "good flamethrower at 250%".

- Pyro-1's own `+50%` plus Pyro-2's `+100%` = `+150%`, total 250% — **exactly at the cap**.
- Pyro-3 casts *Amplify Flame*. Summed percentage is `+250%`, clamped to `+150%`. Overflow: 100 percentage points.
- Damage is **identical**. Pyro-3's entire turn produced nothing.

Now recall that the Resolution Record carries the overflow and that *every layer is visible to everyone by default*. **Pyro-3 will watch a line appear that says their contribution was discarded.** That is a worse experience than a miss.

**How bad.** Medium in isolation, high in aggregate, because the same shape recurs everywhere ceilings exist — and ceilings are the design's answer to stacking, so they will be everywhere.

**When it becomes expensive.** Cheap forever, as long as it is fixed by a Component. But it must be in the **base Ruleset**, not left to third parties, or the default experience is bad.

**Options.**

1. **A default overflow Component in the Ruleset.** A Listener reads `overflow` on the Resolution Record and places a new vector — the excess heat becomes a small area fire vector, the over-amplified gun gains a `overheating` State, the over-helped lock jams noisily. The Substrate already supports this exactly (*"backfire is a Component reading the overflow"*); it just is not scheduled. **Ship it in v1.**
2. **Preview the cap.** The client already runs the pipeline for prediction. Show Pyro-3, at declaration time, that the vector is at capacity. Costs nothing, prevents the wasted turn entirely, and is the single best argument for the optimistic-prediction client.
3. **Let overflow raise the cap at a cost** — spend a Resource to buy Capacity mid-flight. Explicitly forbidden today (*"a vector's Capacity is captured at creation... nothing that spends a Capacity can also raise it mid-flight"*), and the acyclicity argument for that is correct. Leave it.

---

## A15 · Unpolarised Guards make you unhealable

**What it is.** A Guard has polarity and value as separate things, and polarity is *optional* — an unpolarised Guard on a Dimension *"removes heat and cold alike."* If the `vital` Dimension carries harm on the positive side and healing on the negative side (which is the natural reading of `poison → vital +1`), then an unpolarised `vital` Guard **reduces healing by the same proportion it reduces poison.**

Armour that says "resist 30% of vital" makes a character 30% harder to heal. Every content author who writes a Guard without thinking about polarity has written a curse.

**And this is not obviously wrong** — "hard to kill, hard to mend" is a real fiction. The problem is that it is the **default**, silently, and the design gives no signal at authoring time.

**How bad.** Medium. Cheap to fix, guaranteed to bite, and exactly the kind of thing that produces a "the rules are broken" report from a table that is playing correctly.

**Options.**

1. **Make polarity mandatory on every Guard.** No default. CI-enforceable, costs one required field, removes the entire class of bug. Recommended.
2. **Make Landing (R-1200) the only place sign matters** and forbid negative resolved values from meeting Guards at all. Cleaner conceptually; needs a slot decision now.
3. **Ship a lint rule**: any unpolarised Guard on a Dimension whose negative side is used by a healing Channel emits an authoring warning. Weaker, and depends on knowing which Channels are healing.

---

## A16 · Log-integer addition by table is not associative

**RESOLVED — Phase 0, Aug 2026.** Log-integers are **never added** — compare and multiply only. Sums happen in ordinary integers within one Scale. No table ships.

**What it is.** Part 7: *"Addition of log-integers requires a lookup table, which ships as versioned declarative data."* Log-space addition — computing `log(a+b)` from `log a` and `log b` — via a quantised table is **lossy**, and lossy addition is not associative: `(a ⊕ b) ⊕ c ≠ a ⊕ (b ⊕ c)` in general.

Part 2A says *"Within R-300, R-800, R-900 and R-1000, order is irrelevant — addition is commutative."* That claim is true for fixed-point and **false for log-integers**. Anywhere log-integers are summed, order matters, and the determinism discipline's answer ("sort by a stable key") makes it deterministic without making it *correct* — two different stable keys give two different answers.

**How bad.** Medium, and bounded — log-integers are scoped to *"mass, structural magnitude, energy, scale gaps"*, which is a small surface today. It grows if Scale-crossing rules (A17) start doing arithmetic.

**Options.**

1. **Never add log-integers.** Only compare and multiply (which is exact integer addition of exponents). If something must be summed, convert to fixed-point within a Scale, sum, convert back. Simplest and probably correct.
2. **Keep the table, declare a canonical summation order** (descending magnitude, ties by entity ID, byte-wise), and state plainly that log-integer summation is order-defined rather than commutative. Then fix the claim in Part 2A.
3. **Drop log-integers for v1.** Scale as a small exponent already does the work the design wants; log-integers are a second numeric system with its own failure modes and no shipped user yet.

---

## A17 · Scale-crossing will be hit on day one and needs a bespoke rule every time

**RESOLVED — Phase 0, Aug 2026, and promoted out of Medium because it turned out to be Substrate.** A default cross-Scale rule ships: `× 10^(source − target)`, truncated, at **R-750**, as its own visible slot. And the real answer to *how does a person affect a large thing* is that **Scale belongs to the part, not only to the whole** — a Scale-4 airship has Scale-1 doors and rigging, and the Scale that applies is the Scale of the thing actually targeted.

**What it is.** *"Addition is only defined within one Scale... that requires an explicit cross-Scale rule declared by a Component. This is enforced, not merely discouraged."*

The first session will contain: a person picking a lock on a ship's door; a person setting fire to a building; a person hitting a warhorse. Each of those is a Scale-0 attempt against a Scale-1-to-3 Entity, and each needs a Component-declared cross-Scale rule before the engine will let the numbers meet.

**The trap.** Because the enforcement is hard, the cheap workaround is to declare everything Scale 0 — at which point the whole Scale apparatus is unused, and it is Substrate.

**How bad.** Medium, and it is a *content cost that grows without bound* — every new Component that can touch a differently-scaled Entity needs its own rule.

**Options.**

1. **Ship one default cross-Scale rule in the Ruleset** — the conventional one is `effective = value × 10^(scale_source − scale_target)`, truncated, with a floor of zero — and let Components override. Enforcement stays; the common case is free.
2. **Make Scale a property of the *interaction*, not only the Entity**: a door on a ship is Scale 0 even though the ship is Scale 3. This is almost certainly what content wants and it is not currently expressible.
3. **Defer Scale entirely to a Component.** It is currently Substrate; if the only v1 use is "ships exist", it may not earn its permanence.

---

## A18 · The lattice, the tiers, and the dependency rule

**What it is.** The resolution region is 30 slots (E×5, C×6, R×19). On top of that: modifier **tiers** with no maximum, resolved highest-down; timestamp tiebreak within a layer; and *"an explicit declared dependency between Verbs overriding timestamp."*

**The comparison the design itself invokes is the right one and it should be read pessimistically.** Magic: The Gathering's continuous-effect system is **7 layers** (one with four sublayers), timestamps, and a dependency rule that overrides timestamps ([Draftsim on MTG layers](https://draftsim.com/mtg-layers/); the rules text is [CR 613](https://ancestral.vision/spells-abilities-and-effects/interaction-of-continuous-effects.html)). It took thirty years and a professional rules team to reach that, and even sympathetic judges describe it as the thing that *"conjures all sorts of horror stories."*

This design proposes 30 slots plus unbounded tiers plus the dependency override, at v1, authored by one person, frozen forever. The **dependency-overrides-timestamp** rule in particular is the single most complex feature MTG has, and it is being imported before anything is playable.

**And the digital comparison is instructive.** A developer adapting Lancer to a digital tactics game hit the same wall building nested reaction resolution and observed that *"Magic: The Gathering's comparable ruleset spans nearly 200 pages"*; their solution was an explicit event-tree with declared pre-block, validate, execute, followup and reactive phases ([Lancer Tactics devlog](https://wick.itch.io/lancer-tactics/devlog/571282/event-system-aka-how-to-handle-nested-youve-activated-my-trap-card-triggers)). That is the same shape as the R-region, and it is the *whole* of their combat resolution complexity — not one region of a larger lattice.

**How bad.** Medium, but permanent. The likeliest concrete outcome is not a wrong answer, it is that **nobody but the author can reason about a resolution**, which makes third-party Components — a stated commercial pillar — impossible to author correctly.

**Options.**

1. **Cut the dependency-overrides-timestamp rule from v1.** Reserve the concept, do not ship the behaviour. If a real case demands it, it can be added as a Revision only if it changes no existing fold — which it will not, if nothing uses it.
2. **Cap modifier tiers after all.** The acyclicity argument is correct, but a small declared maximum (say 4) is CI-checkable, comprehensible, and reversible upward. "No maximum, only acyclicity" is elegant and unbounded-in-practice.
3. **Reserve more slots than you ship.** Already the plan; make sure the reserved set includes the ones A2 and A4 identify (a cancellation clamp, an absolute-modifier clamp).
4. **Build the resolution explainer before the resolution engine.** §11A puts the instrumentation inside Phase 3, beside the Substrate. Make the *first* Phase 3 deliverable the pipeline visualiser running against hand-written fixtures — it is the only way to know whether 30 slots is comprehensible.

---

## A19 · Depth ≤ 2 plus no cross-Component reads produces one monolithic harm Component

**What it is.** Components may not call each other or read each other's Facets; dependency depth is ≤ 2; there are 5 Sockets. A real game needs health, wounds, conditions, death, fatigue, morale, spells, gear, classes — all of which read each other's state constantly.

Under these constraints the only legal way to make "a wound reduces your capacity to exert force" work is for wounds and capacities to live in **the same Component**. Iterate that a dozen times and the "default harm Component" becomes the monolith the architecture exists to prevent.

**Precedent.** This is what happened to every VTT ecosystem: Foundry's ~350 game systems are each effectively monoliths, with modules patching them ([Foundry VTT](https://en.wikipedia.org/wiki/Foundry_VTT)). The pattern is not a failure of discipline; it is what happens when subsystems genuinely share state.

**How bad.** Medium, and detectable early — by Component #10 you will know.

**Options.**

1. **Accept a "core" Component that is large, and make the *interface* the thing that stays small.** Publish its Nouns; forbid depending on its internals. That is what the Socket Vocabulary/Behaviour split already does — extend the pattern to non-Socket Components.
2. **Add Nouns to the Substrate that everything shares** — a small set of universal Resources and States. This contradicts *"the Substrate ships no Resources"*, which is a stance worth re-examining: §4.0 says *"what the Substrate declines to track is also the design"*, and declining to track anything shared may be declining to make the game.
3. **Measure it.** Write the fifteen to twenty Components on paper first (`phase-map.md` Phase 4) and draw the dependency graph. If it is not depth ≤ 2, the rule is wrong, not the game.

---

## A20 · Event sourcing: the operational reality

**What it is.** A hand-rolled event store in Postgres, fold-on-read, no snapshots, no async projections, one person. The architecture's reasoning for this is unusually good — the deferral list is right, the Postgres sequence-ordering hazard is correctly identified and correctly sidestepped by per-Campaign `seq`, and the rejection of Kafka/EventStore/FoundationDB is well-argued. The risks below are the residual ones.

**What the field reports.**

- **Versioning erodes the audit-log promise.** *"The more versions you have of an event (we have one that is post-fixed with V5), the more of this knowledge dissipates into history"* ([Dennis Doomen, *The Ugly of Event Sourcing*](https://www.dennisdoomen.com/2017/11/the-ugly-of-event-sourcingreal-world.html)). Doomen also reports **an aggregate accumulating 100,000+ events** and degrading on hydration, and **SQL Server identity columns completing out of order under load** — the exact class of bug the design has already anticipated with `tx_id`.
- **Replay is less useful for debugging than it sounds.** *"99% of the time 'bad states' were bad events caused by your standard run-of-the-mill human error"* ([Chris Kiehl, *Event Sourcing is Hard*](https://chriskiehl.com/article/event-sourcing-is-hard)). The design's `ops repro` loop is the right mitigation and should be built early.
- **Long streams cost.** *"When event streams grow longer and reach several thousand events, the projection begins to take quite some time and resources"* ([planetgeek.ch](https://www.planetgeek.ch/2026/05/05/event-sourcing-you-better-prevent-long-event-streams/)). A single Campaign over two years of weekly play, with a Record per Verb per target plus Moment boundaries plus Listener firings, will pass "several thousand" within months. Fold-on-read will need snapshots sooner than "explicitly deferred until measured" implies — probably in year one, not year three.

**Determinism debugging is the expensive part, and it is worth an honest number.** The canonical account of hunting one desync in a shipped RTS describes *"a binary search of printf-ing the current memory hash as the state is walked"*, *"a half dozen machines loop the game as fast as they can waiting for it to break"*, and nearly a week lost to a single bug ([ForrestTheWoods, *Synchronous RTS Engines and a Tale of Desyncs*](https://www.forrestthewoods.com/blog/synchronous_rts_engines_and_a_tale_of_desyncs/)). At 6–12 hours a week, **one desync is a month.** The §9 harness (state hash at every Moment, two-machine diff) is not optional insurance; it is the thing that keeps a single bug from consuming a quarter.

**How bad.** Medium. The architecture has anticipated most of it. The residual risk is schedule, not correctness.

**Options.**

1. **Build the state hash at every Moment on day one**, before the pipeline is interesting. It is cheap then and irreplaceable later.
2. **Plan the snapshot, do not build it.** Reserve the Record type and the Fold seam now so adding snapshots later is not a migration.
3. **Cap Record volume per Moment.** A Verb per target per Moment, plus Listener-fired Records, plus per-layer nothing (good — layers are derived) is already lean. Watch the Listener-fired count; a chatty Component can 10× the Ledger.

---

## A21 · PWA-only versus the asynchronous mode's delivery channel

**What it is.** §15.1 commits to PWA only, and the asynchronous mode's whole loop is *"a short, personal report... it takes five minutes to read and five to decide."* That loop is a notification loop.

**Current iOS constraints.** Web push requires iOS 16.4+, requires the user to have manually added the app to the Home Screen (there is no `beforeinstallprompt`, so the install flow is a hand-written "tap Share → Add to Home Screen" tutorial), Background Sync and Periodic Background Sync are unsupported, and cached data is subject to a **seven-day eviction if the app is not opened** ([MagicBell's iOS PWA guide](https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide)). *(That source also claims PWAs are unavailable in the EU; that is out of date — Apple announced removal in Feb 2024 and [reversed it two weeks later](https://techcrunch.com/2024/03/01/apple-reverses-decision-about-blocking-web-apps-on-iphones-in-the-eu/). Do not plan around the EU claim.)*

The seven-day eviction is the one that matters: **a player who does not open the app for a week — exactly the player the async mode exists for — loses local state and gets a cold start.**

**How bad.** Medium. Nothing is unrecoverable (the server is authoritative, so a cold start is a re-fetch), but the install-to-notification funnel on iOS is the single worst conversion step in the whole product and it gates the differentiator.

**Options.**

1. **Design for zero local persistence.** Treat the client as a pure renderer with no durable cache. This is already almost true (the server folds), so make it exactly true and the eviction stops mattering.
2. **Email as a first-class Dispatch channel, not a fallback.** Email has none of these problems, works on every device, and matches the "five minutes to read" format better than a push notification does. It is also the cheapest thing on this list.
3. **Keep the wrapper door open** — §15.2 already says this, and it is right. Budget it as a real fortnight, not a nicety.

---

## A22 · The time budget does not close, and the comparables are worse than the plan assumes

**What it is.** `phase-map.md` deliberately carries no hour estimates — the sequence is the useful part. That is the right call for a plan, and it does not make the arithmetic go away. At six to twelve hours a week, Phases 0 through 3 are a multi-year stretch on any honest reckoning, and nothing below compares favourably.

**The comparables.**

- **Foundry VTT** — the success case, and the closest structural analogue (a platform with a module ecosystem, sold as a perpetual licence). Founded 2018 by one person, public launch **May 2020** — and by 2023 it was **9 developers plus a 12-person content team** ([Wikipedia](https://en.wikipedia.org/wiki/Foundry_VTT)). Two years to launch, full-time, then two dozen people to sustain it. Note also: Foundry shipped a *tool*, not a game system. This project proposes to ship a platform **and** an original ruleset **and** six settings.
- **One More Multiverse** — launched 2020, **five-person team**, shut down May 2024 with a 90-day grace period, saying that a year of work on a new direction *"is not enough to support the OMM platform"* and that *"ambition can only do so much against the realities of keeping the lights on"* ([TechRaptor](https://techraptor.net/tabletop/news/one-more-multiverse-vtt-platform-announces-closure)).
- **Sigil (Wizards of the Coast)** — Unreal Engine 5, corporate funding, the strongest brand in the industry. **90% of the team laid off three weeks after beta launch**; shutdown announced for October 2026, with all user-created content to be deleted ([GeekNative](https://www.geeknative.com/210648/its-official-wizards-of-the-coast-confirms-dds-sigil-vtt-is-shutting-down/)).

**The pattern.** Well-funded teams of five to fifty fail at *less* than this scope. The one success was full-time from the start, shipped a narrower product, and needed a team within three years.

**The named failure mode is also the documented one.** Derek Yu's *Death Loops* describes exactly this project's risk profile: the **Loop of Restarting** (skills improve, foundations get rewritten) and the **Loop of Polishing**, both feeding on sunk cost and avoidance of release judgement ([derekyu.com](https://www.derekyu.com/makegames/deathloops.html)). `phase-map.md` Phase 2 names the same failure — building the engine first is the most common way a project like this dies — and prescribes the right test: *a group asks to play again without being asked.* That test should have a date attached, not a sentiment.

**How bad.** This is the highest-severity item in the document. Every technical issue above is fixable; this one determines whether any of them matter.

**Options.**

1. **Move the paper playtest to the front, unconditionally.** `phase-map.md` Phase 2 — paper, before any code — answers A1, A9 and A11 — the three issues that decide whether the game is worth building. Doing it before another hour of architecture is the single highest-value action available.
2. **Cut to one Setting and say so in the docs.** Authoring exhaustion is the risk `orientation.md` §11.3 names. `phase-map.md` Phase 6 already reflects the cut — one Setting, one Adventure — and the six-setting ambition belongs after Release, not before it.
3. **Halve the Substrate before building it.** Scale (A17), log-integers (A16), modifier tiers, the dependency-overrides-timestamp rule (A18), and Delivery-beyond-simple could all be *reserved and unbuilt*. `architecture.md` §17's "must be right on day one" list conflates **shape** with **implementation**; `phase-map.md` Phase 3 already makes this distinction correctly and the checklist has not been updated to match.
4. **Write the number down as a decision, not a risk.** "This is a five-year project and I accept that" is a legitimate position. "This is a five-year project" sitting in a risks section is how projects drift.

---

## A23 · Async play: the need is evidenced, the product is not

**What it is.** `field-survey.md` §3 says the async gap is *"real, large, and unserved"*, and `orientation.md` §11.2 already flags the honest doubt: the evidence that scheduling kills campaigns is strong; the evidence that people want to play in twenty-minute slices is much weaker. That doubt deserves more weight than it currently gets, because the whole differentiator rests on it.

**What the precedent shows.** Play-by-post is a stable, small, high-attrition niche. The standard account of its mortality: *"the gap between player posts kept growing. The Game Master stopped asking where everyone was"*; sustainable posting is *"1 to 2 days"* between posts; adventures need to be episodic — *"5 to 10 challenges"* over 6–12 months — because a 28-page module *"might take 1 to 2 years to complete"* ([Gnome Stew](https://gnomestew.com/delaying-the-eventual-death-of-your-play-by-post-game/)). Note what that implies: **the async mode's content unit must be an order of magnitude smaller than a conventional adventure**, and nothing in the design or the plan reflects that.

**And the other failure mode is over-engagement.** Neptune's Pride is the canonical asynchronous multiplayer design and it is famous for *"depriving you of sleep"*, giving *"every conversation you have with fellow players an agenda"*, and being described by its own admirers as *"the most horrible game you will ever play"* ([bit-tech](https://bit-tech.net/reviews/gaming/pc/the-price-of-neptune-s-pride/1/)). `field-survey.md` §4 already identifies "a world that runs continuously without a deadline is a welfare hazard" — the Neptune's Pride case is the concrete evidence for it, and the mitigation (every Decider carries a Moment and a default) is aimed at *stalls*, not at *compulsion*. There is no design element that stops an engaged player checking hourly.

**The multi-group timeline problem is also older than this design.** West Marches campaigns hit it directly: groups put on hold mid-dungeon while time stands still, fixed events that can never occur because no session falls on that date, and single sessions that consume many in-world days and desynchronise everyone — with the honest conclusion that *"no perfect system exists"* and every solution trades one set of problems for another ([Sarainy on West Marches timekeeping](https://sarainy.com/advice/timekeeping-in-west-marches-campaigns/)). The design's answer — scenes are simultaneous until a shared Moment — is a *new* trade, not an escape, and its specific cost is A5.

**How bad.** High, business-side. If the honest market is "the campaign survives your gaps" rather than "you play asynchronously", the product is a much smaller and much cheaper thing: a scheduling-resilient live game with graceful absence, which is most of the Decider/Standing Order machinery and none of the simultaneous-scene machinery.

**Options.**

1. **Test it with the cheapest possible instrument.** Run a play-by-post campaign of an existing game with the target group, with a weekly Dispatch written by hand, for six weeks. Costs nothing, answers the question, and can start this month.
2. **Sequence the two modes.** Build graceful absence (Deciders, Standing Orders, defaults) first — it is cheap, it is uncontroversially valuable, and it does not require simultaneous scenes. Build simultaneous scenes only if the six-week test says people want them.
3. **Size the content unit for async now.** If a scene must complete in 6–12 months of asynchronous play, the Adventure format is 5–10 challenges, and that should be in L11/`phase-map.md` before any Adventure is written.

---

---

# Part A2 — The Phase 0 re-attack

*August 2026. Ten findings against the **fixed** design, every one demonstrated with worked numbers before it was written down. This is what the re-attack step is for: the Phase 0 fixes were good, and they moved the problems rather than removing all of them.*

**All ten are now closed.** Three were unambiguous errors and were fixed on the spot (A31, A32, A33). Of the seven that needed a decision: **two were fixed by changing the pipeline** (A26, A30), **three were accepted as intended behaviour once the numbers were worked properly** (A24, A25, A29), **one dissolved** (A28), and **one was overstated and downgraded** (A27).

---

## A24 · Threshold riders punch through universal flat Guards — **Medium · CLOSED, accepted**

**Overstated on first report, and re-worked.** The rider is not free: against armour 3 it costs 0 integrity at magnitude 6, 1 at 10, 2 at 20 and 5 at 50, and heavy armour blocks it outright — `[20 integrity, 1 vital]` against armour 15 lands `[6, 0]`. The behaviour is also right in fiction: armour that failed to stop the wound should not stop what was on the blade. **Accepted, with the promise written down explicitly: "armour 3" means *reduces any incoming packet by 3*, not *immune to 3 or less on any axis*.**

Proportional redistribution can almost never zero a small Dimension sitting beside a large one, so a low-bar trigger stapled to a big hit is unblockable.

```
target: universal flat Guard 5      bar: "poisoned at vital >= 1"

  vital 1 alone                 → vital 0        blocked
  vital 1 + integrity 10          → vital 1, integrity  5     (integrity alone: 5)
  vital 1 + integrity 1000        → vital 1, integrity 995    (integrity alone: 995)
```

The rider costs the attacker **nothing** — the integrity part lands exactly what it would have landed alone. Under the old per-Dimension rule both were stopped.

**Why it matters.** Generic toughness now protects totals and cannot protect any *trigger*. Every status effect and every low-bar consequence becomes unblockable by armour. And *"a Guard covering all Dimensions covers new ones too"* is now false in the way that matters: a Dimension added in year five is threshold-undefendable by every Guard that already exists.

**Options.** (a) Absorb smallest-Dimension-first rather than proportionally, so small components are eaten before large ones. (b) Split the reads — Thresholds evaluate against a per-Dimension-guarded value while Landing uses the redistributed one.

---

## A25 · Small things cannot hurt large things below a threshold — **CLOSED, intended**

**Not a defect — this is a damage threshold, and it is wanted.** Something a Scale smaller has to land a hard enough blow to injure a larger thing at all; a thousand ordinary axe swings genuinely should not fell an airship. Combined with **Scale on parts**, the answer to *how does a person bring down a warship* is that you cut its Scale-1 rigging rather than punching its Scale-4 hull.

R-750 truncates each vector individually, and R-800 combines afterwards.

```
Scale-2 target, Scale-1 attackers each at magnitude 9

     1 attacker    raw    9   →   0        combine-first would give   0
    10 attackers   raw   90   →   0        combine-first would give   9
  1000 attackers   raw 9000   →   0        combine-first would give 900
```

A thousand axe blows of 9 do nothing; one blow of 900 does 90. It is also a step function — magnitude 19 lands 1, magnitude 20 lands 2, so a `+1` is worth ten times as much at the boundary and nothing anywhere else. Against the design's own guidance that magnitudes run under 10 early, **the entire early game is a dead zone against anything one Scale up.** Scale-on-parts does not fix it: the hull is still a thing and still unbreakable.

**Options.** (a) Move Scale conversion after R-800 — combine within the source Scale, convert the combined total once. (b) Keep it per vector but accumulate the truncated remainder on the target as a Resource, so persistence substitutes for magnitude — *cutting away at it*.

---

## A26 · Guards applied once per Moment — **High · CLOSED, fixed**

**Both halves fixed, and the pipeline changed to do it.** A **flat Guard now acts once per contributing source** at R-850 — five bandits at 10 land 35 rather than 47, eight land 56 rather than 77. **Cancellation moved to R-1000**, between flat and proportional Guards, so the fire elemental is unchanged: a cold bolt of 8 still meets its own aura of 5 and combines to 3 before the temperature-positive Guard is consulted. And **restoration was moved to R-1250** — still an ordinary vector with a negative magnitude, just resolving after harm has landed. Because R-850 and R-1050 are behind it by then, no Guard can reach it and it cannot cancel incoming harm; both fall out of the layer choice rather than being written as exceptions. A simultaneous heal and a delayed heal now come out identical, which kills the free timing exploit.

Guards act once per target per Moment, and the default anchor already synchronises everyone on the target's turn.

```
universal flat Guard 3
  1 attacker  × 10, one Moment   →  7 lands    armour absorbed 30%
  5 attackers × 10, one Moment   → 47 lands    armour absorbed  6%
  8 attackers × 10, one Moment   → 77 lands    armour absorbed  4%
```

**Armour becomes irrelevant exactly as the fight gets harder.** And the mirror of it is a free exploit for healers:

```
poison −6 vital, ally heal +6 vital, target has universal flat Guard 3
  both at the same Moment          net 0     the target gains nothing
  heal pinned one Moment later     −3, +6    the target gains +3
```

Delaying the heal by one Moment is worth exactly the Guard value, costs nothing, and needs no `repin`. *Damage cancels before it reaches the target* means your own side's healing is the only thing that ever pays the armour.

**Options.** (a) Apply flat Guards per contributing source rather than per Moment. (b) Split the packet at R-800 by sign — combine harmful and beneficial vectors separately, Guard the harmful side only, then net.

---

## A27 · Are percentage modifiers dominated by flat ones? — **Low · CLOSED**

**Not demonstrated at realistic sizes.** The original example used a `+8` flat against a base of 8 — an absolute the size of the whole attempt, which nobody would author. At sane sizes percentages stay the bigger lever: base 8 at Capacity 250% gives 20 by percentage against 14 from three `+2` items. **Closed with one enforceable residue: an absolute modifier may not exceed a declared fraction of the Ruleset's magnitude reference, CI-checked**, so *absolutes stay small* is a fact rather than a convention.

The consequence of clamping percentages and not absolutes, worked:

```
lock: base 8, Enhancement Capacity 100%, Participation 1

  three "+100%" amplifiers                →  8     all clamped
  the same three authored as "+8 flat"    → 32     4.0×
  one character carrying 7 flat items     → 22     2.75×
```

Participation Capacity bounds sources of **vectors**. Absolutes arrive as **modifiers**, and gear supplies its modifiers automatically — nothing bounds items per person. Any percentage buff can be re-expressed as the flat buff of equal value at the intended magnitude, and one is capped while the other is not.

**A rational content author never writes a percentage buff again.** That is a whole category of content going dead, which is the re-attack's own test for a fix having gone too far.

**Options.** (a) Clamp the assembled magnitude at R-500/R-600 against Capacity rather than the percentage sum at R-350 — one wall covering both forms. (b) Give absolutes their own ceiling and make it a required authoring field.

---

## A28 · Was zero a safe place to be? — **CLOSED, dissolved**

**Dissolved by reading bars correctly.** The finding existed only because downside consequences were being read as *absolute values below zero* rather than as *distance from the bar*. Read the second way — the same reading as *how far under the target number did the roll land* — an unallocated axis comes in at 0, which is below every positive bar, so **neglect always costs something and zero is never safe.** What remains is that hedging is slightly worse on a bad roll, which is correct fiction: trying to be quiet and botching it is worse than not trying. **Plus one rule: an attempt with no points spent anywhere is not legal.**

An unallocated axis resolves at exactly **0 at every magnitude, including negative** — and zero is the safest possible value against every bar below zero.

```
lock: opens at manip ≥ 5 · guard hears at stealth ≤ 1 · guard ALERTED at stealth ≤ −1

  M = 12   all-in 4/0   manip 12  stealth  0    opens, heard
           hedge  3/1   manip  9  stealth  3    opens, quiet      hedging works
  M = −4   all-in 4/0   manip −4  stealth  0    fails, heard
           hedge  3/1   manip −3  stealth −1    fails, heard, CLATTER
```

**On a failure, hedging is worse than going all-in.** So all-in is simultaneously the maximum-upside and the minimum-downside play, and the player commits before the sign of the magnitude is known. The mitigation adopted in Phase 0 only bites when things go well.

**Also:** spending no points at all leaves `total points = 0`, which is a division by zero the spec does not address. Now raises explicitly in the checks; still needs a rule.

**Options.** (a) Make downside bars magnitude-relative — `stealth ≤ M/4` — so an unallocated axis is not automatically safe. (b) On a negative magnitude, an unallocated axis takes the *full* negative rather than zero, so ignoring an axis is exposure rather than protection.

---

## A29 · How does the Capacity clamp apply to Baselines? — **CLOSED**

**There is nothing to distribute.** Everything that enhances sums into one number, and the ceiling clamps that one number: 200% Capacity with a Baseline plus helpers summing to 250% simply stops at 200%. The parts were summed before the clamp, so no component needs shrinking. **One sub-rule: a Baseline contributes the increase it caused, not its face value** — baselining manipulation to 75% when you allocated 25% contributes 50, because counting 75 charges you twice for what you paid for yourself.

A clamp on a sum does not say which components shrink.

```
raw 0.25 / 0.50 / 0.25, Baseline manipulation 75% → sum 1.5, task Capacity 120%

  shrink the Baseline back    0.45 / 0.50 / 0.25   → M=12:  5.4 / 6.0 / 3.0
  scale everything by 0.8     0.60 / 0.40 / 0.20   → M=12:  7.2 / 4.8 / 2.4

  against bars manipulation ≥ 5 and perception ≥ 5:
    first reading  → both clear.      second → perception 4.8, FAILS.
```

Two natural readings, opposite outcomes. **Lean: shrink the Baseline alone** — *a Baseline may raise the summed shares to at most Enhancement Capacity; your own points are never reduced.* That also preserves the Baseline's stated property of taking nothing from anywhere else.

---

## A30 · Shaping was still specified in decimals — **CLOSED**

**Shaping is expressed in points, never percentages — and Demand is retired outright.** A percentage of 3 points is not always a whole number, and every way of resolving that is an apportionment rule, which is the exact thing integer allocation removed. Bonus Points already worked in points and Baseline now does too (*counts as at least N points*). **Demand was the only form that could not be stated in points, and nothing in the design ever asked for it** — forcing a player to spend their own points somewhere is a strange thing to want. A cost belongs in the Budget, or as a Guard or a State.

Allocation is now integers, but Demand and Baseline are still specified in decimal shares. Two reasonable integer readings of *"Demand manipulation 75%"* on a raw 1/2/1 disagree at every magnitude:

```
  re-denominate exactly, P=12 → points [9,2,1]     M=12 → 9,2,1    M=5 → 3,0,0
  keep the player's P=4       → points [3,1,0]     M=12 → 9,3,0    M=5 → 3,1,0
```

Against a corridor bar of `stealth ≤ 1` they tell different stories. **Choosing the denominator is itself an apportionment decision** — the thing Phase 0 believed it had removed.

**Fix.** Define Shaping as an operation on `(points, total)` pairs only: Bonus Points adds to both; Demand rescales to a declared denominator with a declared apportionment rule; Baseline adds to points without touching the total. Then re-derive A10's table from integers.

---

## A31 · Floor is not truncate-toward-zero, and failure is a negative magnitude — **Critical · CLOSED**

The checks used Python `//` at all three rounding sites. On negative magnitudes floor and truncate diverge, always away from zero, which **manufactures magnitude**.

```
magnitude −7 across two axes    floor  [−4, −4] = −8      truncate [−3, −3] = −6
R-750, magnitude −8, S1 → S2    floor  −1              truncate  0
```

The R-750 case was a genuine degeneracy: at a Scale gap, deliberately *failing* reached further than succeeding.

**Closed.** One `trunc_div` helper at all three sites, plus a property test asserting `|sum of resolved values| ≤ |magnitude|` on both sides of zero, across every point count and axis count.

---

## A32 · R-1000 holds two non-commuting operations — **Critical · PARTLY CLOSED**

Named and universal flat Guards do not commute, and Part 2A said order within R-1000 was irrelevant.

```
[temperature 2, integrity 8], named integrity 6, universal 6
  named first      → [0, 0]    total 0
  universal first  → [1, 0]    total 1

exhaustive over 2 Dimensions, values 0–10, both Guards 0–10:
  4,633 of 14,520 combinations give a different total — 32%
```

**Closed by declaring the order: named acts before universal.** Specific resistance meeting the thing it names first is the only reading in which naming a Dimension means anything.

**Also closed:** a **negative universal flat Guard is now illegal.** It would add magnitude to a packet — `[10]` with a universal −3 becoming `[13]` breaks *reduces toward zero and never past it* — and against a fully cancelled packet it has nothing to redistribute across, so magnitude vanished silently. Vulnerability is a proportional Guard, or a Dimension-named flat one.

**Still open:** whether the two should be separate slots (R-1000 named, R-1050 universal) rather than one slot with an internal order.

---

## A33 · C-500 still captured Capacity from the source — **Medium · CLOSED**

Part 2A said the Capacity belongs to the task, and four lines later said it is captured from the source at creation, with `C-500 capture the source's Enhancement Capacity` still in the slot list. As written, the shoppable ceiling the decision existed to prevent was still there — a 400% source against a 100% task gave 20 instead of 8, a 2.5× difference.

**Closed.** C-500 is retired. The Capacity is read from the **target**, at R-100, in the gather — which also preserves acyclicity, because it is read once before any modifier at R-200 or later.

---

# Part B — Ideas

Things the design makes possible that nobody has written down. The rule I have applied: **a good idea here needs no new mechanism.** Where an idea does need one, I say so.

---

## B1 · Crafting produces Capacity, not bonuses

**What it is.** The obvious progression axis in this system is not "+2 sword". It is **Enhancement Capacity**. A masterwork blade is one that can *hold more amplification*. A ritual circle is a thing with high Participation Capacity. A well-made lockpick raises the Baseline it can support.

Make that the entire crafting system: **a crafting attempt's magnitude becomes the crafted object's Capacity.** A great smith does not make a sharper sword; they make a sword that a battle-mage can pour more into. The whole party's contribution to an item is legible, and the item's value is a number that means something in the fiction ("this gun holds 300%").

**Machinery.** Attempt → magnitude → Threshold places a vector → `alter magnitude` on a Capacity. Participation Capacity for co-crafting. Zero new mechanism.

**Cost.** One Component. It also solves the "progression cannot inflate numbers" problem the design has been circling: **progression raises ceilings, and ceilings are already the design's answer to stacking.**

---

## B2 · A class whose entire kit is `repin`

**What it is.** Because pending vectors are Entities and `repin` exists, a character can specialise in *when things land*. And because flat Guards are applied once per resolution (A8), **merging incoming blows onto one Moment makes them hurt more** and **splitting them across Moments makes them hurt less**.

So: a "tempo" character who *scatters* incoming blows across several of an ally's turn starts to maximise Guard applications, and *gathers* the party's outgoing blows onto one enemy Moment to minimise the enemy's. Same Verb, opposite directions, both tactically deep. A defensive `repin` and an offensive `repin` are the same ability used two ways.

**Machinery.** `repin`, a cost in doubloons, flat Guards at R-850. Nothing new.

**Cost.** One Component, and a strong argument for keeping flat Guards per-resolution even given A8 — because A8's defect is this idea's mechanic. Choose deliberately.

---

## B3 · Information as a tradeable Entity

**What it is.** The design's biggest untapped asset is that Thresholds are hidden and objects are Entities. Therefore *knowledge of an object's bars* is a thing with identity — make it one.

An `information` Category Entity: *"the schematics of the Ridley vault."* It carries the bar values as Facets. Holding it means a Lens shows you the bars. And then everything ordinary becomes interesting:

- It can be **bought, stolen, copied, and destroyed** — ordinary Verbs.
- It can be **forged**: an Entity whose bar values are *wrong*. The Lens shows them confidently. The player allocates against a lie. This is the best possible version of "you allocate against bars you cannot see", and it requires no new machinery at all.
- It can be **sold to a rival** — a Relationship forms, a Connection's magnitudes change.
- Its value **decays** when the lock is changed — a Listener on the lock's Threshold facets.

**Machinery.** Entity + Category + Facet + Delivery + Lens. Zero new mechanism.

**Cost.** One Component and one Lens surface. This is the idea I would build first, because it converts A12's weakness into the design's strongest feature.

---

## B4 · Rumour as a vector in a Knowledge Dimension Space

**What it is.** L21 already contemplates a Knowledge Space. Put rumours in it. A rumour is a vector: **direction** is what it asserts (a position in the knowledge space), **magnitude** is how strongly it is believed. Then, for free:

- A **counter-rumour** is a vector pointing the other way. They cancel by addition, at R-800, before anything. Propaganda is arithmetic.
- **Suppression** is a Guard on a faction.
- **Credulity** is a negative Guard — a vulnerability.
- A rumour's **window** is how long it persists; a **scope** is who hears it; **Participation Capacity** on a town square is how many stories it can carry at once.
- Rumours **land** into a persistent Channel — reputation — via the Landing Socket.

`field-survey.md` §4 warns that "simulation without curation produces noise, not life", and `architecture.md` §17 flags the Chronicle's inputs as foundation. **This is what makes the Chronicle a simulation output rather than an editorial chore.**

**Machinery.** One Dimension Space, a handful of Channels, one Landing rule. No new mechanism.

**Cost.** Medium — L21/L22 work plus a Component. High payoff, because it is the thing that makes the async mode have content between sessions.

---

## B5 · The what-if tool, shipped to players

**What it is.** §11A specifies a what-if that re-resolves any past resolution with a changed input and never writes. That is currently framed as a *tester* tool. **Ship it to players.**

*"Show me what would have happened if I'd put three on the lock."* One click, after the fact, on any resolution.

**Why it matters more than it looks.** A1 establishes that the allocation game is a knapsack with hidden weights and therefore has **no learning gradient**. The what-if tool *is* the gradient. It converts every failure into a lesson without revealing the bars in advance. It is the single highest-value mitigation for the design's biggest mechanical risk, and it is already being built for other reasons.

**Machinery.** Resolution Record (inputs + hash), pure Fold, the client already runs the Ruleset package. Nothing new.

**Cost.** Near zero incremental. Do it.

---

## B6 · The near-miss report

**What it is.** After a resolution, reveal only the bars you **missed by less than some margin** — *"you were 1 short of spotting something"* — and nothing else.

This is the hybrid answer to A12. Bars stay hidden at declaration, so the tension survives. The player learns *that there was something there*, so scouting and memory have value. And a solver cannot pre-compute an Adventure, because the information only exists after an attempt.

**Machinery.** Resolution Record + Delivery + Lens. Nothing new.

**Cost.** Trivial. This should be default behaviour, not an option.

---

## B7 · Overflow as content, shipped in the base Ruleset

**What it is.** A15/A14's fix, stated as a feature. A Listener reads `overflow` from the Resolution Record and places a new vector:

- an over-amplified gun emits an area temperature vector and gains an `overheating` State;
- an over-helped lock **jams**, and the noise vector goes out to the corridor;
- an over-enhanced ritual produces a wild vector on an adjacent Channel — chosen by position in the Dimension Space, so it is *derived*, not authored.

That last one is the good bit: **"what goes wrong" can be computed from where the Channel sits**, using the Alignment function the design already defines but says nothing currently consumes. Alignment gets a job.

**Machinery.** Listener + Resolution Record + Alignment. Nothing new.

**Cost.** One Component. Turns the worst feel-bad moment in the system into its most memorable one.

---

## B8 · Auction the Participation slots

**What it is.** A13's fix as a mechanic. When more contributors want a task than its Participation Capacity allows, they submit a Budget bid with their declaration; a Decider of kind `Auto` resolves at the object's Moment.

This does three things at once: it removes the async land-grab, it gives absent players a way to be involved (a Standing Order can bid), and it makes Participation Capacity a *market* rather than a queue.

**Machinery.** Proposal + Decider `Auto` + the economy. Explicitly permitted — *"a table vote is `Auto`"* is the same shape.

**Cost.** One Component.

---

## B9 · Standing Orders as a real programming layer

**What it is.** A Standing Order is a player-parameterised Listener. Let players **compose** them: a small, ordered list of condition→response pairs with parameters, evaluated top-down. This is Final Fantasy XII's Gambits, Gladiabots, and the "tactics" screen of every good CRPG.

**Why it is more than an absence patch.** It is a *feature people talk about*. It is the answer to "what do I do between sessions" for the player who wants more, not less, engagement. And it is the only known good answer to `orientation.md` §11.2's fairness worry — a player who cannot attend can still *tune* and can still be clever.

**Machinery.** Listener templates published by Components, parameters filled by players. Exactly what the design already specifies; the only addition is *ordering and composition*, which needs a stable evaluation key that is being designed anyway (§18 item 2a).

**Cost.** Interface work, moderate. Almost nothing in the engine.

---

## B10 · Terrain, weather and rooms as standing vectors

**What it is.** A rainstorm is a standing temperature-negative vector with an area scope and a `while it rains` window. A forge is temperature-positive. A cold cellar preserves things. A shrine is a positive vector in the social/knowledge Space.

Then: fighting in the rain **cancels part of every fire attack**, with no weather rules, no environmental modifiers table, and no lookup. And the fire mage's counterplay is obvious and fictional — get indoors.

**Machinery.** Standing vectors, scope, the Place Socket. Nothing new.

**Cost.** Zero engine. It is a content pattern, and it should be in the first Setting because it is the cheapest demonstration of why the vector model earns its keep.

---

## B11 · Procedural creatures by position

**What it is.** A creature's tactical identity in this system is: a point (its aura direction), a set of Guard polarities, an Enhancement Capacity, a Participation Capacity, and a Threshold profile. All numbers. Therefore **you can generate creatures by sampling the Dimension Space** and get genuinely distinct tactical puzzles with no bespoke rules.

Better: the generator can guarantee *coverage* — that the bestiary contains creatures that punish each dominant strategy — because the strategies are positions too.

**Machinery.** L22/L23 + Guards + Capacities. Nothing new.

**Cost.** Small tool. Enormous leverage on A22's authoring-exhaustion risk, because it converts monster-writing from prose into placement.

---

## B12 · The balance dashboard — telemetry nobody in tabletop has

**What it is.** Every Threshold check records the margin. Every resolution records every input. Every Campaign is a Ledger. Therefore you can compute, across every table playing:

- the empirical distribution of magnitude, per Ruleset, against the declared **magnitude reference**;
- the fraction of Thresholds missed by ≤ 1 (the "near-miss rate", which is the real measure of whether bars are set well);
- which Channels are never used, which Capacities are never allocated to, which Components' Listeners never fire;
- **which allocations players actually choose** — the direct empirical test of A1's all-in prediction.

No tabletop designer has ever had this. It is the strongest argument for the whole architecture, and it is a *product* in itself.

**Machinery.** The Ledger, the Resolution Record, `ops repro`. Already specified as instrumentation; not currently framed as an ongoing design instrument.

**Cost.** Small, incremental on §11A. It should be in the pitch.

---

## B13 · Prophecy as a fork

**What it is.** §11A specifies forking a Campaign at any Moment. Expose it in the fiction: a divination Component that **forks the fold forward one Moment** under an assumption and shows the diviner a Lens over the result — accurate, partial, and *non-binding*, because the fork is never written.

This is the single most paper-impossible thing in the whole design and it is currently filed under debugging.

**Machinery.** Fork + Lens + Delivery. The Fold is pure, so a speculative fold is free.

**Cost.** Small once forking exists, which it must anyway. High marketing value.

---

## B14 · Preparation as a third modifier capture time

**What it is.** Blades in the Dark's flashback is the best-loved mechanic of the last decade — it lets a player declare, retroactively, that they prepared for the situation they are now in ([Blades planning & engagement](https://bladesinthedark.com/planning-engagement)). The equivalent here is a modifier whose capture time is neither snapshot (at creation) nor ambient (at resolution) but **retroactive** — *"I bought the guard's cousin a drink last week."*

The Ledger cannot be rewritten, and it should not be. But this does not require rewriting: it is a **new Record at the current Moment, carrying a snapshot modifier whose justification is a past state**, paid for with a Resource. Mechanically it is an ordinary ambient modifier with a cost. Fictionally it is a flashback.

**Machinery.** A modifier + a Resource cost + a Record type. **Flag:** the design says modifiers are captured at one of *two* times and that this is a field on the modifier. Adding a third value to that field is additive and legal; adding a third *semantics* is a Substrate question. Worth deciding deliberately rather than discovering.

**Cost.** Small. Very high player-facing value.

---

## B15 · Wagers, insurance and debts

**What it is.** A Proposal is a pending Entity with a Decider and a Moment; a Listener can watch a Resolution Record. Therefore a player can stake a Resource on another player's attempt, and a faction can *insure* a caravan.

**Why it matters for the async mode.** It gives a player who is not in this week's scene something real to do in five minutes: read the Dispatch, stake something on the outcome, leave a Standing Order. That is the async loop working for a spectator, which is most of the table most of the time.

**Machinery.** Proposal, Decider, Listener, `transfer`. Nothing new.

**Cost.** One Component.

---

## B16 · The Dispatch as the free artifact

**What it is.** `architecture.md` §18 open question 6 — *"what is the free artifact a stranger encounters?"* — is unanswered, and the field survey says distribution is the binding constraint.

**The answer is already built.** The Dispatch is a bounded, personal, weekly, readable-in-one-sitting report that ends in a decision. Run one public demonstration world. Publish its **Chronicle** weekly, in public, as prose. Anyone can read it; anyone can see the Resolution Records behind any event in it; anyone can open a resolution and watch the pipeline.

That is simultaneously: a marketing asset, a design-writing habit `phase-map.md`'s Audience track and `work-tracks.md` B2 already recommend, an integration test, and a demonstration of the one thing the software does that paper cannot. It costs the world-building that is happening anyway.

**Machinery.** Chronicle, Dispatch, Delivery, the resolution explainer. All specified.

**Cost.** The prose. Which is the scarce resource — but it is prose that was going to be written for a Setting regardless.

---

## B17 · Mechanics from other games that slot in with no new machinery

Each of these is a design that already exists, is well-tested, and lands directly on existing primitives. Listed because they are *free content* — proof that the Substrate is expressive, and a shortcut past a lot of original design.

| Mechanic | Where it's from | What it lands on |
|---|---|---|
| **Clocks / fronts / countdowns** | Blades in the Dark, Apocalypse World | `advance clock` Verb + Threshold. Already in the Verb list, unused. |
| **Progress tracks** | Ironsworn | A Resource with Thresholds. Exact fit. |
| **Momentum / burn** | Ironsworn | A Resource spent to raise **Enhancement Capacity** at creation. This is the mechanic the Capacity system was made for and nobody has named it. |
| **Stress → trauma** | Blades | Resource crosses a Threshold → Listener → `set state`. Canonical example already in the docs. |
| **Devil's bargains** | Blades | A Proposal with a Decider and a default. |
| **Helping-dice limits** | Torchbearer, Mouse Guard | **Participation Capacity**, exactly. |
| **Advantage / Threat side-effects** | Genesys, FFG Star Wars | Thresholds on secondary Dimensions of the same attempt. This is a genuine validation — a shipped, popular game does the *"consequences at other Thresholds"* idea and it works ([Genesys narrative dice](https://philgamer.wordpress.com/2018/07/25/lets-study-genesys-part-1-narrative-dice-basic-rules/)). |
| **Special-effect menus** | Mythras | Thresholds declared by the weapon rather than by the system. Note the cautionary half — see A9. |
| **Structure / stress damage tables** | Lancer | Listener on a Resource threshold placing a triggered vector. |
| **Raise / See** | Dogs in the Vineyard | Two opposed vectors at a shared Moment. Falls out of combination. |
| **Card-driven initiative** | Gloomhaven | A base-Ruleset turn order produced from committed choices. Since only *how order is produced* is Ruleset, this is a drop-in alternative. |
| **Simultaneous written orders** | Diplomacy, play-by-mail | Another base-Ruleset turn order, and probably the *right* one for the asynchronous mode — it is the only initiative system in existence designed for players who are not in the same room or the same day. |
| **Oracles / "ask the oracle"** | Ironsworn | A Decider of kind `Auto` reading the counter-based PRNG. This is the GM-less tier, already required by §4.3A as the automated escape valve. |
| **Seasons + a shared Covenant** | Ars Magica | The cadence Moment plus a shared Entity that rewards feed. Forty years of evidence that "the reward feeds the shared thing" sustains a campaign — directly relevant to `orientation.md` §11.2's doubt about non-capability rewards. |
| **Beliefs / Instincts** | Burning Wheel | An Instinct is *literally a Standing Order*: a player-authored condition→response. The mechanic already exists in print and is beloved; this design can execute it. |

---

## B18 · Progressive disclosure of the pipeline as onboarding

**What it is.** Because every layer of a resolution is derivable, the client can show **any prefix of it**. So the Lens tiers (L20) should not be "simple/medium/complex" flavours — they should be **how many slots of the pipeline you are shown**, and they should advance automatically as a player uses features that need them.

A new player sees: *base 8 → your fire → 20 → armour took 3 → 17.* Four lines. A player who has cast their first amplifier sees the percentage-sum line appear, once, with a one-sentence explanation. Nobody is ever shown a layer they have never interacted with.

**Machinery.** Resolution Record layers are derived; Lenses are outside the Fold and can be rewritten freely. Nothing new.

**Cost.** Interface work, and it is the direct mitigation for A9. L20 currently says Lens tier names *"must not imply a skill ladder"* — that constraint should be revisited, because "how much of the machine do you want to see" is not a skill ladder and pretending it is may be costing the clearest possible design.

---

## B19 · Opposed everything, for free

**What it is.** Worth writing down explicitly because it is a large amount of rules text the design does not have to write: an opposed roll, a chase, a tug-of-war, a debate, an arm-wrestle, a siege and a bidding war are all **two vectors pointing opposite ways in one Space, combining at a shared Moment**. There is no opposed-roll subsystem, no contest rules, no chase rules.

The corollary worth exploiting: an object can declare Thresholds **on both signs** of a Dimension, which makes a rope in a tug-of-war a first-class Entity with a bar at each end. Contests become objects, and objects take turns, so contests get a turn.

**Machinery.** Existing. **Cost.** Zero. It belongs in `the-game.md`, because it is one of the clearest demonstrations of the central claim.

---

## B20 · Determinism as a player-facing promise

**What it is.** Every Campaign is exportable, the Fold is pure, and there is a state hash at every Moment. Therefore a player can be told, truthfully: **"you can download your entire campaign and re-run it yourself, and get exactly the same answers."**

No tabletop product can say that. It is the strongest possible version of "nobody has to trust that the person with the rulebook got it right", it costs nothing beyond what §9 already requires, and it is a genuine differentiator against every VTT — none of which have canonical state at all.

**Machinery.** Export, the Fold, the state hash. Already required.

**Cost.** Publish the Ruleset package and a one-command replay tool. A weekend, and it converts an internal engineering property into the marketing claim.

---

# Closing: what I would do next

Not a plan, a priority ordering, given everything above.

1. **The paper playtest, this month.** It answers A1, A9 and A11 — which between them decide whether the core mechanic is worth the Substrate. One evening. Nothing else on this list has that ratio.
2. **Fix the four arithmetic findings while they are free** — A2, A3, A4, A7: the missing cancellation clamp (A2), the flat-Guard dominance (A3), the absolute-modifier hole in Enhancement Capacity (A4), and the two rounding-site contradiction (A7). *(Not the same set as the four foundation findings that open Phase 0 — those are A1, A2, A3, A4, ordered by what they can move in the lattice. A2, A3 and A4 are in both.)* All four are slot decisions and all four are Edition breaks after launch.
3. **Declare the undeclared orders**: Shaping (A10), apportionment (A6), Participation ties (A13), log-integer summation (A16). Each is a paragraph today and a determinism bug later.
4. **Rule on the shared-Resource double-spend (A5)** before any async design proceeds.
5. **Decide the transparency question (A12)** and write it down as a stance, not a dial. My recommendation is B6 — hidden at declaration, near-misses revealed after.
6. **Run the six-week play-by-post test (A23)** with the target group, using an existing game. It costs nothing and it is the only way to learn whether the differentiator is a differentiator.
7. **Build B5, B6 and B12 as part of the instrumentation**, since they are the same code, and ship them to players rather than testers.
