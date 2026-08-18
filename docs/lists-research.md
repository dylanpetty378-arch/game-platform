# Research for the remaining lists

*August 2026. Six research passes run against the field before proposing L31 (Timings), L26 (Listeners), L5 (States), L25 (Landing), L4 (Tags) and L1–L3 (Categories and Attributes). This is the digest — the findings that change a decision. The full reports are in `research-timing.md`, `research-listeners.md`, `research-states.md`, `research-entities.md`.*

**Historical — this digest predates the settlements.** Every candidate list below was a proposal to react to; the lists have since closed, and where this digest and the settled decisions disagree, **`dictionary.md` Part 12 governs**. Known divergences worth naming: the Landing section speaks of a Landing Socket and Landing Component that were retired when the Track merge landed (a push lands on the Track the Dimension names; the per-Dimension landing models are base Ruleset); this digest recommended cascade depth 32 where the full report `research-listeners.md` recommended a generation limit plus a per-Moment budget — the 32 was adopted, and the report's sharper concerns are carried as `open-questions.md` Q3.8 and Q3.10; the Tag count and State vocabulary here predate L4's provisional twenty-four and the State→Track merge.

---

# 1 · Timings — for L31

**The headline, and it reframes the list.** The deepest systems do not have one timing field. They have **three orthogonal fields**: a *category* (how the ability gets used at all), a *speed* (when it may be used), and a *cost/frequency* (what it consumes and how often). Most games contaminate all three into one word — which is precisely the fusion Dylan's cost shape already separates.

Magic and Yu-Gi-Oh converged **independently** on the same four-way category split. And both keep their actual *speed* set tiny: two members and three respectively.

## Magic's four categories (CR 113.3)

| Category | What it is |
|---|---|
| **Spell ability** | instructions followed while the spell resolves |
| **Activated** | `[Cost]: [Effect]` — a player may activate it whenever they have priority |
| **Triggered** | begins with *when*, *whenever*, or *at* — goes on the stack the next time a player would receive priority |
| **Static** | continuously true, never uses the stack, never "does" anything |

**This maps onto our design almost exactly**, and it is worth saying which of ours is which:

- **Activated** → an ability with a `cost` and a `timing`. This is the normal case.
- **Triggered** → a **Listener**. Already ours, already class `Triggered`, already pinned to a later Moment.
- **Static** → a **Modifier** or a **Guard**. Never a Verb, never resolved, just present at R-200/R-300 or R-850/R-1050.
- **Spell ability** → the vector's own resolution. Not a separate thing for us.

**So the timing list is only about the Activated category.** Triggered and static are already other machinery. That shrinks the list a great deal and is the single most useful structural finding.

## The speed set is tiny everywhere it survives

| System | Speed tiers |
|---|---|
| MTG | 2 — sorcery speed, instant speed |
| Yu-Gi-Oh | 3 — Spell Speed 1, 2, 3 |
| PF2e | 2 — on your turn, or a reaction with a stated trigger |
| D&D 4e | 4 — and it was cut to 3 in 5e, then disowned |

**D&D 4e's interrupt/reaction distinction is the one genuinely contested case.** 4e separated *immediate interrupt* (resolves **before** the trigger, and may prevent it) from *immediate reaction* (resolves **after**). 5e collapsed both into "reaction." The recorded verdict is split: interrupts allow the most satisfying plays in the game (negating the attack that would kill you) and are also the single largest source of table arguments, because "before" requires rewinding a declared action. Worth a decision, not a default.

## Multi-Moment activation

Every system that has it uses the same shape: **declare now, resolve later, and the gap is visible.** Final Fantasy Tactics' Charge Time, MTG's suspend, Exalted's Speed, Feng Shui's carryover into the next sequence. The consistent design requirement is that **the pending thing is visible and interruptible** — a cast time nobody can respond to is just a worse instant.

For us this is free: a pending vector is already an Entity, and pinning is already how it works.

## Sustained / maintained

Named consistently across systems (concentration, sustained, upkeep, channel) and always with the same two properties: **it occupies something while it lasts**, and **it ends if the thing that occupies it is disturbed**. Our answer is already the `committed` spend mode plus a Listener — no new timing word needed unless we want the shorthand.

## What goes wrong when the timing set is too large

D&D 4e is the recorded case: standard / move / minor / free / immediate interrupt / immediate reaction / opportunity, plus a substitution hierarchy (standard downgrades to move, move to minor). The documented cost is players "eking out every last drop" of each type every turn, and combat inflating to twelve possible actions at high tiers. **The cost is not the number of names — it is the number of *pairwise interactions* between names.** Two names have one interaction; seven have twenty-one.

## Frequency caps fused into the timing name

Repeatedly done, repeatedly regretted. D&D's "bonus action" is a size, a slot and a once-per-turn cap in one word — its own designer's verdict is that fusing them is why it failed. Keeping `cap` a separate field is the supported choice.

## Candidate closed set — six

| Timing | Means | Precedent |
|---|---|---|
| `own` | only during a Moment I own | sorcery speed · PF2e "on your turn" |
| `any` | during any Moment, mine or not | instant speed · Spell Speed 2 |
| `respond` | only during a Moment I do **not** own, and only when a stated condition holds | reaction · Spell Speed 2 with trigger |
| `interrupt` | as `respond`, but resolves **before** the thing that prompted it | 4e immediate interrupt · Spell Speed 3 |
| `pending` | declared now, resolves at a named later Moment; visible and interruptible meanwhile | suspend · Charge Time · Exalted Speed |
| `standing` | no Moment at all — continuously present while its condition holds | MTG static abilities |

**Open questions for the list:**

1. Is `interrupt` worth its cost? It is the most powerful and the most argued-about.
2. Is `standing` a timing at all, or is it just "this is a Modifier, not an ability"? Leaning: it is *not* a timing and should be cut — it is the static category, already covered.
3. Does `any` need to exist, or is it just `own` ∪ `respond` with no condition?

---

# 2 · Listeners and cascades — for L26

**Magic's state-based actions are the proof our design works at scale**, and the mechanism should be copied closely.

## The loop that terminates

MTG rule 704.3, in effect:

```
1. whenever a player WOULD receive priority, check every state-based condition
2. perform ALL applicable ones SIMULTANEOUSLY, as one event
   — nobody controls them, nobody may respond, they do not use the stack
3. if any were performed, GOTO 1
4. when none apply, put all waiting triggered abilities on the stack
5. GOTO 1
6. only when neither fires does a player receive priority
```

Three things matter for us:

- **704.1a draws exactly our line.** An ability that watches state but uses the stack is a *triggered ability*, not a state-based action. MTG maintains both mechanisms deliberately and does not treat them as interchangeable. That is our Listener/Modifier split.
- **704.4: state-based actions "pay no attention to what happens during the resolution of a spell or ability."** A creature whose toughness dips to 0 mid-resolution and recovers before the check **survives**. Only the state at the check point exists. This is our "evaluated at a fixed layer" rule, and it is load-bearing: it makes intermediate states *unobservable and therefore unspecified*, which is what lets the Fold be optimised without changing answers.
- **MTG terminates without a depth counter.** It runs to a fixpoint. Loops that would run forever without changing game state are handled by a *social* rule (the game is a draw), not a mechanical one. **We cannot copy that** — we have no table to appeal to. So we need the counter MTG doesn't.

## Depth limits actually chosen elsewhere

| System | Limit | At the limit |
|---|---|---|
| SQL Server nested triggers | **32** | error, transaction rolled back |
| Hearthstone | small hard cap on re-entrant triggers | queued effects dropped |
| Drools | `no-loop` / `lock-on-active` per rule | rule simply does not re-fire |
| MTG | none | draw (a social outcome) |

**32 is the number the database world converged on and nobody has argued with it in twenty years.** It is high enough that no legitimate design reaches it and low enough to catch a runaway in milliseconds.

**Recommended behaviour at the limit: halt without applying, and write a Record.** Rolling back is wrong for us (the Ledger is append-only). Silently dropping is worse (it is invisible). A Record of the halt makes it a debuggable finding rather than a mystery, and it is the honest version of the rule that "if you can violate it silently, the gate is missing."

## Deterministic ordering of simultaneous triggers

Yu-Gi-Oh's **SEGOC** (Simultaneous Effects Go On Chain) is the only fully specified ordering in any game, and its structure is worth stealing: a fixed **priority classification** first, then turn-player-first within each class, then a declared tiebreak. Ours already is `(layer, component_id, listener_id, target_entity_id)` — the finding is that the *first* key should be a semantic class, not just a layer number, and that a fully specified order is achievable.

Drools' conflict-resolution strategies are the caution: salience-based ordering is *deterministic* but not *stable* under rule-set edits — adding a rule changes the order of unrelated rules. Our sort key must be composed only of values that do not move when unrelated content is added. `component_id` and `listener_id` satisfy that; a global priority number would not.

## Candidate condition forms

| Form | Example |
|---|---|
| a value crosses a bar | `vitality Resource ≤ 0` |
| a value compares to another value | `my standing < theirs` |
| an Entity holds a State | `is prone` |
| an Entity holds a Tag (optionally with magnitude ≥ N) | `has Flammable` |
| a set is non-empty / has size N | `hostiles within reach ≥ 3` |
| a Resolution Record exists matching a shape | *how reflection and retribution work* |
| a Moment of a named kind has occurred | `start of my turn` |

**On the last-but-one:** "a Resolution Record exists matching a shape" is our substitute for event-watching, and the research supports it — it is state (the Record exists, it is a durable fact in the Ledger), not an event, and it is exactly how Delta Green's bond-damage and Exalted's decision points are structured. It is also the only way to express "when you are healed by another," which is a real authoring need.

---

# 3 · States — for L5

## The design we already have is shipping in the most-played RPG in the world

D&D 5e conditions have **no intrinsic duration**. A condition ends because the effect that imposed it ends, or because a named action ends it. That is our "ended only by a Verb," already validated at enormous scale.

## Magnitude: take-higher, never add

Pathfinder 2e is the reference: conditions with numeric values (`frightened 2`, `clumsy 3`, `drained`, `doomed`) **take the higher value when applied twice, never the sum**. This is not a stylistic choice — additive stacking makes any repeatable source unbounded. `frightened` also decreases by 1 at the end of each turn, which is a self-ending magnitude and worth noting as a pattern: **the magnitude is also the timer.**

For us this lands on L18: the aggregation operator for States is `max`, and the research is unambiguous.

## Implication is a documented cost

5e's `paralyzed`, `stunned` and `unconscious` all *include* `incapacitated`, and the 2024 revision had to widen `incapacitated` — which then cascaded to all three. One condition definitionally implying another is the same failure as tag hierarchy (§5), and it is a live maintenance cost in a shipping product.

## Deliberate shrinking is the recorded trend

3e/PF1 carried at least 34 conditions. 4e carried more, with save-ends/end-of-turn/encounter durations layered on top, and the tracking load is its most-cited failure. 5e cut to 15 and dropped `dying` and `weakened` as formal conditions. **Nobody has grown a condition list and been glad.**

## Candidate exclusivity axes

Axes, not conditions — the axis is what L5 is deciding.

| Axis | Members (illustrative — Components fill these) |
|---|---|
| `posture` | standing · prone · seated · airborne |
| `restraint` | free · grabbed · restrained · immobilised |
| `consciousness` | awake · asleep · unconscious |
| `awareness` | aware · surprised · unaware |
| `visibility` | seen · concealed · hidden · unseen |
| `animacy` | living · dying · dead |
| `containment` | free · contained · submerged |

Seven axes, and each is genuinely exclusive — you cannot be both prone and airborne, both grabbed and free. The test that produced them: *can two members be true at once?* If yes, they are two axes or they are Tags.

**Deliberately not axes:** anything numeric (that is a Dimension or a Resource), anything that is really membership (that is a Tag), anything with a duration that ticks (that is a Resource with a Threshold).

## Diminishing returns is an exclusivity axis in disguise

WoW's crowd-control DR categories are literally exclusivity axes with a decay rule attached. Worth knowing when a Component wants "you cannot be stunned twice in a row" — that is an axis plus a Listener, not a new mechanism.

---

# 4 · Landing — for L25 and the Landing Socket

**Eleven distinct landing models exist in the field.** The taxonomy is the useful output.

| | Model | What it is | Precedent |
|---|---|---|---|
| L0 | **Evaporate** | nothing outlives the Moment | Fate stress · Mouse Guard disposition |
| L1 | **Deplete a pool** | subtract from a number | D&D HP · CoC Sanity |
| L2 | **Fill a track** | position on the track carries the penalty | WoD health levels · 5e exhaustion |
| L3 | **Cross a bar → name a condition** | below the bar nothing, above it a State | GURPS major wound · Mythras · Fate consequences |
| L4 | **Write a phrase into a graded slot** | severity typed, contents authored | Blades harm · Fate consequences |
| L5 | **Advance a clock** | harm is progress toward a named outcome | Apocalypse World · Ironsworn |
| L6 | **Convert to another axis** | lands on A, changes B | Lancer HP→Structure · Blades Heat→Wanted |
| L7 | **Draw on a table** | the persistent object is drawn | Rolemaster criticals · WFRP |
| L8 | **Edit a standing scalar** | harm rewrites a Capacity permanently | Delta Green adaptation cost · Twilight 2000 |
| L9 | **Harden** | harm makes you *harder* to harm on the same axis | **Unknown Armies** · Delta Green Adaptation |
| L10 | **Land on a Relationship** | the persistent effect is on a Connection, held by one participant | **Exalted 3e Intimacies** · Delta Green Bonds |
| L11 | **Bank and discharge** | accumulate off-target, convert at a bar, carry the remainder | Blades Heat · Ars Magica Reputation |

## The universal architecture is the same three stages everywhere

**Buffer → convert → name.**

| System | Buffer (evaporates) | Trigger | Named persistent thing |
|---|---|---|---|
| Fate | stress boxes | overflow | Consequence (an aspect) |
| Blades | stress 0–9 | 9th box | Trauma |
| Lancer | HP | 0 HP | Structure damage + table result |
| Delta Green | Sanity | Breaking Point | Disorder |
| Mouse Guard | disposition | 0 | Condition |
| Blades (public) | Heat 0–9 | 9 | Wanted Level +1 |

**This says the Landing Socket is not one Component but a pipeline shape:** a per-Dimension buffer whose contents are *not* durable, a declared conversion rule, and a durable Noun. It also means **the buffer belongs to the Landing Component, not the Substrate** — and it is the one place a Setting with "no Resources" quietly still has a number, but a number that never survives a Moment.

## Proposed Dimension → model mapping

| Dimension | Primary model | Precedent |
|---|---|---|
| `temperature` (bipolar) | L11 bank + L6 convert | Lancer Heat · WFRP *Ablaze* |
| `integrity` | L1 pool + L6 convert at zero | Lancer HP→Structure · Mörk Borg |
| `substance` | L8 permanent scalar edit | Twilight 2000 · GURPS DR degradation |
| `vitality` | L3 bar → named condition, read **highest** | GURPS major wound · Mythras · Ars Magica |
| `vigor` | L2 track, non-linear boxes | 5e exhaustion · GURPS FP · Ars Magica Fatigue |
| `mobility` | L3 bar → condition, exclusive within an axis | WFRP *Prone/Entangled* · Lancer *Immobilized* |
| `acuity` | L3 bar → condition | WFRP *Blinded/Deafened* · GURPS stunning |
| `composure` | L0 buffer + L6 convert at cap | Blades stress→Trauma · Fate mental stress |
| `clarity` | L3 **moving** bar + L7 table draw | **Delta Green Breaking Point** · CoC |
| `will` | **L9 harden** + L3 bar | **Unknown Armies** hardened/failed notches |
| `regard` | **L10 land on a Connection** | **Exalted 3e Intimacies** · Delta Green Bonds |
| `standing` | L11 bank and discharge | **Ars Magica Reputation** · Blades Heat |
| `working` (bipolar) | L11 bank, discharge at **both** bars | Lancer Heat (one end only) — no complete precedent |
| `essence` | L8 + L3 at zero | Ars Magica Warping · Vampire Humanity |

Three observations that came out of the mapping:

1. **Nothing in the field uses an ablative pool for a *capability* axis.** Capability harm is always a named condition, because "you have 4 of 7 sight" is meaningless. That cleanly splits our physical block into pool-then-convert (`integrity`, `vitality`) and bar-then-name (`mobility`, `acuity`).
2. **The mental block wants a two-signed axis the physical block does not.** No physical system makes you harder to injure by injuring you; every serious mental system does. Unknown Armies is the definitive model — parallel *hardened* and *failed* notch tracks, where a hardened notch at or above the incoming stress rank means you auto-pass without rolling, and five failed notches is permanent.
3. **The social block never lands on the target.** Both `regard` and `standing` land somewhere else — on a Connection, or on a public accumulator — and the target's own Facets are untouched. This is not stylistic; it is what social harm is.

## The threshold trap, and it is documented

Bar-based landing has two named failure modes:

- **"Tink-tink-boom."** Repeated harm produces no state change at all, then death all at once.
- **All-in strikes.** Mythras has 40+ special effects; players converge on exactly three — *Choose Location*, *Bypass Armour*, *Maximise Damage* — all of which exist solely to push one blow over a bar. **Threshold landing is a magnitude-concentration incentive** and players find it immediately.

The universal fix in the good systems is a **residue accumulator**: Delta Green keeps sub-Breaking-Point loss in the pool; Blades carries the Heat remainder; Ars Magica rounds *up* so any positive damage yields at least a Light wound. And Delta Green's **moving bar** — the Breaking Point resets to a new value each time it is crossed — is the single best mechanism found for having thresholds without the all-in incentive.

**Direct consequence for us:** reading a Threshold as `highest` **is** the all-in incentive; reading it as `sum` is not. Both stay, but the Landing Vocabulary should say so out loud.

## A Setting with no Resources is playable, and there is proof

**Masks: A New Generation** has five Conditions — *Afraid, Angry, Guilty, Hopeless, Insecure* — and that is the entire health system. No HP, no track, no pool. **Mouse Guard** has six. Both are well-regarded, shipping games where marking a condition *is* the damage.

What it costs: no attrition arc, condition-space saturation (Masks caps at five and then harm does nothing), and **every landing model except L1/L2/L5 must ship an explicit recovery path**, because numbers heal by default and named conditions do not.

## The hazard to write a test for

**When one axis lands two ways depending on magnitude, the landing stops being a pure function of the packet.** In Fate, two 2-shift hits produce different persistent state from one 4-shift hit. In Mythras, two blows at location HP give two Serious Wounds; one blow at 2× gives one Major Wound.

If the packet is `[vitality −7]` and the Landing has both a pool and a bar, the answer depends on **how the 7 was assembled** — which the packet no longer knows. Either the Landing reads only the packet (and therefore only one contributor-reading per Dimension), **or the Landing must be handed the contributor list, which is a Substrate finding.** Lancer has an open issue on exactly this boundary case. Worth deciding deliberately rather than discovering.

---

# 5 · Tags — for L4

## The number that matters: 222 published, ~17 always-live

Magic has **222 keyword abilities, 78 keyword actions, 69 ability words and 350 creature types** — published over 33 years without collapse. The set a player must hold in working memory is **~17 evergreen**. Mark Rosewater in 2007, at ~11: *"the number was higher than what we had but we were not far away from the limit."* It settled at ~17 and has been flat for fifteen years.

**Read: there is no cap on the total vocabulary. There is a hard cap on the always-on vocabulary, around 15–20.**

Path of Exile is the counter-warning: **46 gem tags, all mechanically live simultaneously**, and they are the source of that game's most notorious confusion. 46 live tags is already too many when every one of them gates modifiers.

**Target: 10–15 mechanically-live Tags in the Substrate seed, under 30 for the base Ruleset, then Components publish forever.**

## "A Tag never implies another Tag" — strongly validated

This is the best-supported rule in the whole set.

- MTG creature types do not imply other types. The one exception — `Wall` implying "can't attack" — was **surgically removed**: `defender` was keyworded and every prior Wall was errata'd. R&D chose to touch thousands of cards rather than keep one implication.
- PF2e's `Goblin` trait means three different things depending on host, and softly implies darkvision (*"Goblins tend to have darkvision"*). Every consumer has to special-case it.
- PF2e's `Good` implied an entire alignment subsystem. The Remaster deleted it; both vocabularies now coexist forever.
- Path of Exile's Righteous Fire is the canonical failure: it carries `Spell` and `AoE` tags, and **neither spell-damage nor area-damage modifiers affect it.** Ten years of confusion, documented on their own wiki as a warning.

**The refinement the research forces:** the rule is only enforceable if we also forbid *derivation at read time*. A Component that computes `if hasTag(Metallic) then treatAs(Conductive)` has reintroduced hierarchy in behaviour while passing the schema check. **The CI gate must be "no Tag ID appears in the definition or resolution predicate of another Tag," and the Fold must never synthesise Tag membership.** If that can be written inside a Component's `behavior.ts` with no gate firing, the gate is missing.

The cost is authoring: everything that is "metallic and therefore conductive" needs both Tags placed explicitly. That is the correct trade.

## Magnitude: declared per Tag, not optional per instance

Lancer's data is the best evidence: **67 tags, 19 carrying a value.** But the value's *type* varies per tag and is not a magnitude — `Reliable 2` is a damage floor, `Blast 2` is a radius, `Overkill 1` is a **die face**, `Recharge 5+` is a threshold, `Deadly d10` is a die size. **Nothing generic can be written over "the tag's magnitude."** And when a value changed the *shape* of a rule, Lancer forked the tag rather than parameterising it (`Loading` vs `Loading (Multiple Uses)`).

**Proposed change to our current rule:** a Tag's published schema says either "carries no magnitude" or "carries a magnitude in unit U" — permanently, from mint. Optional *per instance* means every reader writes `if (magnitude !== undefined)`, which turns "absent is not zero" into a per-call-site judgement, which is where silent divergence lives. And **comparing or summing magnitudes across two different Tag IDs should be a CI failure.**

## ID not name — validated at brutal cost by Yu-Gi-Oh

Yu-Gi-Oh's archetype membership is by **card-name substring**. The documented consequences: `Cipher Soldier` predates the "Cipher" archetype by ~16 years and is an accidental member; membership diverges between Japanese and English; Konami had to invent archetype *inclusion* and *exclusion* conditions as patch mechanisms, rename cards, and handle archetype splits across languages. The rules now consult ruby text in Japanese and have per-language grammatical-gender clauses.

Magic's `oracle_id` is the opposite and it bought two things we want: **retroactive cluster membership** (surveil and landfall were promoted in 2022 and older cards had their Oracle text updated to join) and **free renames** (the `Tribal` card type became `Kindred` at zero cost).

## Only mint a Tag when something else must reference it

Rosewater's flanking/bushido test: *flanking* **has** to be a keyword, because other cards need to say "creature without flanking." *Bushido* does not. Applied to us: **if no Modifier, Guard, Threshold or Listener will ever key on the cluster, it is documentation, not a Tag, and it should not consume an ID.**

## The Tag / Category / State boundary

Every system draws it at cardinality and closure, and it matches what the dictionary already says:

> Exactly one value true, values partition the space → **Category**.
> Any number true at once, new ones minted forever → **Tag**.
> Exactly one true within an axis, started and ended by a Verb → **State**.

`Metallic` is a Tag. `Solid/Liquid/Gaseous` is a State axis. `Humanoid` is a Category.

## Candidate seed — 11 Substrate, 13 more at base Ruleset

**Substrate seed (11)** — the ones the Substrate structurally cannot function without:

`Mass` *(magnitude)* · `Bulk` *(magnitude)* · `Hardness` *(magnitude)* · `Reach` *(magnitude)* · `Multiplicity` *(magnitude)* · `Manufactured` · `Portable` · `Anchored` · `Container` · `Consumable` · `Unique`

**Base Ruleset (13):** `Reliability` *(magnitude)* · `Volatility` *(magnitude)* · `Signature` *(magnitude)* · `Illumination` *(magnitude)* · `Living` · `Sapient` · `Metallic` · `Mineral` · `Organic` · `Fibrous` · `Flammable` · `Conductive` · `Porous`

Notes: `Flammable` is deliberately **not** derived from `Organic`, and `Conductive` deliberately not from `Metallic` — those derivations are exactly the hierarchy being forbidden. `Anchored` is not the negation of `Portable`; a thing can be neither. No creature-kind labels (`Humanoid`, `Undead`, `Beast`) — those are Categories by the cardinality test, and PF2e's `Goblin` shows the cost of filing them as Tags.

---

# 6 · Entities and Attributes — for L1, L2, L3

## The best precedent for a faction-as-character is Reign, and the best for a ship is Star Trek Adventures

**Star Trek Adventures gives ships six Systems where characters have six Attributes**, and six Departments where characters have Disciplines — deliberately parallel. The reviews are positive, but the praise is about *terminology consistency*, not simulation fidelity. And the load-bearing finding is buried in the resolution rules:

> **The ship does not act. It assists.** When characters perform functions on a ship, they roll their own stats, and an assisted roll is made for the ship that can add successes.

That is a direct answer to *"does a faction/ship/place need to be able to attempt things?"* The most-praised implementation of a ship-as-character **does not let the ship roll**. Worth taking seriously against the instinct to make everything symmetric.

## Relationship as per-participant stance — supported, but not universal

| System | Shape |
|---|---|
| Exalted 3e Intimacies | **per-holder** — the Intimacy is a Facet on the person who holds it, about a subject |
| Delta Green Bonds | **per-holder** — your bond, your number |
| Smallville / Cortex relationship dice | **per-holder** — each character rates the relationship separately |
| Monsterhearts Strings | **per-holder, directional** — I hold strings on you |
| Blades faction status | **a shared edge** — one number between two factions |

Four of five match "one Connection per participant, each stance stored independently, never an edge." Blades does not, and Blades' faction game is the part of that system most often houseruled. **Prefer the Exalted/Delta Green shape** — which is what the dictionary already says.

## Person-assumptions that leak

The recurring ones across generic systems: **initiative** (a rumour does not act), **carrying capacity** (a faction does not carry), **movement speed** (a lock does not move), **level/advancement** (a storm does not learn), and **hit points** (which the Landing research already says the Substrate should not ship).

## Candidate L2 — universal attributes

Applying the four-way test to each: *rumour · lock · faction · storm*.

| Candidate | rumour | lock | faction | storm | Verdict |
|---|---|---|---|---|---|
| identity (permanent ID) | ✓ | ✓ | ✓ | ✓ | **universal** |
| Category | ✓ | ✓ | ✓ | ✓ | **universal** |
| Tags | ✓ | ✓ | ✓ | ✓ | **universal** |
| Scale | ✓ | ✓ | ✓ | ✓ | **universal** — and Scale belongs to parts as well as wholes |
| Place / containment reference | ~ | ✓ | ~ | ✓ | **argue** — a rumour's "place" is where it is believed, a faction's is its turf; both are real but both are stretched |
| Facets (per-Component data) | ✓ | ✓ | ✓ | ✓ | **universal**, but it is structure rather than an attribute |
| the fourteen non-attempt Dimensions | ~ | ✓ | ✓ | ✓ | **argue** — a rumour has no `temperature`, but "absent is not zero" already covers that |
| the fifteen attempt Dimensions | ✗ | ✗ | ~ | ✗ | **not universal** → L3 |

**L2 looks like four or five entries.** That is brutally short, which is what the guide already predicted, and the shortness is the evidence the model is not a person schema.

## Candidate L1 — Categories that recur

`Being` · `Object` · `Place` · `Group` · `Relationship` · `Knowledge` · `Phenomenon` · `Proposal` · `Vector`

The last two are ours, not the field's — a pending vector and a Proposal are both Entities with identity, and if either needs Attributes it needs a Category.

**The test each must pass:** a Category that brings no Attributes is a Tag. `Phenomenon` (a storm, a fire, a plague) is the one I would attack first — it may be an `Object` with Tags.

---

# What this changes about the plan

1. **L31 · Timings is a new list**, and it is small — six candidates, maybe four after the argument. It comes before L1–L3 because the cost shape depends on it.
2. **L25 is now much more concrete** — the Dimension→model mapping above is a real starting position rather than a blank table.
3. **L5's decision is axes, not conditions**, and seven candidate axes are on the table.
4. **L4's seed splits into Substrate (11) and base Ruleset (13)**, with the magnitude rule tightened from "optional per instance" to "declared per Tag."
5. **L26 gets three concrete numbers**: depth limit 32, halt-and-Record at the limit, and a sort key composed only of values that do not move when unrelated content is added.
6. **L2 is four or five entries**, and the attempt Dimensions are confirmed as L3, not L2.

Two things worth attacking before they settle:

- **Whether a ship or faction may *attempt* at all.** The best precedent says no — it assists. That would be a real narrowing and it deserves a decision rather than an assumption.
- **Whether a Dimension may land two different ways depending on magnitude.** If yes, the Landing needs the contributor list and that is a Substrate finding. If no, each Dimension picks one reading and lives with it.
