# Categorization and Action

What five literatures have established about representing everything that can exist and everything that can be done — and what it changes about the Substrate.

Research passes: verb semantics and lexical decomposition · categories and definitions · AI planning and knowledge representation · systemic game design and parser interactive fiction · game theory and action spaces.

---

# Part 1 — The headline findings

Read these five before anything else. Each one contradicts something we had assumed.

**1. Nobody has ever succeeded at a small closed set of action primitives.** Every serious attempt either stayed small and was shown to lose information, or grew past 100 primitives once it had to actually run. Schank's Conceptual Dependency held at 11 primitive ACTs and could not reconstruct meaning. VerbNet — the largest working system — needed 153–162 semantic predicates and 39 thematic roles. Wierzbicka's Natural Semantic Metalanguage holds at 65 primes and is the only inventory with a serious universality claim, but it is a *paraphrase* metalanguage, not an execution model. Levin's classification needed 192 fine classes for 3,024 verbs.

**2. Fixed property lists across all kinds have failed independently in five fields.** Definitions by necessary-and-sufficient conditions do not exist for most concepts (Wittgenstein, Rosch, lexicography). The property list cannot be fixed in advance, because relevance is goal-dependent and any two things share unboundedly many properties. Hierarchies are not natural except at one cognitively privileged level. The periodic table is the rare success, and it works because there is a single discrete causally dominant parameter — atomic number — and even it frays at the edges.

**3. You can never enumerate all the preconditions of an action.** This is the **qualification problem**, and it is a formal result, not a practical annoyance. There is no finite list of things that must be true for "start the car" to work.

**4. The frame problem is not solved. It is legislated away.** STRIPS made state transition a *function on a set* rather than an entailment in a theory: everything not named in an action's effect is unchanged **by definition**. This is the single most important design decision in the whole planning literature, and it is what makes execution tractable. The price is that anything you failed to list silently does not happen.

**5. Interactive fiction — the field with the most direct experience of "the player types anything" — concluded that more verbs made games worse.** Inform 7 ships exactly 77 built-in actions, and **20 of those do nothing at all unless a rule intervenes.** The real machinery is not the verb list; it is the rulebook that lets any specific situation be special-cased on top of a tiny base.

---

# Part 2 — What this changes

Two of the four blocking decisions were framed wrongly. Not wrong in ambition — wrong in what they were asking.

## 2.1 The Verb set was misframed

We had been looking for a closed set of verbs that every action a player might attempt decomposes into. **That is the thing that has never worked**, and finding 1 says it won't.

But the requirement is weaker than we thought, and the weaker version is achievable:

> **The Substrate does not need to represent the action. It needs to represent the consequence.**

A player says *"I sing the guard's mother's favourite song to win him over."* The Substrate needs no concept of singing, of songs, of mothers, or of nostalgia. It needs: an attempt was made, against some difficulty, producing a Degree and a Cost, which changed a relationship value and created a piece of knowledge.

**Actions are infinite. Consequences are finite.** The Verb set is not a taxonomy of *doing* — it is a taxonomy of *state change*. That is a far smaller and far more tractable object, and it is why twelve verbs might work where twelve actions never could.

Four independent lines of evidence converge on this:

- **STRIPS** — an action formally *is* its precondition/effect pair. It has no other content. The name is a label for humans.
- **The Sims' smart objects** — objects broadcast what needs they satisfy, so the AI never needs to know what a given object *is*. The affordance is declared by the target, not known by the actor.
- **Fate's four actions** — overcome, create advantage, attack, defend. These are not actions. They are *outcome shapes*, and that is why four is enough.
- **Blades' position and effect** — a universal adjudication frame that never asks what the character is doing.

**The revised test for the Verb set** is therefore not "can I express this action" but:

> **Can I express the full consequence of this action, given that the fiction has already decided what happened?**

That is a genuinely different exercise, and most things that looked like they needed a new verb turn out not to.

## 2.2 The Noun set was misframed

We had been looking for the fine-grained values that every Entity is *built from* — an essence, decomposed. Finding 2 says that has failed everywhere it has been tried.

The frames that survived contact with the data are two, and they agree with each other:

**Homeostatic property clusters** (Boyd). A kind is not an essence — it is a set of properties that reliably co-occur because some mechanism keeps them together. There is no defining property, membership is graded, and the boundary is genuinely fuzzy. This is how biology actually works after the species problem.

**Conceptual spaces** (Gärdenfors). An entity is a point in a space of quality dimensions; a concept is a convex region in that space. Similarity is distance. Categories are not lists — they are neighbourhoods.

Both point the same way, and it is not where we were headed:

> **Do not model what a thing IS. Model what a thing AFFORDS.**

This is Gibson's affordance concept, and it also appears in the most rigorous upper ontology as the distinction between a **quality** (what a thing is like) and a **disposition** (what a thing is capable of, whether or not it is currently doing it). BFO keeps these strictly apart, and dispositions are the half that actions interact with.

A Substrate value like *capacity to exert force* is a disposition. It applies to a person, a winch, a faction, and a storm without absurdity, because it never claimed to describe what any of them *are*. A Substrate value like *Strength* is an essence claim wearing a costume, and it is why every universal system that tried it needed exceptions within a year.

**The revised question for the Noun set:**

> **What are the dimensions along which an attempt can be helped or resisted?**

That is answerable. "What is a person made of" is not.

---

# Part 3 — Findings that add machinery

## 3.1 The information-set invariant — a real bug in the Lens design

From extensive-form game theory. For any two states a player cannot distinguish, the *available action menus must be identical*:

> For all histories `h, h'` in the same information set `I`: `A(h) = A(h')`.

The reasoning is airtight. If two states a player cannot tell apart offer different menus, then the player **can** tell them apart — by looking at the menu. The game is ill-formed.

Applied to Lenses this is sharper than the rule we already had. We said a Lens never changes what a character *can do*. The invariant says something stronger: **the menu a Lens presents must not differ in a way that reveals hidden state.** A simpler Lens showing fewer options is fine only when the omitted options are omitted *unconditionally* — never when they are hidden because of something the player is not supposed to know. Otherwise the absence of an option is itself a leak.

This is testable, and it belongs in the Lens validator next to calibration.

Related: extensive-form games define the action set **as a function of history**, `A(h)`, never as a global object. The formalism's own answer to unbounded action spaces was there from the start, and it is the same shape as "the Substrate defines consequences and the fiction generates actions."

## 3.2 The qualification problem makes GM override a necessity, not a nicety

Since preconditions cannot be finitely enumerated, **there will always be attempts the system cannot adjudicate.** That is a formal guarantee, not a gap in the design.

So the GM-override-as-first-class-feature is not generosity toward human GMs. It is the required escape valve for a provably incomplete system. And the GM-less tier needs the same valve in automated form: a defined behaviour for "the fiction has produced something the rules do not cover."

Tabletop already knows this. PbtA's answer is *if you do it, you do it* — the fiction is primary and the move is only consulted when it triggers. Fate's is *say yes or roll dice*. Both are procedures for the unenumerable case.

## 3.3 The STRIPS assumption should be explicit

Make the state transition a **function on a set**, not an entailment. Everything not named in an Effect is unchanged by definition.

We had this implicitly — Effects are data, applied at Barriers. Making it explicit buys the frame problem's disappearance and costs exactly one thing, which should be written on the wall: **anything you fail to list simply does not happen, silently.** That is the failure mode to design tests around.

## 3.4 Open World versus Closed World

Description logics and OWL use the **Open World Assumption** — the absence of a fact is not its negation. Databases and Prolog use the **Closed World Assumption** with negation-as-failure.

This matters more than it sounds, because additive-only schemas and OWA are natural allies. If a Component has not said anything about an Entity's disposition toward fire, the correct reading is *unknown*, not *zero*. Under CWA, adding a new Component silently changes the meaning of every existing Record that predates it.

The Substrate needs to say which it is, once, and mean it. **The recommendation is OWA for anything a Component might later have an opinion about, and explicit presence everywhere** — never conflate absent with zero, which was already rule 4.4 and now has a formal reason behind it.

## 3.5 Basic-level categories set the granularity

Rosch's experimental result: one level of any taxonomy is cognitively privileged. *Chair* is basic; *furniture* is too abstract and *Windsor chair* too specific. Basic-level terms are learned first, named fastest, and have the shortest words. Berlin found the same structure cross-culturally in folk biology, with cultures naming roughly 500 folk genera regardless of environment.

For the Substrate this is a sizing heuristic with real evidence behind it. **The Substrate should sit one level below basic** — fine enough that basic-level concepts are compositions of it, coarse enough that a human can hold the list. And roughly 500 is the empirical ceiling on how many named kinds people carry comfortably, which is a useful number for the Component library's eventual size rather than for the Substrate.

## 3.6 The two-axis Outcome is decision-theoretically real, with a caveat

**[Research as written in Aug 2026. The two-axis Outcome it analyses was subsequently deleted — an attempt is a vector, and Cost became consequences at other Thresholds. The reasoning below is why the two-axis version would have needed a scalarization rule, which is part of why it was dropped.]**

Vector-valued payoffs are standard, and a two-dimensional outcome is coherent. What you lose relative to a scalar is **total ordering**: with Degree and Cost as independent axes, some outcomes are genuinely incomparable — more of what you wanted at more cost is neither better nor worse without a further rule.

That is a feature for drama and a problem for automation. Anything that has to *choose* between outcomes — a GM-less tier, an auto-resolving Component, an AI-driven faction — needs a declared scalarization, and it should be declared once in the Substrate rather than invented per Component.

## 3.7 What systemic games actually learned

**Multiplicative rather than additive.** Breath of the Wild's chemistry engine is the clearest statement: a small number of material properties and a small rule set, where value comes from interactions rather than from content count. Fire ignites wood; wood floats; metal conducts; metal attracts lightning. Nobody authored "burning wooden shield used as a raft."

**The object declares, the actor does not know.** The Sims' smart objects broadcast what needs they satisfy. This inversion is what makes an open action space tractable — an actor with 12 verbs meeting an object with 6 declared affordances needs no knowledge of what the object is.

**And the honest cost, from the same designers:** combinatorial testing burden and degenerate strategies. Systemic design means you cannot test the space, only sample it, and players will find the one interaction that trivialises everything. Immersive sims are famously the most expensive games per unit of content to QA.

**Dwarf Fortress** computes combat from material physics — density, sharpness, tensile strength — rather than hand-authored rules, which produces both its legendary emergent stories and its legendary absurdities.

**Ultima Online's ecology** is the tombstone on the other side: fully simulated, entirely unnoticed by players, quietly removed.

## 3.8 What tabletop already settled

**Fate's four actions** — overcome, create advantage, attack, defend — is the only widely-used complete action taxonomy in the hobby, and it works precisely because the four are outcome shapes rather than activities. Any fictional action maps to one of them by asking what the player wants to *happen*, not what the character is *doing*.

**Blades' position and effect** does the same job with two dials and never asks what the action is.

**PbtA's move-triggering problem** is the documented failure mode of the opposite approach: when moves are defined by fictional triggers, tables argue endlessly about whether a given action triggered a given move. That argument is the qualification problem arriving at a real table.

---

# Part 4 — The revised shape

Putting it together. This is a proposal, not a decision.

## 4.1 The Substrate has four kinds of thing, not one *(five until Aug 2026 — State and Resource merged into Track)*

Rather than "twenty attributes," the evidence points at five distinct kinds of Substrate value, each with different behaviour:

**Dispositions** — capacities, graded, continuous. *Capacity to exert force. Capacity to endure. Capacity to perceive. Capacity to influence.* What an attempt is resisted or assisted by. Kind-agnostic by construction, because they never claim to describe what a thing is. This is the closest thing to "attributes" and it should be small.

**Tags** — cluster membership, open, unbounded, no defining property. *Flammable. Living. Sacred. Metal. Bound-by-oath.* Homeostatic property clusters made mechanical. Tags are what Components key on, and they are the multiplicative surface — the thing that makes twelve verbs interesting.

**States** — named conditions with optional magnitude, exclusive within their own axis. Not a bag of booleans (the documented ECS failure mode), but *one field per axis*. What other rules can key on by name.

**Resources** — depletable, replenishable, with thresholds. The only genuinely numeric-over-time values.

**Relations** — first-class edges between Entities, with kind, magnitude, and direction. Every system in the entity survey stored these as a list on one endpoint, which is exactly why relationship mechanics desync in play.

The important claim: these five have **different rules for aggregation, for change, and for how a Lens renders them.** Treating them as one undifferentiated pool of numbers is what forced every previous universal system into exceptions.

## 4.2 Verbs are state-change operations, not activities

Re-read against the reframe, the candidate set looks better than it did — and the gaps are different than expected.

Roughly the operations needed are: **create · destroy · move · alter a magnitude · transfer between holders · set or clear a state · add or remove a tag · form or break a relation · reveal or conceal · bind a consequence to a future condition · advance a clock**.

Notice what is *not* there: nothing about attacking, persuading, crafting, climbing, or singing. Those are fictional descriptions of attempts. The Substrate sees only what changed.

**The revised twenty-operation test** should therefore be run on *consequences*, and the interesting cases are the ones where a fictional action has a consequence that seems to need a new operation. Those are the real findings.

## 4.3 The action pipeline

What the research collectively suggests, end to end:

```
1. FICTION       A player says what they want to do. Unbounded. Natural language.
2. FRAMING       Someone — GM, or the module's script, or a default —
                 decides what is actually at stake. This step is provably
                 unautomatable in general (qualification problem).
3. RESISTANCE    Which Dispositions assist, which resist, what Tags apply.
                 Difficulty is assembled here, from Substrate values.
4. RESOLUTION    A Component produces a canonical Outcome: Degree and Cost.
   [SUPERSEDED Aug 2026 — an attempt is a vector; see dictionary.md Part 2C]
                 The Lens shows the player whatever dice it likes; the
                 probability is the Substrate's.
5. CONSEQUENCE   Effects, composed of Verbs, applied at a Barrier in Layer
                 order. Everything not named is unchanged, by definition.
6. RENDERING     Each participant's Lens narrates what happened at their
                 own granularity, including what it cannot show.
```

Only steps 3–5 are Substrate. Step 1 is unbounded and always will be. Step 2 is the human, or an explicit default. Step 6 is presentation.

**That division is the answer to "a player can attempt anything."** The Substrate never needed to contain the actions. It needed to contain what actions can *change*.

---

# Part 5 — What to be suspicious of

Honest counterweights to everything above.

**Systemic design is the most expensive thing to test that games have.** Multiplicative interactions mean the state space cannot be enumerated, only sampled, and degenerate strategies are found by players within days. Every immersive sim is a QA nightmare, and they have studios.

**Simulation without perception is worthless** — Ultima Online's ecology. If a Substrate distinction never reaches any Lens, it does not exist for players and it is pure cost.

**The 500-genus finding cuts against large Component libraries** as much as it supports a modest Substrate. People carry a few hundred named kinds comfortably. A catalogue in the thousands is a search problem, not a richness win.

**Fate's four actions are complete because Fate is coarse.** The taxonomy holds up because the resolution beneath it is deliberately abstract; a system with a finer Outcome space may find four insufficient in exactly the places the extra resolution was meant to serve.

**And the honest one about decomposition itself:** the standard objection in linguistics is that decomposition never quite reconstructs the original meaning. "Kill" is not "cause to become not alive." If the Substrate is a decomposition of consequence, expect to keep discovering that a specific consequence has a residue the primitives cannot carry. Tags are the pressure valve for that, and they will absorb more than they look like they should.
