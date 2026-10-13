#!/usr/bin/env python3
"""One working Claude at a time (Dylan, Oct 12: "you are the code chat"; no overlapping sessions overwriting code).

  python3 scripts/lock.py status            # who holds it, until when
  python3 scripts/lock.py take "<who>" [h]  # take it for h hours (default 3); refuses if someone else holds a live lock
  python3 scripts/lock.py take "<who>" --force   # Dylan said "get going" in THIS chat → take over
  python3 scripts/lock.py release "<who>"

The lock is ops/lock.json on the refurbish branch, so every device and every session sees the same one. Commit +
push right after taking it. A lock that has expired is free. A chat Dylan is talking to always wins (--force): he is
the authority, and the scheduled runner backs off when it sees a newer holder.
"""
import json, os, sys, time, datetime
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ops', 'lock.json')
now = time.time()
def read():
    try: return json.load(open(P))
    except Exception: return {}
def iso(t): return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
a = sys.argv[1:]
L = read(); live = L.get('until', 0) > now
if not a or a[0] == 'status':
    print(f"held by {L.get('who')} until {iso(L['until'])}" if live else 'free'); sys.exit(0)
who = a[1] if len(a) > 1 else 'unknown'
if a[0] == 'take':
    if live and L.get('who') != who and '--force' not in a:
        print(f"BUSY: {L.get('who')} holds the lock until {iso(L['until'])} — do read-only work, or --force if Dylan is in this chat"); sys.exit(2)
    h = next((float(x) for x in a[2:] if x.replace('.', '').isdigit()), 3.0)
    os.makedirs(os.path.dirname(P), exist_ok=True)
    json.dump({'who': who, 'since': iso(now), 'until': now + h * 3600}, open(P, 'w')); print('taken by', who, 'until', iso(now + h * 3600))
elif a[0] == 'release':
    if L.get('who') == who: json.dump({}, open(P, 'w')); print('released')
    else: print('not yours; left alone')
