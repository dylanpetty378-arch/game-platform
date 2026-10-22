#!/usr/bin/env python3
"""Facebook Marketplace (Oct 22 2026): listings Dylan's Refurbish Watcher extension saved, scored for free, reviewed on demand.

The extension (tools/fb-extension, runs in Chrome on Dylan's home computer when he starts it) writes JSON batches to
db/fb/inbox/ on branch refurbish. Then:

  python3 scripts/fb.py score            # GitHub Actions (fb-score workflow, on every inbox push): new inbox rows ->
                                         #   text filters, CLIP egg/type, encyclopedia value, similar-sold (kNN), melt floor,
                                         #   distance from Keller -> db/fb/scored/<date>.jsonl
  python3 scripts/fb.py prep [--max 480] # a Claude chat ("review the facebook posts"): unreviewed scored rows, best first,
                                         #   -> /tmp/eye/fb-<ts>/ sheets + notes, exactly like scripts/lowuse.py prep
  python3 scripts/fb.py done <run>       # after verdicts are logged: every row shown in <run> -> db/fb/reviewed.jsonl
  python3 scripts/fb.py stats            # inbox / scored / reviewed counts, last sweep

Facebook rows are LOCAL PICKUP around Keller TX: ≤ 30 mi on short notice, ≤ 50 mi with notice (Dylan, Oct 22 2026).
Fixed prices (usually negotiable), and good ones go within hours — review soon after a sweep.
Only listing data is stored (id, title, price, city, photo URL, category). Never seller names or profiles.
"""
import os, sys, re, json, glob, math, time, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
FB = os.path.join(ROOT, 'db', 'fb')
STATE = os.path.join(FB, 'state.json')
REVIEWED = os.path.join(FB, 'reviewed.jsonl')
KELLER = (32.934, -97.229)
MAX_PRICE = 400
KEEP_DAYS = 7          # unreviewed rows older than this drop out of the review queue (they've sold by then)

# approximate city centres, DFW and around (for the 30 / 50 mile bands)
CITY = {'keller': (32.934, -97.229), 'fort worth': (32.755, -97.331), 'dallas': (32.777, -96.797), 'arlington': (32.736, -97.108),
        'denton': (33.215, -97.133), 'grapevine': (32.934, -97.078), 'southlake': (32.941, -97.134), 'colleyville': (32.881, -97.155),
        'euless': (32.837, -97.082), 'bedford': (32.844, -97.143), 'hurst': (32.823, -97.171), 'north richland hills': (32.834, -97.229),
        'richland hills': (32.816, -97.228), 'haltom city': (32.800, -97.269), 'watauga': (32.858, -97.255), 'roanoke': (33.004, -97.226),
        'trophy club': (32.998, -97.184), 'westlake': (32.991, -97.195), 'flower mound': (33.015, -97.097), 'lewisville': (33.046, -96.994),
        'coppell': (32.954, -97.015), 'irving': (32.814, -96.949), 'grand prairie': (32.746, -96.998), 'mansfield': (32.563, -97.142),
        'burleson': (32.542, -97.321), 'weatherford': (32.759, -97.797), 'azle': (32.895, -97.546), 'saginaw': (32.860, -97.364),
        'haslet': (32.975, -97.348), 'justin': (33.085, -97.296), 'argyle': (33.121, -97.183), 'carrollton': (32.954, -96.890),
        'plano': (33.020, -96.699), 'frisco': (33.151, -96.824), 'mckinney': (33.198, -96.615), 'allen': (33.103, -96.671),
        'richardson': (32.948, -96.730), 'garland': (32.913, -96.639), 'mesquite': (32.767, -96.599), 'cleburne': (32.348, -97.387),
        'granbury': (32.442, -97.794), 'decatur': (33.234, -97.586), 'little elm': (33.163, -96.937), 'the colony': (33.089, -96.886),
        'crowley': (32.579, -97.362), 'benbrook': (32.673, -97.461), 'white settlement': (32.759, -97.458), 'lake worth': (32.805, -97.445),
        'duncanville': (32.652, -96.908), 'cedar hill': (32.588, -96.957), 'desoto': (32.590, -96.857), 'rowlett': (32.903, -96.564),
        'sanger': (33.364, -97.174), 'aubrey': (33.304, -96.986), 'prosper': (33.236, -96.801), 'celina': (33.325, -96.784),
        'midlothian': (32.482, -96.994), 'waxahachie': (32.387, -96.848), 'rockwall': (32.931, -96.459), 'wylie': (33.015, -96.539),
        'springtown': (32.966, -97.683), 'aledo': (32.696, -97.602), 'krum': (33.262, -97.238), 'corinth': (33.154, -97.065),
        'highland village': (33.092, -97.047), 'kennedale': (32.647, -97.226), 'forest hill': (32.672, -97.269),
        'everman': (32.631, -97.289), 'joshua': (32.461, -97.388), 'keene': (32.397, -97.324), 'alvarado': (32.407, -97.212),
        'boyd': (33.079, -97.565), 'rhome': (33.053, -97.471), 'northlake': (33.083, -97.256), 'ponder': (33.183, -97.287),
        'pilot point': (33.396, -96.960), 'addison': (32.962, -96.838), 'farmers branch': (32.927, -96.896), 'university park': (32.850, -96.800),
        'highland park': (32.833, -96.792), 'sachse': (32.976, -96.595), 'lancaster': (32.592, -96.756), 'red oak': (32.518, -96.804),
        'ennis': (32.330, -96.625), 'terrell': (32.736, -96.275), 'forney': (32.748, -96.472), 'seagoville': (32.640, -96.538),
        'balch springs': (32.729, -96.623), 'sunnyvale': (32.796, -96.561), 'princeton': (33.180, -96.498), 'anna': (33.349, -96.548),
        'melissa': (33.286, -96.573), 'mineral wells': (32.808, -98.113), 'stephenville': (32.221, -98.202), 'gainesville': (33.626, -97.133)}

def miles(city):
    c = CITY.get((city or '').lower().strip())
    if not c: return None
    la1, lo1 = map(math.radians, KELLER); la2, lo2 = map(math.radians, c)
    a = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return round(3959 * 2 * math.asin(math.sqrt(a)))

def band(mi):
    if mi is None: return '?mi'
    return f'{mi}mi' + ('' if mi <= 30 else ' (needs notice)' if mi <= 50 else ' (too far?)')

def load_jsonl(p):
    if not os.path.exists(p): return []
    out = []
    for l in open(p):
        try: out.append(json.loads(l))
        except Exception: pass
    return out

def scored_rows(days=KEEP_DAYS):
    fs = sorted(glob.glob(os.path.join(FB, 'scored', '*.jsonl')))[-days - 1:]
    return [r for f in fs for r in load_jsonl(f)]

# ---------------------------------------------------------------- score (GitHub Actions)
def score():
    st = json.load(open(STATE)) if os.path.exists(STATE) else {'scored_files': []}
    done = set(st['scored_files'])
    files = [f for f in sorted(glob.glob(os.path.join(FB, 'inbox', '*.json'))) if os.path.basename(f) not in done]
    if not files: print('fb: nothing new in inbox'); return
    have = {r['id'] for r in scored_rows(30)}
    rows, seen = [], set()
    for f in files:
        try: d = json.load(open(f))
        except Exception as e: print('bad inbox file', f, e); continue
        for x in d.get('rows', []):
            k = 'fb' + str(x.get('id'))
            if k in have or k in seen or x.get('sold'): continue
            seen.add(k)
            rows.append({'src': 'fb', 'id': k, 't': (x.get('t') or '')[:140], 'p': float(x.get('p') or 0), 'b': 0, 'end': None,
                         'img': x.get('img') or '', 'url': f"https://www.facebook.com/marketplace/item/{x.get('id')}/",
                         'c': x.get('cat') or '', 'city': x.get('city') or '', 'st': x.get('st') or '', 'seen': x.get('ts')})
    print(f'fb: {len(rows)} new listings from {len(files)} inbox files', flush=True)
    import shortlist, melt
    from enc_digest import build
    makers = shortlist.load_makers()
    keep = []
    for r in rows:
        r['mi'] = miles(r['city'])
        if r['p'] > MAX_PRICE or not r['img'] or shortlist.JUNK.search(r['t']): continue
        if r['mi'] is not None and r['mi'] > 60: continue
        m = melt.floor(r['t'], r['p'])
        if m: r['melt'] = m
        r['ign'] = shortlist.ign_score(r['t'], r['p'], 0)
        r['down'] = sorted(set(w.lower() for w in shortlist.DOWN.findall(r['t'])))[:4]
        r['maker'] = bool(makers and makers.search(r['t']))        # fixed price + seller named it: usually priced to match
        keep.append(r)
    print(f'fb: {len(keep)} after filters (price ≤ ${MAX_PRICE}, ≤ 60 mi, junk)', flush=True)
    if keep:
        digest = {k: v for k, v in build().items() if v['top']}
        clip = shortlist.Clip(digest); keep = clip.run(keep)
        try:
            import knn; knn.query(keep)
        except Exception as e: print('::warning::knn failed:', e)
        for r in keep:
            k = r.get('knn'); r['kv'] = math.log10(max(k['p50'], 1) / max(r['p'], 5)) if k else 0
            r['dv'] = (1 + 0.5 * (len(r['down']) - 1)) * r['spread'] if r['down'] else 0
        z = shortlist.z
        if len(keep) > 1:
            for r, ze, zt, zi, zd, zk in zip(keep, z([r['egg'] for r in keep]), z([r['tval'] for r in keep]),
                                             z([r['ign'] for r in keep]), z([r['dv'] for r in keep]), z([r['kv'] for r in keep])):
                r['score'] = round(ze + 0.8 * zt + 0.5 * zi + 0.7 * zd + 0.8 * zk - (0.7 if r['maker'] else 0)
                                   + (3 if r.get('melt', {}).get('ok') else 0) - (0.5 if (r['mi'] or 0) > 30 else 0), 3)
        else:
            keep[0]['score'] = 0
        for r in keep: r.pop('_e', None)
    os.makedirs(os.path.join(FB, 'scored'), exist_ok=True)
    p = os.path.join(FB, 'scored', dt.date.today().isoformat() + '.jsonl')
    with open(p, 'a') as f:
        for r in keep: f.write(json.dumps(r, ensure_ascii=False) + '\n')
    st['scored_files'] = sorted(done | {os.path.basename(f) for f in files})[-5000:]
    json.dump(st, open(STATE, 'w'))
    print(f"fb: scored {len(keep)} -> {p}; melt leads {sum(1 for r in keep if r.get('melt', {}).get('ok'))}", flush=True)

# ---------------------------------------------------------------- review (Claude chat)
def prep(maxn=480, agents=None):
    import lowuse
    rev = {r['id'] for r in load_jsonl(REVIEWED)}
    q = [r for r in scored_rows() if r['id'] not in rev]
    q.sort(key=lambda r: -r.get('score', 0))
    for r in q: r['t'] = f"{r['t']} [{r.get('city') or '?'} {band(r.get('mi'))}]"
    path = '/tmp/fb_queue.json'
    json.dump({'made': dt.datetime.now(dt.timezone.utc).isoformat(), 'pool': {'fb': len(q)}, 'rows': q[:maxn]}, open(path, 'w'))
    print(f'fb queue: {len(q)} unreviewed (last {KEEP_DAYS} days); sheets for the top {min(maxn, len(q))}')
    lowuse.prep(maxn, agents, path=path, prefix='fb')

def done(run):
    idx = json.load(open(f'/tmp/eye/{run}/index.json'))
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    with open(REVIEWED, 'a') as f:
        for r in idx.values(): f.write(json.dumps({'id': r['id'], 'run': run, 'ts': now}) + '\n')
    print(len(idx), 'facebook rows marked reviewed')

def stats():
    inbox = sorted(glob.glob(os.path.join(FB, 'inbox', '*.json')))
    rev = {r['id'] for r in load_jsonl(REVIEWED)}; sc = scored_rows()
    last = json.load(open(inbox[-1])).get('sweep') if inbox else None
    print(f'inbox files {len(inbox)} | scored (last {KEEP_DAYS} d) {len(sc)} | unreviewed {sum(r["id"] not in rev for r in sc)} | last sweep {last}')

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == 'score': score()
    elif a[0] == 'prep': prep(int(a[a.index('--max') + 1]) if '--max' in a else 480)
    elif a[0] == 'done': done(a[1])
    elif a[0] == 'stats': stats()
