# Open Questions

*Everything not yet decided, in one place, organised by when it has to be answered.*

Every question here gives: **what it is**, **why it matters**, **what is blocked by it**, **the options with their consequences**, and **a lean** where I have one. A lean is a recommendation, not a decision.

Where a question was already answered elsewhere and only *looks* open, it is not in this document. Where a question is genuinely unanswerable without playing the game, it says so.

**Five parts, in the order the answers are needed:**

| Part | | Blocks |
|---|---|---|
| **1** | Repair decisions | ~~Everything~~ — **CLOSED August 2026.** Record in `work-repair.md` |
| **2** | Decisions made while filling the lists | Phase 1 |
| **3** | Decisions needed before any code | Phase 3 |
| **4** | Decisions needed before content and launch | Phases 6–8 |
| **5** | Questions only Dylan can answer | The shape of the product and the business |

---

# Part 1 — Repair decisions — ~~OPEN~~ **CLOSED, August 2026**

**All of Part 1 is answered.** Q1.1 through Q1.5 were the four foundation findings plus the determinism set, and every one is now decided, recorded in `dictionary.md` Part 12 with its reasoning, and covered by a numeric test in `phase-0-checks.py`.

The full record of what was decided and why is **`work-repair.md`**. In one line each:

| | Was | Now |
|---|---|---|
| **Q1.1** Do whole Allocation Points survive? | Granularity waste and all-in dominance | **Yes.** Resolution is one integer operation, `⌊points × magnitude ÷ total points⌋`. All-in is answered by requiring a downside bar in authored content, not by changing the arithmetic |
| **Q1.2** What bounds standing self-scoped vectors? | Nothing | **Content pricing, not an engine limit.** R-780 reserved as insurance, unbounded in v1 |
| **Q1.3** Can an interior Channel ever be worth placing? | No — pure was 7× better | **Yes.** A universal flat Guard now acts on the packet total and is redistributed. Every direction lands the same |
| **Q1.4** Where does Enhancement Capacity clamp? | Three holes | **Percentages, and only percentages.** Absolutes are bounded by Participation Capacity instead. Baselines are percentages so the same ceiling covers them. The ceiling belongs to the task, never the source |
| **Q1.5** The determinism set | Four undeclared rules | **All four declared.** Apportionment dissolved; three rounding sites (R-400, R-750, R-1050), all truncating toward zero; Shaping is stated in points, has two forms, and runs Bonus Points → Baseline; log-integers are never added |

**One question was promoted into this phase and answered with it.** A17, crossing Scales, was ranked Medium and turned out to be Substrate: a default conversion rule now ships at R-750, and **Scale belongs to the part as well as the whole** — a Scale-4 airship has Scale-1 doors and rigging, and the Scale that applies is the Scale of the thing actually targeted.

**What is still open from this territory, deliberately:**

- **How many Allocation Points a character has, and where they come from.** Belongs to L29 and to paper play — see Q3.1.
- **Whether the Shaping order feels right.** Arithmetically arbitrary, so only play can say. On the playtest watchlist.
- **Whether the all-in authoring requirement holds at a live table.** Instrumented rather than assumed: the tooling counts tasks that ship with no downside bar.

---

# Part 2 — Decisions made while filling the lists

These are answered *by* filling the lists. They are here because each one has a trap in it worth seeing before you start.

---

## Q2.1 · What is on the Capacity list, and how many?

**The most load-bearing decision left**, because the list does two jobs: what a character is made of, *and* the axes an attempt splits across.

**The test each candidate must pass.** State it as a capacity, not a quality, then check it applies without absurdity to **a person, a ship, a faction and a storm.** *Capacity to exert force* passes. *Strength* does not.

**The trap: the number is the interface.** Eight is a choice a player makes at a glance. Twenty is a spreadsheet, and comprehension load is the one risk in this design that no amount of code can fix.

**And record what you leave off.** Nothing above the Substrate can put it back. What is deliberately absent is where the stance lives.

---

## Q2.2 · How many Dimension Spaces, and how separated?

Packets in different Spaces **never** interact. That is the main thing keeping the system comprehensible as the Component library grows — and it is also a hard wall.

**The trap.** Physical harm is obviously a Space. Social pressure probably is. But if knowledge, wealth and morale each become one, nothing can ever be traded off against anything else — a bribe cannot offset a threat. **Decide the separations you want before you decide the Spaces**, because the separations are the actual design.

---

## Q2.3 · What is on the Socket list?

Currently five: Time, Place, Resolution, Landing, Budget.

**The trap.** Every Socket is a permanent dependency for every Component ever written. An over-long list quietly rebuilds the monolith the Component design exists to prevent. **Five feels near the ceiling.** A capability belongs in a Socket only if the Substrate genuinely cannot function with it empty.

**Still undecided within it:** whether Place is really irreducible, or whether scope can be expressed generically enough that it is not a Socket at all.

---

## Q2.4 · What are the Economy Units?

The *names* a cost can be denominated in — `action` and whatever else. Substrate, because every spell ever written depends on them; the economics belong to the Budget Socket.

**The trap.** *Bonus action* is economics wearing a unit's costume. A unit names a **kind of thing being spent**. A rule about how many of them you get is not a unit.

**And one dependency:** a `repin` must name an Economy Unit as its cost. If the list is wrong, repinning is unbounded.

---

## Q2.5 · Listener cascades — three blanks

All three are still empty and the third is a determinism hazard:

1. **The depth limit.** How many rounds of Listener-triggered Verbs before it stops.
2. **The behaviour at the limit.** Lean: halt without applying the pending round and write a `cascade limit reached` Record, so the world sits at the last complete Moment.
3. **The evaluation order across simultaneously-satisfied Listeners.** This must come from a stable key in the data — proposed: `(layer, component_id, listener_id, target_entity_id)`. **Registration order is not an answer.** Get it wrong and the same Ledger folds differently on two machines.

---

## Q2.6 · The remaining aggregation operators

Settled for the resolution path: everything adds, percentages sum, nothing compounds. **Not settled** for the other Noun kinds — Tags as set union, States taking the highest within an axis, Relationships needing their own rule.

**Why it matters.** This is named in the architecture as *the single most likely source of "the same Ledger produced different state."*

---

## Q2.7 · Two small ones carried from the timing model

**A vector whose target is removed from play entirely** — not dead, but gone. Fizzle and record it, or resolve against nothing? Sounds pedantic; it is the kind of thing that crashes a replay three years in.

**Names for the four standing-vector kinds** — reactive/scheduled × durable/depleting. All four are real mechanics and none has a word.

---

## Q2.8 · Is the Verb set complete? — **the one irreversible decision**

**What it is.** L6. The closed set of operations that change state. Preliminary candidates exist in `dictionary.md` L6; none of them is committed.

**Why it is here and not in Part 1.** It cannot be answered early and it must not be. The evidence for completeness is worked examples, and worked examples come out of every other list. Settling Verbs first means settling them against imagination.

**Why it outranks everything else in this document.** Every other decision here is expensive to change. This one is *impossible* to change — a Verb is the instruction set, and the Ledger is replayed against it forever. **If exactly one question in this file gets full attention, it is this one.**

**The closing procedure.** When L1–L5, L7, L18, L21–L23 and L25–L29 are done: take every entry across those lists and every worked example produced along the way; for each, assume the fiction has already decided what happened, write only what changed in the world, then which Verbs express it. *If a consequence needs an operation not on the list, that is a real finding. If it merely needs a Tag, a Channel, or a Component formula, it is not.*

**Answered when:** a full pass over every worked example adds nothing.

---

## Q2.9 · The nine lists that are pending but not blocking

Not urgent, and listed so they are not mistaken for settled: **L10** Challenge Profile axes · **L11** Asset types · **L12** Rails binding scopes · **L13** Record types · **L19** Causal tag vocabulary · **L20** Lens tiers · **L24** Guard presets · **L26** Listener condition forms (its three blanks are Q2.5 above) · **L30** Instrumentation surfaces.

**The one with a dependency worth knowing:** L24 (Guard presets) cannot be filled until Q1.3 is answered, because a preset written against flat per-Dimension Guards is wrong if Guards become a shared pool.

---

# Part 3 — Decisions needed before any code

---

## Q3.1 · How many Allocation Points does a character have, and where do they come from?

Five is a placeholder with nothing behind it.

**The natural home is a Capacity** — *capacity to divide attention* — which makes it kind-agnostic and lets a distracted character have fewer and a practised one more. It also makes it a progression axis that **cannot inflate damage**, because points buy precision rather than power.

**Blocked by it.** Character creation, progression, the interface, and every Threshold's difficulty.

---

## Q3.2 · Is there a ceiling on summed Baseline shares?

Baselines raise total effect. Eight of them on eight Dimensions multiplies total effect several times over.

**Open:** whether the ceiling exists at all, and if it does, whether it shares Enhancement Capacity's budget or holds its own. **Related to Q1.4** and probably answered by the same decision.

---

## Q3.3 · What is the Ruleset's default policy for entering Ordered time?

**Entry is the Time Socket's decision, not the Substrate's** — three Substrate rules were tried and each failed on a real case:

- Ally/enemy labels → undefined for strangers, under the open-world rule.
- *"A Moment that doesn't exist yet"* → catches everything, since every future Moment is yet to exist.
- *"Anchored to another Entity"* → wrongly drags healing an ally into combat.

**Leading candidate:** a vector placed on an **unwilling target**, where willingness is a property of the placement — declared by content, refusable by the target's controller — and never a stored relationship label. Manual initiation always exists as well.

**The case it does not catch:** two allies racing to cut the same rope. Nobody is unwilling and ordering still matters. Manual initiation covers it, but it is worth knowing the rule is incomplete by design.

---

## Q3.4 · Does the Record shape carry `delivery` from day one?

Absent means *everyone*, so it can be added later without breaking history. **Cheap, not urgent.**

**But the coupled decision is not deferrable:** the server folds and is authoritative. If clients ever fold from Records, the first withheld Record silently diverges that client's state. Decide `delivery` whenever; decide server-side folding before the first commit.

---

## Q3.5 · What does turn position do to defensive load?

Everything pinned to your turn lands at once. So the creature that acts last in a round eats an entire round of accumulated vectors in one resolution, and the one that acts first eats almost none — a large swing, decided by initiative rather than by any decision the player made.

**This is the Time Socket's problem, which means it is swappable** — but every piece of content will be balanced against whatever the default does. Options: stagger arrivals within a round, cap arrivals per Moment, or accept it and design initiative around it.

---

## Q3.6 · Does a shared Resource permit a double-spend across simultaneous scenes?

Two scenes are simultaneous until their shared Moment. If both spend from the same faction treasury, both spends are valid in their own scene and the conflict only surfaces later.

**Participation Capacity solves the *unique object* case.** It does not solve the *divisible resource* case. This needs a rule and does not have one.

**Options:** reserve at declaration; resolve overdrafts at the shared Moment with a declared rule; or forbid cross-scene spending of shared Resources entirely.

---

# Part 4 — Decisions needed before content and launch

---

## Q4.1 · Which instrumentation surfaces ship to real tables?

Some are so good that hiding them behind a tester flag is a mistake — resolution expansion, notes, the event log. Some would ruin a scene if a player opened them mid-fight — time travel, what-if, direct state authoring.

**The interesting one is what-if.** Given to players, it is the missing learning gradient for a system whose failure mode is *"I have no idea why that didn't work."* Given to players *mid-scene*, it is a solver.

---

## Q4.2 · Is threshold visibility on or off by default?

It is a built-in GM setting, so both work. **But the default decides what the game is**, because allocating against bars you cannot see is the source of the tension — and it is also the source of the frustration.

**Untestable on paper alone.** This is a Phase 5 measurement.

---

## Q4.3 · What does a Component look like to a customer?

An expansion? A subscription tier? A class? A rules module? **The mental model determines the price point, and the price point is close to irreversible after launch.**

---

## Q4.4 · Which Asset types get user authoring, and in what order?

Every authoring surface is a real unit of work, and authorable types are what let users build without buying — which is a commercial decision as much as a technical one.

---

# Part 5 — Questions only Dylan can answer

No amount of research substitutes for these, and several of them change everything upstream.

---

## Q5.1 · Is the ruleset ever a book?

**The highest-consequence unanswered question in the project.**

If a printed or PDF core book exists as a saleable object, it inherits the entire art-cost structure *and* the single-work trademark problem — a title of a single creative work is not registrable.

If it is only ever software and web documentation, **both problems largely dissolve**, because software and games are explicitly exempt from that trademark bar.

This decides the branding strategy, the art budget, and the legal filing, and it can be answered today.

---

## Q5.2 · Can the game be played without your server?

Not *would anyone* — **can it.**

This decides whether the obsolescence objection (*"what happens to my campaign when you stop paying for hosting"*) has a structural answer or only a rhetorical one. It is an architecture decision wearing a marketing question's clothes, and the append-only Ledger plus byte-identical export is most of the answer already — if you commit to it.

---

## Q5.3 · Do you genuinely want third-party Component authors?

*Users author instances, never types* is a hard architectural line, enforced structurally.

**If it holds absolutely, there is no third-party ecosystem** — which removes the most powerful free marketing this hobby has, and reads to part of the audience as a closed platform.

**If there is a sanctioned path for a developer to author types**, then: who is eligible, what does it cost them, and what stops the type space becoming incoherent?

---

## Q5.4 · Is the brand the system, the platform, or the company — and are those one thing or three?

Three is more flexible and three times the trademark cost. One is cheaper and fuses everything to a single name.

**Everything in the naming work depends on this**, and it is executable immediately once it is answered.

---

## Q5.5 · Are you willing to be personally visible?

A named human building in public is the cheapest acquisition channel available, and the strongest counter-signal against AI-slop suspicion in a market that is currently very alert to it.

It is also exposure you may not want, and it fuses the brand to you in a way that is hard to undo.

---

## Q5.6 · Which invented words must a player hold in their head to take a turn?

You know this and I do not. **That list is the only one the jargon research applies to.** Everything else is documentation and can be as precise as you like.

The related question: **would you accept the community renaming things?** They will. If that would be intolerable, the player-facing vocabulary has to be *sayable* rather than merely correct — because sayable wins every time.

---

## Q5.7 · What happens if it works?

Three thousand people playing asynchronously, generating support load, while you have a full-time job and two young stepkids. **The failure mode here is public** — an unanswered Discord and a stale changelog is how a platform brand dies visibly.

This is worth an answer before launch, not after.

---

# The short version

**Already answered:** Q1.1 through Q1.5, plus A17. Closed in Phase 0, recorded in `work-repair.md` and `dictionary.md` Part 12, tested in `phase-0-checks.py`.

**Answer today because they change everything upstream:** Q5.1 (is it ever a book) and Q5.4 (what is the brand).

**Answer while filling the lists:** all of Part 2 — and **Q2.8 last, alone, with more care than anything else in this file.** It is the only decision here that cannot be revised at any price.

**Answer before the first commit:** Q3.1 through Q3.6, and the server-folding half of Q3.4 before anything at all.

**Answer with playtest data, not by thinking:** Q1.1's final form, Q4.1, Q4.2.
