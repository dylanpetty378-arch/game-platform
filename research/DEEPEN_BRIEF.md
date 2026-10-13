# Deepen brief: make existing encyclopedia entries reference-grade

Dylan (Oct 12): "spend more time on each… finding information on the type of item, brands, finishes, quality, nuances,
and putting all of that in the encyclopedia." He also quotes entries to his buyers, so they must be accurate.

For EACH slug in your list file (8 slugs):
1. Read /home/claude/game-platform/docs/encyclopedia/entries/<slug>.md, the template in
   /home/claude/game-platform/docs/encyclopedia/README.md, and the rubric fields in /home/claude/game-platform/docs/rubric.md.
2. Research with WebSearch/WebFetch, using **at most 4 searches per slug (30 total)**. Spend them on identification
   depth, not prices:
   - the makers, brands and lines that matter, with marks/labels and date ranges
   - materials and finishes, and how to tell quality from cheap production and old from new
   - the specific model or variant details that move value (the "nuances" a collector checks first)
   - common damage, repairs and reproductions
   Note each source URL.
3. Rewrite the entry as ONE coherent entry in the template, at least twice as detailed in the identification
   sections.
   - KEEP every existing fact, comp, Terapeak line, source, rubric value and "Seen in sweeps" line.
   - Do not invent sold comps. Price statements must come from the existing entry or a cited source.
   - Add a "### Quick ID checklist" (5–10 bullets a buyer can check from photos) inside Makers/brands/variants.
   - Add a "### What to tell the buyer" paragraph in Selling it: factual, quotable listing copy points.
   - Keep the `Updated:` date and append " · deepened 2026-10-13".
   - Size rule: anything bigger than a car's passenger seat is excluded.
4. Write the result to /tmp/res/deep/out/<slug>.md (mkdir -p). Do not write into the repo. Check that the rubric JSON parses:
   `python3 -c "import json,re,sys; t=open(sys.argv[1]).read(); json.loads(re.search(r'## Rubric.*?\x60\x60\x60json\s*(\{.*?\})\s*\x60\x60\x60', t, re.S).group(1))" FILE`

Final report (short): slugs written, plus any probable errors you corrected in the old entry.

## No generalization (Dylan, Oct 13)
Every entry must answer: **which specific brands, marks, models, variants, materials or dates make one of these worth
a multiple of the ordinary one, and how do you see that in a seller's photo?** Add, inside Makers/brands/variants:
`### Golden-egg tells` — a list of `<specific variant/mark/brand> — ~<multiple or $ band> vs the common version —
<how to spot it in a photo>`. At least 5 lines where the type has that many; "varies by maker" is not a line. A
generic value range without the variants that drive it is a defect.
