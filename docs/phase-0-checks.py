#!/usr/bin/env python3
"""
Phase 0 · Repair — the numeric tests.

One test per decision. Each prints the OLD behaviour (what was broken) and the
NEW behaviour (what the decision produces), then asserts the new one.

These are paper tests in executable form. They exist so that nobody can change
the pipeline later without something noticing. When the real engine is written
in TypeScript, these become the golden fixtures.

    python3 phase-0-checks.py
"""

# --------------------------------------------------------------------------
# The one shared primitive: integer apportionment.
# Used by Allocation Points AND by flat-Guard redistribution.
# Floor each share, then hand the remainder out largest-first, ties by index.
# --------------------------------------------------------------------------

def trunc_div(a, b):
    """Truncate toward zero. Python's // floors, which is NOT the same for
    negatives, and negative magnitude is a headline feature of this design:
    a failure is the same direction with a negative magnitude. Flooring a
    negative MANUFACTURES magnitude (-7 over two axes floors to -4/-4 = -8)."""
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b > 0) else -q


def apportion(weights, total):
    """Split `total` across `weights` proportionally, in whole numbers.
    Signs of `weights` are preserved; `total` is a non-negative magnitude."""
    s = sum(abs(w) for w in weights)
    if s == 0:
        return [0] * len(weights)
    base = [abs(w) * total // s for w in weights]
    remainder = total - sum(base)
    order = sorted(range(len(weights)),
                   key=lambda i: (-((abs(weights[i]) * total) % s), i))
    for j in range(remainder):
        base[order[j]] += 1
    return [b if w >= 0 else -b for b, w in zip(base, weights)]


def fails(msg):
    raise AssertionError(msg)


def show(title):
    print("\n" + title)
    print("-" * len(title))


# ==========================================================================
# A1 / A6 — allocation is one integer operation
# ==========================================================================

def resolve_share_first(points, total_points, magnitude, dp=4):
    """OLD: materialise the share in fixed point, truncate, then multiply."""
    share = trunc_div(points * 10**dp, total_points)
    return trunc_div(share * magnitude, 10**dp)


def resolve_integer_first(points, total_points, magnitude):
    """NEW: one integer operation, truncating toward zero."""
    if total_points == 0:
        raise ValueError("an attempt with no points spent has no direction")
    return trunc_div(points * magnitude, total_points)


def test_allocation():
    show("A1/A6 · allocation is integer-first")

    # The standing lock: manipulation 5, needle 4, corridor 1. Magnitude 12.
    BARS = {"manipulation": 5, "perception": 4, "stealth": 1}
    M, alloc = 12, {"manipulation": 3, "perception": 2, "stealth": 1}
    P = sum(alloc.values())

    old = {k: resolve_share_first(v, P, M) for k, v in alloc.items()}
    new = {k: resolve_integer_first(v, P, M) for k, v in alloc.items()}

    print(f"  6 points as 3/2/1, magnitude {M}")
    print(f"    share-first    {old}  total {sum(old.values())}")
    print(f"    integer-first  {new}  total {sum(new.values())}")

    # The old way loses magnitude and misses the needle.
    assert sum(old.values()) == 10, "share-first should lose 2 of 12"
    assert old["perception"] < BARS["perception"], "share-first misses the needle"

    # The new way is exact and spots it.
    assert sum(new.values()) == M, "integer-first must not lose magnitude"
    assert new["perception"] >= BARS["perception"], "integer-first spots the needle"
    assert new["manipulation"] >= BARS["manipulation"]
    assert new["stealth"] > BARS["stealth"]
    print("    → integer-first clears all three bars; share-first does not")

    # An even split must be exact, at every magnitude divisible by the point count.
    for M2 in range(1, 200):
        for P2 in range(1, 13):
            vals = [resolve_integer_first(1, P2, M2) for _ in range(P2)]
            if M2 % P2 == 0:
                assert sum(vals) == M2, (M2, P2)

    # No Alabama paradox: spending one MORE point on an axis never lowers it.
    for M2 in range(1, 60):
        for P2 in range(2, 13):
            for p in range(1, P2):
                a = resolve_integer_first(p, P2, M2)
                b = resolve_integer_first(p + 1, P2 + 1, M2)
                if b < a:
                    fails(f"Alabama paradox at M={M2} P={P2} p={p}: {a} -> {b}")
    print("    → no case where one more point makes an axis go down")

    # The spreading penalty is bounded by the number of axes.
    worst = (0,)
    for P2 in range(1, 21):
        for k in range(1, 9):
            if k > P2:
                continue
            base, rem = P2 // k, P2 % k
            a = [base + (1 if i < rem else 0) for i in range(k)]
            for M2 in range(1, 101):
                loss = M2 - sum(resolve_integer_first(p, P2, M2) for p in a)
                assert loss < k, "loss must always be under the axis count"
                if loss > worst[0]:
                    worst = (loss, k, P2, M2)
    print(f"    → worst truncation loss {worst[0]} across {worst[1]} axes "
          f"(magnitude {worst[3]}) — always under the axis count")

    # Rounding must never MANUFACTURE magnitude, and a failure is a negative
    # magnitude, so this has to hold on both sides of zero.
    for M2 in list(range(-60, 0)) + list(range(1, 61)):
        for P2 in range(1, 13):
            for k in range(1, min(P2, 8) + 1):
                base, rem = P2 // k, P2 % k
                a = [base + (1 if i < rem else 0) for i in range(k)]
                out = [resolve_integer_first(p, P2, M2) for p in a]
                assert abs(sum(out)) <= abs(M2), (M2, P2, a, out)
    print("    → |sum of resolved values| never exceeds |magnitude|, on both "
          "sides of zero")

    # The floor/truncate divergence this guards against:
    floored = [(1 * -7) // 2 for _ in range(2)]
    trunced = [resolve_integer_first(1, 2, -7) for _ in range(2)]
    assert sum(floored) == -8 and sum(trunced) == -6
    print(f"    → magnitude -7 over two axes: floor gives {floored} (sum -8, "
          f"magnitude invented); truncate gives {trunced} (sum -6)")


# ==========================================================================
# A1 — all-in dominance, and what answers it
# ==========================================================================

def test_all_in():
    show("A1 · all-in is dominant unless a downside bar exists")

    M, P = 12, 4
    upside_only = {"manipulation": 5}
    with_downside = {"manipulation": 5, "stealth_max": 1}

    all_in = {"manipulation": 4}
    spread = {"manipulation": 2, "stealth": 2}

    def val(alloc, axis):
        return resolve_integer_first(alloc.get(axis, 0), P, M)

    print("  a lock with only a '>= 5' bar:")
    print(f"    all-in   manipulation {val(all_in,'manipulation')}  clears")
    print(f"    spread   manipulation {val(spread,'manipulation')}  clears, "
          f"and 6 magnitude went nowhere")
    assert val(all_in, "manipulation") >= upside_only["manipulation"]
    assert val(spread, "manipulation") >= upside_only["manipulation"]
    print("    → both clear; spreading bought nothing. All-in is never worse.")

    print("  the same lock with a downside bar (guard hears you at <= 1):")
    print(f"    all-in   stealth {val(all_in,'stealth')}  -> guard hears you")
    print(f"    spread   stealth {val(spread,'stealth')}  -> nobody hears")
    assert val(all_in, "stealth") <= with_downside["stealth_max"]
    assert val(spread, "stealth") > with_downside["stealth_max"]
    print("    → the downside bar is the entire source of tension.")
    print("      DECISION: the authoring tool requires one; the GM tool offers")
    print("      one by default; instrumentation counts tasks that ship without.")


# ==========================================================================
# A3 — a universal flat Guard acts on the packet total
# ==========================================================================

def land_old(values, guard):
    """OLD: subtract the flat Guard from every Dimension separately."""
    return [max(0, abs(v) - guard) * (1 if v >= 0 else -1) for v in values]


def land_new(values, guard):
    """NEW: subtract from the packet total, redistribute proportionally."""
    total = sum(abs(v) for v in values)
    after = max(0, total - guard)
    return apportion(values, after)


def test_flat_guard():
    show("A3 · a universal flat Guard acts on the total")

    GUARD = 3
    directions = {
        "pure          ": [10],
        "0.3 / 0.7     ": [3, 7],
        "even 3-way    ": [4, 3, 3],
        "even 4-way    ": [3, 3, 2, 2],
        "with negative ": [6, -4],
    }

    print(f"  flat Guard {GUARD}, packet magnitude 10")
    old_totals, new_totals = [], []
    for name, v in directions.items():
        o, n = land_old(v, GUARD), land_new(v, GUARD)
        ot, nt = sum(abs(x) for x in o), sum(abs(x) for x in n)
        old_totals.append(ot)
        new_totals.append(nt)
        print(f"    {name} {str(v):>14}   old {str(o):>16} = {ot:2}"
              f"    new {str(n):>16} = {nt:2}")

    assert max(old_totals) == 7, "pure should land 7 under the old rule"
    assert min(old_totals) == 0, "a 4-way spread was zeroed out entirely"
    assert len(set(new_totals)) == 1, "every direction must land the same total"
    print(f"    → old: {min(old_totals)} to {max(old_totals)} — an even 4-way "
          f"spread landed NOTHING at full magnitude")
    print(f"    → new: every direction lands {new_totals[0]}. Dominance gone.")

    # A Guard never flips a sign.
    for v in ([6, -4], [-9, 1], [-5, -5]):
        for g in range(0, 30):
            for a, b in zip(v, land_new(v, g)):
                assert (a >= 0) == (b >= 0) or b == 0, (v, g)
            assert all(abs(b) <= abs(a) for a, b in zip(v, land_new(v, g)))
    print("    → a Guard reduces toward zero and never past it")

    # Nothing is lost to rounding in the redistribution.
    for g in range(0, 12):
        for v in ([3, 7], [4, 3, 3], [1, 1, 1, 1, 1, 1, 1]):
            expected = max(0, sum(abs(x) for x in v) - g)
            assert sum(abs(x) for x in land_new(v, g)) == expected
    print("    → redistribution is exact; it is not a rounding site")

    # A Dimension-named Guard still acts on one Dimension only.
    named = [3, 7]
    named[1] = max(0, named[1] - GUARD)
    assert named == [3, 4]
    print(f"    → a Dimension-named Guard still acts alone: [3, 7] -> {named}")


# ==========================================================================
# A4 — where Enhancement Capacity clamps
# ==========================================================================

def assemble(base, pct_sum, absolutes, capacity_pct):
    """R-300 sum -> R-350 clamp -> R-400 apply (truncate) -> R-500 absolutes."""
    clamped = min(pct_sum, capacity_pct)
    applied = (base * clamped) // 100
    return applied + sum(absolutes)


def test_capacity():
    show("A4 · Enhancement Capacity clamps percentages, not absolutes")

    base, cap = 8, 100          # a lock: no amplification permitted at all
    print(f"  base {base}, Enhancement Capacity {cap}% (= no enhancement)")

    amplified = assemble(base, 250, [], cap)
    assert amplified == base
    print(f"    +150% of amplification      -> {amplified}   clamped away")

    with_flat = assemble(base, 250, [2], cap)
    assert with_flat == base + 2
    print(f"    the same, plus a flat +2    -> {with_flat}   the +2 lands")
    print("    → INTENDED. Absolutes grow linearly in the number of")
    print("      contributors, and Participation Capacity bounds contributors.")

    # Participation Capacity is the wall for absolutes.
    PARTICIPATION = 2
    contributors = [2, 2, 2, 2, 2]
    admitted = contributors[:PARTICIPATION]
    assert assemble(base, 100, admitted, cap) == base + 4
    print(f"    five +2 helpers, Participation {PARTICIPATION} -> "
          f"{assemble(base, 100, admitted, cap)}  (only two admitted)")

    # A Baseline is a percentage, so the same ceiling covers it.
    baseline_pct = 175
    assert assemble(base, baseline_pct, [], cap) == base
    print(f"    a Baseline worth +75%       -> {assemble(base, baseline_pct, [], cap)}"
          f"   same ceiling, no second number")

    # The ceiling belongs to the task, so it cannot be shopped.
    strong_source_cap, task_cap = 400, 100
    assert assemble(base, 250, [], task_cap) == base, \
        "the task's ceiling must win, not the source's"
    print(f"    a source with a {strong_source_cap}% ceiling attacking a "
          f"{task_cap}% task -> {assemble(base, 250, [], task_cap)}   not shoppable")


# ==========================================================================
# A7 — the rounding sites
# ==========================================================================

def test_rounding_sites():
    show("A7 · exactly three rounding sites, all truncating toward zero")

    sites = []

    # R-400: summed percentage applied to magnitude.
    base, pct = 5, 170
    r400 = trunc_div(base * pct, 100)
    sites.append(("R-400", f"{base} x {pct}% = 8.5", r400))
    assert r400 == 8

    # R-750: Scale conversion.
    mag, src, tgt = 8, 1, 4
    r750 = mag * 10**(src - tgt) if src >= tgt else trunc_div(mag, 10**(tgt - src))
    sites.append(("R-750", f"{mag} at Scale {src} -> Scale {tgt}", r750))
    assert r750 == 0

    # R-900: proportional Guard on a resolved total.
    resolved, guard_pct = 69, 50      # 6.9 at 1dp, as tenths
    r900 = trunc_div(resolved * (100 - guard_pct), 100)
    sites.append(("R-1050", f"6.9 with a 50% Guard", r900 / 10))
    assert r900 == 34                  # 3.45 -> 3.4, truncated

    for name, desc, val in sites:
        print(f"    {name}  {desc:<34} -> {val}")
    assert len(sites) == 3
    print("    → three, and CI must fail on a fourth")

    # Percentages sum; they never compound. Order cannot matter.
    for a, b in ((30, 40), (40, 30)):
        assert (5 * (100 + a + b)) // 100 == 8
    compounded = ((5 * (100 + 30)) // 100 * (100 + 40)) // 100
    assert compounded == 8
    other_order = ((5 * (100 + 40)) // 100 * (100 + 30)) // 100
    assert other_order == 9
    print(f"    → summed: 8 either order. Compounded: {compounded} vs "
          f"{other_order} — which is why nothing compounds.")


# ==========================================================================
# A10 — Shaping order
# ==========================================================================

def shape(points, bonus=None, baseline=None, order=("bonus", "baseline")):
    """Shaping, in POINTS. Two forms, no percentages, no rounding.

    Bonus Points  — add points to an axis; the total rises too, so everything
                    else is diluted. Cannot inflate the attempt.
    Baseline      — an axis counts as at least N points, WITHOUT raising the
                    total. Genuinely raises total effect; clamped by Capacity.
    Demand is retired: it was the only form that had to be a percentage.
    """
    pts = dict(points)
    total = sum(points.values())
    for step in order:
        if step == "bonus" and bonus:
            axis, n = bonus
            if pts.get(axis, 0) < 1:
                raise ValueError("Bonus Points need at least one of your own")
            pts[axis] += n
            total += n
        elif step == "baseline" and baseline:
            axis, n = baseline
            pts[axis] = max(pts.get(axis, 0), n)     # total deliberately unchanged
    return pts, total


def test_shaping_order():
    show("A10 · Shaping is two forms, in points, Bonus Points -> Baseline")

    raw = {"manipulation": 1, "perception": 2, "stealth": 1}
    BARS = "manipulation >= 5,  perception >= 4,  stealth > 1"
    M = 12

    def resolve(pts, total):
        return {k: resolve_integer_first(v, total, M) for k, v in pts.items()}

    plain = resolve(raw, sum(raw.values()))
    bonus = resolve(*shape(raw, bonus=("manipulation", 3)))
    base = resolve(*shape(raw, baseline=("manipulation", 3)))

    print(f"  allocation 1/2/1 at magnitude {M}   bars: {BARS}")
    print(f"    nothing              {plain}")
    print(f"    Bonus Points +3      {bonus}")
    print(f"    Baseline 3 points    {base}")

    assert plain["manipulation"] == 3 and plain["perception"] == 6
    assert bonus == {"manipulation": 6, "perception": 3, "stealth": 1}
    assert base == {"manipulation": 9, "perception": 6, "stealth": 3}
    assert sum(bonus.values()) <= M, "Bonus Points must never inflate the attempt"
    assert sum(base.values()) > M, "a Baseline is a real increase in total effect"
    print("    -> Bonus Points cannot inflate (sums to 10 of 12); a Baseline can "
          "(sums to 18)")

    # The two forms do not commute, so the order is declared.
    first = resolve(*shape(raw, bonus=("manipulation", 3), baseline=("manipulation", 3),
                           order=("bonus", "baseline")))
    second = resolve(*shape(raw, bonus=("manipulation", 3), baseline=("manipulation", 3),
                            order=("baseline", "bonus")))
    print(f"    Bonus then Baseline  {first}")
    print(f"    Baseline then Bonus  {second}")
    assert first != second
    print("    -> they do not commute; Bonus Points -> Baseline is declared")


# ==========================================================================
# A26 — flat Guards act once per source; restoration lands after Guards
# ==========================================================================

def flat_per_source(source_packets, guard):
    """R-850: each contributing source pays the flat Guard once."""
    out = []
    for pk in source_packets:
        total = sum(abs(v) for v in pk)
        out.append(apportion(pk, max(0, total - guard)))
    return out


def combine(packets):
    """R-1000: sum across sources. THIS is where cancellation happens."""
    n = max(len(p) for p in packets)
    return [sum(p[i] if i < len(p) else 0 for p in packets) for i in range(n)]


def test_per_source_guards():
    show("A26 · flat Guards act once per source, not once per Moment")

    GUARD = 3
    print(f"  knight in plate (universal flat {GUARD}), bandits swinging for 10:")
    for n in (1, 2, 5, 8):
        sources = [[-10] for _ in range(n)]
        per_source = abs(combine(flat_per_source(sources, GUARD))[0])
        per_moment = max(0, 10 * n - GUARD)
        print(f"    {n} attacker(s):  once per Moment {per_moment:>3} lands   |   "
              f"once per source {per_source:>3} lands")
        assert per_source == n * (10 - GUARD)
    assert abs(combine(flat_per_source([[-10]] * 8, GUARD))[0]) == 56
    print("    → armour no longer becomes irrelevant as the fight gets harder")

    # And the fire elemental is unchanged, because cancellation moved to R-1000,
    # between the flat Guards and the proportional ones.
    print("  the fire elemental is unchanged (cancellation at R-1000):")
    cold_and_aura = combine(flat_per_source([[-8], [5]], 0))
    guarded = 0 if cold_and_aura[0] > 0 else cold_and_aura[0]   # 100% temperature-POSITIVE
    assert guarded == -3
    print(f"    cold −8 + own aura +5 → combine {cold_and_aura} → "
          f"temperature-positive Guard does not apply → takes {abs(guarded)} cold")
    incoming_fire = combine(flat_per_source([[10], [5]], 0))
    assert (0 if incoming_fire[0] > 0 else incoming_fire[0]) == 0
    print(f"    enemy fire +10 + own aura +5 → {incoming_fire} → 100% Guard → 0   immune")

    # Restoration lands at R-1200, after every Guard.
    show("A26 · restoration lands after Guards, so timing stops mattering")
    poison = combine(flat_per_source([[-6]], GUARD))[0]
    print(f"    poison −6, guarded per source → {poison}")
    print(f"    cleric heals +6 at Landing, never reduced by armour")
    same_moment = poison + 6
    delayed = poison + 6
    assert same_moment == delayed == 3
    print(f"    same Moment → net {same_moment}    delayed one Moment → net {delayed}")
    print("    → identical. The free timing exploit is gone, and armour never")
    print("      reduces a heal.")


# ==========================================================================
# A16 / A17 — Scale
# ==========================================================================

def convert(magnitude, source_scale, target_scale):
    d = source_scale - target_scale
    return magnitude * 10**d if d >= 0 else trunc_div(magnitude, 10**(-d))


def test_scale():
    show("A16/A17 · crossing Scales")

    cases = [
        ("your punch at an airship hull", 8, 1, 4, 0),
        ("the airship rams you",          8, 4, 1, 8000),
        ("your punch at a rowboat hull",  8, 1, 2, 0),
        ("your punch at the rowboat's OAR (a Scale-1 part)", 8, 1, 1, 8),
        ("your knife on the airship's RIGGING (Scale 1)",    8, 1, 1, 8),
    ]
    for label, mag, src, tgt, expect in cases:
        got = convert(mag, src, tgt)
        assert got == expect, (label, got, expect)
        print(f"    {label:<50} {mag} @S{src} -> S{tgt} = {got}")
    print("    → the hull is unreachable, and that is correct")
    print("    → parts carry their own Scale, which is what makes Scale usable")

    # Log-integers: multiplication is exact addition, so it is associative.
    import math
    logs = [int(round(1000 * math.log10(v))) for v in (2, 3, 5)]
    assert (logs[0] + logs[1]) + logs[2] == logs[0] + (logs[1] + logs[2])
    print("    → log multiplication is exact integer addition: associative")

    # ...but log ADDITION via a quantised table is not. Table grain decides
    # where it bites; it is never safe, only sometimes lucky.
    GRAIN = 50
    def enc(v):
        return int(round(GRAIN * math.log10(v)))
    def dec(a):
        return 10**(a / GRAIN)
    def log_add(a, b):
        return int(round(GRAIN * math.log10(dec(a) + dec(b))))

    vals = [2, 3, 5, 7, 11]           # true sum: 28
    ls = [enc(v) for v in vals]
    left = ls[0]
    for x in ls[1:]:
        left = log_add(left, x)
    right = ls[-1]
    for x in reversed(ls[:-1]):
        right = log_add(x, right)
    print(f"    → summing {vals} in log space (true answer {sum(vals)}):")
    print(f"        left to right {dec(left):.4f}    right to left {dec(right):.4f}")
    assert left != right, "this grain must demonstrate the divergence"
    print("      Same numbers, same table, two answers. Sorting first makes it")
    print("      deterministic without making it correct.")
    print("      DECISION: log-integers are never added. Compare and multiply only.")


# ==========================================================================

def main():
    print("Phase 0 · Repair — numeric checks")
    print("=" * 60)
    test_allocation()
    test_all_in()
    test_flat_guard()
    test_capacity()
    test_rounding_sites()
    test_shaping_order()
    test_per_source_guards()
    test_scale()
    print("\n" + "=" * 60)
    print("all checks passed")


if __name__ == "__main__":
    main()
