# The repository, and how it stays in sync

*Written August 2026, after three sessions of git failing in ways that were not obvious. Read this before touching git in this project.*

---

## The invariant

> **Every session that changes a file ends with a commit and a push. No exceptions, no "I'll do it next time."**

The design documents *are* the project. There is no code yet. A session's output that never reaches GitHub did not happen, and the next session — possibly on a different machine, certainly with no memory of this one — will start from stale files and quietly undo work.

**Verify, don't assume.** A session is finished when `git status -sb` reads:

```
## main...origin/main
```

with nothing after it. Anything else — `ahead 1`, a list of modified files, a detached HEAD — means the session is not finished.

---

## Where everything lives

| | |
|---|---|
| **Remote** | `git@github.com:dylanpetty378-arch/game-platform.git` |
| **Local path** | `~/Documents/GitHub/game-platform` |
| **Branch** | `main`, tracking `origin/main` |
| **Auth** | SSH key at `~/.ssh/id_ed25519`, fingerprint `SHA256:Lui2DPf/whr71uOEdESRgrwD5X0+SLrxDQsg7yDCbq8` |

```
game-platform/
├── CLAUDE.md            the working rules — read automatically by any Claude session
├── sync.command         commit + push in one call
├── .gitignore
└── docs/
    ├── README.md            what each document is for
    ├── the-game.md          plain terms, start here
    ├── orientation.md       everything at length
    ├── architecture.md      reasoning and engineering
    ├── dictionary.md        THE source of truth — every term, list and decision
    ├── list-log.md          the argument behind each list
    ├── lists-research.md    research digest for the open lists
    ├── research-*.md        four full research reports with sources
    ├── work-*.md            phase guides
    ├── substrate-lists.xlsx the workbook, one tab per list
    ├── design-docs.html     the built reader — regenerate, never hand-edit
    ├── build_reader.py      builds design-docs.html from the markdown
    ├── channels.py          single source of truth for the 88 Channels
    └── phase-0-checks.py    the numeric tests; must pass before any push
```

**`design-docs.html` is generated.** Never edit it. Run `python3 build_reader.py` after changing any markdown, and `node t3.mjs` to smoke-test it.

**A new document is not in the reader until it is registered** in the `DOCS` list at the top of `build_reader.py` and mentioned in `docs/README.md`.

---

## How to run git — and the trap

**Run git through `osascript` → `do shell script`. Never through the folder bridge.**

```
osascript:  do shell script "cd ~/Documents/GitHub/game-platform && git ..."
```

### Why

A cloud session reaches the Mac two ways, and only one of them works for git.

**The folder bridge** (`device_bash`, `device_list_dir`, `device_commit_files`) mounts the folder read-write but **forbids deletion** — `rm`, `rmdir` and `unlink` all fail with *Operation not permitted*. Git's entire safety mechanism is lock files: write `index.lock`, rename it over `index`, delete it on abort. The rename works; the delete does not. So every git command leaves a stale lock, and the next command refuses to run.

**It is worse than an error.** Working around the locks by moving `index.lock` aside mid-operation destroys the staged content, and the commit then succeeds with an **empty tree**. That happened once — commit `aa2c640`, since amended. A commit that reports success and contains nothing is the worst possible failure mode, because nothing announces it.

**`osascript` runs as the user, on the real filesystem, with no sandbox.** Deletion works. Locks clean themselves up. Git behaves exactly as it does in Terminal. Use it for everything: status, add, commit, push, and cleanup.

### The rule

- **File contents** → write in the cloud workspace, deliver with `SendUserFile`, land with `device_commit_files`. That path is reliable.
- **Every git operation** → `osascript`.
- **Any deletion on the Mac** → `osascript`.

Do not mix. Do not use `device_bash` for git.

---

## The one command

```bash
bash ~/Documents/GitHub/game-platform/sync.command "what changed"
```

It clears any lock debris, stages everything, commits with the message given (or a dated one), prints the last five commits, and pushes if a remote exists. It is safe to run when there is nothing to commit.

From a session, the same thing:

```
osascript: do shell script "cd ~/Documents/GitHub/game-platform && bash sync.command 'what changed'"
```

---

## Starting on a machine that has never seen this repo

Four steps. Only the second needs a human.

**1. Check for a key.**

```bash
ls ~/.ssh/id_ed25519.pub 2>/dev/null || ssh-keygen -t ed25519 -C "dylanpetty378@gmail.com" -f ~/.ssh/id_ed25519 -N "" -q
```

**2. Add it to GitHub — this is the only manual step, and it cannot be automated.**

Adding a key is an account settings change. Claude will not do it, on any machine, ever. Copy the public key to the clipboard, open `https://github.com/settings/ssh/new`, paste, save. Confirm with:

```bash
ssh -T git@github.com     # expects: Hi dylanpetty378-arch! You've successfully authenticated
```

That command also **reports the account name**, which is how a session works out the remote URL without being told.

**3. Configure SSH.** Append to `~/.ssh/config` if `Host github.com` is not already there:

```
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new
```

**4. Clone.**

```bash
mkdir -p ~/Documents/GitHub && cd ~/Documents/GitHub
git clone git@github.com:dylanpetty378-arch/game-platform.git
cd game-platform
git config user.name "Dylan Petty"
git config user.email "dylanpetty378@gmail.com"
```

---

## Starting a session on a machine that already has it

**Always pull first.** Another machine or another session may have pushed since.

```bash
cd ~/Documents/GitHub/game-platform && git pull --ff-only origin main
```

If that fails because of local changes, they are real work from an interrupted session — commit them before pulling, never discard them.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `Unable to create '.git/index.lock': File exists` | git was run through the folder bridge | Switch to `osascript`. Then `rm -f .git/*.lock .git/refs/heads/*.lock` |
| `warning: unable to unlink ...` | same | Harmless in isolation, but it means git ran on the mount. Re-verify the commit tree is not empty |
| A commit exists but `git ls-tree -r HEAD --name-only` returns nothing | the empty-tree failure described above | `git reset --soft HEAD~1`, re-stage, re-commit. Always check the file count after committing |
| `git@github.com: Permission denied (publickey)` | key not on the account, or the wrong account | `ssh -vT git@github.com` and check the offered fingerprint matches the one above |
| `Operation not permitted` on `rm` | running through the folder bridge | `osascript` |
| Pushed but GitHub shows nothing | pushed to a branch other than `main` | `git status -sb` and `git push -u origin main` |

---

## Never

- **Never hand-edit `design-docs.html`.** It is generated.
- **Never force-push.** History here is the record of how decisions were made; that is the point of `list-log.md`.
- **Never commit without running `python3 phase-0-checks.py` and `python3 channels.py`** if anything numeric or Channel-related changed. Both must pass.
- **Never leave a session with unpushed commits.**
- **Never authenticate as Dylan.** Adding keys, creating repos, changing account settings — those are his, always.
