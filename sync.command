#!/bin/bash
# game-platform — one-command sync.
#   bash sync.command "what changed"
# Clears any stale locks, commits everything, pushes if a remote exists.
set -e
cd "$(dirname "$0")"
rm -rf _to_delete .git/*.lock .git/refs/heads/*.lock 2>/dev/null || true
find .git/objects -name 'tmp_obj_*' -delete 2>/dev/null || true
git add -A
if git diff --cached --quiet; then
  echo "nothing to commit"
else
  git commit -q -m "${1:-Design documents updated $(date +%Y-%m-%d)}"
  echo "committed: ${1:-dated}"
fi
git --no-pager log --oneline | head -5
if git remote get-url origin >/dev/null 2>&1; then
  git push -q origin main && echo "pushed to origin"
else
  echo "no remote yet"
fi
