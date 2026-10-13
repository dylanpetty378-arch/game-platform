# Upgrade brief: bring older encyclopedia entries up to the full template

Each entry lives at /home/claude/game-platform/docs/encyclopedia/entries/<slug>.md. These were written in earlier
sweeps. They are missing sections and the machine-readable rubric, and some contain several merged earlier write-ups
("Additional research" blocks).

For EACH slug in your list file:
1. Read the entry with the Read tool.
2. Rewrite it into ONE coherent entry in the template from
   /home/claude/game-platform/docs/encyclopedia/README.md: Slug/Summary/Buy rule (short) lines, then every required
   section, ending with `## Rubric` (a ```json block with ALL fields from /home/claude/game-platform/docs/rubric.md)
   and `## Seen in sweeps`.
   - **Keep every fact, comp, source, URL and "Seen in sweeps" line already in the file.** Merge the duplicate
     write-ups; do not drop information. Where they disagree, keep both and say which is more recent.
   - Fill the new sections (Makers/brands/variants, Materials/finishes/quality tells, Condition/damage/repairs,
     Fakes/repros, Market, Selling it) from the existing text plus solid general knowledge. Mark anything from general
     knowledge as "(general knowledge, verify)". Never invent specific sold comps.
   - Rubric: fill every field. Set `"confidence"` to "medium" if dated sold comps exist in the entry, else "low".
     Size rule: anything bigger than a car's passenger seat gets `"size_class": "bigger"`, and the buy rule says it is
     excluded.
   - Keep the `Updated:` date and append " · upgraded 2026-10-13".
3. Write the result to /tmp/res/upg/<slug>.md. Do not write into the repo.
4. Check that the JSON block parses: `python3 -c "import json,re,sys; t=open(sys.argv[1]).read(); json.loads(re.search(r'## Rubric.*?\x60\x60\x60json\s*(\{.*?\})\s*\x60\x60\x60', t, re.S).group(1))" /tmp/res/upg/<slug>.md`

You have no web search budget in this run. Work from the entry text and your knowledge only.

Final report: the slugs written, plus any entry where you found contradictions or a probable error worth fixing.
