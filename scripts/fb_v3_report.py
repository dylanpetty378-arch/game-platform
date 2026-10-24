#!/usr/bin/env python3
"""FB review v3: build a dated site report (db/fbreport/<rep>.jsonl) from Stage C judge output.

  python3 scripts/fb_v3_report.py <C dir> <rep> <meta.json>

<C dir> holds flags.json (fb_comp_panels.py) and out_*.json (judge agents, research/FB_JUDGE_BRIEF.md).
meta.json = {title, made, reviewed, summary_md (may use {N} {A} {B} {C}), howto_md, method_md}."""
import sys, os, json, glob, base64, io, re
from PIL import Image
C, REP, META = sys.argv[1], sys.argv[2], sys.argv[3]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
flags = json.load(open(os.path.join(C, 'flags.json')))
idx = {f.split('/')[3]: json.load(open(f)) for f in glob.glob('/tmp/eye/fbx-*/index.json')}
items, kills = [], 0
for f in sorted(glob.glob(os.path.join(C, 'out_*.json'))):
    for o in json.load(open(f)):
        fl = flags[int(o['n'])]
        if o.get('verdict') != 'lead': kills += 1; continue
        m = re.search(r'\[([^\[\]]*?)\s+(\d+)mi\b[^\]]*\]\s*$', fl['title'])
        im = Image.open(f"/tmp/eye/{fl['run']}/panels/{fl['id']}.jpg").convert('RGB').crop((2, 2, 398, 398)); im.thumbnail((400, 400))
        b = io.BytesIO(); im.save(b, 'JPEG', quality=80)
        match = [int(k) - 1 for k in o.get('match', []) if str(k).isdigit() and 0 < int(k) <= len(fl['comps'])]
        comps = [fl['comps'][k] for k in match] or fl['comps'][:3]
        it = dict(kind='item', id=fl['id'], title=re.sub(r'\s*\[.*?\]\s*$', '', fl['title']), price=fl['price'],
                  value=o.get('value'), max_offer=o.get('max_offer'), city=m.group(1) if m else '', mi=int(m.group(2)) if m else None,
                  url=fl['url'], photo='data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode(), comps=comps)
        for k in ('name', 'category', 'tier', 'confidence', 'size', 'price_note', 'what', 'evidence', 'resale', 'plan',
                  'checks', 'message', 'offer_plan', 'risks'):
            it[k] = o.get(k, [] if k == 'checks' else '')
        if it['tier'] not in ('A', 'B', 'C'): it['tier'] = 'C'
        items.append(it)
items.sort(key=lambda x: ('ABC'.index(x['tier']), -((x['value'] or 0) - (x['max_offer'] or 0))))
for n, it in enumerate(items, 1): it['rank'] = n
meta = json.load(open(META)); meta.update(kind='meta', report=REP)
t = {k: sum(1 for x in items if x['tier'] == k) for k in 'ABC'}
for k in ('summary_md', 'method_md'): meta[k] = meta[k].replace('{N}', str(len(items))).replace('{A}', str(t['A'])).replace('{B}', str(t['B'])).replace('{C}', str(t['C'])).replace('{K}', str(kills)).replace('{F}', str(len(flags)))
out = os.path.join(ROOT, 'db', 'fbreport', REP + '.jsonl')
with open(out, 'w') as f:
    f.write(json.dumps(meta) + '\n')
    for it in items: f.write(json.dumps(it) + '\n')
print(out, len(items), 'leads', t, kills, 'kills')
for x in items: print(x['rank'], x['tier'], x['name'], '|', x['price'], '->', x['value'], '|', x['city'], x['mi'], '|', len(x['comps']), 'comps')
