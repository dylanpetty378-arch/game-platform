#!/bin/bash
# One-time git setup for game-platform. Double-click, or run:
#     bash ~/Documents/GitHub/game-platform/init-repo.command
set -e
cd "$(dirname "$0")"
echo "Working in: $(pwd)"

# A previous attempt left a lock file behind that could not be removed remotely.
rm -f .git/index.lock

if [ ! -d .git ]; then git init -b main; fi
git config user.name  "Dylan Petty"
git config user.email "dylanpetty378@gmail.com"

git add -A
git commit -m "Design documents: Substrate settled through Phase 0

Vector model, 30-slot resolution lattice, five Sockets, and the
thirty numbered lists. Phase 0 (Repair) closed: eight foundation
decisions plus ten re-attack findings, each recorded in
dictionary.md Part 12 and covered by phase-0-checks.py."

echo
echo "Committed. Log:"
git --no-pager log --oneline
echo
echo "To put it on GitHub, either:"
echo "  gh repo create game-platform --private --source=. --push"
echo "or create an empty repo on github.com and then:"
echo "  git remote add origin https://github.com/<you>/game-platform.git"
echo "  git push -u origin main"
