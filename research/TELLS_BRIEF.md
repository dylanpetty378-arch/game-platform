# Golden-egg tells brief: make an entry specific (Dylan, Oct 13: "no generalization")

For EACH slug in your list file (8 slugs):
1. Read /home/claude/game-platform/docs/encyclopedia/entries/<slug>.md.
2. Research with WebSearch/WebFetch, **at most 3 searches per slug (24 total)**, aimed at ONE question: which specific
   brands, marks, models, variants, materials, sizes or dates make one of these worth a multiple of the ordinary one,
   and how is that visible in a seller's photo? Collector guides, mark databases, auction results and dealer pages
   are the sources. Note each URL.
3. Insert, inside `## Makers, brands and variants` (after any `### Quick ID checklist`), a section:
   `### Golden-egg tells` with 5–12 lines, each exactly:
   `- <specific variant/mark/brand/model> — ~<multiple>× or $<band> vs the common version — <what to look for in the photo> (<source URL or "entry comp">)`
   Use multiples grounded in the entry's own comps where they exist; otherwise cite the source. No line may be
   generic ("older is better", "condition matters"). If the type truly has no valuable variant, write one line saying
   so and why, and set the rubric `undervalue_frequency` to 1.
4. Keep everything else in the entry exactly as it is. Append " · tells 2026-10-13" to the `Updated:` line.
5. Write the result to /tmp/res/tells/out/<slug>.md. Check the rubric JSON still parses.

Final report (short): slugs written; the single best tell you found per slug (one line each).
