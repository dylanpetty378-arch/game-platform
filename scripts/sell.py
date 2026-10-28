#!/usr/bin/env python3
"""Selling log tool — db/selling/items.jsonl (one row per item Dylan is selling).

  python3 scripts/sell.py list                      # every open item: id, list price, days up, last stats
  python3 scripts/sell.py check <id> C S M [note]   # append today's clicks/saves/messages
  python3 scripts/sell.py sold <id> <price> [where] # close an item (also: donated / hauled / withdrawn)
  python3 scripts/sell.py stats                     # the feedback loop: days-to-sell, % of list, click→message, by family
  python3 scripts/sell.py card <id>                 # the paste-ready listing from the row (title/body/prices) + its checks
  python3 scripts/sell.py report                    # by-family table (median days to sell, % of list, clicks→msg) for playbook §1/§4

Row shape: {id, what, family?, plan, list, day4, day6, channels, listed:{when, where, price}, groups:[...],
            checks:[{when, clicks, saves, messages, note}], outcome:{status, when, where, price, note}}
`family` is one of the section names in docs/selling/household-families.md or an encyclopedia slug.
"""
import json, os, sys, datetime as dt
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'db', 'selling', 'items.jsonl')

def rows(): return [json.loads(l) for l in open(P) if l.strip()]
def save(rs): open(P, 'w').write(''.join(json.dumps(r) + '\n' for r in rs))
def now(): return dt.datetime.now(dt.timezone(dt.timedelta(hours=-5))).strftime('%Y-%m-%dT%H:%M-05:00')
def day(s):
    try: return dt.date.fromisoformat(s[:10])
    except Exception: return None
def listed_day(r): return day((r.get('listed') or {}).get('when') or '')

def cmd_list():
    today = dt.date.today()
    for r in rows():
        if r.get('outcome'): continue
        ld = listed_day(r); up = (today - ld).days if ld else None
        c = (r.get('checks') or [None])[-1] or {}
        print(f"{r['id']:36} ${r.get('list', 0):>4}  up {up if up is not None else '-':>3}d  "
              f"clicks {c.get('clicks', '-'):>3} saves {c.get('saves', '-'):>2} msgs {c.get('messages', '-'):>2}  {len(r.get('groups', []))} group-shares")

def cmd_check(i, c, s, m, note=''):
    rs = rows()
    for r in rs:
        if r['id'] == i or r['id'].endswith(i):
            r.setdefault('checks', []).append({'when': now(), 'clicks': int(c), 'saves': int(s), 'messages': int(m), 'note': note})
            save(rs); print('logged', r['id']); return
    sys.exit('no such id')

def cmd_sold(i, price, where='fb'):
    rs = rows()
    for r in rs:
        if r['id'] == i or r['id'].endswith(i):
            status = 'sold' if price.replace('.', '').isdigit() else price
            r['outcome'] = {'status': status, 'when': now()[:10], 'where': where, 'price': float(price) if status == 'sold' else None}
            save(rs); print('closed', r['id'], r['outcome']); return
    sys.exit('no such id')

def cmd_stats():
    rs = rows(); today = dt.date.today()
    sold = [r for r in rs if (r.get('outcome') or {}).get('status') == 'sold' and r['outcome'].get('price')]
    open_ = [r for r in rs if not r.get('outcome') and r.get('listed')]
    print(f'{len(rs)} items: {len(sold)} sold, {len(open_)} open, {len(rs)-len(sold)-len(open_)} other/unlisted\n')
    if sold:
        print('SOLD — days to sell, % of list price achieved')
        for r in sold:
            ld, sd = listed_day(r), day(r['outcome']['when'])
            d = (sd - ld).days if ld and sd else None
            pct = round(100 * r['outcome']['price'] / r['list']) if r.get('list') else None
            print(f"  {r['id']:36} {d if d is not None else '-':>3}d  {pct if pct else '-':>3}% of list  ${r['outcome']['price']:.0f} via {r['outcome'].get('where','?')}")
        ds = [(day(r['outcome']['when']) - listed_day(r)).days for r in sold if listed_day(r) and day(r['outcome']['when'])]
        ps = [100 * r['outcome']['price'] / r['list'] for r in sold if r.get('list')]
        if ds: print(f'  median days to sell {sorted(ds)[len(ds)//2]}, median % of list {round(sorted(ps)[len(ps)//2])}%')
    if open_:
        print('\nOPEN — clicks/day and click→message so far')
        for r in open_:
            c = (r.get('checks') or [None])[-1] or {}
            ld = listed_day(r); up = max((today - ld).days, 1) if ld else None
            cl = c.get('clicks'); ms = c.get('messages')
            cpd = round(cl / up, 1) if cl is not None and up else '-'
            rate = f"{round(100*ms/cl)}%" if cl and ms is not None else '-'
            print(f"  {r['id']:36} ${r.get('list',0):>4}  {cpd:>5} clicks/day  saves {c.get('saves','-')}  msg rate {rate}")
    print('\nBenchmarks (playbook §1): <2 clicks in 12 h = not shown; dozens of clicks + 0 messages = normal day 1; '
          'many saves + 0 messages = cut 5–10%.')

def cmd_card(i):
    for r in rows():
        if r['id'] == i or r['id'].endswith(i):
            L = r.get('listing') or {}
            print(f"# {r['id']}  ({r.get('family','?')})\nList ${r.get('list')}  day4 ${r.get('day4')}  day6 ${r.get('day6')}  channels {', '.join(r.get('channels', []))}")
            print('Title:', L.get('title') or '(not stored — see plan: ' + r.get('plan', '') + ')')
            if L.get('body'): print('Body:\n' + L['body'])
            if r.get('listed'): print('Listed:', json.dumps(r['listed']))
            for c in r.get('checks', []): print('  check', c.get('when'), f"clicks {c.get('clicks')} saves {c.get('saves')} msgs {c.get('messages')}", c.get('note', ''))
            for g in r.get('groups', []): print('  groups', g.get('when'), len(g.get('groups', [])))
            if r.get('outcome'): print('Outcome:', json.dumps(r['outcome']))
            return
    sys.exit('no such id')

def cmd_report():
    import collections
    by = collections.defaultdict(list)
    for r in rows(): by[r.get('family') or 'unknown'].append(r)
    print('| Family | n | sold | median days to sell | median % of list | clicks/day (open) | click→msg |\n|---|---|---|---|---|---|---|')
    today = dt.date.today()
    for fam, rs in sorted(by.items()):
        sold = [r for r in rs if (r.get('outcome') or {}).get('status') == 'sold' and r['outcome'].get('price')]
        ds = sorted((day(r['outcome']['when']) - listed_day(r)).days for r in sold if listed_day(r) and day(r['outcome']['when']))
        ps = sorted(100 * r['outcome']['price'] / r['list'] for r in sold if r.get('list'))
        cl = ms = 0; cpd = []
        for r in rs:
            if r.get('outcome') or not r.get('listed'): continue
            c = (r.get('checks') or [None])[-1] or {}
            if c.get('clicks') is not None:
                up = max((today - listed_day(r)).days, 1); cpd.append(c['clicks'] / up); cl += c['clicks']; ms += c.get('messages') or 0
        med = lambda xs: (xs[len(xs)//2] if xs else '-')
        print(f"| {fam} | {len(rs)} | {len(sold)} | {med(ds)} | {round(med(ps)) if ps else '-'} | {round(sum(cpd)/len(cpd),1) if cpd else '-'} | {f'{round(100*ms/cl)}%' if cl else '-'} |")

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    c = a[0]
    if c == 'list': cmd_list()
    elif c == 'check': cmd_check(*a[1:])
    elif c == 'sold': cmd_sold(*a[1:])
    elif c == 'stats': cmd_stats()
    elif c == 'card': cmd_card(a[1])
    elif c == 'report': cmd_report()
    else: print(__doc__)
