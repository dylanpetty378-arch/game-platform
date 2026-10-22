#!/usr/bin/env python3
"""Low-usage Claude session tooling (Oct 21 2026). Reads the free shortlist and prepares everything an eye needs in
as few tool calls as possible. Procedure: docs/low-usage.md.

  python3 scripts/lowuse.py prep [--max 1000]          # git-pulled shortlist -> /tmp/eye/lu-<ts>/: sheets, per-sheet
                                                      #   encyclopedia notes, agent batches (prints the run name)
  python3 scripts/lowuse.py panels <run> <flags.tsv>   # flagged cells -> one photo panel per item (all photos) + flagged.md
  python3 scripts/lowuse.py log <run> <verdicts.tsv>   # verdicts -> db listings/events + research/pools/lowuse-log.jsonl
  python3 scripts/lowuse.py misses [days]              # weekly: the last <days> (7) of misses -> /tmp/eye/misses-<ts>/ sheets

flags.tsv    lines: sheet<TAB>cell<TAB>why                     (cell = the yellow number)
verdicts.tsv lines: sheet<TAB>cell<TAB>egg|lead|kill<TAB>value_low<TAB>max_bid<TAB>note

Sheets are 8×6 = 48 photos at 220 px (larger than the old 120-cell sheets: the eye reads marks and quality, not
just shape). Each sheet has a notes file listing each cell's price/bids/title and the CLIP-matched encyclopedia
types, followed by the money tells (top tier + photo tell) of every type matched on that sheet, plus the
highest-value tells overall, so the eye judges with the encyclopedia without loading it.
"""
import os, sys, io, re, json, time, datetime as dt, urllib.request, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
SL = os.path.join(ROOT, 'research', 'pools', 'shortlist.json')
DIG = os.path.join(ROOT, 'research', 'enc_digest.json')
COLS, ROWS, CELL = 8, 6, 220
PER = COLS * ROWS

def wdir(run): d = f'/tmp/eye/{run}'; os.makedirs(d, exist_ok=True); return d

def fetch(u):
    from PIL import Image
    try:
        b = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=25).read()
        return Image.open(io.BytesIO(b)).convert('RGB')
    except Exception: return None

def tags(r):
    """Data signals for a row, in words the eye and the deep review can use."""
    out = []
    m = r.get('melt')
    if m and m['net'] >= 25: out.append(f"MELT {m['label']} {m['g']}g floor ${m['net']} (max bid ${m['max_bid']}{', CLEARS RULE' if m.get('ok') else ''})")
    k = r.get('knn')
    if k: out.append(f"SIMILAR SOLD (SGW, picker prices) median ${k['p50']} p75 ${k['p75']} n={k['n']}: " +
                     '; '.join(f"${f} {t}" for f, _, t in k['best'][:2]))
    o = r.get('ocr') or {}
    if o.get('makers'): out.append('PHOTO MARK (not in title): ' + ', '.join(o['makers']))
    if o.get('metal'): out.append(f"PHOTO METAL MARK: {o['metal']}")
    if o.get('text') and not o.get('makers'): out.append('photo text: ' + o['text'][:80])
    return out

def ended(r):
    e = r.get('end') or ''
    try:
        if e.endswith(' PT'): t = dt.datetime.fromisoformat(e[:-3]).replace(tzinfo=dt.timezone(dt.timedelta(hours=-7)))
        else: t = dt.datetime.fromisoformat(e.replace('Z', '+00:00'))
        return t < dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=30)
    except Exception: return False

def hours_left(r):
    e = r.get('end') or ''
    try:
        if e.endswith(' PT'): t = dt.datetime.fromisoformat(e[:-3]).replace(tzinfo=dt.timezone(dt.timedelta(hours=-7)))
        else: t = dt.datetime.fromisoformat(e.replace('Z', '+00:00'))
        return (t - dt.datetime.now(dt.timezone.utc)).total_seconds() / 3600
    except Exception: return None

def prep(maxn=1000, agents=None, path=SL, prefix='lu'):
    from PIL import Image, ImageDraw
    from enc_digest import line
    S = json.load(open(path)); dig = json.load(open(DIG))
    rows = [r for r in S['rows'] if not ended(r)][:maxn]
    run = prefix + '-' + time.strftime('%Y%m%d-%H%M', time.gmtime()); d = wdir(run)
    big = [u.replace('s-l500', 's-l500') for u in (r['img'] for r in rows)]
    with cf.ThreadPoolExecutor(24) as ex: ims = list(ex.map(fetch, big))
    top_tells = sorted(((s, e) for s, e in dig.items() if e['top'] >= 2000), key=lambda x: -x[1]['top'])[:40]
    index, nsheets = {}, (len(rows) + PER - 1) // PER
    for k in range(nsheets):
        part = rows[k * PER:(k + 1) * PER]
        sh = Image.new('RGB', (COLS * CELL, ((len(part) + COLS - 1) // COLS) * CELL), 'white'); dr = ImageDraw.Draw(sh)
        notes = [f'# Sheet {k + 1} of {nsheets} — {len(part)} listings (cell number = yellow tag, top-left)\n',
                 'cell | source | price, bids, hours left | title | encyclopedia types the photo resembles (CLIP, prob)']
        types = {}
        for j, r in enumerate(part):
            im = ims[k * PER + j]; x, y = (j % COLS) * CELL, (j // COLS) * CELL
            if im: im.thumbnail((CELL - 4, CELL - 4)); sh.paste(im, (x + 2, y + 2))
            dr.rectangle([x, y, x + 34, y + 16], fill='yellow'); dr.text((x + 3, y + 2), str(j), fill='black')
            h = hours_left(r); hl = f'{h:.0f}h' if h is not None else '?'
            tps = [f"{s} {p:.1f}" for s, p in r.get('types', []) if p >= 0.15]
            for s, p in r.get('types', []):
                if p >= 0.25 and s in dig and dig[s]['top'] >= 300: types[s] = max(types.get(s, 0), p)
            dn = (' ↓LABELLED CHEAP: ' + ','.join(r['down'])) if r.get('down') else ''
            notes.append(f"{j} | {r['src']} | ${r['p']}, {r['b']}b, {hl} | {r['t'][:75]} | {', '.join(tps[:2])}{dn}")
            for tg in tags(r): notes.append(f"    ↳ {tg}")
            index[f'{k + 1}:{j}'] = r
        sh.save(f'{d}/sheet_{k + 1:02d}.jpg', quality=80)
        notes.append('\n## Encyclopedia money tells for the types on this sheet (top tier = where the money is)')
        for s in sorted(types, key=lambda s: -dig[s]['top'])[:16]: notes.append(line(s, dig[s], 1))
        open(f'{d}/sheet_{k + 1:02d}.md', 'w').write('\n'.join(notes) + '\n')
    open(f'{d}/top-tells.md', 'w').write('# Highest-value types in the encyclopedia — look for these anywhere\n' +
                                          '\n'.join(line(s, e, 1, 120) for s, e in top_tells[:30]) + '\n')
    json.dump(index, open(f'{d}/index.json', 'w'))
    agents = agents or max(1, min(4, (nsheets + 6) // 7))
    batches = [[i + 1 for i in range(nsheets) if i % agents == a] for a in range(agents)]
    json.dump(batches, open(f'{d}/batches.json', 'w'))
    src = {s: sum(r['src'] == s for r in rows) for s in ('ebay', 'sgw')}
    print(f"{run}: {len(rows)} live listings ({src}), {nsheets} sheets, {agents} agent batches {batches} | shortlist made {S['made'][:16]}Z "
          f"from pool {S.get('pool')}")

def read_tsv(p, n):
    out = []
    for ln in open(p):
        x = ln.rstrip('\n').split('\t')
        if len(x) >= 2 and x[0].strip().isdigit(): out.append(x + [''] * (n - len(x)))
    return out

def panels(run, tsv):
    from PIL import Image, ImageDraw
    d = wdir(run); index = json.load(open(f'{d}/index.json')); md = ['# Flagged — full photos in panels/<id>.jpg\n']
    os.makedirs(f'{d}/panels', exist_ok=True)
    for sh, cell, why, *_ in read_tsv(tsv, 3):
        r = index.get(f'{int(sh)}:{int(cell)}')
        if not r: md.append(f'- {sh}:{cell} not found'); continue
        det = r.get('det') or {}
        if not det and r['src'] == 'sgw':
            try:
                import sgw; dd, desc, imgs = sgw._detail(r['id']); det = {'imgs': imgs, 'desc': desc[:1200], 'weight': dd.get('displayWeight')}
            except Exception: pass
        imgs = (det.get('imgs') or [r['img']])[:12]
        with cf.ThreadPoolExecutor(12) as ex: ims = list(ex.map(fetch, imgs))
        C, W = 4, 400; n = len(ims); P = Image.new('RGB', (C * W, ((n + C - 1) // C) * W), 'white'); dr = ImageDraw.Draw(P)
        for j, im in enumerate(ims):
            if im: im.thumbnail((W - 4, W - 4)); P.paste(im, ((j % C) * W + 2, (j // C) * W + 2))
            dr.rectangle([(j % C) * W, (j // C) * W, (j % C) * W + 26, (j // C) * W + 16], fill='yellow')
            dr.text(((j % C) * W + 3, (j // C) * W + 2), str(j + 1), fill='black')
        P.save(f"{d}/panels/{r['id']}.jpg", quality=82)
        md.append(f"## {sh}:{cell} {r['id']} — ${r['p']} {r['b']} bids, ends {r.get('end')} — {r['src']}\n{r['t']}\n{r['url']}\n"
                  f"eye: {why}\ntypes: {r.get('types')}\nphotos: {len(imgs)} (of {len(det.get('imgs') or [1])}) · ship {det.get('ship')} · "
                  f"weight {det.get('weight')} · loc {det.get('loc')} · cond {det.get('cond')}\naspects: {det.get('aspects')}\n"
                  f"signals: {' · '.join(tags(r)) or 'none'}\n"
                  f"desc: {(det.get('desc') or '')[:900]}\n")
    open(f'{d}/flagged.md', 'w').write('\n'.join(md))
    print(len(md) - 1, 'flagged ->', f'{d}/flagged.md', 'and', f'{d}/panels/')

def log(run, tsv):
    import db
    d = wdir(run); index = json.load(open(f'{d}/index.json')); ev, li, lg = [], [], []
    known = db.known_pids()
    for sh, cell, verdict, vlow, mx, note in read_tsv(tsv, 6):
        r = index.get(f'{int(sh)}:{int(cell)}')
        if not r: continue
        pid = r['id']
        if pid not in known:
            li.append({'pid': pid, 'source': {'ebay': 'ebay', 'fb': 'facebook'}.get(r['src'], 'shopgoodwill'), 'harvest_id': run, 'posted': 0,
                       'price': r['p'], 'title': r['t'], 'area': '', 'region': r['src'].upper(), 'cat': r.get('c'),
                       'imgs': (r.get('det') or {}).get('imgs') or [r['img']], 'score': r.get('score'), 'clip': r.get('egg'),
                       'url': r['url'], 'ends': r.get('end'), 'bids': r['b']})
        v = verdict.strip().lower()
        ev.append({'pid': pid, 'stage': 'decided', 'run': run, 'by': 'claude', 'status': {'egg': 'find', 'lead': 'find'}.get(v, 'kill'),
                   'note': note, 'data': {'verdict': v, 'value_low': vlow, 'max_bid': mx, 'types': r.get('types'), 'mode': 'lowuse'}})
        lg.append({'ts': db.now(), 'run': run, 'pid': pid, 'verdict': v, 'value_low': vlow, 'max_bid': mx, 'title': r['t'],
                   'url': r['url'], 'price': r['p'], 'end': r.get('end'), 'note': note})
    if li: db.append('listings', li)
    if ev: db.append('events', ev)
    with open(os.path.join(ROOT, 'research', 'pools', 'lowuse-log.jsonl'), 'a') as f:
        for x in lg: f.write(json.dumps(x, ensure_ascii=False) + '\n')
    print(len(ev), 'verdicts logged')

def misses(days=7):
    """Weekly review input: top misses of the last <days> days as 48-cell sheets + notes (cell -> final, title)."""
    from PIL import Image, ImageDraw
    import glob, outcomes
    files = sorted(glob.glob(os.path.join(ROOT, 'research', 'pools', 'misses', '*.md')))[-days:]
    rows = []
    for f in files:
        for ln in open(f):
            if ln.startswith('- $'):
                x = [p.strip() for p in ln[2:].split(' · ')]
                rows.append({'final': x[0], 'bids': x[1], 'seen': x[3], 't': x[4], 'cat': x[5], 'img': x[6]})
    rows = rows[:240]
    run = 'misses-' + time.strftime('%Y%m%d-%H%M', time.gmtime()); d = wdir(run)
    with cf.ThreadPoolExecutor(24) as ex: ims = list(ex.map(fetch, [r['img'] for r in rows]))
    for k in range(0, len(rows), PER):
        part = rows[k:k + PER]; sh = Image.new('RGB', (COLS * CELL, ((len(part) + COLS - 1) // COLS) * CELL), 'white')
        dr = ImageDraw.Draw(sh); notes = [f'# Misses sheet {k // PER + 1} — sold high, title silent. What is it, and what in the photo showed it?']
        for j, r in enumerate(part):
            im = ims[k + j]; x, y = (j % COLS) * CELL, (j // COLS) * CELL
            if im: im.thumbnail((CELL - 4, CELL - 4)); sh.paste(im, (x + 2, y + 2))
            dr.rectangle([x, y, x + 34, y + 16], fill='yellow'); dr.text((x + 3, y + 2), str(j), fill='black')
            notes.append(f"{j} | {r['final']} {r['bids']} | {r['seen']} | {r['t']} | {r['cat']}")
        sh.save(f'{d}/sheet_{k // PER + 1:02d}.jpg', quality=80); open(f'{d}/sheet_{k // PER + 1:02d}.md', 'w').write('\n'.join(notes) + '\n')
    print(run, len(rows), 'misses from', len(files), 'days ->', d)

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == 'prep':
        m = int(a[a.index('--max') + 1]) if '--max' in a else 1000
        g = int(a[a.index('--agents') + 1]) if '--agents' in a else None
        prep(m, g)
    elif a[0] == 'panels': panels(a[1], a[2])
    elif a[0] == 'log': log(a[1], a[2])
    elif a[0] == 'misses': misses(int(a[1]) if len(a) > 1 else 7)
