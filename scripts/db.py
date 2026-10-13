#!/usr/bin/env python3
"""Refurbish database — append-only JSONL tables in db/, queried through SQLite.

WHY THIS SHAPE (full reasoning: docs/decisions.md):
  * The repo branch IS the database. Any Claude session that can clone/push the branch can read and write it;
    anything that can fetch a URL can read it (raw.githubusercontent.com/.../refurbish/db/...).
  * Append-only JSON Lines: one record per line, never rewritten. Two sessions appending at once merge cleanly
    in git (no binary SQLite conflicts). Full history is kept automatically.
  * Mutable things (a listing's current stage) are expressed as EVENTS; the current state is the latest event.
  * Big tables are sharded by month (db/<table>/YYYY-MM.jsonl) so no file grows without bound.
  * SQLite is built on demand from the JSONL (`db.py sql ...`), so queries are real SQL.

Run from the repo root (the folder that contains db/ and scripts/):
  python3 scripts/db.py stats
  python3 scripts/db.py sql "SELECT stage,COUNT(*) FROM listing_status GROUP BY 1"
  python3 scripts/db.py harvest  <cl_nat.json> --source craigslist --hours 48 --cats ata,cba,... [--note ...]
  python3 scripts/db.py queue    <lens_pri.json> --run run14 --harvest <harvest_id>
  python3 scripts/db.py lens     <all.json> --run run14 [--pri lens_pri.json]      (Chrome exportAll() output)
  python3 scripts/db.py event    <pid> <stage> [--status keep|kill|pass|find|ask|...] [--type slug] [--note ...] [--run ...] [--data '{json}']
  python3 scripts/db.py comp     --type slug --query "exact search" --source ebay_sold --prices 120,95,210 [--pid ..] [--note ..]
  python3 scripts/db.py itemtype <slug> --name "Carved santo" [--volume c-d] [--aliases a,b]
  python3 scripts/db.py search   --site craigslist --query "..." --purpose "..." [--results N] [--run ...]
  python3 scripts/db.py run      <run_id> --data '{json summary}'
  python3 scripts/db.py seen     > seen.txt            (every pid already through Lens — feed to lens_prep.py)
  python3 scripts/db.py worklist <stage>               (listings whose latest stage is <stage>, e.g. flagged)
  python3 scripts/db.py show     <pid>                 (everything known about one listing)
"""
import json, os, sys, time, glob, sqlite3, argparse, datetime, statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, 'db')
SQLITE = os.environ.get('REFURB_SQLITE', '/tmp/refurb.sqlite')

# Pipeline stages, in order. A listing's current stage = its event with the latest ts (ties: later line wins).
STAGES = ['harvested', 'queued', 'lensed', 'flagged', 'photo_review', 'identified', 'comps',
          'decided', 'contacted', 'bought', 'listed', 'sold', 'expired']
# Tables: name -> (sharded by month?, key fields used for SQLite columns)
TABLES = {
    'harvests':   False,   # one row per harvest/search sweep of a site
    'searches':   False,   # one row per individual query typed anywhere (eBay comps, web, site search)
    'listings':   True,    # one row per listing the pipeline touched (first time it is seen)
    'lens':       True,    # one row per Google Lens result (every one, flagged or not)
    'events':     True,    # one row per stage change of a listing
    'comps':      False,   # sold-price comparables
    'item_types': False,   # encyclopedia index (slug -> name, volume); the prose lives in docs/encyclopedia
    'runs':       False,   # one summary row per run
}

# Base columns every table always has in SQLite (extra fields found in the data are added automatically)
SCHEMA = {
    'harvests': ['ts','harvest_id','source','hours','cats','n_listings','by_cat','file','note'],
    'searches': ['ts','site','query','purpose','results','run','note'],
    'listings': ['ts','pid','source','harvest_id','posted','price','title','area','region','cat','imgs','url'],
    'lens': ['ts','pid','run','i','img','price','best','med','n','ratio','collect','sources','ai','ai_value','flag'],
    'events': ['ts','pid','stage','status','type','note','run','by','data'],
    'comps': ['ts','type','query','source','prices','median','n','pid','note','run'],
    'item_types': ['ts','slug','name','volume','aliases','note'],
    'runs': ['ts','run'],
}

def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def month(ts=None):
    return (ts or now())[:7]

def path(table, ts=None):
    if TABLES[table]:
        d = os.path.join(DB, table); os.makedirs(d, exist_ok=True)
        return os.path.join(d, month(ts) + '.jsonl')
    os.makedirs(DB, exist_ok=True)
    return os.path.join(DB, table + '.jsonl')

def append(table, rows):
    rows = [rows] if isinstance(rows, dict) else list(rows)
    by = {}
    for r in rows:
        r.setdefault('ts', now())
        by.setdefault(path(table, r['ts']), []).append(r)
    for p, rs in by.items():
        with open(p, 'a') as f:
            for r in rs: f.write(json.dumps(r, separators=(',', ':'), ensure_ascii=False) + '\n')
    return len(rows)

def read(table):
    files = sorted(glob.glob(os.path.join(DB, table, '*.jsonl'))) if TABLES[table] else [os.path.join(DB, table + '.jsonl')]
    for p in files:
        if not os.path.exists(p): continue
        with open(p) as f:
            for line in f:
                line = line.strip()
                if line:
                    try: yield json.loads(line)
                    except Exception: pass

def known_pids():
    return {str(r['pid']) for r in read('listings')}

# ---------------------------------------------------------------- SQLite view
def build_sqlite():
    if os.path.exists(SQLITE): os.remove(SQLITE)
    con = sqlite3.connect(SQLITE)
    for t in TABLES:
        rows = list(read(t))
        cols = list(SCHEMA[t])
        for r in rows:
            for k in r:
                if k not in cols: cols.append(k)
        con.execute(f'CREATE TABLE {t} (' + ','.join(f'"{c}"' for c in cols) + ')')
        def val(v): return json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v
        con.executemany(f'INSERT INTO {t} VALUES (' + ','.join('?' * len(cols)) + ')',
                        [[val(r.get(c)) for c in cols] for r in rows])
    # current stage per listing = latest event
    con.executescript('''
    CREATE VIEW listing_status AS
      SELECT l.pid, l.source, l.title, l.price, l.area, l.cat, l.url, e.stage, e.status, e.type, e.note, e.ts AS stage_ts
      FROM listings l LEFT JOIN (
        SELECT * FROM events e1 WHERE rowid = (SELECT e2.rowid FROM events e2 WHERE e2.pid = e1.pid ORDER BY e2.ts DESC, e2.rowid DESC LIMIT 1)
      ) e ON e.pid = l.pid;
    ''')
    con.commit(); return con

def cmd_sql(q):
    con = build_sqlite(); cur = con.execute(q)
    names = [d[0] for d in cur.description] if cur.description else []
    print('\t'.join(names))
    for row in cur.fetchall(): print('\t'.join('' if v is None else str(v) for v in row))

# ---------------------------------------------------------------- writers
def cmd_harvest(a):
    L = json.load(open(a.file))
    cats = {}
    for r in L: cats[r.get('cat')] = cats.get(r.get('cat'), 0) + 1
    hid = a.id or f"{a.source}-{datetime.datetime.now().strftime('%Y%m%d-%H%M')}"
    append('harvests', {'harvest_id': hid, 'source': a.source, 'hours': a.hours, 'cats': a.cats,
                        'n_listings': len(L), 'by_cat': cats, 'file': os.path.basename(a.file), 'note': a.note})
    print(hid)

def cmd_queue(a):
    P = json.load(open(a.file)); have = known_pids(); rows = []; ev = []
    for i, r in enumerate(P):
        pid = str(r['pid'])
        if pid not in have:
            rows.append({'pid': pid, 'source': 'craigslist', 'harvest_id': a.harvest, 'posted': r.get('posted'),
                         'price': r.get('price'), 'title': r.get('title'), 'area': r.get('area'), 'region': r.get('region'),
                         'cat': r.get('cat'), 'imgs': r.get('imgs'),
                         'url': f"https://www.craigslist.org/view/d/{r.get('slug')}/{r.get('uuid')}"})
        ev.append({'pid': pid, 'stage': 'queued', 'run': a.run, 'data': {'pos': i}})
    append('listings', rows); append('events', ev)
    print(f'listings +{len(rows)}  queued events +{len(ev)}')

def cmd_lens(a):
    A = json.load(open(a.file)); P = json.load(open(a.pri or 'lens_pri.json'))
    already = {(r['run'], r['i']) for r in read('lens')}
    rows = []; ev = []
    for x in A:
        i = x.get('i')
        if i is None or i >= len(P) or (a.run, i) in already: continue
        r = P[i]
        if r['imgs'][0] != x.get('img'): print('WARN index mismatch at', i, file=sys.stderr); continue
        pid = str(r['pid']); ts = datetime.datetime.fromtimestamp((x.get('ts') or time.time()*1000)/1000, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        rows.append({'ts': ts, 'pid': pid, 'run': a.run, 'i': i, 'img': x.get('img'), 'price': x.get('price'),
                     'best': x.get('best'), 'med': x.get('med'), 'n': x.get('n'), 'ratio': x.get('ratio'),
                     'collect': x.get('c'), 'sources': x.get('s'), 'ai': x.get('ai'), 'ai_value': x.get('av'), 'flag': x.get('f')})
        ev.append({'ts': ts, 'pid': pid, 'stage': 'flagged' if x.get('f') else 'lensed', 'run': a.run,
                   'data': {'med': x.get('med'), 'ratio': x.get('ratio')}})
    append('lens', rows); append('events', ev)
    print(f'lens +{len(rows)}  flagged {sum(1 for r in rows if r["flag"])}')

def cmd_event(a):
    assert a.stage in STAGES, f'stage must be one of {STAGES}'
    append('events', {'pid': str(a.pid), 'stage': a.stage, 'status': a.status, 'type': a.type, 'note': a.note,
                      'run': a.run, 'by': a.by, 'data': json.loads(a.data) if a.data else None})
    print('ok')

def cmd_comp(a):
    prices = [float(p) for p in a.prices.split(',') if p.strip()] if a.prices else []
    append('comps', {'type': a.type, 'query': a.query, 'source': a.source, 'prices': prices,
                     'median': statistics.median(prices) if prices else None, 'n': len(prices),
                     'pid': a.pid, 'note': a.note, 'run': a.run})
    print('median', statistics.median(prices) if prices else None, 'n', len(prices))

def cmd_itemtype(a):
    append('item_types', {'slug': a.slug, 'name': a.name, 'volume': a.volume,
                          'aliases': a.aliases.split(',') if a.aliases else [], 'note': a.note}); print('ok')

def cmd_search(a):
    append('searches', {'site': a.site, 'query': a.query, 'purpose': a.purpose, 'results': a.results, 'run': a.run, 'note': a.note}); print('ok')

def cmd_run(a):
    d = json.loads(a.data); d['run'] = a.run_id; append('runs', d); print('ok')

def cmd_seen():
    s = {str(r['pid']) for r in read('lens')}
    print('\n'.join(sorted(s)))

def cmd_worklist(stage):
    con = build_sqlite()
    for row in con.execute('SELECT pid,price,area,title,url FROM listing_status WHERE stage=? ORDER BY stage_ts', (stage,)):
        print('\t'.join(str(v) for v in row))

def cmd_show(pid):
    pid = str(pid)
    for t in ('listings', 'lens', 'events', 'comps'):
        for r in read(t):
            if str(r.get('pid')) == pid: print(t, json.dumps(r, ensure_ascii=False))

def cmd_stats():
    for t in TABLES: print(f'{t:<11} {sum(1 for _ in read(t))}')
    con = build_sqlite()
    print('-- current stage of every listing')
    for row in con.execute('SELECT stage,status,COUNT(*) FROM listing_status GROUP BY 1,2 ORDER BY 3 DESC'): print(' ', *row)

if __name__ == '__main__':
    p = argparse.ArgumentParser(); s = p.add_subparsers(dest='c')
    x = s.add_parser('sql'); x.add_argument('q')
    x = s.add_parser('harvest'); x.add_argument('file'); x.add_argument('--source', default='craigslist'); x.add_argument('--hours', type=float); x.add_argument('--cats'); x.add_argument('--id'); x.add_argument('--note')
    x = s.add_parser('queue'); x.add_argument('file'); x.add_argument('--run', required=True); x.add_argument('--harvest')
    x = s.add_parser('lens'); x.add_argument('file'); x.add_argument('--run', required=True); x.add_argument('--pri')
    x = s.add_parser('event'); x.add_argument('pid'); x.add_argument('stage'); [x.add_argument('--' + k) for k in ('status', 'type', 'note', 'run', 'by', 'data')]
    x = s.add_parser('comp'); [x.add_argument('--' + k) for k in ('type', 'query', 'source', 'prices', 'pid', 'note', 'run')]
    x = s.add_parser('itemtype'); x.add_argument('slug'); [x.add_argument('--' + k) for k in ('name', 'volume', 'aliases', 'note')]
    x = s.add_parser('search'); [x.add_argument('--' + k) for k in ('site', 'query', 'purpose', 'results', 'run', 'note')]
    x = s.add_parser('run'); x.add_argument('run_id'); x.add_argument('--data', required=True)
    s.add_parser('seen'); s.add_parser('stats')
    x = s.add_parser('worklist'); x.add_argument('stage')
    x = s.add_parser('show'); x.add_argument('pid')
    a = p.parse_args()
    {'sql': lambda: cmd_sql(a.q), 'harvest': lambda: cmd_harvest(a), 'queue': lambda: cmd_queue(a), 'lens': lambda: cmd_lens(a),
     'event': lambda: cmd_event(a), 'comp': lambda: cmd_comp(a), 'itemtype': lambda: cmd_itemtype(a), 'search': lambda: cmd_search(a),
     'run': lambda: cmd_run(a), 'seen': cmd_seen, 'stats': cmd_stats, 'worklist': lambda: cmd_worklist(a.stage),
     'show': lambda: cmd_show(a.pid)}.get(a.c, p.print_help)()
