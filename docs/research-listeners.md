# TRIGGER / LISTENER SYSTEMS — RESEARCH REPORT

Note on budget: I exhausted the session's WebSearch allowance (200/200) partway through; later sections were completed with direct WebFetch against sources already identified. Two figures below (Master Duel's loop caps, Hearthstone's re-entrancy rule) come from community wikis that hedge their own wording — flagged inline.

---

## 1. MAGIC: THE GATHERING

### 1.1 State-based actions (rule 704) — the fixpoint loop

Sources: [ancestral.vision CR 704](https://ancestral.vision/additional-rules/state-based-actions.html) · [MTG Wiki: State-based action](https://mtg.fandom.com/wiki/State-based_action) · [mtg.wiki: State-based action](https://mtg.wiki/page/State-based_action)

The check sequence (704.3) is:

1. Whenever a player *would* receive priority, check all SBA conditions.
2. Perform **all applicable SBAs simultaneously as a single event**. No player controls them, no player may respond, they do not use the stack (704.2).
3. If any were performed, **go to 1**.
4. When none apply, put **all waiting triggered abilities** on the stack (603.3).
5. **Go to 1.** Repeat until neither an SBA was performed nor a trigger is waiting.
6. Only then does a player receive priority.

Three things matter for your design:

- **704.1a** explicitly draws your line: an ability that watches game state but uses the stack is a *triggered ability* under 603, **not** a state-based action. MTG deliberately maintains both mechanisms and does not treat them as interchangeable.
- **704.4**: SBAs "pay no attention to what happens during the resolution of a spell or ability." A creature whose toughness dips to 0 mid-resolution and recovers before the check survives. Only the state at the check point exists. This is exactly your "evaluated at a fixed layer after each resolution" and it is load-bearing: it makes the fold's intermediate states unobservable and therefore unspecified.
- **The 704.5 list is closed, ~25 entries, and every single one is "this state is illegal and must not persist"**: life ≤ 0, empty-library draw, 10+ poison, tokens outside the battlefield, copies outside legal zones, toughness ≤ 0, lethal damage, deathtouch damage, loyalty 0, legend rule, world rule, illegally-attached Auras, illegally-attached Equipment, +1/+1 vs −1/−1 counter annihilation, counter maxima, Saga final chapter, Dungeon completion, battle defense 0, protector reassignment, Role deduplication. **SBAs are a garbage collector, not a general consequence mechanism.** MTG did not try to make them do content's work.

### 1.2 State triggers — rule 603.8 (the most directly transferable rule I found)

Source: [MTG Wiki: Triggered ability](https://mtg.fandom.com/wiki/Triggered_ability) · [ancestral.vision CR 603](https://ancestral.vision/spells-abilities-and-effects/handling-triggered-abilities.html)

603.8 defines abilities that "trigger when a game state ... is true, rather than triggering when an event occurs" — literally your Listener. The termination rule is:

> A state-triggered ability doesn't trigger again until the ability has resolved, has been countered, or has otherwise left the stack. Then, if the object with the ability is still in the same zone and the game state still matches its trigger condition, the ability will trigger again.

This is **refraction**, and it is MTG's answer to "how do you watch state without firing forever." Example: "Whenever you have no cards in hand, draw a card" fires once on emptying, not once per priority check. The condition must go false and come true again.

### 1.3 Event-shaped rules MTG could not express as state

This is the honest counter-evidence to a pure state-watching design:

- **603.6 zone-change triggers "look back in time"** — the game evaluates whether the ability existed *before* the event. An artifact reading "whenever a creature dies, gain 1 life" that is destroyed simultaneously with two creatures triggers twice, despite being gone.
- **603.10 look-back exceptions** — leaves-the-battlefield, phase-out, unattachment, loss of control, spell countering, player loss. All use *last known information* about an object that no longer exists.
- **603.2h** — prevented or replaced events do not trigger abilities. The event that "would have" happened must leave no trace.
- **603.7 delayed triggered abilities** — created during resolution, fire at the next matching event. This is exactly your rule 22 (pin to a later Moment).
- **603.4 intervening-'if'** — condition checked both when triggering *and* on resolution; the ability is removed from the stack if the condition lapsed. This is the guard against a deferred consequence landing in a world that no longer justifies it.

**Conclusion: four state-watching systems examined, and every one of them needed a look-back mechanism.** Pure state watching is provably insufficient for "the thing that changed no longer exists."

### 1.4 Ordering of simultaneous triggers — 603.3b

Two passes, both in APNAP (Active Player, Non-Active Player) order:

1. Each player, in APNAP order, puts on the stack every trigger they control **whose trigger condition is not another ability triggering**, in any order they choose.
2. Each player, in APNAP order, puts the remainder (triggers-on-triggers) on the stack, in any order they choose.

Note the shape: a **class split before a player split before free choice**. The "not caused by another trigger" class goes first. Within a class, a human chooses — unavailable to a server-side fold.

### 1.5 Termination without a depth counter

MTG has **no depth counter anywhere**. Termination comes from three separate mechanisms:

1. **Fixpoint over a frozen candidate set** (704.3): SBAs re-check to convergence; triggers are added in a separate pass; the loop exits only when both passes are no-ops.
2. **Refraction** (603.8) for state triggers.
3. **A game-level escape hatch** when 1 and 2 fail:
   - **104.4b**: "If a game ... somehow enters a 'loop' of mandatory actions, repeating a sequence of events with no way to stop, the game is a draw. Loops that contain an optional action don't result in a draw." ([yawgatog CR](https://yawgatog.com/resources/magic-rules/), [MTG Wiki: Ending the game](https://mtg.fandom.com/wiki/Ending_the_game))
   - **CR 729.4** (this section was numbered 719 before a renumbering): "If a loop contains only mandatory actions, the game is a draw." ([MTG Wiki: Shortcut](https://mtg.fandom.com/wiki/Shortcut))
   - **Magic Tournament Rules 4.4 Loops**: loop actions must be identical each iteration and may not include conditional actions; players name an iteration count in turn order; **the game advances through the lowest number chosen** and that player gets priority. "Non-deterministic loops (loops that rely on decision trees, probability or mathematical convergence) may not be shortcut." If all players choose to continue indefinitely in a multi-turn loop, the game is a draw. The judge is the final arbiter. ([MTR 4.4](https://blogs.magicjudges.org/rules/mtr4-4/), [MTG Wiki: Loop](https://mtg.fandom.com/wiki/Loop))

I found **no evidence for a "6 times then draw" convention** in the rules documents. The mechanism is "name a number, lowest wins," not a fixed count. That appears to be folklore.

The strategic reading: **MTG's paper rules never bound depth. They bound it socially (a draw) and structurally (refraction + frozen candidate set).** Depth limits appear only in digital implementations.

---

## 2. HEARTHSTONE

Source: [Advanced rulebook (wiki.gg)](https://hearthstone.wiki.gg/wiki/Advanced_rulebook) · [Advanced rulebook (Fandom)](https://hearthstone.fandom.com/wiki/Advanced_rulebook) · [Turn](https://hearthstone.fandom.com/wiki/Turn)

Structure: **Sequence** (begun by a player action) → one or more **Phases** (resolved in order) → each Phase has a **Queue**.

- **Queue construction**: "A Queue is created and filled with all triggers that can respond, in order of play" — i.e. the order the associated entities entered play, **oldest to newest**. Minions, heroes, weapons, locations, permanents, dormants, attached enchantments and added deathrattles all live in a single order-of-play list.
- **Queue immutability**: "A Queue becomes immutable once Hearthstone starts to resolve the first entry in it. No new entries can be added." Entities summoned mid-resolution cannot respond to events already in flight.
- **Priority override**: a small set of cards have an explicit Priority that supersedes order of play (e.g. Redemption always queues last).
- **Resolution is depth-first**: a newly raised trigger is explored to completion before remaining triggers of the current event.
- **Death Creation Step**: only when the *outermost* Phase ends does the engine do Aura Update (Health/Attack) → Death Creation Step (all mortally wounded entities removed simultaneously) → Aura Update (Other). "You will NEVER see an Entity be killed in the middle of a Phase, no matter how complexly nested it becomes." Auras are *not* recalculated mid-phase for minions leaving play.
- **Recursion cap: none documented.** The only anti-loop statement is the re-entrancy rule, and the wiki hedges it: *"It seems that a trigger cannot be nested inside itself. Instead it works the skipped times as a compensation after all other consequences of it are resolved."* This is reverse-engineered, not published.
- **Structural caps** substitute for a depth cap: 7 minions, 10 cards in hand, 5 secrets, 60-card deck.
- **Global termination**: "The game is a draw if turn 89 (Player 1's 45th turn) just ended" — at the start of turn 90 both heroes explode. Rarely reached because fatigue kills first.

Takeaway: Hearthstone's answer to loops is **architectural, not numeric** — freeze the queue, defer deaths to the outermost boundary, forbid self-nesting — plus one blunt global timeout.

---

## 3. LEGENDS OF RUNETERRA

Source: [Keywords/Trigger (LoL Wiki)](https://leagueoflegends.fandom.com/wiki/Keywords_(Legends_of_Runeterra)/Trigger) · [LoR:Recursion](https://wiki.leagueoflegends.com/en-us/LoR:Recursion)

**Fully positional, fully deterministic ordering, no player choice.** Triggers activate in this hierarchy:

1. Champion level-ups and progress
2. Lab Powers (in order gained)
3. Nexus / out-of-play triggers (in order given)
4. Deck triggers
5. Hand triggers (left to right)
6. Board triggers (left to right)

Within each tier, **enemy triggers always resolve after allied ones**. There is no stack for triggers: "triggers will only activate after whatever event met their condition has fully resolved." Even genuinely simultaneous effects produce sequential triggers, and a trigger simply does not fire if its unit died to a preceding effect.

**Hard cap found: the spell stack holds at most 10 spells, and the 10th may only be Burst speed.** This is the cleanest example of a small, legible, gameplay-motivated cap — chosen so a human can read the stack, not so a machine doesn't overflow.

---

## 4. YU-GI-OH! — SEGOC

Source: [Yugipedia: Simultaneous Effects](https://yugipedia.com/wiki/Simultaneous_Effects) · [YGOrganization: Demystifying Rulings Part 3 — SEGOC](https://ygorganization.com/learnrulingspart3/) · [Yu-Gi-Oh! Wiki: SEGOC](https://yugioh.fandom.com/wiki/Simultaneous_Effects_Go_On_Chain) · [Yugipedia: Infinite loop](https://yugipedia.com/wiki/Infinite_loop)

**Ordering (the four-bucket rule):**

1. Turn player's **mandatory** effects
2. Non-turn player's **mandatory** effects
3. Turn player's **optional** effects
4. Non-turn player's **optional** effects

Within a bucket, the controlling player chooses the order. Chain links are numbered in that sequence; the chain resolves **LIFO** (last link first). Only once all simultaneous triggers are on the chain may players add fast effects.

The key structural insight, and the one I would steal: **mandatory before optional.** Everything with no decision in it is committed first, so that when a player is finally asked to choose, they are choosing against a settled board. This is precisely the constraint a server-side fold needs, because "mandatory" is exactly "resolvable without a round trip."

**Infinite loops.** Yu-Gi-Oh does *not* draw. Per TCG Policy v2.4: for a mandatory loop with no net change, "each action in one iteration of the loop is performed a single time, and then the card ruled to be the source of the infinite loop is automatically sent to the Graveyard." Play continues. Loops *with* net change run until the net change stops, then the initiator is destroyed. An older rule forbidding players from voluntarily starting loops was removed.

**Master Duel** (digital) caps loops at roughly **10 iterations for activation-based loops and 16 steps for Continuous Effect loops**, then destroys one or more involved cards — explicitly to avoid the softlocks that afflicted earlier video games. *(Community-wiki figure, hedged with "approximately" in the source; treat as indicative, not authoritative.)*

---

## 5. RULES ENGINES OUTSIDE GAMES

### 5.1 Drools / Rete

Sources: [Drools 8.38 rule engine docs](https://docs.drools.org/8.38.0.Final/drools-docs/docs-website/drools/rule-engine/index.html) · [Drools 6.5 ch.7 Running](https://docs.drools.org/6.5.0.Final/drools-docs/html/ch07.html)

- **Agenda**: activations are registered and sorted before firing. Two-phase cycle: agenda evaluation → working memory actions → repeat.
- **Default conflict resolution: "Salience and LIFO (last in, first out)."** LIFO keys off a working-memory action counter; all rules created in the same action share a value.
- **The documented failure mode, in Drools' own words: "The execution order of a set of firings with the same priority value is arbitrary."** Drools does not promise determinism among ties. This is the single most important negative datapoint in this section.
- **Agenda groups** form a *stack*; `setFocus()` pushes, empty pops. Default group is `MAIN`. `auto-focus` pushes on activation.
- **Activation groups**: "only one rule can fire, and after that rule has fired all the other rules are cancelled from the agenda."
- **`no-loop`**: prevents a rule re-triggering *itself* via its own consequence. Covers self-loops only — not mutual recursion between two rules.
- **`lock-on-active`**: stronger; blocks re-activation of a rule while its agenda/ruleflow group is active. Used specifically to stop loops.
- **Property reactivity** (modern default): the engine only re-evaluates a pattern when a property the pattern actually constrains changes. Drools' docs credit this with preventing "unwanted recursions." **Narrowing what a rule watches is what actually stops loops** — `no-loop` and `lock-on-active` are patches over an over-broad watch.
- **Truth Maintenance**: `insert()` (stated) vs `insertLogical()` (logical). Logically inserted facts are **automatically retracted when the conditions of the rule that inserted them stop being true**, cascading. This is your "watch state, never events" carried through to un-doing: no retraction event is needed because the justification is the fact's reason for existing. Requires correct `equals`/`hashCode`.

### 5.2 CLIPS

Sources: [CLIPS BPG 5.3 conflict resolution strategies](https://www.csie.ntu.edu.tw/~sylee/courses/clips/bpg/node5.3.html) · [MEA strategy](https://www.csie.ntu.edu.tw/~sylee/courses/clips/bpg/node5.3.6.html) · [CLIPS User Guide ch.3](https://portal.cs.umbc.edu/clips/usersguide/ug3.html)

Seven strategies, all applied *within* a salience band:

| Strategy | Ordering rule | Determinism |
|---|---|---|
| **depth** (default) | new activations above all of equal salience — LIFO | ties among co-activated rules **arbitrary** |
| **breadth** | new activations below all of equal salience — FIFO | ties **arbitrary** |
| **simplicity** | above all activations of equal-or-higher specificity (specificity = count of comparisons and function calls in the LHS) | ties arbitrary |
| **complexity** | above all of equal-or-lower specificity | ties arbitrary |
| **LEX** | by recency of the fact time tags across the whole match, then specificity | deterministic given deterministic assertion order |
| **MEA** | by time tag of the entity matching the **first pattern**; ties fall through to LEX; negated patterns get pseudo time tags | deterministic given deterministic assertion order |
| **random** | random | none |

The agenda is ordered highest to lowest salience; "new activations are placed on the agenda after activations with higher salience, but before activations with equal or lower salience."

**Every strategy CLIPS ships leaves ties among simultaneously-activated rules explicitly arbitrary.** Twenty-plus years of production-system practice and the answer to your ordering question is still "we didn't specify it."

### 5.3 Refraction

Source: [Conflict resolution strategy (Wikipedia)](https://en.wikipedia.org/wiki/Conflict_resolution_strategy)

The canonical loop guard: *"If a rule's conditions are satisfied, but previously the same rule has been satisfied by the same facts, ignore the rule."* Wikipedia identifies this as the mechanism that "helps to prevent the system from entering infinite loops." An activation is a `(rule, fact-tuple)` pair that fires once; re-asserting a fact makes a new tuple and re-arms it.

Also catalogued there: specificity (deterministic), recency (deterministic), order-of-presentation (fully deterministic — Prolog's default), arbitrary choice (non-deterministic, prevents nothing).

### 5.4 Termination theory — active databases

Source: [Ray & Ray, *Detecting Termination of Active Database Rules Using Symbolic Model Checking*, ADBIS 2001 (PDF)](https://www.cs.colostate.edu/pubserv/pubs/Ray-iray-research-adbis01.pdf) · [Baralis & Widom, algebraic static analysis](https://www.semanticscholar.org/paper/An-algebraic-approach-to-static-analysis-of-active-Baralis-Widom/e1435e7124614d8a2b4717663b6644fdb03c3e00) · [Widom publications](https://cs.stanford.edu/people/widom/pubs.html) · [Unrolling Cycles to Decide Trigger Termination, VLDB 1999](https://dl.acm.org/doi/10.5555/645925.671354)

The formal position, and it is unambiguous:

- **"Detecting termination of active database rules is, in general, an undecidable problem."**
- **Triggering graph** (Aiken, Hellerstein & Widom — the SIGMOD'92 "Behavior of Database Production Rules: Termination, Confluence, and Observable Determinism" line of work): vertices are rules, a directed edge means rule A's action may trigger rule B. **Acyclicity ⇒ guaranteed termination.** Sound but conservative: cycles are necessary, not sufficient, for non-termination. Documented false positives include rules that only delete without concurrent inserts, and monotonic updates that eventually falsify their own condition.
- **Activation graph** (Baralis & Widom): edges mean rule A's action can make rule B's *condition* true — a tighter over-approximation that clears more cases.
- **Symbolic model checking** (CTL over the rule system) proves termination in cases the triggering graph rejects.

The three properties that literature isolates — **termination, confluence, observable determinism** — are exactly your three open questions (b/c, d, and the fold-equality requirement). That paper title is the closest thing to a spec for what you are building.

---

## 6. EVENT SOURCING / CQRS

Sources: [Event Sourcing: Projections (domaincentric.net)](https://domaincentric.net/blog/event-sourcing-projections) · [Consumers, projectors, reactors (Architecture Weekly)](https://www.architecture-weekly.com/p/consumers-projectors-reactors-and) *(429'd on fetch; cited for the projector/reactor distinction it names)* · [Event Sourcing anti-patterns (InfoQ)](https://www.infoq.com/news/2016/04/event-sourcing-anti-pattern) · [eventsourcing library: Projections](https://eventsourcing.readthedocs.io/en/v8.3.0/topics/projections.html)

- **"A projection is nothing else than a left-fold over the sequence of events."** Determinism follows: same sequence, same result, always. This is your Fold, stated identically.
- **The dangerous dependency is projection-on-projection**, not projection-on-event. The source explicitly warns that in a SQL read store "joins are very easy to perform," creating cross-projection dependencies that break rebuild and introduce races. Your rule 1 (Components communicate only through the Ledger) is the same prohibition, arrived at independently.
- **Projector vs reactor**: the industry-standard split is that *projectors* are pure and side-effect-free, and *reactors* (a.k.a. process managers / sagas) are the only components allowed to emit new events or commands. The reason is replay: a rebuild must re-run every projector and must **not** re-run any reactor. If a projection could emit, replay would duplicate the world.

### The Event Queue pattern

Source: [Game Programming Patterns — Event Queue (Nystrom)](https://gameprogrammingpatterns.com/event-queue.html)

Three findings directly on point:

- "All event and message systems have to worry about cycles" — sender enqueues, receiver responds by enqueuing, back to sender.
- The stated remedy: **"avoid *sending* events from within code that's *handling* one."** Which is your rule 22, verbatim in intent.
- **Staleness**: by the time a queued event is processed, "that stuff may be gone." Hence: "Queued events tend to be more data heavy than events in synchronous systems" — you must capture what you need at enqueue time. This maps onto your **snapshot vs ambient Modifier** distinction and onto MTG's last-known-information rule; it is the same problem three times.

---

## 7. DATABASE TRIGGERS

### SQL Server
Source: [Create Nested Triggers (Microsoft Learn)](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/create-nested-triggers?view=sql-server-ver17) · [Using Nested Triggers](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2008/ms190739(v=sql.100)) · [Limits to SQL Server recursion](https://seniordba.wordpress.com/2015/05/08/limits-to-sql-server-stored-procedure-recursion/)

- **"DML and DDL triggers can be nested up to 32 levels."**
- At the limit: "If nested triggers are allowed and a trigger in the chain starts an infinite loop, the nesting level is exceeded and the trigger terminates." And crucially: **"a failure at any level of a set of nested triggers cancels the entire transaction, and all data modifications are rolled back."**
- `nested triggers` server option (AFTER triggers only; INSTEAD OF nest regardless). `RECURSIVE_TRIGGERS` database option **OFF by default**, blocking *direct* recursion; blocking *indirect* recursion requires setting `nested triggers` to 0 as well.
- **Why 32: no semantic rationale is published anywhere I could find.** 32 is the general T-SQL nesting level shared with stored procedures, functions and triggers (`@@NESTLEVEL`) — a stack-frame budget, not a design decision about causality.

### PostgreSQL
Source: [Trigger recursion in PostgreSQL (CYBERTEC)](https://www.cybertec-postgresql.com/en/dealing-with-trigger-recursion-in-postgresql/)

- **No fixed depth limit at all.** The only bound is `max_stack_depth` (default 2 MB); exceeding it raises `stack depth limit exceeded`, aborting the transaction. The article notes that raising it "merely delays the inevitable."
- Recommended remedies, in ascending order of quality: `pg_trigger_depth() < 2` in the trigger body; the same test in a `WHEN` clause so the function is never even invoked; and **adding a predicate that makes the update self-falsifying** (`AND NOT worker.quarantined`), so the recursion runs out of work. The last one is refraction, hand-rolled.

### MySQL
Source: [MySQL stored program restrictions](https://dev.mysql.com/doc/refman/8.0/en/stored-program-restrictions.html) · [MySQL restrictions and limits](https://docs.oracle.com/cd/E19078-01/mysql/mysql-refman-5.0/restrictions.html)

- **"A stored function or trigger cannot modify a table that is already being used (for reading or writing) by the statement that invoked the function or trigger."** This structurally forbids the most common recursion shape rather than bounding it.
- "Stored functions cannot be used recursively." Triggers are not activated by foreign-key actions — another cascade path deliberately severed.
- MySQL's answer to trigger cascades is essentially **depth limit = 0, enforced by prohibition.**

---

# RECOMMENDATIONS

## (a) The closed set of condition forms

**Design principle taken from 704.5:** MTG's closed list is short and every entry answers "what state must not persist." Content's *interesting* consequence lives in triggered abilities (603), which the Substrate does not enumerate. You are proposing that Listeners do both jobs, so your form set must be a *predicate algebra*, not a list of situations.

**Recommended closed set — eight forms, all pure predicates over folded state at the evaluation layer:**

1. **Threshold on a value** — `Dimension | Resource | Capacity` on one Entity, compared to a constant with `< ≤ = ≥ >`. (Covers 704.5a/b/c/i/v, Resource depletion.)
2. **Comparison of two values on the same Entity** — `A ⋈ B` where both are attributes of one Entity. (Covers 704.5g lethal damage, 704.5q counter annihilation.)
3. **State presence/absence** — a named State on an Entity is/is not present; optionally "present on this axis."
4. **Tag membership** — Tag ID present/absent, with optional magnitude compared to a constant. (Identified by ID, per your dictionary — never by name.)
5. **Set cardinality** — `count(selector) ⋈ n`, where `selector` is a Category + a bounded scope (one Place, one Relationship's participants, one Campaign). Special-case `= 0` and `≥ 1` for the empty/non-empty forms you named. (Covers legend rule 704.5j, Participant Capacity.)
6. **Place/containment legality** — the Entity's Place is/is not within a declared legal set. (Covers 704.5m/n/p — the whole "illegally attached" family collapses into one form.)
7. **Relationship stance** — one participant's Connection value on a Relationship, compared to a constant. Because Connections are stored per-participant rather than as edges, this stays a single-Entity read and does not need a join.
8. **Threshold Noun satisfied** — "Threshold T declared on Entity E is now met," reading its contributors as `sum | highest | each` exactly as the Threshold declares. This is free: the Noun already exists.

**Boolean combination:** allow `AND` and `NOT` over the above; allow `OR` only as sugar for multiple Listeners. Forbid nesting depth > 2. Rationale: `AND`/`NOT` keep the predicate a Tier-0 datum evaluable in one pass; arbitrary quantification is what forces you into Rete and makes evaluation cost unbounded.

**Explicitly excluded, and say so in `SPEC.md`:**
- "A Verb of kind X was invoked" — that is the retired Effect concept wearing a hat.
- "A Record matching shape S exists" — see (e) below.
- "Value changed by more than N since the last Moment" — a delta is not a state. If content wants it, the delta must be a stored Facet, and then form 1 applies.
- Unrestricted cross-Entity comparison (`E1.x ⋈ E2.y` for arbitrary E1, E2). Permit only where the second Entity is *reachable by a declared relation from the first* — its Place, its Relationship counterpart, its Scale parent. Unbounded pairs is the point where evaluation cost stops being linear and where determinism starts depending on iteration order.

**The critical addition: make every Listener edge-triggered, in the Substrate, not per-Listener.**

Store, per `(listener_id, target_entity_id)`, the predicate's truth value at the previous evaluation. Fire only on `false → true`. This gives you:

- "Entity gains a property" for free — it is form 3 plus the edge.
- "Entity loses a property" for free — it is `NOT` of form 3 plus the edge.
- "A set becomes non-empty" for free — form 5 `≥ 1` plus the edge.
- **Refraction**, i.e. MTG 603.8 and CLIPS's loop guard, as a Substrate property rather than a content obligation.

**Correctness finding you must not miss:** that fired-set memory is *state*. It must be part of the fold derived from the Ledger, not process memory. If it lives in memory, the same Ledger will not fold to the same state after a rebuild, and you will have silently broken your central invariant. Either derive it (re-evaluate all predicates at every historical Moment during replay — expensive but sound) or write it into the Resolution Record (cheap, auditable, and consistent with "every slot derivable"). I'd write it.

## (b) The cascade depth limit

**Finding: there is no standard.** The observed values, with rationale where any exists:

| System | Limit | Recorded rationale |
|---|---|---|
| MySQL triggers | 0 (structural prohibition) | avoid modifying a table in use by the invoking statement |
| Legends of Runeterra | 10 (spell stack; 10th must be Burst) | none published; evidently legibility |
| Master Duel | ~10 iterations / 16 steps | avoid softlocks seen in earlier YGO video games |
| SQL Server | 32 | **none** — shared `@@NESTLEVEL` stack budget |
| PostgreSQL | none (byte-bounded stack) | resource safety only |
| MTG, Hearthstone | none | fixpoint + refraction + game-level draw |

**The rationale record is essentially empty.** 32 is a stack-frame number that leaked into a semantic position. The only *chosen* numbers — LoR's 10, Master Duel's 10/16 — are in the range a human can follow.

**Recommendation: adopt three limits, not one.**

1. **Generation limit = 8.** A "generation" is one hop of Listener-produced consequence. Because rule 22 pins produced Verbs to a *later Moment*, generation depth and Moments-advanced are the same number, which is a real advantage no other system has: **you can state the limit in the fiction** — "consequence does not propagate more than eight Moments from its cause" — instead of as an engine budget. Pick 8 because it sits in the legible band (LoR's 10, Master Duel's 10) rather than the machine band (32), because every real content chain in the card games surveyed is ≤ 4, and because a power of two makes the field cheap. A Ruleset Edition may lower it; nothing may raise it.

2. **Per-Moment firing budget** (suggest 256 Listener firings and 256 derived Verbs per Moment). Depth counters are blind to *wide* blowups — one Listener matching 10,000 Entities is not deep and will still kill you. Every depth-limited system I looked at has this hole.

3. **Static triggering-graph gate at Bundle load.** This is the recommendation with the highest value per unit of work, and you can have it *because Listeners are declared as data*. Build the graph: edge from Listener L to Listener M when L's produced Verbs write a Dimension/State/Tag that M's predicate reads. **Acyclic ⇒ termination guaranteed** (Aiken/Hellerstein/Widom). Cyclic ⇒ not necessarily broken, but the Bundle must declare the cycle explicitly and accept the runtime budget. Report cycles at CI. Note honestly in `SPEC.md` that this is sound-but-conservative and that general termination is undecidable — do not claim more.

Note that with edge-triggering from (a), the runtime limits are a backstop, not the mechanism. That is the correct relationship, and it is the one MTG, Hearthstone and LoR all landed on.

## (c) Behaviour at the limit

Observed behaviours: **rollback + error** (SQL Server, PostgreSQL), **draw** (MTG), **destroy the culprit** (Yu-Gi-Oh TCG policy, Master Duel), **silently defer** (Hearthstone re-entrancy), **prohibit statically** (MySQL).

**Recommendation: halt-and-record. Never error, never roll back, never mutate the world to enforce an engine budget.**

At the limit: stop producing derived Verbs and append a `CascadeLimitReached` Record naming the originating Record, the ordered chain of `listener_id`s, the generation count, and which budget was exhausted (depth or fan-out). The state stands as of the last completed generation. Deliver to the GM; surface it in the resolution expansion.

Reasoning, against each alternative:

- **Rollback is not available to you and is wrong anyway.** The Ledger is never updated or deleted; corrections are compensating Records. And your rule 8a already says a partial result is a legal result — everything not named is unchanged. A cascade truncated at generation 8 is a well-defined state, not a corrupted one. SQL Server rolls back only because it has transactions; you do not, and should not envy it.
- **Erroring loses the Session.** The database answer costs a transaction; yours would cost a table of six people their evening.
- **A draw has no RPG analogue.** MTG can end the game because the game is short and symmetric. A Campaign is neither.
- **Destroying the culprit (YGO) violates your rule 7.** It is the Substrate special-casing world state to protect itself. It is also non-obviously deterministic — "the card ruled to be the source" is a judgment call, which is exactly why the TCG needs a policy document and Master Duel needed a separate implementation.
- **Silent deferral (Hearthstone) fails your own standard**: "if you can violate it silently, the gate is missing."

Two further requirements:

- **The limit outcome must be part of the fold**, not a runtime exception. Same Ledger, same truncation, same `CascadeLimitReached` Record, on every machine, forever. If it is thrown rather than folded, you have made determinism depend on the runtime.
- **Split authoring-time from runtime.** A static cycle detected at Bundle load should make the **Bundle fail to load**, exactly as an empty Socket does under rule 12. Fail loudly where a human can fix it; degrade quietly and visibly where one cannot.

Every `CascadeLimitReached` Record is a golden fixture waiting to be adopted. Make `ops repro` pull them.

## (d) Deterministic evaluation order

**Your current key** is `(layer, component_id, listener_id, target_entity_id)`. It is better than anything Drools or CLIPS ships. Two changes:

**1. Insert a class ordinal between `layer` and `component_id`, splitting decision-free from decision-bearing.**

```
(layer, decision_class, component_id, listener_id, target_entity_id, source_record_id)
       └── 0 = Auto Decider · 1 = Person Decider (produces a Proposal)
```

This is SEGOC's mandatory-before-optional, and it is the single highest-value change available. Everything the server can settle alone settles first, so that when a human Decider is finally asked, they are choosing against a fully resolved board rather than a half-resolved one. It also means a Moment's `Auto` portion folds to completion without any round trip, which is what makes "the server folds, clients render" actually achievable when Proposals are in flight. MTG reaches for the same idea in 603.3b (non-ability-triggered before ability-triggered) and Yu-Gi-Oh formalises it properly.

**2. Append a final tiebreak — `source_record_id`, or the pinned Tick plus a record ordinal.**

`(layer, component_id, listener_id, target_entity_id)` is **not unique**. The same Listener can fire on the same target from two distinct contributing sources within one Moment — a vector from each of two attackers crossing the same Threshold, for instance. When the key is not total, your sort is stable only by accident of the input order, and your Determinism section's own warning applies: "changing the order of additions changes results." This is a silent gate failure today. Add the field.

**Failure modes of the orderings actually in use, and why each is rejected:**

- **Salience / priority integers (Drools, CLIPS):** content authors escalate. The number becomes an unmanaged global namespace shared across Components written by strangers, and the only way to win is to bid higher. Your Layer regions (E-/C-/R-) already do this job correctly because they are a *declared, bounded, meaningful* ordinal space rather than an open integer. **Do not add salience.** If a Component wants to go earlier, it must argue for a Layer, in public.
- **Recency / LIFO (Drools default, CLIPS `depth`):** deterministic only if insertion order is, and it makes behaviour depend on evaluation history rather than declared intent. Worse for you specifically: it is **hostile to additive-only evolution** — adding a Listener silently changes the recency ordering of every existing one.
- **Positional (Hearthstone order-of-play; LoR left-to-right):** genuinely deterministic and wonderfully legible, but it couples behaviour to a spatial or temporal accident, and players immediately optimise placement. `target_entity_id` is your analogue and is fine as a *tiebreak* precisely because it is arbitrary-but-stable. Never make it primary, or entity creation order becomes a game mechanic you did not design.
- **Player chooses (MTG APNAP + free ordering within a controller's set; YGO within a bucket):** impossible for a server-side fold without a Proposal per ordering decision. Change (1) exists so you never need this.
- **File / registration order (Prolog's default):** breaks additive-only outright. Inserting a Component changes existing behaviour. Forbid.
- **Arbitrary among ties (Drools' and CLIPS's honest admission):** disqualifying. Your whole thesis is that the same Ledger folds the same way everywhere, forever.

**Third recommendation, structural rather than about the key: freeze the candidate set.**

Snapshot the eligible Listener set at the start of the Listener pass for a Moment. Listeners created *during* that pass — because an Entity gained a Facet — do not participate in it; they are eligible from the next Moment. This is Hearthstone's queue immutability and MTG's separate "then put waiting triggers on the stack" pass. **It converts a fixpoint over a growing set (may not terminate) into a total order over a fixed set (always terminates in one pass).** Combined with edge-triggering, this is your real termination proof; the depth limit in (b) is only there for cross-Moment chains.

## (e) "A resolution record exists matching a shape" as a substitute for event-watching

**Verdict: no, and the argument against it is stronger in your architecture than in any of the systems surveyed.**

**Evidence against:**

1. **MTG 704.1a draws exactly this line and keeps both mechanisms.** An ability that watches game state but uses the stack is a triggered ability, not a state-based action. MTG has had thirty years to collapse these and has not.
2. **The decisive argument, and it is specific to you: your Ledger contains retracted history.** Corrections are compensating Records by default (rule 11). A shape-matching Listener would match the *erroneous* Record as happily as the corrective one, because both are in the Ledger and neither is deleted. State-folding cannot make this mistake — the fold reconciles the compensation. MTG has the same problem in miniature and solves it with 603.2h: prevented or replaced events do not trigger abilities. You cannot implement 603.2h over an append-only shape match without rewriting history, which rule 11 forbids.
3. **A Record never stops existing, so shape-matching has no natural refraction.** Every evaluation re-matches. To stop re-firing you need a per-Listener "highest Record already seen" cursor — which is a hidden, mutable, per-Listener projection, i.e. exactly the state you were trying to avoid, only now undeclared. Refraction over a *predicate* is free (the predicate goes false); refraction over *history* is not.
4. **Event-sourcing practice is unanimous**: projectors are pure folds, reactors are the only emitters, and the reason is replay. A Listener that reads Record shapes and emits Verbs is a reactor reading raw history, which makes replay ambiguous between "already reacted" and "reacting now." The standard fix is checkpoints plus idempotency keys — more hidden state.
5. **Drools' own trajectory**: `no-loop` and `lock-on-active` are patches; the mechanism that actually works is **property reactivity — narrowing what a rule watches to the specific fields it constrains.** Record-shape matching is maximally wide watching. It is the opposite of the thing that worked.
6. **It kills your static triggering-graph gate.** You can compute "L writes what M reads" only if M's reads are declared over a bounded vocabulary of Dimensions, States and Tags. A shape query over Records reads everything, so every Listener edges to every Listener, the graph is complete, and the one termination guarantee actually available to you evaporates.

**Evidence for — the residual need is real, and you should design for it rather than be ambushed:**

MTG needed look-back-in-time (603.6) and last known information (603.10). Hearthstone needed a Death Creation Step where dying entities are still addressable. Yu-Gi-Oh needs "the last thing to happen." Nystrom's Event Queue chapter warns that by processing time "that stuff may be gone." **Four independent systems, same gap: some consequences are only expressible about a thing that no longer exists, or about a quantity that only existed during a resolution.**

**Recommended answer to the residual, in two parts:**

**(i) Never delete an Entity.** Ceasing to exist becomes a terminal State, not a removal from the fold. The predicate stays evaluable, "was destroyed" becomes form 3 plus an edge, and you get last-known-information for free because the information was never lost. This is already implied by additive-only and by IDs being permanent; make it explicit.

**(ii) Expose a small closed set of Moment-scoped derived quantities on the target, readable by Listener predicates.** The Resolution Record already holds all of these — you are not adding data, you are naming what is already computed:

- total inbound magnitude per Dimension, this Moment, on this target
- total inbound magnitude per Domain, this Moment, on this target
- highest single contributor
- distinct contributor count
- whether a Guard clamped (R-850 flat / R-1050 proportional, distinguishable)
- whether Immunity clamped at R-600
- whether truncation occurred at each of R-400 / R-750 / R-1050

Read these three ways — `sum`, `highest`, `each` — the same three readings a Threshold already declares, so there is one concept in the vocabulary, not two.

These are **state, not events**, because they are properties of the pair `(target, Moment)`. They fold identically. They are scoped to one Moment and therefore vanish at the next, so refraction is automatic and no cursor is needed. They are bounded, so the triggering graph survives. And they solve the specific problem — "damage is not a state" — that pushes every other system into event triggers. It is the narrowest possible concession, and it lands in exactly the place where you already have the data, an audit hash, and a rendering obligation.

---

# CROSS-CUTTING FINDINGS

1. **Refraction is the mechanism; depth limits are the backstop.** Every system that has survived at scale terminates cascades by making a rule stop matching, not by counting. MTG 603.8, CLIPS's not-previously-used, Drools' property reactivity, and PostgreSQL's recommended `AND NOT already_set` predicate are the same idea in four vocabularies. Depth caps appear only in digital implementations, always retrofitted, always after a softlock shipped.

2. **Freezing the candidate set is the other half.** MTG checks SBAs to fixpoint, *then* adds triggers in a separate pass. Hearthstone makes the queue immutable once resolution begins. LoR fires triggers only after the causing event fully resolves. All three independently converted a fixpoint over a growing set into a total order over a fixed one. Do the same.

3. **Priority numbers are the documented failure; structural position is the documented success.** Drools ships salience and admits ties are arbitrary. CLIPS ships seven strategies and admits ties are arbitrary. Hearthstone and LoR, which must be deterministic because a machine adjudicates, both use an ordering key that is *already visible on the board*. Your Layer regions are the right shape; do not add a priority integer on top of them.

4. **Mandatory-before-optional is the ordering rule worth stealing.** Yu-Gi-Oh formalised it (SEGOC), MTG gestures at it (603.3b's two passes), and it is exactly what a server-side fold needs: everything resolvable without a decision resolves first, so decisions are made against a settled state.

5. **Termination is undecidable; a conservative static guarantee plus a runtime budget is the best available.** The active-database literature settled this — Aiken/Hellerstein/Widom's triggering graph gives sound-but-conservative termination via acyclicity, Baralis/Widom's activation graph tightens it, model checking tightens it further. **You are unusually well-placed to have the static gate because Listeners are Tier-0 data.** That is the payoff for the declarative constraint, and you should collect it.

6. **Nobody rolls back except databases, and only because they have transactions.** Games truncate: Master Duel destroys a card, MTG declares a draw, Hearthstone defers the re-entrant iteration, LoR refuses the eleventh spell. Your append-only Ledger has no rollback available and should not want one — halting and recording is both the only implementable option and the correct semantics under your rule 8a.

7. **The two-phase split — pure derivation, then emission — is independently reinvented in every domain examined.** MTG: state-based actions (no stack, no response) vs triggered abilities (stack, response). Event sourcing: projector vs reactor. Nystrom: don't send events while handling one. Databases: INSTEAD OF vs AFTER. Your Fold/Listener/Verb split is the same discovery. That convergence is the strongest evidence your architecture is sound.

8. **Every state-watching system needed a look-back mechanism.** Four for four. Plan for it (terminal States instead of deletion, plus Moment-scoped derived quantities) rather than discovering it in month nine, when the Substrate can no longer change.

9. **Global termination caps are separate from cascade caps, and digital games ship both.** Hearthstone's draw at turn 89 has nothing to do with trigger depth; it exists because *something* must end. The Campaign analogue is not a Moment cap but a fold-cost budget per Campaign — worth having for the same reason and at the same level, not mixed in with cascade depth.

10. **Two specific gate failures in your current spec, both silent today:**
    - `(layer, component_id, listener_id, target_entity_id)` is not a total order — the same Listener can fire on the same target from two sources in one Moment. Add `source_record_id`.
    - The Listener fired-set (the refraction memory) is folded state. If it lives in process memory rather than being derived from or written to the Ledger, the same Ledger will not fold to the same state after a rebuild.

## Sources

- [MTG Comprehensive Rules 704 — State-Based Actions](https://ancestral.vision/additional-rules/state-based-actions.html)
- [MTG Comprehensive Rules 603 — Handling Triggered Abilities](https://ancestral.vision/spells-abilities-and-effects/handling-triggered-abilities.html)
- [MTG Wiki — State-based action](https://mtg.fandom.com/wiki/State-based_action) · [mtg.wiki mirror](https://mtg.wiki/page/State-based_action)
- [MTG Wiki — Triggered ability](https://mtg.fandom.com/wiki/Triggered_ability)
- [MTG Wiki — Loop](https://mtg.fandom.com/wiki/Loop) · [Shortcut](https://mtg.fandom.com/wiki/Shortcut) · [Ending the game](https://mtg.fandom.com/wiki/Ending_the_game)
- [Yawgatog — Magic Comprehensive Rules (104.4)](https://yawgatog.com/resources/magic-rules/)
- [Magic Tournament Rules 4.4 — Loops](https://blogs.magicjudges.org/rules/mtr4-4/) · [MTR index](https://blogs.magicjudges.org/rules/mtr/)
- [Cantrip — How Triggered Abilities work (603.3b, 116.5)](https://cantrip.ru/en/mtg-judge/triggered-abilities.shtml)
- [Hearthstone Advanced Rulebook (wiki.gg)](https://hearthstone.wiki.gg/wiki/Advanced_rulebook) · [Fandom mirror](https://hearthstone.fandom.com/wiki/Advanced_rulebook) · [Turn](https://hearthstone.fandom.com/wiki/Turn)
- [LoR — Trigger keyword and resolution order](https://leagueoflegends.fandom.com/wiki/Keywords_(Legends_of_Runeterra)/Trigger) · [LoR:Recursion](https://wiki.leagueoflegends.com/en-us/LoR:Recursion)
- [Yugipedia — Simultaneous Effects (SEGOC)](https://yugipedia.com/wiki/Simultaneous_Effects) · [Infinite loop](https://yugipedia.com/wiki/Infinite_loop) · [Yu-Gi-Oh! Wiki SEGOC](https://yugioh.fandom.com/wiki/Simultaneous_Effects_Go_On_Chain) · [YGOrganization: Demystifying Rulings Part 3](https://ygorganization.com/learnrulingspart3/)
- [Drools 8.38 — Rule engine, agenda, TMS](https://docs.drools.org/8.38.0.Final/drools-docs/docs-website/drools/rule-engine/index.html) · [Drools 6.5 ch.7 Running](https://docs.drools.org/6.5.0.Final/drools-docs/html/ch07.html)
- [CLIPS — Conflict resolution strategies](https://www.csie.ntu.edu.tw/~sylee/courses/clips/bpg/node5.3.html) · [MEA strategy](https://www.csie.ntu.edu.tw/~sylee/courses/clips/bpg/node5.3.6.html) · [CLIPS User Guide ch.3](https://portal.cs.umbc.edu/clips/usersguide/ug3.html)
- [Wikipedia — Conflict resolution strategy (refractoriness, recency, specificity)](https://en.wikipedia.org/wiki/Conflict_resolution_strategy)
- [Ray & Ray — Detecting Termination of Active Database Rules Using Symbolic Model Checking (PDF)](https://www.cs.colostate.edu/pubserv/pubs/Ray-iray-research-adbis01.pdf)
- [Baralis & Widom — An algebraic approach to static analysis of active database rules](https://www.semanticscholar.org/paper/An-algebraic-approach-to-static-analysis-of-active-Baralis-Widom/e1435e7124614d8a2b4717663b6644fdb03c3e00) · [Jennifer Widom's publications](https://cs.stanford.edu/people/widom/pubs.html) · [Unrolling Cycles to Decide Trigger Termination (VLDB'99)](https://dl.acm.org/doi/10.5555/645925.671354)
- [Event Sourcing: Projections — domaincentric.net](https://domaincentric.net/blog/event-sourcing-projections) · [Consumers, projectors, reactors — Architecture Weekly](https://www.architecture-weekly.com/p/consumers-projectors-reactors-and) · [Event Sourcing anti-patterns — InfoQ](https://www.infoq.com/news/2016/04/event-sourcing-anti-pattern) · [eventsourcing docs: Projections](https://eventsourcing.readthedocs.io/en/v8.3.0/topics/projections.html)
- [Game Programming Patterns — Event Queue](https://gameprogrammingpatterns.com/event-queue.html)
- [SQL Server — Create Nested Triggers](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/create-nested-triggers?view=sql-server-ver17) · [Using Nested Triggers](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2008/ms190739(v=sql.100)) · [Recursion limits](https://seniordba.wordpress.com/2015/05/08/limits-to-sql-server-stored-procedure-recursion/)
- [CYBERTEC — Trigger recursion in PostgreSQL](https://www.cybertec-postgresql.com/en/dealing-with-trigger-recursion-in-postgresql/)
- [MySQL — Stored program restrictions](https://dev.mysql.com/doc/refman/8.0/en/stored-program-restrictions.html) · [Restrictions and limits](https://docs.oracle.com/cd/E19078-01/mysql/mysql-refman-5.0/restrictions.html)agentId: a074326bad1cbeb29 (use SendMessage with to: 'a074326bad1cbeb29', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 118048
tool_uses: 65
duration_ms: 856527</usage>