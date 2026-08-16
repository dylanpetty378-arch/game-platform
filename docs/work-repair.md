# Phase 0 · Repair — CLOSED

**Closed August 2026.** Every item below is decided, recorded in `dictionary.md` Part 12 with its reasoning, and covered by a numeric test in **`phase-0-checks.py`** that fails against the old behaviour and passes against the new.

This document is now the record of what was decided and why, not a worklist. The worklist is `work-lists.md`.

---

## What changed, in one place

| | Finding | Outcome |
|---|---|---|
| 1 | **A1** Allocation Points | **Fixed and partly accepted.** Integer-first resolution; all-in answered by authoring |
| 2 | **A4** Enhancement Capacity | **Fixed and partly accepted.** Percentages clamped, absolutes deliberately not |
| 3 | **A3** Flat Guards | **Fixed.** Universal flat Guards act on the packet total, once per source |
| 4 | **A2** Standing self-scoped vectors | **Accepted, with a reserved slot** |
| 5 | **A6** Apportionment | **Dissolved.** There is no fixed-point direction to apportion |
| 6 | **A7** The multiplication at R-1050 | **Fixed.** Three declared rounding sites |
| 7 | **A10** Shaping order | **Fixed.** Bonus Points → Baseline, in points. Demand retired |
| 8 | **A16** Log-integer associativity | **Fixed.** Logs are never added |
| — | **A17** Scale-crossing | **Promoted into Phase 0 and fixed.** Default conversion rule, and Scale on parts |
| 9 | Renumber the lattice | **Done.** Twenty-six slots became thirty |
| 10 | Re-attack | **Done.** Findings folded back into `issues-and-ideas.md` |

---

## 1 · A1 — Allocation Points

**Decided.** The resolved value on an axis is **one integer operation**:

```
value on axis i  =  ⌊ pointsᵢ × magnitude ÷ total points ⌋
```

A share is never stored as a decimal and never multiplied by anything.

**Why.** The obvious alternative — work out the share, then multiply — gives a different and worse answer. Six points as 3/2/1 on a magnitude of 12:

```
share first     6, 3, 1     total 10, and 2 magnitude vanishes
integer first   6, 4, 2     total 12, nothing lost
```

Against the standing lock those two readings tell **different stories**: share-first misses the needle at 3 against a bar of 4; integer-first spots it at exactly 4.

**What it also bought.** There is no fixed-point direction for an attempt, so there is no apportionment method to choose and no Alabama paradox — no case where spending one more point makes an axis go *down*. Checked exhaustively.

**The residual truncation is the intended penalty for spreading.** Loss is always under the number of axes used, so it is nothing on a large roll and total on a small one: eight points across eight axes on a roll of 7 leaves every axis at zero.

**All-in — accepted, and answered by authoring rather than arithmetic.** With only `≥` bars, one point all-in is always at least as good as spreading; the tension comes entirely from downside bars. Rather than change the arithmetic:

- **Authored content:** a Threshold set is not valid without a downside bar. The authoring tool enforces it structurally.
- **A live GM:** trusted to decide on the fly, and not required to write anything down. The task-creation surface *offers* a downside bar by default rather than asking them to invent one.
- **Instrumentation:** count how many tasks ship with no downside bar, so playtesting measures this instead of guessing at it.

**Still open, and deliberately:** how many points a character has, and where they come from. That belongs to L29 and to paper play.

---

## 2 · A4 — Enhancement Capacity

**Decided, in three parts.**

**Percentages are clamped. Absolutes are not, and that is deliberate.** A flat `+2` is worth 2 no matter how many amplifiers are present, so absolutes cannot run away by stacking — they grow linearly in the number of contributors, and **Participation Capacity already bounds contributors**. Percentages are the direction that compounds, so percentages get the ceiling. Two failure modes, two walls, neither redundant.

The consequence, stated plainly so nobody reads it as a leak: *a lock at Enhancement Capacity 100% cannot be amplified, but it can still be helped by a flat bonus.*

**A Baseline is a percentage, so the same ceiling covers it.** No second Capacity, no second number on an item. This closes the longest-standing PENDING in Part 2C.

**The Capacity belongs to the task or the target, never the source.** The lock says how much help it absorbs; the gun says how much amplification it holds. A source-owned ceiling would be shoppable — the party would route every vector through whoever held the highest.

---

## 3 · A3 — Flat Guards

**Decided.** A **universal** flat Guard subtracts from the **packet total**, then what remains is redistributed across Dimensions in proportion to their pre-Guard absolute values, by the same integer apportionment Allocation Points use. Signs are preserved. **A Guard reduces toward zero and never past it.**

A **Dimension-named** flat Guard still acts on that Dimension alone, which is correct — that is what specific resistance means. Named acts before universal.

**And a flat Guard acts once per contributing source, at R-850, before anything cancels** — see the re-attack section below, which is where that came from. A **proportional** Guard is the other half of the pair: it acts once on the combined total at R-1050, after everything has cancelled. Armour meets each blow; what you are made of meets the remainder.

**Why.** Per-Dimension subtraction made mixed directions strictly worse than pure ones, and not by a little:

```
flat Guard 3, magnitude 10          old        new
  pure                              7          7
  0.3 / 0.7                         4          7
  even 3-way                        1          7
  even 4-way                        0          7
```

An evenly-spread attack at full magnitude landed **nothing**. Nobody would ever have placed a Channel off-axis, which would have deleted the reason Dimension Spaces exist. Under the new rule every direction lands the same total, by arithmetic rather than by content discipline.

**One mechanism, two uses.** Guard redistribution and Allocation Points now share the same apportionment function.

---

## 4 · A2 — Standing self-scoped vectors

**Accepted as a content decision.** An Entity that keeps an aura on itself is a large ability, and it gets priced per creature. Fire elementals *should* be hard to fight. This is balance, not a Substrate hole.

**With insurance: R-780 is reserved** as a ceiling on standing self-scoped cancellation, and left **unbounded in v1**. Reserving a slot costs nothing. Discovering later that a player can assemble the stack — through items, or through `assume category` — and having to add a slot at that point is an Edition break that refolds every Campaign.

---

## 5 · A6 — Apportionment

**Dissolved by the A1 decision.** There is no fixed-point direction for an attempt, so there is nothing to apportion and no method to choose. Channel directions are still fixed-point, but they are **authored** rather than computed, so CI validates that each sums in absolute value to exactly 1.0000 and the problem never arises.

---

## 6 · A7 — Rounding sites

**Decided.** There are **exactly three**, all truncating toward zero:

| Site | What rounds | Scope |
|---|---|---|
| **R-400** | the summed percentage applied to magnitude | per vector |
| **R-750** | Scale conversion to the target's Scale | per vector |
| **R-1050** | a proportional Guard applied to a resolved total | per target |

The old claim that *"two fixed-point numbers are never multiplied together"* was false and is retired — a proportional Guard is exactly that. What survives is narrower and still worth saying: inside one vector's own assembly there is one multiplication and one rounding.

**CI fails on a fourth site.**

**And every truncation is a visible step** in the resolution expansion, showing the value before and after and how much was lost. Rounding is where a system quietly stops making sense to a player, so it never happens off-screen.

---

## 7 · A10 — Shaping order

**Decided: Bonus Points → Baseline**, and **Shaping is stated in points, never percentages.**

**Demand is retired.** It was a third form that forced a minimum allocation and squeezed everything else into what remained. Nothing in the design ever asked for it, forcing a player to spend their own points somewhere is a strange thing to want, and it was the only form that had to be a percentage — which reintroduced the rounding problem integer allocation had just removed. A cost belongs in the Budget, or as a Guard or a State.

The two survivors do not commute, so the order still matters. Raw 1/2/1 at magnitude 12, with `+3 points on manipulation` and `manipulation counts as at least 3 points`:

```
Bonus Points first   4/2/1 of 7   →   6, 3, 1
Baseline first       3/2/1 of 4   → +3 → 6/2/1 of 7  →  10, 3, 1
```

The three do not commute and the swing is large — 3.4× on one axis from ordering alone. The order is arithmetically arbitrary; what matters is that it is declared once and never varied by content. **It is on the playtest watchlist**, because only play will say whether it feels right.

---

## 8 · A16 — Log-integers

**Decided: log-integers are never added.** Compare and multiply only — multiplication is exact integer addition of exponents and is associative. Where things must be summed, they are converted to ordinary integers within one Scale, summed, and converted back. No lookup table ships, and there is nothing to version.

Demonstrated in the checks: the same five values summed in log space left-to-right and right-to-left give **27.54 and 28.84**. Sorting first makes that deterministic without making it correct.

---

## 9 · A17 — Crossing Scales *(promoted into Phase 0)*

This was ranked Medium and turned out to be Substrate, because *how does a person affect a large thing* is a question every session asks.

**A default conversion rule ships**, at **R-750**, as its own visible slot:

```
converted = magnitude × 10^(source Scale − target Scale), truncated toward zero
```

```
your punch, 8 at Scale 1, at a Scale 4 airship hull   →  0
the airship rams you, 8 at Scale 4, at Scale 1        →  8000
```

**And Scale belongs to the part, not only to the whole.** The conversion rule alone would mean a person cannot hurt a rowboat, which is wrong. A Scale-4 airship has Scale-1 doors, ropes, hatches and crew. You do not punch the airship — you cut its rigging, pick the lock on its hold, set fire to its sails. **The Scale that applies is the Scale of the thing actually targeted**, and a knife against a warship's hull correctly does nothing.

What counts as a part, and how parts roll up into the whole, is a Component question. The Substrate only guarantees that a part can carry its own Scale and its own Thresholds.

---

## 10 · The lattice, renumbered

**Twenty-six slots became twenty-eight.** Two additions, both in the R region:

- **R-750 · Scale conversion** — convert each resolved vector to the target's Scale, truncate toward zero. Its own slot because a player whose attack does nothing has to be able to see why.
- **R-780 · standing cap** — reserved, unbounded in v1.
- **R-850 · flat Guards, once per contributing source** — added by the re-attack.
- **R-800 / R-1000 · the combine, split in two** — within a source, then across sources. **R-1000 is where cancellation happens**, between the two kinds of Guard.

R-200 through R-750 run per vector. **R-780 through R-850 run once per contributing source.** R-1000 onward run once for the target.

That is **thirty slots: E×5, C×6, R×19.**

References updated in `dictionary.md` Part 2A and L7, `architecture.md` §8 and §11A, `substrate-checklist.md` C3, `orientation.md` §4.4, and `issues-and-ideas.md` A18.

---

## The tests

`phase-0-checks.py` — run it with `python3 phase-0-checks.py`.

Every decision above has a check that prints the old behaviour beside the new one and asserts the new. Several are exhaustive rather than illustrative: the no-Alabama-paradox check walks every point count from 1 to 12 against every magnitude to 60, and the truncation-loss bound is checked across every axis count to 8.

**These become golden fixtures when the engine is written.** Do not regenerate them to make a test pass.

---

## What the re-attack found, and what it changed

Ten findings, all written up in `issues-and-ideas.md` **Part A2**, all closed. It was worth doing: **three were errors that would have shipped**, and **two changed the pipeline.**

**The three errors.** The checks used Python's `//`, which floors — and floor is not truncate-toward-zero on negatives, which matters because *a failure is a negative magnitude*. Flooring manufactured magnitude, and at a Scale gap it made deliberately failing reach further than succeeding. The dictionary also still said Capacity is captured from the source four lines after saying it belongs to the task, so the shoppable ceiling was still there in the slot list. And named and universal flat Guards were sharing a slot without a declared order, disagreeing on a third of an exhaustive sweep.

**The two pipeline changes.** A **flat Guard now acts once per contributing source** rather than once per Moment — plate absorbed 3 whether one bandit swung or eight, so eight attackers landed 77 instead of 56. And **cancellation moved to R-1000**, between flat and proportional Guards, which lets armour meet each blow while leaving the fire elemental exactly as it was. **Restoration lands after every Guard and is never reduced by one**, which also removes a free exploit where delaying a heal by a Moment was worth the Guard's value.

**Three findings turned out to be the design working.** Small things needing a hard enough blow to hurt large things is a damage threshold and is wanted. A poisoned blade delivering its poison when it wounds you is right. And the Capacity clamp needs no distribution rule, because everything sums before it.

**The four questions it asks are worth keeping, and worth running after every change:**

- Is there a degenerate strategy — something that is always right?
- Is there a build that gets something for nothing?
- Does anything happen in two orders and give two answers?
- What is now strictly dominated? If a whole category of choice went dead, the fix went too far.
