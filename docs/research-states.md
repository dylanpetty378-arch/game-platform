Research complete. Here is the report.

---

# STATUS EFFECT / CONDITION SYSTEM DESIGN — SURVEY AND FINDINGS

---

## 1. D&D 5e (2014) — 15 conditions, binary, no intrinsic duration

**The list** ([SRD Appendix A](https://dnd5e.info/appendices/appendix-ph-a-conditions/), [D&D Beyond](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/appendix-a-conditions)): blinded, charmed, deafened, exhaustion, frightened, grappled, incapacitated, invisible, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious.

Three structural facts matter more than the list:

- **Strictly binary.** "A creature either has a condition or doesn't" — multiple instances of the same condition don't worsen it. Exhaustion is the sole exception, and it is not really a condition (§9).
- **No intrinsic duration.** A 5e condition has no timer of its own. It ends because the *effect that imposed it* ends, or because a named action ends it (grappled: "ends if the grappler is incapacitated or the creature is removed from reach"). **This is your design already, shipping in the most-played RPG in the world.**
- **Implication cascade.** Paralyzed, stunned and unconscious all *include* incapacitated. 2024 tightened this: incapacitated now also breaks concentration and blocks speech, "effects that cascade to paralyzed, stunned, and unconscious" ([MakeMythic](https://makemythic.com/blog/dnd-2024-conditions-cheat-sheet/)). One condition definitionally implies another.

**Deliberate shrink from 4e.** Merric Blackman's contemporaneous analysis ([merricb.com](https://merricb.com/2014/07/04/basic-dd-changes-to-conditions/)): 5e "reduced conditions from sixteen to thirteen," dropping *dying* and *weakened* as formal conditions, and dropping *incorporeal* and *intoxicated* (the latter repackaged into poisoned). Against 3e/PF1's "at least 34 conditions," 5e consolidated to 13 + exhaustion. The stated reason is that conditions "provide a useful shorthand" — the value is in the *reference count*, not the coverage.

**2024 revision** ([Roll20 2024 compendium](https://roll20.net/compendium/dnd5e/Rules:Conditions), [Arcane Eye](https://arcaneeye.com/mechanic-overview/exhaustion-5e/), [Gaming Nexus](https://www.gamingnexus.com/News/65272/)): list still 15, but exhaustion's six bespoke tiers were replaced by a single linear formula (−2 per level to every d20 test, −5 ft speed per level, death at 6, −1 per long rest). **A numeric condition with per-level hand-authored effects was refactored into magnitude × coefficient + a threshold.** That is the single most useful data point in this whole survey for your Substrate.

---

## 2. D&D 4e — 16 conditions, three duration models, and the documented tracking failure

**The list** ([4e crib sheet](https://www.kassoon.com/dnd/crib-sheet/), corroborated by [EN World compiled list](https://www.enworld.org/threads/compiled-conditions-list-updated-reformatted.220368/)): blinded, dazed, deafened, dominated, dying, helpless, immobilized, marked, petrified, prone, restrained, slowed, stunned, surprised, unconscious, weakened. Rules Compendium adds insubstantial, ongoing damage, grabbed.

**Durations** ([D&D4 Wiki](https://dnd4.fandom.com/wiki/Durations), [Conditions](https://dnd4.fandom.com/wiki/Conditions)) — the crucial part. 4e is the system that made duration a *first-class typed field*:
- **End of your next turn / start of your next turn** — the workhorse, sub-round.
- **Save ends** — roll d20 at the end of your turn, 10+ removes it. One roll *per save-ends effect*, so N conditions = N rolls.
- **Until the end of the encounter** — a coarse boundary.
- **Sustain (minor/move/standard)** — requires the source to spend action economy every round to keep it alive.

"Most conditions are short term, usually lasting for a turn or until ended by a save, but some conditions last until the end of the encounter or even longer."

**The community verdict is unambiguous and it is about tracking, not about the conditions themselves.** From the Angry GM's 4e retrospective comments ([theangrygm.com](https://theangrygm.com/reflecting-on-dd-4e/)): at higher levels, "because of all the tracking of status conditions… everyone was tossing status conditions around and most of them had a 'Until end of next turn' duration," and the problem was not just remembering "what creature had the effect, but also **who put it there**." On EN World ([when status effects annoy the players](https://www.enworld.org/threads/when-status-effects-annoy-the-players.275325/)): "They had the same annoyances with keeping track of things like marks, hunter's quarry, etc… It felt more like being an **accountant** at times, than a player."

Two engineering lessons, both directly actionable:
1. **The killer was not count-per-entity, it was (count × attribution × per-turn resolution).** Every save-ends condition is a per-turn dice event; every mark is a directed edge to a specific source.
2. **"Who put it there" is a required field.** 4e's *marked* is not a property of the marked creature — it is a property of the *pair*. So is *dominated*.

---

## 3. Pathfinder 2e — ~42 conditions, numeric values, three distinct interaction rules

This is the most carefully engineered condition system in tabletop, and the one closest to what you're building. Get the exact rules; they are load-bearing.

### 3a. The three rules, verbatim

From the ORC SRD ([pf2orc.d20pfsrd.com](https://pf2orc.d20pfsrd.com/rules/home/gamemastering/conditions/), matching [Archives of Nethys](https://2e.aonprd.com/Rules.aspx?ID=774) and the [Remaster appendix](https://2e.aonprd.com/Rules.aspx?ID=2455)):

> **Condition Values.** "Some conditions have a number after the condition, called a condition value. This value conveys the severity of a condition, and such conditions often give you a bonus or penalty equal to their value."

> **Redundant Conditions.** "You can have a given condition only once at a time. If an effect would impose a condition you already have, you now have that condition for the longer of the two durations."

> **Redundant Conditions with Values.** "Conditions with different values are considered different conditions. If you're affected by a condition with a value multiple times, **you apply only the highest value**, although you might have to **track both durations** if one has a lower value but lasts longer."

> **Overriding Conditions** ([AoN ID 2457](https://2e.aonprd.com/Rules.aspx?ID=2457)). "Some conditions override others. This is always specified in the entry for the overriding condition. When this happens, all effects of the overridden condition are **suppressed** until the overriding condition ends. **The overridden condition's duration continues to elapse, and it might run out while suppressed.**"

**These are three different mechanisms and your "exclusive within an axis" only covers one of them.** See §11, finding C — this is the most important structural gap I found in your design.

### 3b. Numeric-valued conditions

Eleven carry values ([pf2calc](https://pf2calc.com/conditions/), [AoN conditions](https://2e.aonprd.com/Conditions.aspx)): clumsy, doomed, drained, enfeebled, frightened, persistent damage, sickened, slowed, stunned, stupefied, wounded.

- **Frightened** is the archetypal self-decaying magnitude: "You take a status penalty equal to this value to all your checks and DCs. **Unless specified otherwise, at the end of each of your turns, the value of your frightened condition decreases by 1.**" Note the escape hatch — "unless specified otherwise" — so the decay is a *default* on the definition, overridable per application.
- **Clumsy / enfeebled / stupefied / drained** are Dex/Str/mental/Con penalties equal to value. **Sickened** penalizes all checks. These have zero content beyond "a number that penalizes a category."
- **Slowed** N: "reduce the number of actions regained by your slowed value." **Stunned** N: same, but "**Stunned overrides slowed.** If the duration of your stunned condition ends while you are slowed, you count the actions lost to the stunned condition toward those lost to being slowed." That is an explicit ordered-override with carry-over accounting.

### 3c. No declared maximum, and the resulting confusion

Paizo's own forum thread on condition values ([paizo.com/threads/rzs42zr5](https://paizo.com/threads/rzs42zr5?Condition-values=)): players widely believed values cap at 4; they do not. "Most abilities that inflict these conditions specifically say they max out at −4," but there is **no core-rules cap**. The cap exists "primarily within individual ability descriptions rather than as core rulebook limitations, creating a **soft cap through design practice** rather than explicit mechanics." Designers avoid high values because they become absurd — high frightened destroys DCs, high slowed removes turns entirely.

**Take-higher saves them.** Because PF2 is take-higher rather than add, the effective ceiling is "the largest value any single source can apply," so the missing cap never actually detonates. Under an *add* rule the same omission would be catastrophic (§7).

### 3d. Condition groups — PF2's answer to having ~42 conditions

Six named groups ([Remaster appendix](https://2e.aonprd.com/Rules.aspx?ID=2455)):

| Group | Members | Exclusive? |
|---|---|---|
| Degrees of Detection | observed, hidden, undetected, unnoticed | Yes, ordered, **per-observer** |
| Senses | blinded, concealed, dazzled, deafened, invisible | Partially (blinded/dazzled ordered) |
| Death and Dying | doomed, dying, unconscious, wounded | No — these co-hold and interact |
| Attitudes | hostile, unfriendly, indifferent, friendly, helpful | Yes, ordered, **per-observer** |
| Lowered Abilities | clumsy, drained, enfeebled, stupefied | No — independent axes |
| Action Modification | quickened, slowed, stunned | Effectively (stunned overrides slowed) |

**Detection and attitude are explicitly relative, not properties of the entity.** From the detection rules ([AoN ID 2414](https://2e.aonprd.com/Rules.aspx?ID=2414)): "With the exception of invisible, these conditions are **relative to the viewer** — it's possible for a creature to be observed to you but hidden from your ally." Invisible is the exception precisely because it *is* an absolute property of the creature.

**This is your Relationship Noun, not your State Noun.** More in §11 finding B.

### 3e. Dying / wounded / doomed — the death track

From [AoN ID 376](https://2e.aonprd.com/Rules.aspx?ID=376):
- **Dying** N: "If this value ever reaches dying 4, you die." Recovery check at start of turn each round. Increases by 1 on taking damage while dying.
- **Wounded** N: "Anytime you lose the dying condition, you become wounded 1 if you didn't already have the wounded condition. If you already have the wounded condition, your wounded condition value instead increases by 1." And: "If you gain the dying condition while wounded, **increase the dying condition's value by your wounded value**."
- **Doomed** N: "The maximum dying value at which you die is **reduced by your doomed value**." Decreases by 1 per full night's rest.

Decompose it in your vocabulary: **dying** = a Resource with a Threshold at 4. **wounded** = a persistent Modifier on the *initial value* of that Resource. **doomed** = a Modifier on the *Threshold itself*. Not one of the three is a State. §9.

### 3f. Persistent damage — a recurring vector, not a state

"You are taking damage from an ongoing effect… After taking damage, roll a **DC 15 flat check** to see if you recover." A magnitude, a Moment cadence, and a stochastic end condition. In your model: a vector pinned to a repeating Moment with a Listener that ends it on a check — not a State at all.

---

## 4. Lancer — the removability split

Lancer separates **statuses** from **conditions**, and the distinguishing property is *not* thematic.

- **Statuses** (9) ([lancer.wiki.gg/Status](https://lancer.wiki.gg/wiki/Status)): Danger Zone, Down and Out, Engaged, Exposed, Hidden, Intangible, Invisible, Prone, Shut Down.
- **Conditions** (7) ([lancer.wiki.gg/Condition](https://lancer.wiki.gg/wiki/Condition)): Immobilized, Impaired, Jammed, Lock On, Shredded, Slowed, Stunned.

The rule: "There are 7 conditions in Lancer; other things can go wrong with your mech, but none of them qualify as a condition, and hence, for example, **can't be cleared with `stabilize`**."

**The split exists solely to define the domain of one removal action.** It is a `removable_by` flag on the definition, promoted to a taxonomy. The wiki itself notes several effects behave like statuses but lack the designation "due to a rules oversight" — evidence that promoting a flag to a type creates classification debt.

Note also **Engaged**: a Lancer status that is inherently about a *pair* of mechs. Same shape as 4e *marked*.

---

## 5. Gloomhaven — sign split, one instance, refresh-on-reapply

([Gloomhaven rules, m-ender compilation](https://github.com/m-ender/gloomhaven-rules); [Dized](https://rules.dized.com/game/I7lEsCGOS2-zgol-ZRNf3g/daYNJBtBTXSv0t6Gbcc87w/conditions))

- **Negative:** poison, wound, immobilize, disarm, stun, muddle, curse.
- **Positive:** invisible, strengthen, bless.

**The stacking rule, verbatim:** "**Only one of each condition type may be applied to any single figure at a time, however conditions can be reapplied to refresh their duration.**"

Duration model: most expire "at the end of its next turn" (token removed). Poison and wound are the exceptions — they persist **until removed by a Heal ability**. Curse/bless are token-in-deck: they self-consume on draw.

Three findings:
1. **Refresh-on-reapply** is the fourth stacking model, distinct from take-higher/add/refuse. Cheap and bounded.
2. The **positive/negative split is a required field**, because abilities say "remove all negative conditions." You need a valence to select on.
3. Poison and wound (the "until healed" ones) are exactly your "never expires unless ended" model — **and Gloomhaven ships an explicit removal channel (Heal) for exactly those two.** The design pairs the persistence with the remover.

---

## 6. Digital systems

### 6a. WoW — diminishing returns are exclusivity axes with a decay rule

([Warcraft Wiki](https://warcraft.wiki.gg/wiki/Diminishing_returns), [Wowpedia](https://wowpedia.fandom.com/wiki/Diminishing_returns), [Maxroll](https://maxroll.gg/wow/resources/crowd-control-diminishing-returns))

**DR categories:** roots, stuns, incapacitates, disorients, silences, knockbacks, disarms. "**Effects within the same category share diminishing returns.**"

**Schedule:** first application full duration; a second within 18s → 50% duration; third → 25%; then **immune to all effects in that category** for 18s. The 18s window measures from the *end* of the previous duration.

Your intuition in the brief is exactly right: **a DR category is an exclusivity axis whose members share a resistance counter.** The axis carries state (the DR level and its expiry) that no individual member owns. If you ship axes, the axis is an addressable object with its own Facet potential — not just a validation constraint.

### 6b. WoW — the debuff slot cap is the documented unbounded-list failure

([Vanilla WoW Archive: Debuff](https://vanilla-wow-archive.fandom.com/wiki/Debuff), [Blizzard forums](https://us.forums.blizzard.com/en/wow/t/debuff-limit-on-classic-servers/8693))

Vanilla capped a target at **8 debuff slots**, raised to 16 in patch 1.7.0, 40 in TBC, then removed. When full, **new debuffs displaced old ones** — a raid-critical Sunder Armor could be knocked off by "a Hunter's weak Serpent Sting DoT." Blizzard's fix (announced Feb 2006, live in 1.11.0) was a **priority system** preventing weaker debuffs from displacing stronger ones; the cap itself was eventually deleted.

**The lesson is precise: a hard numeric cap on simultaneous conditions is the wrong control.** It converts "too many conditions" into non-deterministic silent loss of the *important* ones. The correct control is structural (exclusivity axes) or priority-ordered, not a count limit.

### 6c. WoW — pandemic: the bounded refresh

([Maxroll: Pandemic](https://maxroll.gg/wow/resources/pandemic), [Ask Mr. Robot](https://blog.askmrrobot.com/how-wow-works-periodic-damage-and-healing-dots-and-hots/))

Refreshing a DoT adds the remaining duration to the new one, **capped at 130% of base duration**. Refresh-with-add, plus a hard cap, because uncapped duration-add was exploitable. Same lesson as §7: any additive combination ships with a declared maximum or it breaks.

### 6d. League of Legends — CC as a capability matrix, not a ladder

([Types of Crowd Control](https://wiki.leagueoflegends.com/en-us/Types_of_Crowd_Control), [Summary matrix](https://wiki.leagueoflegends.com/en-us/Types_of_Crowd_Control/Summary))

Three top categories — **disables**, **displacements**, **movement impairment** — but the operative document is a **matrix of CC type × blocked capability**: movement / basic attacks / abilities / interrupts channels / summoner spells / affected by tenacity.

| Type | Move | Attack | Abilities |
|---|---|---|---|
| Stun, Sleep, Airborne, Stasis, Suppression | ✗ | ✗ | ✗ |
| Root | ✗ | ✓ | partial |
| Silence | ✓ | ✓ | ✗ |
| Disarm | ✓ | ✗ | ✓ |
| Polymorph | ✓ | ✗ | ✗ |
| Blind | ✓ | miss | ✓ |
| Slow / Drowsy | reduced | ✓ | ✓ |
| Cripple | ✓ | reduced | ✓ |
| Ground | partial | ✓ | partial |
| Nearsight | ✓ | partial | partial |

Plus a **cleansability tier**: Suppression and Stasis cannot be removed by ordinary cleanses (Suppression only by Quicksilver), and Tenacity — which shortens most CC — does not touch Stasis, Suppression or Kinematics.

**Two findings.** (i) The blocked-capability set is *not* one ordered axis; root and silence block disjoint things and legitimately co-hold. Don't force capability gating into a single axis. (ii) "Which removal tools can touch this" is a first-class field in the most-tuned CC system in the industry — same conclusion as Lancer's stabilize split, arrived at independently.

### 6e. Slay the Spire — the cleanest formal statement of the two stacking models

([Debuffs](https://slaythespire.wiki.gg/wiki/Debuffs), [Buffs](https://slaythespire.wiki.gg/wiki/Buffs))

Every power is typed by **stack semantics**:
- **Duration** — stack count *is* remaining turns; decrements 1 at end of turn. Vulnerable, Weak, Frail, Blur, Lock-On, No Block.
- **Intensity** — stack count is potency; persists for the combat. Strength, Dexterity, Focus, Plated Armor, Strength Down, Choked.
- **Counter** — decrements on an event, not on a clock. Double Tap, Burst.

Reapplication **adds stacks** in all cases. Caps are explicit and per-power: Strength/Focus −999…999, Plated Armor 0…999, everything else at the integer limit. A few (Confusion, Entangled) are declared non-stacking.

**Poison and Regen are both intensity *and* duration simultaneously** — "Poison is the ONLY Debuff with both Intensity and Duration stack types": deal N damage, then decrement N by 1. **A single scalar cannot represent both magnitude and remaining time.** If you allow only one magnitude per State, you cannot express poison; you need magnitude and a separate decay/counter, or you must model it as a recurring vector (which is what PF2 does with persistent damage).

### 6f. Guild Wars 2 — the two models named, with caps, and the suppression queue

([GW2 Wiki: Effect stacking](https://wiki.guildwars2.com/wiki/Effect_stacking))

- **Stacking intensity (vertical):** "Each application of an intensity-stacking effect applies and expires **independently of and simultaneously with** other applications." Bleeding, Vulnerability, Might.
- **Stacking duration (horizontal):** "Applications of duration-stacking effects apply **sequentially and only one application is effective at a given time**." Crucially: "**the source with the greatest intensity will be used up first**," and when it expires the next-strongest resumes with its remaining duration.
- **Caps, mandatory:** Might / Stability / Vulnerability 25; most intensity effects 1,500; general boons 5.

**GW2's duration-stacking queue is structurally identical to PF2's overriding-conditions suppression.** Two systems designed a decade apart and in different genres converged on: *keep the losers, suppress them, let the strongest be active, let their clocks keep running.* That convergence is the strongest single signal in this survey (§11, finding C).

---

## 7. Take-higher vs add — the evidence

| Model | Systems | Bounded by construction? | Cap shipped? | Cost |
|---|---|---|---|---|
| **Take-higher** | PF2 (values), WoW (strongest aura of a category), GW2 duration-stacking | **Yes** — ceiling = strongest single source | Not needed; PF2 ships none and survives | Must track multiple durations |
| **Add** | Slay the Spire, GW2 intensity, WoW stacks, WoW pandemic (duration) | **No** | **Always, in every case** — 25 / 999 / 1500 / 130% | Unbounded without a cap; cap is mandatory |
| **Refresh duration** | Gloomhaven, WoW pre-pandemic | Yes (magnitude), no (duration) | Pandemic added a 130% cap | Loses granularity; encourages spam |
| **Refuse / one instance** | Daggerheart, 5e (binary), StS Confusion/Entangled | Yes trivially | n/a | No granularity at all |

**The evidence is one-directional.** Every additive system in the survey ships a hard cap, and the two documented failure modes come from additive systems without adequate ones: WoW's pandemic (uncapped duration-add), and PF2's *absence* of a rules cap on values ([Paizo thread](https://paizo.com/threads/rzs42zr5?Condition-values=)), which is survivable only because PF2 is take-higher. No take-higher system in the survey has a stacking blowup.

**The cost of take-higher is stated explicitly by the only system that uses it in tabletop:** "you might have to **track both durations** if one has a lower value but lasts longer." That is not a bug, it is the honest price — and it is *the same data structure* as the suppression stack in §6f and §3a. Take-higher and override-suppression want the identical implementation.

For your engine, the CI gate writes itself:

> A State definition whose `combine` policy is `add` and which does not declare a `max` **fails to load.** `take_higher` needs no `max` and may not declare one (the ceiling is derived).

The article-length treatment ([Game Developer, "A Status Effect Stacking Algorithm"](https://www.gamedeveloper.com/design/a-status-effect-stacking-algorithm)) reaches a compatible conclusion for real-time games: match the **highest potency** and adjust duration to conserve total potency×duration, explicitly rejecting matching-highest-duration ("makes additional hits appear to *weaken* effects"), averaging, and raw potency-increase ("introduces unpredictability and exploitation risk"). Its stated benefit is perceptual monotonicity: "the player won't see enemies speeding up when hit by a slow spell." **Take-higher on magnitude is the choice that makes reapplication never look like a downgrade** — worth preserving in your Lens calibration.

---

## 8. How many is too many

| System | Count | Direction |
|---|---|---|
| Daggerheart | **3** standard (Hidden, Restrained, Vulnerable) + temporary/special classes | Deliberate minimum |
| Lancer | 7 conditions + 9 statuses = 16 | — |
| Draw Steel | **9** (bleeding, dazed, frightened, grabbed, prone, restrained, slowed, taunted, weakened) | Deliberate shrink |
| Gloomhaven | 10 | — |
| 5e (2014 & 2024) | **15** | Shrank from 4e's 16 |
| 4e | 16 core + Rules Compendium additions | — |
| 3e / PF1 | ~34 | — |
| PF2 | ~39–42 | **Grew** — but bought tractability with groups + uniform value semantics |

([Daggerheart SRD](https://daggerheartsrd.com/rules/conditions/), [Steel Compendium](https://steelcompendium.io/v2/Browse/condition/), [merricb](https://merricb.com/2014/07/04/basic-dd-changes-to-conditions/), [pf2calc](https://pf2calc.com/conditions/))

**The count is not the variable that predicts pain.** PF2 has ~2.6× 5e's condition count and does not generate 4e's complaints. What differs:

1. PF2 conditions are **grouped** into six named sets with declared interactions. 4e's sixteen were a flat namespace.
2. PF2's durations are mostly **coarse** (until the end of the encounter, until you rest, until a specific action). 4e's were mostly **per-turn** with a per-turn die roll each.
3. PF2 uses **one uniform value semantics** across eleven conditions, so learning one teaches eleven. 4e's conditions each had bespoke text.

Corroborating complaints ([EN World: when status effects annoy the players](https://www.enworld.org/threads/when-status-effects-annoy-the-players.275325/), [Rating the 4e conditions](https://www.enworld.org/threads/rating-the-4e-conditions.250319/), [4E Conditions](https://www.enworld.org/threads/4e-conditions.274341/)): the two named pains are (a) accounting overhead and (b) *action denial* — "miss your turn" conditions. Also: severity is **not** globally rankable — "Marked by itself would be weighted higher on a battlemind… less on a swordmage… and would be absolutely useless on a fighter." **Do not put a global severity number on a State definition.** Severity is a function of the target's Facets, not of the State.

**Conclusion for you: budget axes, not conditions.** A per-entity ceiling of ~10–16 simultaneous *distinguishable* states is where systems live; PF2 stays comfortable at 42 definitions because exclusivity holds the live count down.

---

## 9. Conditions that are actually a Resource or a track in disguise

This is a long list, and it is the highest-leverage section for your Noun boundaries.

| Real system's "condition" | What it actually is |
|---|---|
| **5e exhaustion (2014)**, six bespoke tiers | A Resource with a Threshold at 6 and a per-level effect table — **and WotC refactored it in 2024** into magnitude × coefficient (−2 d20, −5 ft per level) + Threshold. Direct vendor admission. |
| **PF2 dying** N | A Resource, 0–4, with a death Threshold |
| **PF2 wounded** N | A persistent Modifier on the *initial value* of the dying Resource — a scar counter |
| **PF2 doomed** N | A Modifier on the dying **Threshold** itself |
| **PF2 clumsy / enfeebled / stupefied / drained / sickened / frightened** | Modifiers with a magnitude and a scope. Their entire content is "penalty equal to value on category X" |
| **PF2 slowed / quickened / stunned** N | Modifiers on the action-economy Budget (an Economy Unit, in your terms) |
| **PF2 persistent damage** | A vector pinned to a recurring Moment, ended by a stochastic Listener |
| **4e ongoing damage** | Same |
| **4e marked**, **Lancer engaged**, **4e dominated** | **Relationships** — a Connection per participant |
| **PF2 detection group** (observed/hidden/undetected/unnoticed) | **Relationship** — explicitly "relative to the viewer" |
| **PF2 attitude group** (hostile…helpful) | **Relationship** with an ordinal magnitude on the Connection |
| **Gloomhaven wound** | Recurring vector at start of turn |
| **Gloomhaven poison** | Modifier on incoming attacks (+1 Attack for enemies) |
| **Gloomhaven curse / bless** | A Resource-in-a-deck; self-consuming |
| **StS Strength / Dexterity / Focus / Plated Armor** | Modifiers with integer magnitude |
| **StS Vulnerable / Weak / Frail** | Modifier + a countdown Resource fused into one integer |
| **GW2 might / vulnerability** | Stacked Modifiers with a declared cap |
| **LoL slow / cripple / nearsight** | Modifiers on movement speed / attack speed / vision range |
| **Blades in the Dark harm** ([bladesinthedark.com](https://bladesinthedark.com/consequences-harm)) | A track of slots by severity tier (lesser 1 / moderate 2 / severe 3 / fatal 4) with **overflow**: "If you need to mark a harm level, but the row is already filled, the harm moves up to the next row above" |

**The discriminating test.** A thing deserves to be a **State** when it changes what is *legal* — it occupies an axis slot and gates Verb classes. It is a **Modifier** when its whole content is a number applied to a category. It is a **Resource** when it accumulates toward a Threshold. It is a **Relationship** when its truth depends on *whose* perspective you take.

By that test, of PF2's ~42 "conditions": roughly a dozen are true States (prone, grabbed, restrained, immobilized, blinded, deafened, paralyzed, unconscious, petrified, invisible, confused, controlled, fleeing, fascinated, broken), eleven are Modifiers, nine are Relationships (detection + attitudes), three or four are Resources, and one is a recurring vector. **PF2's condition list is four Nouns wearing one Noun's clothes.** You already have the four Nouns. Don't let States absorb the other three.

---

## 10. CANDIDATE AXIS LIST

Criteria applied: (a) genuinely mutually exclusive — at most one member holds; (b) recurs in ≥3 surveyed systems; (c) the exclusion is *semantic*, not a balance patch; (d) it survives the §9 test — it changes legality, not just numbers. Marked **BASE** where it is plausibly true in all Settings ("If it is true in all of them, it is base Ruleset"), **COMPONENT** otherwise.

### Tier 1 — ship these; the evidence is overwhelming

**A1. POSTURE** — *standing (default) / kneeling / prone / supine* — **BASE**
Present in 5e, 4e, PF2, Lancer, Draw Steel, Gloomhaven-adjacent, LoL (knockdown). Genuinely exclusive: nothing is prone and standing. Has a natural default member, which is important — an axis with a default is *never absent*, which sits well with rule 8b ("absent is not zero"). Recovery is universally an explicit action (4e: standing is a move action; Draw Steel: the Stand Up maneuver).

**A2. RESTRAINT** — *free (default) / engaged / grabbed / restrained / immobilised / bound* — **BASE**, ordered
PF2 states the ordering as a rule: "**Restrained overrides grabbed.**" 5e distinguishes grappled from restrained. Lancer has immobilized; LoL has root; WoW has a whole DR category for roots. This axis is **ordered by severity and needs suppression, not replacement** — grabbed must survive underneath restrained and can outlive it.

**A3. RESPONSIVENESS / CONSCIOUSNESS** — *alert (default) / dazed / stunned / unconscious* — **BASE**, ordered
PF2 states the ordering: "**Stunned overrides slowed**," with explicit carry-over accounting for lost actions. 4e's severity thread ranked exactly this ladder: dazed < stunned < unconscious < helpless. 5e's incapacitated → paralyzed/stunned/unconscious cascade is the same axis with implication. LoL's stun/sleep/suppression/stasis cluster all block everything.
**Caveat:** 4e community consensus was that these are the *least fun* conditions in play ("miss your turn"). That is a Ruleset-content warning, not a Substrate one, but worth recording.

**A4. VITAL STATE** — *hale (default) / dying / dead* — **BASE**, ordered, **Resource-backed**
Universally present, universally implemented as a Threshold on a Resource rather than as a plain State (PF2 dying 0–4; 5e death saves; Blades' fatal row). The axis is the *observable* projection of the Resource. Model the Resource as the truth and the axis membership as a derived Lens/Threshold reading — do not store both.

**A5. VISION (self's own sight)** — *sighted (default) / dazzled / blinded* — **BASE**, ordered
PF2 dazzled and blinded are graded degrees of one thing. 5e blinded, 4e blinded, Gloomhaven muddle (a cousin), LoL blind. Clean single axis.

**A6. HEARING** — *hearing (default) / deafened* — **BASE**
Two-member axis. Boring, universal, and cheap. 5e, 4e, PF2 all ship it.

**A7. COMMUNICATION / SIGNAL** — *open (default) / silenced / jammed* — **COMPONENT**
Lancer jammed, LoL silence, WoW silences DR category, 5e's silence spell (notably *not* a 5e condition, which is a gap 5e is criticised for). Not universal enough for base — a Setting with no verbal magic and no comms doesn't need it. **Note your dictionary already rules that silence is a State, not a Channel (rule 17c) — this is that axis.**

**A8. MATERIAL STATE** — *corporeal (default) / insubstantial / intangible / petrified* — **COMPONENT**
4e insubstantial + petrified, Lancer intangible, 5e petrified, LoL stasis. Exclusive and clearly one axis. Not universal (many Settings have no ghosts and no basilisks).

### Tier 2 — real axes, but they are Relationships, not States

These are exclusive **per (subject, observer) pair**, not per entity. PF2 says so in the rules text. Under your dictionary these are Categories of Entity holding one Connection per participant, each stance stored independently — **never an edge**. Which is exactly right: A can be hidden from B while observed by C.

**A9. DETECTION** — *observed / concealed-to-them / hidden / undetected / unnoticed* — **Relationship**, ordered
PF2: "these conditions are relative to the viewer — it's possible for a creature to be observed to you but hidden from your ally." **With one exception: `invisible` is absolute** and is therefore a genuine State on its own two-member axis (visible/invisible). PF2 carves out exactly that exception. Copy the carve-out.

**A10. ATTITUDE** — *hostile / unfriendly / indifferent / friendly / helpful* — **Relationship** with ordinal magnitude
PF2's cleanest ordered exclusive set. Five members, one holds, directional.

**A11. THREAT BINDING** — *unmarked / marked-by-X / taunted-by-X / engaged-with-X* — **Relationship**
4e marked, Draw Steel taunted, Lancer engaged, LoL taunt. **This is the exact thing 4e players complained they couldn't track** — "not only remember what creature had the effect, but also who put it there." That complaint is a schema complaint: they were storing a directed fact in an undirected slot.

**A12. VOLITION** — *self-directed (default) / fascinated-by-X / frightened-of-X / compelled-toward-X / compelled-away-from-X / controlled-by-X* — **Relationship**, ordered
PF2 fascinated/fleeing/confused/controlled, 5e charmed/frightened, 4e dominated, LoL charm/taunt/flee/berserk. Every member names a source. PF2's frightened is the interesting hybrid: it carries a *magnitude* (a penalty) as well as a *source*. So the Connection needs a magnitude too — which your Relationship Noun already permits ("each stance stored independently").

### Tier 3 — reject these as axes; they are something else

**R1. Capability gating** (disarmed / silenced / can't-cast / can't-use-items). **Not one axis.** The LoL matrix proves it: root and silence block disjoint capabilities and legitimately co-hold; disarm and silence are orthogonal; polymorph is their conjunction. Model as **independent binary gates per Verb class**, or as Guards on Verb legality — not as members of a shared axis. (A7 above is the one sliver of this that *is* exclusive, because silenced and jammed are degrees of the same blockage.)

**R2. Action economy rate** (hasted / normal / slowed / stunned). Tempting, and PF2 groups quickened/slowed/stunned. But quickened and slowed are opposite *signs of one magnitude* on the action Budget, not two axis members — this is your bipolar-Dimension pattern, and your Budget Socket already owns it. Stunned belongs on A3.

**R3. Lowered abilities** (clumsy / enfeebled / drained / stupefied). PF2 groups them for pedagogy only; they are four independent Modifiers that co-hold freely. **A group is not an axis.** Do not let PF2's presentation mislead you here.

**R4. Encumbrance / fatigue / exhaustion.** A Resource with Thresholds. See §9.

**R5. Valence** (positive / negative). Gloomhaven's split and Lancer's stabilize set both need it, but it is a **field on the definition** used to *select* States for bulk removal — it is orthogonal to every axis. Not an axis.

### Sizing

Tier 1 gives **8 State axes** (6 base, 2 component). Tier 2 gives **4 Relationship axes**. Under strict per-axis exclusivity, an entity's maximum simultaneous State count is 8 — before any one-member axes that Components add. **That is the structural answer to "how does the list not grow forever."** See §11 finding E.

---

## 11. CROSS-CUTTING FINDINGS

### A. A well-designed condition definition — the field list

Synthesised from PF2's rules text, StS's stack typing, GW2's stacking taxonomy, Lancer's removability split, Gloomhaven's valence, and 4e's attribution failure. Fields marked ⚠ are the ones a system was documented to have *suffered from omitting*.

**Identity**
- `id` — permanent integer, never reused (your rule 5)
- `name` — display only, never an identifier (PF2 Tags-by-ID discipline applies here too)
- `edition` / `component_version` — pinned

**Placement**
- `axis_id` — **required, never nullable.** A State with no natural axis gets a private one-member axis. Making it non-nullable is what makes the "at most one per axis" invariant checkable without a special case.
- `rank_within_axis` — integer, total order. Drives override. PF2 needs it ("restrained overrides grabbed", "stunned overrides slowed"); GW2 needs it ("the source with the greatest intensity will be used up first").
- `on_conflict` — `replace` | `suppress_lower` | `refuse`. **Three values, because PF2 demonstrably uses all three.** Default `suppress_lower` (see finding C).

**Magnitude**
- `has_magnitude` — explicit boolean (your rule 8b: absent is not zero, explicit presence on every field)
- `min` / `max` — `max` **required when `combine = add`**, **forbidden when `combine = take_higher`**
- `combine` — `take_higher` (default) | `add` | `refuse`. Evidence in §7.
- ⚠ `magnitude_semantics` — `intensity` | `countdown`. StS proves one scalar can't be both (poison is the only power that is both, and it needs two). If you allow only one magnitude, Poison-shaped effects must be modelled as a recurring vector instead, which is what PF2 does. **Decide explicitly; don't let it emerge.**

**Provenance** ⚠
- `source_entity_id` — required. Not optional. 4e's single loudest complaint was inability to answer "who put it there," and it is required to *author* the end condition: 5e grappled "ends if the grappler is incapacitated"; PF2 frightened is frightened *of* something.
- `origin_vector_id` — the vector that placed it, for the Resolution Record

**Duration and end** ⚠
- `end_listeners` — a **non-empty** set of Listener conditions. Under "never expires unless ended," an empty set is a permanent State, and permanent States should be *declared*, not accidental. **Make empty a load-time error unless `permanent: true` is set explicitly.** This is the single most valuable CI gate for your design.
- `decay` — optional `{ delta, at_moment }`. PF2 frightened is `{-1, end_of_own_turn}`. **Implement as a Listener producing a class-`Triggered` Verb, not as engine-special duration logic** — otherwise it violates your own "only ended by a Verb" invariant silently.
- `suppressed_clock_runs` — boolean. PF2: "The overridden condition's duration continues to elapse, and **it might run out while suppressed**." Non-obvious and easy to get wrong.

**Removal** ⚠
- `valence` — `beneficial` | `harmful` | `neutral`. Needed by "remove all negative conditions" (Gloomhaven) and by Lens presentation.
- `removal_class` — which removal Verbs may target it. Lancer's stabilize set and LoL's cleanse tiers (Suppression: Quicksilver only; Stasis: nothing) are the same field arrived at independently. Not a separate Noun kind — a field.

**Effects**
- `modifiers` / `guards` / `thresholds` — declarative references only, Tier 0. **No free-form "what it does."**
- ⚠ `implied_states` — 5e (incapacitated cascade) and PF2 (unconscious "you have the blinded and off-guard conditions") both need this. **This collides with your dictionary: "Tag … never implies another Tag."** See finding F.

**Not a field**
- `severity` — do not. Community consensus is emphatic that severity is a function of the target ("a fighter and a wizard losing opportunity attacks are not equivalent").

### B. Detection, attitude, threat and volition are Relationships — resist the pull

PF2 is the only tabletop system that says this out loud, and it says it as a rule: "these conditions are **relative to the viewer**." Every other system that put these in the condition list generated tracking complaints (4e marked). **~9 of PF2's 42 conditions are misfiled**, and PF2 gets away with it only because a human GM does the filing.

You have a Relationship Noun that stores one Connection per participant, each stance independent, explicitly never an edge. That is precisely the right shape for detection and attitude. **Rule you can enforce:** if a State's meaning requires the phrase "…to you" or "…of X" or "…by X," it is a Relationship. Test the whole base list against that sentence.

The exception PF2 carves out is instructive and worth copying verbatim: `invisible` is absolute (a property of the creature) while `hidden` is relative. So the same fictional situation splits across two Nouns, correctly.

### C. Your model is missing SUPPRESSION, and this is the significant gap

You have "exclusive within an axis." Two independently designed systems say exclusivity must **retain the loser**:

- **PF2:** "all effects of the overridden condition are **suppressed** until the overriding condition ends. The overridden condition's duration continues to elapse, and it might run out while suppressed."
- **GW2 duration-stacking:** applications queue; "the source with the greatest intensity will be used up first"; when it expires "the next-strongest resumes with its remaining duration."

If your axis rule *removes* the loser on application, you lose the PF2 grabbed-under-restrained case: when the restraint ends, the grab should still be there if its own end condition hasn't fired. This is not an edge case — it is the normal behaviour of every grapple chain in play.

**Recommendation:** an axis holds an **ordered set**, of which exactly one member is *active* (highest `rank_within_axis`, ties broken by your deterministic sort). Non-active members are retained, their end Listeners still armed, their clocks still running. `on_conflict = replace` becomes the *special* case (correct for detection and attitude, where the loser is meaningless), not the default.

**This also unifies with take-higher.** PF2's "you might have to track both durations if one has a lower value but lasts longer" is the *same data structure*: an ordered set of applications, highest active, lower ones retained with independent end conditions. Take-higher on magnitude and suppress-lower on axis membership are one mechanism, not two. That is a real Substrate simplification.

### D. Take-higher, with add as an opt-in that requires a declared max

§7. Every additive system ships a cap; no take-higher system needed one. Take-higher additionally gives perceptual monotonicity (reapplication never looks like a downgrade), which matters for your Calibrated Lens requirement (rule 19).

**CI gates:** `combine = add` without `max` fails to load. `combine = take_higher` with `max` fails to load (the ceiling is derived, and declaring it invites drift).

### E. "Never expires unless explicitly ended" is viable — it is 5e — but it needs four companions

**Precedent is strong.** 5e conditions have no intrinsic duration at all; they end because the imposing effect ends or a named action ends them. Gloomhaven's poison and wound persist until a Heal. PF2's drained/wounded/doomed persist until rest. StS Powers persist until combat ends. The model is well-attested.

**What must exist alongside it, all four:**

1. **A mandatory, non-empty end-Listener set at application time** (unless `permanent: true` is explicit). This is what makes "never expires" a *statement* rather than an *oversight*. Under your dictionary, "Listener … the only way consequence propagates" already implies this; make it a load-time check.
2. **Coarse-grained sweep Moments with Ruleset-level Listeners.** Every surveyed system has at least one: 4e end-of-encounter, 5e long rest, PF2 daily preparations, Gloomhaven end-of-scenario, StS end-of-combat. These are the garbage collector. **Without them the list grows monotonically and nothing in your architecture stops it.** Ship `encounter_end`, `rest`, `session_end` as base Moments with sweep Listeners selectable by `valence` and `removal_class`.
3. **Provenance on every State** (finding A), because a large fraction of real end conditions reference the source.
4. **Universal axis membership** (finding E-2 below) as the *structural* bound.

**Do not solve growth with a count cap.** WoW's 8/16 debuff limit is the documented failure: hitting the cap silently displaced the *important* debuffs with trivial ones, Blizzard patched it with a priority rule in 1.11.0, and eventually deleted the cap entirely. A count cap converts a bookkeeping problem into a correctness problem.

**E-2. The structural bound.** Require every State to belong to a declared axis (nullable-never), and publish the axis list per Edition as a closed set. Then **the maximum number of simultaneous active States on an Entity is exactly the axis count** — 8 in the Tier-1 list above, plus one per Component-declared one-member axis. Growth becomes a *published, reviewable, additive-only* quantity rather than an emergent one. That falls straight out of the exclusivity rule you already have; you just have to make axis membership mandatory to get it.

### F. `implied_states` collides with your Tag rule — flag it

Your dictionary says a Tag "never implies another Tag." Every surveyed system has States that imply other States: 5e paralyzed/stunned/unconscious all include incapacitated; PF2 unconscious "you have the blinded and off-guard conditions"; PF2 prone "you are off-guard"; PF2 paralyzed "you have the off-guard condition."

Three ways out, and you should pick one deliberately rather than discover it:
- (i) **Materialise.** Applying unconscious also emits separate blinded and off-guard States with provenance pointing at the unconscious. Honest, auditable, additive; costs N extra Records per application and requires cascade removal on end.
- (ii) **Derive.** Never store implied States; Thresholds and Guards read the axis directly (`if RESPONSIVENESS ≥ unconscious then …`). Cheapest, and consistent with "the server folds"; costs every rule author having to know the transitive closure.
- (iii) **Forbid**, and require Ruleset content to state the full set explicitly at every application site. Purest; guarantees content bloat and drift.

**(ii) is the best fit for your architecture** — it keeps the Ledger clean, needs no cascade, and reduces to an ordered comparison on an axis, which you already have from `rank_within_axis`. But it means axis rank is semantically load-bearing, not just a tie-break, and that deserves to be written down before the first Component is built.

### G. Duration models ranked by bookkeeping cost (evidence-backed)

1. **Until explicitly ended** (5e, your design) — zero per-turn cost, zero rolls. Cost moves entirely to (a) remembering it's there and (b) having a remover. **Lowest measured load.**
2. **Coarse boundary** (encounter end, rest) — one sweep per boundary. Nearly free.
3. **Countdown magnitude** (PF2 frightened −1/turn, StS duration stacks) — one integer decrement at a known Moment, no roll, and it is **self-terminating**, so it cannot leak. Excellent middle ground and the reason PF2 tolerates 42 conditions.
4. **End of next turn** (4e) — cheap individually, but 4e's failure shows it scales badly by *count × attribution*.
5. **Save ends** (4e) — a die roll per condition per turn. **Documented worst.** This is the mechanic behind "it felt more like being an accountant than a player."

**PF2's frightened is the sweet spot and you can express it natively:** magnitude + a Listener at `end_of_own_turn` emitting a class-`Triggered` decrement Verb, which removes the State when it hits zero. Self-ending, deterministic, no roll, no engine special case, and it satisfies "only ended by a Verb" literally. **I'd make that the canonical worked example in your SPEC.**

### H. Exclusivity axes carry their own state — WoW's DR proves it

WoW's DR is a *category-level* counter with an expiry, shared by all members. Nothing in the individual condition owns it. If you build axes as mere validation constraints, you can't express diminishing returns, escalating resistance, or "third application this scene fails." **Make the axis an Entity, so a Component can hang a Facet on it.** That costs nothing now and is impossible to retrofit under additive-only.

### I. Two things I could not resolve, flagged rather than guessed

- **Slay the Spire's Poison** is the only surveyed effect that is genuinely intensity *and* duration in one scalar. Your `has_magnitude` + optional `max` cannot represent it as a State; it has to become a recurring vector (PF2's persistent-damage shape). That is probably correct, but it means **some real-world "conditions" are not States in your model at all**, and content authors will reach for the wrong Noun. Worth an explicit note in the dictionary.
- **4e's `sustain (minor/move/standard)`** duration — a condition kept alive by the *source* spending action economy each round. That is a State whose continued existence depends on a recurring Verb from a *different* Entity than the one it sits on. It is expressible with a Listener plus a Budget spend, but it's the one duration model in the survey that doesn't fall out of your Moment/Listener machinery cleanly, and per your "when something doesn't fit" rule I'm flagging it rather than papering over it.

---

## Sources

**D&D 5e / 2024**
- [Appendix PH-A: Conditions — 5e SRD](https://dnd5e.info/appendices/appendix-ph-a-conditions/)
- [Appendix A: Conditions — D&D Beyond Basic Rules](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/appendix-a-conditions)
- [Conditions — Roll20 5e Compendium](https://roll20.net/compendium/dnd5e/Conditions)
- [Conditions — Roll20 D&D 2024 Compendium](https://roll20.net/compendium/dnd5e/Rules:Conditions)
- [D&D 2024 Conditions Cheat Sheet — MakeMythic](https://makemythic.com/blog/dnd-2024-conditions-cheat-sheet/)
- [Exhaustion in D&D 5e (updated for 2024) — Arcane Eye](https://arcaneeye.com/mechanic-overview/exhaustion-5e/)
- [The old Exhaustion chart… — Gaming Nexus](https://www.gamingnexus.com/News/65272/The-old-Exhaustion-chart-could-kill-you2c-but-the-new-Exhaustion-in-the-DD-2024-Players-Handbook-makes-more-sense-as-it-kills-you)
- [Basic D&D: Changes to Conditions — Merric's Musings](https://merricb.com/2014/07/04/basic-dd-changes-to-conditions/)
- [D&D Basic: Combat and Conditions — Brandes Stoddard](https://www.brandesstoddard.com/2014/07/dd-basic-combat-and-conditions/)

**D&D 4e**
- [Conditions — D&D4 Wiki](https://dnd4.fandom.com/wiki/Conditions)
- [Durations — D&D4 Wiki](https://dnd4.fandom.com/wiki/Durations)
- [D&D 4e Combat Crib Sheet — Kassoon](https://www.kassoon.com/dnd/crib-sheet/)
- [Compiled Conditions List — EN World](https://www.enworld.org/threads/compiled-conditions-list-updated-reformatted.220368/)
- [Rating the 4e conditions — EN World](https://www.enworld.org/threads/rating-the-4e-conditions.250319/)
- [4E Conditions — EN World](https://www.enworld.org/threads/4e-conditions.274341/)
- [When status effects annoy the players — EN World](https://www.enworld.org/threads/when-status-effects-annoy-the-players.275325/)
- [Stacking same condition (save ends) — EN World](https://www.enworld.org/threads/stacking-same-condition-save-ends.252726/)
- [Reflecting on D&D 4E — The Angry GM](https://theangrygm.com/reflecting-on-dd-4e/)
- [Condition Tracker — Dungeon's Master](https://dungeonsmaster.com/2009/07/condition-tracker/amp/)
- [For D&D, how many 'Condition' effects is too many? — The Gaming Den](http://www.tgdmb.com/phpBB3/viewtopic.php?t=53063)

**Pathfinder 2e**
- [Conditions — Archives of Nethys (Rules ID 774)](https://2e.aonprd.com/Rules.aspx?ID=774)
- [Conditions Appendix (Remaster) — AoN ID 2455](https://2e.aonprd.com/Rules.aspx?ID=2455)
- [Condition Values — AoN ID 775](https://2e.aonprd.com/Rules.aspx?ID=775)
- [Overriding Conditions — AoN ID 2457](https://2e.aonprd.com/Rules.aspx?ID=2457)
- [Conditions Related to Death and Dying — AoN ID 376](https://2e.aonprd.com/Rules.aspx?ID=376)
- [Detecting Creatures — AoN ID 2414](https://2e.aonprd.com/Rules.aspx?ID=2414)
- [Conditions list — Archives of Nethys](https://2e.aonprd.com/Conditions.aspx)
- [Conditions — PF2 ORC SRD (verbatim Redundant/Overriding text)](https://pf2orc.d20pfsrd.com/rules/home/gamemastering/conditions/)
- [Conditions — PF2 SRD](https://pf2.d20pfsrd.com/rules/conditions/)
- [PF2e Conditions Reference (39 conditions, grouped) — pf2calc](https://pf2calc.com/conditions/)
- [Condition values — Paizo forums](https://paizo.com/threads/rzs42zr5?Condition-values=)
- [Pathfinder 2e: How Frightened & Other Conditions Work — CBR](https://www.cbr.com/pathfinder-2e-frightened-conditions-dnd/)

**Other tabletop**
- [Status — LANCER Wiki](https://lancer.wiki.gg/wiki/Status)
- [Condition — LANCER Wiki](https://lancer.wiki.gg/wiki/Condition)
- [Gloomhaven rules (unofficial searchable) — m-ender/gloomhaven-rules](https://github.com/m-ender/gloomhaven-rules)
- [Gloomhaven Conditions — Dized](https://rules.dized.com/game/I7lEsCGOS2-zgol-ZRNf3g/daYNJBtBTXSv0t6Gbcc87w/conditions)
- [Conditions and Effects — Gloomhaven Wiki](https://gloomhaven.fandom.com/wiki/Conditions_and_Effects)
- [Conditions — Daggerheart SRD](https://daggerheartsrd.com/rules/conditions/)
- [Conditions — Steel Compendium (Draw Steel)](https://steelcompendium.io/v2/Browse/condition/)
- [Consequences & Harm — Blades in the Dark](https://bladesinthedark.com/consequences-harm)
- [Harm in Blades in the Dark — The Walking Mind](https://walkingmind.evilhat.com/2017/12/11/harm-in-blades-in-the-dark/)

**Digital**
- [Diminishing returns — Warcraft Wiki](https://warcraft.wiki.gg/wiki/Diminishing_returns)
- [Diminishing returns — Wowpedia](https://wowpedia.fandom.com/wiki/Diminishing_returns)
- [Crowd Control Diminishing Returns — Maxroll](https://maxroll.gg/wow/resources/crowd-control-diminishing-returns)
- [Debuff (vanilla debuff limit) — Vanilla WoW Archive](https://vanilla-wow-archive.fandom.com/wiki/Debuff)
- [Debuff Limit on Classic Servers — Blizzard forums](https://us.forums.blizzard.com/en/wow/t/debuff-limit-on-classic-servers/8693)
- [Pandemic — Maxroll](https://maxroll.gg/wow/resources/pandemic)
- [How WoW Works: Periodic Damage and Healing — Ask Mr. Robot](https://blog.askmrrobot.com/how-wow-works-periodic-damage-and-healing-dots-and-hots/)
- [Types of Crowd Control — League of Legends Wiki](https://wiki.leagueoflegends.com/en-us/Types_of_Crowd_Control)
- [Types of Crowd Control / Summary matrix — LoL Wiki](https://wiki.leagueoflegends.com/en-us/Types_of_Crowd_Control/Summary)
- [Debuffs — Slay the Spire Wiki](https://slaythespire.wiki.gg/wiki/Debuffs)
- [Buffs — Slay the Spire Wiki](https://slaythespire.wiki.gg/wiki/Buffs)
- [Effect stacking — Guild Wars 2 Wiki](https://wiki.guildwars2.com/wiki/Effect_stacking)

**Design writing**
- [A Status Effect Stacking Algorithm — Game Developer](https://www.gamedeveloper.com/design/a-status-effect-stacking-algorithm)
- [RPG Status Effect and Cooldown Architecture](https://salivity.github.io/game-development/article/rpg-status-effect-and-cooldown-architecture)
- [Status Effects (Buffs/Debuffs) in an ECS Architecture — GameDev.net](https://www.gamedev.net/forums/topic/692150-status-effects-buffs-debuffs-in-an-ecs-architecture/)
- [Status effect — Wikipedia](https://en.wikipedia.org/wiki/Status_effect)
- [Mind Control, Stun, and Fire, Oh My! — Wayward Strategy](https://waywardstrategy.com/2024/03/20/mind-control-stun-and-fire-oh-my-a-discussion-about-status-effects-in-real-time-strategy-games/)agentId: a90a0de5e53785806 (use SendMessage with to: 'a90a0de5e53785806', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 120545
tool_uses: 88
duration_ms: 725475</usage>