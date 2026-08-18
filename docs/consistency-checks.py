#!/usr/bin/env python3
"""
The document lint. Retired vocabulary and stale counts, corpus-wide.

The corpus's own rule applies to the corpus: if you can violate it silently,
the gate is missing. Every contradiction found in the August 2026
reconciliation pass would have been caught by this file. It runs inside
`sync.command` before every commit — if it fails, fix the document, never
the lint.

Scope: the LIVING documents — the ones that state what the system is.
Research documents and the adversarial review are records of their moment
and are deliberately not linted (each carries a banner saying the
settlements win). `design-docs.html` is generated and follows its sources.

    python3 consistency-checks.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# The documents that must say exactly what the system is.
LIVING = [
    ROOT / "CLAUDE.md",
    HERE / "dictionary.md",
    HERE / "architecture.md",
    HERE / "orientation.md",
    HERE / "START-HERE.md",
    HERE / "README.md",
    HERE / "the-game.md",
    HERE / "phase-map.md",
    HERE / "open-questions.md",
    HERE / "work-lists.md",
    HERE / "work-repair.md",
    HERE / "substrate-checklist.md",
    HERE / "list-log.md",
    HERE / "worked-builds.md",
    HERE / "categorization-and-action.md",
    HERE / "repo-and-sync.md",
]

# A line may mention a retired thing while telling the story of its
# retirement. These markers exempt a line.
EXEMPT = re.compile(
    r"SUPERSEDED|superseded|retired|Retired|RETIRED|retirement|merged into"
    r"|Until August 2026|used to say|no longer|Where it started"
    r"|the story of the cut|historical|Historical|first pass said"
    r"|amended|Amended|Don't say|don't say|was the mistake"
    r"|became|become|died this way|first statement|Postscript"
)

# (pattern, why it is forbidden as a live claim)
FORBIDDEN = [
    (r"Landing Socket", "the Landing Socket is retired — landing is the Track push"),
    (r"Landing occupant", "no occupant: the base Ruleset's landing spec"),
    (r"Landing Component", "no occupant: the base Ruleset's landing spec"),
    (r"[Ff]ive Sockets?\b", "there are two Sockets: Place and Resolution"),
    (r"[Tt]hree Sockets?\b", "there are two Sockets: Place and Resolution"),
    (r"three: Place, Resolution", "there are two Sockets"),
    (r"Budget is a Socket", "Budget is Substrate (rule 16a/16b)"),
    (r"Budget — A SOCKET", "Budget is Substrate (rule 16a/16b)"),
    (r"[Ff]ive Noun kinds", "four Noun kinds — State and Resource merged into Track"),
    (r"[Nn]ine universal fields", "eight universal fields"),
    (r"[Ee]ight Moment kinds", "nine Moment kinds — turn count (n) is the ninth"),
    (r"The eight Moment", "nine Moment kinds"),
    (r"Twenty-six slots", "forty-one slots in five regions"),
    (r"Thirty slots", "forty-one slots in five regions"),
    (r"thirty-slot", "forty-one slots in five regions"),
    (r"twenty-eight are live", "thirty are live (L31, L32 added; L8, L9 retired)"),
    (r"fourteen are blocking", "sixteen are blocking"),
    (r"22 provisional", "L4 is provisional at twenty-four"),
    (r"provisional,? at 22\b", "L4 is provisional at twenty-four"),
    (r"negative magnitude, resolving at R-1250",
     "restoration is a positive direction on the axis it restores"),
    (r"Baseline is a percentage", "Shaping is points, never percentages (rule 18g)"),
    (r"\bDemand\b", "Demand is retired — Shaping has two forms"),
    (r"[Tt]welve Dimensions", "fourteen non-attempt Dimensions"),
    (r"E-/C-/R- pipeline", "the pipeline has five regions: E-/M-/C-/R-/X-"),
    (r"Baselines are percentages", "Shaping is points, never percentages (rule 18g)"),
    (r"Landing Vocabulary", "the landing spec, base Ruleset — no Socket Vocabulary"),
    (r"twenty-eight of them live", "thirty of thirty-two numbered lists are live"),
    (r"Sockets \(three\)", "there are two Sockets"),
    (r"closed, eight kinds", "nine Moment kinds"),
    (r"ordinary vector with a negative magnitude",
     "restoration is a positive direction on the axis it restores"),
    (r"only three have mixed", "four Channels mix help and harm on unipolar axes"),
]

# The other direction: sentences the corpus must actually contain.
# A stale rewrite that deletes the settled statement fails here.
REQUIRED = [
    ("CLAUDE.md", "two of them — Place and Resolution"),
    ("CLAUDE.md", "Push` · `Set` · `Place` · `Repin` · `Link` · `Create` · `Decide"),
    ("dictionary.md", "Five: `physical`, `mental`, `social`, `mystic`, `attempt`"),
    ("dictionary.md", "fifteen Dimensions"),
    ("dictionary.md", "Forty-one slots"),
    ("START-HERE.md", "Two Sockets"),
]


def lint():
    problems = []
    for path in LIVING:
        if not path.exists():
            problems.append(f"{path.name}: MISSING — a living document is gone")
            continue
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            if EXEMPT.search(line):
                continue
            for pat, why in FORBIDDEN:
                if re.search(pat, line):
                    problems.append(
                        f"{path.name}:{lineno}: /{pat}/ — {why}\n"
                        f"    {line.strip()[:120]}")
    return problems


def channel_invariants():
    sys.path.insert(0, str(HERE))
    import channels
    problems = []
    if len(channels.CHANNELS) != 88:
        problems.append(f"channels.py: {len(channels.CHANNELS)} Channels, expected 88")
    for n, d in channels.CHANNELS.items():
        if sum(abs(v) for v in d.values()) != 100:
            problems.append(f"channels.py: {n} does not sum to 100")
    seen = {}
    for n, d in channels.CHANNELS.items():
        k = tuple(sorted(d.items()))
        if k in seen:
            problems.append(f"channels.py: {n} shares a position with {seen[k]}")
        seen[k] = n
    for dim, _, _ in channels.DIMS:
        signs = {(v > 0) for d in channels.CHANNELS.values()
                 for k, v in d.items() if k == dim}
        if signs != {True, False}:
            problems.append(f"channels.py: Dimension {dim} used on one sign only")
    return problems


def required():
    problems = []
    by_name = {p.name: p for p in LIVING}
    for name, needle in REQUIRED:
        path = by_name[name]
        if path.exists() and needle not in path.read_text():
            problems.append(f"{name}: missing required statement: {needle!r}")
    return problems


if __name__ == "__main__":
    problems = lint() + channel_invariants() + required()
    if problems:
        print(f"consistency-checks: {len(problems)} problem(s)\n")
        print("\n".join(problems))
        sys.exit(1)
    print("consistency-checks: clean")
