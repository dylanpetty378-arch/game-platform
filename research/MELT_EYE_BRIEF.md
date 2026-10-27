# Melt-lane brief (Oct 27 2026) — one question per cell

These lots are already decided by free compute: the seller states a weight and a purity (or a photographed mark /
XRF readout says it), and weight × purity × spot at refiner payout clears Dylan's money rule. The `MELT` line under
each cell gives the floor and the max bid. The eye's only job is to catch the two ways that line is wrong:

1. **Not all metal.** Stones, pearls, beads, enamel, cord, leather, watch movements, shell cameos, jade, onyx — anything
   that is not the stated metal — is in the stated weight. Estimate the metal fraction from the photo:
   - all-metal chain, band, bangle, cross, hollow charm → 1.0
   - ring with one small stone / thin gem band → 0.8–0.9
   - heavy stone, cameo, cluster ring with large stones → 0.4–0.6
   - pearl / bead strand on a gold clasp → 0.05 (the clasp only) → KILL
2. **Plated after all.** The photo shows brassy wear-through, a "GF", "1/20", "HGE", "RGP", "925" or "vermeil" mark, or a
   watch case (most are gold-filled) → KILL.

Everything else is a LEAD. Do not research, do not look for maker value — this lane is metal only. If a cell plainly
shows more than metal (a named maker's mark, antique hand work, real gemstones), say so in the reason so the main
session can look closer.

Sheets look at every melt cell; a 0.8 fraction on a 3 g chain still clears, a 0.5 fraction on a $9 ring may not:
recompute roughly — max bid × fraction must still be above the current price by a margin worth an evening (≥ $50 and
≥ the price).

## Output — one line per cell that stays a LEAD, tab-separated, nothing else in the file
`M<melt sheet number>\t<cell>\tLEAD — metal fraction ≈ <f>, <what it is in 6 words>; or KILL — <why, 6 words>`

Write a line for every cell (LEAD or KILL) so the log is complete. End with counts per sheet.
