# Phase 1 · The Lists — the working guide

*Companion to `substrate-lists.xlsx`. **Phase 0 closed in August 2026, so this is startable now.***

The workbook has the tabs and the columns. This has **what each list is actually deciding, the test an entry has to pass, how to know the list is finished, and the mistake that is easy to make in it.**

> **The workbook is no longer blank.** Every blocking tab opens with **PROPOSED rows on a pale yellow background** — a starting position to react to, not an answer. Each also has a **CONSIDERED AND REJECTED** block already seeded with things I think should be cut, and why.
>
> **Do one of three things with every proposed row: accept it, edit it, or cut it.** Cutting is the most valuable of the three, and a row you cut belongs in the rejected block with a reason — not deleted.

---

## Before starting anything

**Three habits, and they matter more than any individual list.**

**Write down what you leave off.** Every list has a "considered and rejected" that is as important as the list itself. Nothing above the Substrate can put back something the Substrate omitted, and in two years you will not remember whether something is missing because you decided against it or because you never thought of it. Use the last rows of each tab.

**Count the jargon as you go.** Every entry that introduces a word is a word a player has to meet. Keep a running total and a first-contact budget — the number a new player meets in their first hour. Research says a glossary does not repair this; only meeting fewer words does.

**Attack each list when you think it is done.** Not review it — attack it. Find the degenerate entry, the one that dominates, the one nobody will ever pick. That is what found the four foundation findings that open Phase 0.

---

## The order, and why

Each list needs the one before it. Doing them out of order means doing some of them twice.

```
L21  Dimension Spaces      ── which kinds of push can meet each other at all
 ↓
L29  Capacities            ── which ARE the Dimensions of the attempt Space
 ↓
L22  Dimensions            ── the axes inside the remaining Spaces
 ↓
L23  Channels              ── named directions placed in those Spaces
 ↓
L27  Sockets ── L28 Economy Units      ── what content is allowed to name
 ↓
L1 ── L2 ── L3             ── Categories, Universal, Category Attributes
                              (and the three character sheets)
 ↓
L4 Tags ── L5 States ── L18 Aggregation ── L25 Conversions
 ↓
L7   the lattice outside resolution
 ↓
L26  Listener conditions, the cascade limit, the evaluation order
 ↓
L6   VERBS — last
```

**L21 before L29 is the one that looks backwards.** The Capacities *are* the Dimensions of the attempt Space, so you cannot fill them until you know that Space exists and what it is for. Deciding the Spaces is a coarse, quick decision; deciding the Capacities is not.

---

# L21 · Dimension Spaces

**Deciding:** which kinds of push can meet each other. Packets in different Spaces **never** interact — that is the wall keeping the system comprehensible as it grows.

**The test.** For any two Spaces, ask: *should a thing in A ever offset a thing in B?* If yes, they are one Space. If no, they are two, forever.

**The mistake, and it is the real work.** Decide the **separations you want** before you decide the Spaces. Physical harm is obviously one. Social pressure probably is. But if wealth, morale and knowledge each become their own, then **a bribe can never offset a threat** — and that might be exactly right, or it might be the thing that makes the game feel like four unrelated games.

**Done when:** you can name, for every pair of Spaces, a concrete situation where you *wanted* them to interact and are content that they cannot.

---

# L29 · Capacities

**Deciding:** what a character is made of, *and* the axes an attempt splits across. One list, two jobs — which is what makes it the most load-bearing item in the project.

**The test, per candidate.** State it as a *capacity to do something*, never as a quality. Then check it applies without absurdity to **a person, a ship, a faction and a storm.**

```
capacity to exert force        person ✓   ship ✓   faction ✓   storm ✓   → keep
strength                       person ✓   ship ~   faction ✗   storm ✗   → cut
capacity to notice             person ✓   ship ✓   faction ✓   storm ✗   → argue about it
```

Three out of four is the interesting case. Either the fourth reveals the Capacity is really about people, or it reveals the storm needs a Category that supplies it.

**How many.** Eight is a choice a player makes at a glance. Twelve is manageable. Twenty is a spreadsheet, and comprehension load is the risk in this design that no amount of code can fix. **Twelve is the working ceiling. If you are at thirteen and still adding, something on the list is really two things or really a Tag.**

**The mistake.** One Capacity per skill. *Thieves' tools* is not a Capacity — it is gear supplying a modifier to `manipulation`. If a candidate is something you *own* or something you *learned*, it is a Tag or an item, not a Capacity.

**Done when:** every entry passes four-way, the count is twelve or fewer, the rejected list is longer than the kept list, and you can hand someone the list and have them allocate points across it without asking what anything means.

**Proposed in the workbook:** eight — *exert force, endure, move, notice, manipulate, persist, sway, conceal*. Three of them (`notice`, `manipulate`, `sway`) fail the four-way test on a storm or a ship, and they are proposed deliberately, because that is the argument worth having. Seeded as rejected: strength, intelligence, lockpicking, charisma, luck.

---

# L22 · Dimensions, per Space

**Deciding:** the axes inside each Space. Positive and negative both mean something.

**The test.** A Dimension is real if there is a *pair of opposites* worth having cancel. `thermal` earns its place because heat and cold should meet. A Dimension with no meaningful negative is probably a Tag.

**Free to be wrong about, in one direction.** Dimensions are additive-only — a Component may add one forever, unspecified defaults to zero, and nothing that exists breaks. So a **missing** Dimension is recoverable. A Dimension that turns out to be two things is not.

**The mistake.** Too many, too early. Each one widens every vector in the system.

**Done when:** each Dimension has a stated positive and negative meaning, and no two Dimensions in a Space are describing the same opposition.

---

# L23 · Named Channels

**Deciding:** the named directions content actually uses. `fire`, `cold`, `force`.

**The test, and it is arithmetic.** Absolute values must sum to **exactly 1**. That is why lightning is `0.3 / 0.7` and not `1 / 1` — it makes magnitude mean the same thing for every Channel.

**Check every row.** The workbook has a column for the absolute sum. It should read 1.0 on every line.

**The good news.** Placing a Channel determines its relationship to every other Channel automatically, and **a Channel added in ten years is correct against every one that already exists**, with no consistency check possible to fail. This is the list you can be most relaxed about extending later.

**The thing Phase 0 unblocked.** Interior Channels used to be strictly worse than axis-aligned ones — against armour 3, an even four-way split at full magnitude landed *nothing*. A3 fixed it: a universal flat Guard now acts on the packet total, once per contributing source, so every direction lands the same. **Place interior Channels freely.**

**Done when:** every row sums to 1, transient/persistent is marked on each, and at least three interior Channels exist and are worth using.

**Proposed in the workbook:** nine — `fire`, `frost`, `impact`, `lightning` (0.3/0.7), `venom`, `acid` (0.7/0.3), `scalding steam` (0.6/0.4), `intimidation`, `appeal`. Three sit in the interior on purpose, because that is the property the whole Dimension Space idea rests on.

---

# L27 · Sockets

**Deciding:** which holes the Substrate declares and cannot fill. Currently five: Time, Place, Resolution, Landing, Budget.

**The test.** *Can the Substrate function with this empty?* If yes, it is not a Socket — it is an ordinary Component. If no, it is a Socket and it is a permanent dependency for every Component ever written.

**Each entry needs both halves.** The **Vocabulary** — the names content may depend on, additive-only. And the **Behaviour** — everything else, which content never names. Without the split, swapping an occupant breaks every spell ever written.

**The mistake.** Adding a sixth. Every Socket is permanent weight, and an over-long list quietly rebuilds the monolith the Component design exists to prevent. **Five feels near the ceiling.**

**Worth genuinely questioning:** is `Place` irreducible, or can scope be expressed generically enough that it is not a Socket at all?

**Done when:** each of the five has a Vocabulary anyone could write content against, and you have tried and failed to remove one.

---

# L28 · Economy Units

**Deciding:** the *names* a cost can be denominated in. Substrate, because every spell ever written depends on them.

**The test.** A unit names **a kind of thing being spent.** A rule about *how many you get* is not a unit — it belongs to the Budget Socket occupant.

```
action           a kind of thing spent          → unit
reaction         a kind of thing spent          → probably a unit
bonus action     a rule about how many          → not a unit
```

**One hard dependency.** A `repin` must name an Economy Unit as its cost. If the list is wrong, repinning is unbounded and Ordered time can be held open forever.

**Done when:** three to six entries, each unambiguously a *kind of thing* rather than a rule, and a repin has something to name.

---

# L1 · Categories, L2 · Universal Attributes, L3 · Category Attributes

**Deciding:** what kinds of thing exist, what every Entity has, and what each kind adds.

**Do them in that order, and do L2 second.** Universal Attributes are the ones **every** Entity has. Test each candidate against a rumour, a lock, a faction and a storm. If any of those does not need it, it is a Category Attribute and belongs in L3.

**The mistake in L1.** A Category that brings no Attributes is a Tag. If `haunted` adds nothing to the sheet, it is not a Category.

**The mistake in L2.** Putting anything in it that only people need. L2 should be brutally short — possibly three or four entries.

**Done when:** the three character sheets (below) can be written entirely from L1–L3 plus L29.

---

## The three character sheets — do these alongside L1–L3

**Write the character sheet first**, at the most detailed Lens you can imagine. What is printed on it is what has to exist underneath.

Then write one for **a ship** and one for **a faction**.

The values all three need are the Capacity set. **The values only a person needs are the test** — if there are many, the Substrate is a person schema in a costume, and L29 needs redoing.

---

# L4 · Tags and L5 · State axes

**L4 is the seed vocabulary** Components may rely on existing. Keep it under thirty. Six are proposed, including `armoured` carrying its Guard value as a Tag magnitude — worth deciding early, because if that pattern is right then a great deal of gear becomes Tags rather than Facets. Tags carry an **optional magnitude**, are identified by **ID not name**, and **never imply other Tags**.

**L5 is the shape, not the contents.** Most States live in Components. What is being decided here is the axes the base Ruleset ships, and the fields a State definition carries — name, axis, whether it has a magnitude, and an **optional maximum**.

**The mistake in L5.** Forgetting the max. Values add by default, so without a ceiling `poisoned 47` is reachable.

---

# L18 · Aggregation operators

**Deciding:** how multiple contributions to one value combine, for the Noun kinds outside the resolution path.

Settled already: everything on the resolution path adds, percentages sum, nothing compounds. **Proposed in the workbook:** `max` for States and Baselines, `union` for Tags, `clamp` for Resources — and for Relationships the rule is **never merge**, each participant's stance standing alone, which is the whole reason a Relationship is a Category of Entity rather than an edge.

**Why this one deserves care.** It is named in the architecture as *the single most likely source of "the same Ledger produced different state."*

**The test.** For each operator, apply it to the same three inputs in six different orders. Any operator that gives different answers is wrong.

---

# L25 · Transient-to-Persistent conversions

**Deciding:** what a vector that survives Guards actually does. This is the Landing Socket's Vocabulary.

**Without it, vectors arrive and nothing happens.** This is the list that connects the whole arithmetic to anything a player cares about.

**The mistake.** Assuming health. A Setting may legitimately have none — the Substrate ships no Resources. The list is *what persistent state each Dimension can address*, and health is one answer among several.

---

# L7 · The lattice outside resolution

**Deciding:** the ordering slots for progression, economy, movement, knowledge and social standing. The resolution region is already drafted.

**The test that produced the drafted region, and should produce the rest.** Take a mechanic you want. Write out what must already be settled before it can be computed. If no existing slot supplies it, that is a new slot.

**Err high.** Gaps of 100 so 650 can be inserted. An unused slot costs nothing; a missing one is a foundation break.

---

# L26 · Listener condition forms

**Deciding:** the closed set of things a Listener may watch. **State, never Verbs** — *is this now true*, never *did that just happen*.

**Three blanks that must be filled here, not later:**

1. The cascade **depth limit**.
2. The **behaviour at the limit** — lean: halt without applying, and record it.
3. The **evaluation order** when several Listeners fire at once. This must come from a stable key in the data. **Registration order is not an answer** — get it wrong and the same Ledger folds differently on two machines.

Seven condition forms are proposed, including *a Resolution Record exists matching a shape* — which is how reflection and retribution work without any Listener ever watching an event.

---

# L6 · Verbs — LAST

**Deciding:** the closed set of operations that change state. **The one genuinely irreversible decision in the system.**

**Do not start this until everything above is done.** Every list above produces worked examples, and those examples are the only real evidence of completeness. Settling Verbs first means settling them against imagination.

**The closing procedure.** Take every entry from every other list, plus every worked example produced along the way. For each: *assume the fiction has already decided what happened*, write only what changed in the world, then which Verbs express it.

> **If a consequence needs an operation not on the list, that is a real finding.**
> **If it merely needs a Tag, a Channel, or a Component formula, it is not.**

**The mistake.** Adding a Verb for something that is really a Component's behaviour composed from existing Verbs. Tags absorb far more than they look like they should.

**Done when:** every worked example from every list expresses cleanly, and you have gone a full pass without adding anything.

---

## Phase 1 is done when

- [ ] Every blocking list filled, and every entry passes its own test
- [ ] Every list has a "considered and rejected" section that is not empty
- [ ] The three character sheets written, and the person-only values are few
- [ ] The jargon count is known, and the first-hour budget is set
- [ ] Each list attacked after completion, and what the attack found is written down
- [ ] L6 closed **last**, by the closing procedure, with a clean final pass
- [ ] `dictionary.md` Part 12 has a row for every decision worth revisiting
