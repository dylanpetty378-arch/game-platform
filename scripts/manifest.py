#!/usr/bin/env python3
"""Writes db/manifest.json: every db/**/*.jsonl file and encyclopedia entry with its git blob sha. The Refurbish
website (Vectus, server/src/refurbish/sync.ts) reads this from raw.githubusercontent instead of the GitHub API, which
is rate-limited per IP and shared on Fly. Run before every commit that touches db/ or the encyclopedia; the cloud
workflow runs it in its commit step. Blob sha = sha1("blob <len>\\0" + bytes), the same id git uses."""
import os, sys, json, hashlib, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def blob(p):
    b = open(p, 'rb').read(); return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
files, entries = [], []
for dp, _, fs in os.walk(os.path.join(ROOT, 'db')):
    for f in sorted(fs):
        rel = os.path.relpath(os.path.join(dp, f), ROOT)
        if f.endswith('.jsonl') and not rel.startswith('db/inbox'): files.append({'path': rel, 'sha': blob(os.path.join(dp, f))})
ed = os.path.join(ROOT, 'docs', 'encyclopedia', 'entries')
for f in sorted(os.listdir(ed)):
    if f.endswith('.md'): entries.append({'slug': f[:-3], 'sha': blob(os.path.join(ed, f))})
out = {'made': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'files': sorted(files, key=lambda x: x['path']), 'entries': entries}
json.dump(out, open(os.path.join(ROOT, 'db', 'manifest.json'), 'w'), indent=0)
print(len(files), 'files,', len(entries), 'entries')
