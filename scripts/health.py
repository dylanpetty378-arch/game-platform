#!/usr/bin/env python3
"""Health check of every step of the Refurbish machine. Read-only. Run from the repo root:
  python3 scripts/health.py            # table of PASS / WARN / FAIL with the numbers behind each
Exit code 1 if anything FAILs. Used by the review cycle (docs/review-cycle.md §1) and by humans.
"""
import json, os, sys, time, subprocess, datetime, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import db
ROOT = db.ROOT
now = time.time()
def age_h(ts):
    try: return (now - datetime.datetime.fromisoformat(ts.replace('Z', '+00:00')).timestamp()) / 3600
    except Exception: return 1e9
rows = []
def check(name, ok, detail, warn=False):
    rows.append(('PASS' if ok else ('WARN' if warn else 'FAIL'), name, detail))

# 1. cloud workflow
try:
    out = subprocess.run(['gh', 'api', 'repos/dylanpetty378-arch/game-platform/actions/runs?per_page=8', '-q',
                          '.workflow_runs[] | "\\(.status) \\(.conclusion) \\(.event) \\(.created_at)"'], capture_output=True, text=True, timeout=30).stdout.strip().splitlines()
    done = [l for l in out if l.startswith('completed')]
    bad = [l for l in done[:5] if ' success ' not in l]
    check('workflow: last 5 completed runs succeeded', not bad, f"{len(done[:5]) - len(bad)}/{len(done[:5])} ok" + (f"; failed: {bad[0]}" if bad else ''))
except Exception as e:
    check('workflow: run history', False, f'gh not available ({e.__class__.__name__}) — check repo Actions tab', warn=True)
H = list(db.read('harvests'))
if H:
    h = H[-1]; a = age_h(h['ts']); fr = (h.get('failed_requests') or 0) / max(1, h.get('requests') or 1)
    check('harvest: last harvest < 6 h old', a < 6, f"{h.get('harvest_id')} {a:.1f} h ago, {h.get('n_listings')} listings, {h.get('n_selected')} queued")
    check('harvest: failed requests < 5%', fr < 0.05, f"{fr:.1%}")
else:
    check('harvest: any harvest', False, 'none in db/harvests.jsonl')
# 2. queue
try:
    m = json.load(open(os.path.join(ROOT, 'q', 'current', 'meta.json')))
    n = len(open(os.path.join(ROOT, 'q', 'current', 'queue.txt')).read().split(';'))
    check('queue: built < 6 h ago', age_h(m['made']) < 6, f"id {m['id']}, made {age_h(m['made']):.1f} h ago")
    check('queue: >= 500 pending', n >= 500, f'{n} entries')
except Exception as e:
    check('queue: readable', False, str(e))
# 3. Lens worker
L = sorted(db.read('lens'), key=lambda r: r.get('ts') or '')
if L:
    a = age_h(L[-1]['ts'])
    check('lens worker: newest result < 2 h old', a < 2, f'{a:.1f} h ago (WARN only if Dylan\'s Chrome may be closed)', warn=True)
    last = L[-200:]; n = len(last)
    priced = sum(1 for r in last if (r.get('n') or 0) > 0) / n
    empty = sum(1 for r in last if 'personalized' in (r.get('best') or '') or not r.get('best')) / n
    ai = sum(1 for r in last if len(r.get('ai') or '') > 20) / n
    vers = {}
    for r in last: vers[(r.get('q') or {}).get('v', 'v1')] = vers.get((r.get('q') or {}).get('v', 'v1'), 0) + 1
    check('lens quality: >= 80% of last 200 have priced matches', priced >= .8, f'{priced:.0%}')
    check('lens quality: <= 5% empty reads', empty <= .05, f'{empty:.0%}')
    check('lens quality: AI text share (info)', True, f'{ai:.0%} (Google omits AI on some images)')
    check('lens worker: version of last 200', True, json.dumps(vers))
    flag = sum(1 for r in last if r.get('flag')) / n
    check('lens: flag rate 20–60%', .2 <= flag <= .6, f'{flag:.0%}', warn=True)
else:
    check('lens worker: any results', False, 'no lens rows')
# 4. database integrity
badlines = 0
for dp, _, fs in os.walk(os.path.join(ROOT, 'db')):
    for f in fs:
        if f.endswith('.jsonl'):
            for line in open(os.path.join(dp, f)):
                if line.strip():
                    try: json.loads(line)
                    except Exception: badlines += 1
check('database: all JSONL lines parse', badlines == 0, f'{badlines} bad lines')
inbox = [f for f in os.listdir(os.path.join(ROOT, 'db', 'inbox'))] if os.path.isdir(os.path.join(ROOT, 'db', 'inbox')) else []
check('database: inbox drained', len(inbox) <= 2, f'{len(inbox)} files waiting', warn=True)
cur = {}
for e in db.read('events'):
    p = str(e['pid']); o = cur.get(p)
    if o is None or (e.get('ts') or '') >= (o.get('ts') or ''): cur[p] = e
flagged = sum(1 for e in cur.values() if e['stage'] == 'flagged')
check('review backlog: flagged waiting <= 300', flagged <= 300, f'{flagged} waiting for photo review', warn=True)

# 5. knowledge & leads
try:
    import enc
    ents = list(enc.entries()); withc = sum(1 for _, t in ents if 'Terapeak' in t)
    check('encyclopedia: entries with Terapeak sold comps', withc / max(1, len(ents)) >= .5, f'{withc}/{len(ents)} ({withc/max(1,len(ents)):.0%})', warn=True)
except Exception as e: check('encyclopedia readable', False, str(e))
leads = [p for p, e in cur.items() if e['stage'] == 'decided' and e.get('status') in ('ask', 'find')]
check('open leads (ask/find) — Dylan to decide', True, f'{len(leads)} open')
lensed_wait = sum(1 for e in cur.values() if e['stage'] == 'lensed')
check('text-triage backlog (lensed, unread) <= 600', lensed_wait <= 600, f'{lensed_wait} waiting', warn=True)

w = max(len(r[1]) for r in rows)
for s, n, d in rows: print(f'{s:<5} {n:<{w}}  {d}')
sys.exit(1 if any(r[0] == 'FAIL' for r in rows) else 0)
