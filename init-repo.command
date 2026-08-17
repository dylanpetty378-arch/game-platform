#!/bin/bash
# game-platform — git helper.
#
# The first commit is already done. Keep this around for two jobs:
#
#   1. Clearing the stale lock files a cloud session leaves behind
#      (it can write to your disk but cannot delete, so git's own
#      lock and temp files pile up in .git and block the next commit).
#   2. Committing whatever has changed since.
#
# Run it with a message:
#     bash ~/Documents/GitHub/game-platform/init-repo.command "what changed"
# or with no message for a dated one.

set -e
cd "$(dirname "$0")"

echo "→ clearing stale git locks and temp objects"
rm -f .git/index.lock .git/HEAD.lock .git/objects/maintenance.lock
rm -f .git/refs/heads/*.lock 2>/dev/null || true
find .git/objects -name 'tmp_obj_*' -delete 2>/dev/null || true
find .git -maxdepth 1 -type f -size -1k ! -name 'HEAD' ! -name 'config' \
     ! -name 'description' ! -name 'packed-refs' -newer .git/config -delete 2>/dev/null || true

if [ ! -d .git ]; then
  git init -b main
  git config user.name  "Dylan Petty"
  git config user.email "dylanpetty378@gmail.com"
fi

MSG="${1:-Design documents updated $(date +%Y-%m-%d)}"

git add -A
if git diff --cached --quiet; then
  echo "→ nothing to commit"
else
  git commit -q -m "$MSG"
  echo "→ committed: $MSG"
fi

echo
git --no-pager log --oneline | head -10
echo

if git remote get-url origin >/dev/null 2>&1; then
  echo "→ pushing to origin"
  git push -u origin main
else
  cat <<'EOF'
No remote yet. To put this on GitHub, either:

  gh repo create game-platform --private --source=. --push

or make an empty repo on github.com and then:

  git remote add origin https://github.com/<you>/game-platform.git
  git push -u origin main
EOF
fi
