#!/usr/bin/env python3
"""FB review v3, Stage C prep: for each Stage-A identified flag, one side-by-side panel image — the Facebook listing
photo on the left, up to 8 eBay SOLD comps (thumbnail + price + date + title) on the right — plus judge batches.

  python3 scripts/fb_comp_panels.py <A.tsv> <comps.json> <outdir> [--per 20]

A.tsv   Stage A lines: run, sheet, cell, id, identification, q1||q2, checks (research/FB_VERIFY_BRIEF.md)
comps   {query: [{t, p, d, id, img}]} from tools/ebay_sold_comps.js
Writes <outdir>/panel_<fbid>.jpg, <outdir>/flags.json, <outdir>/judge_NN.md."""
import sys, os, json, glob, hashlib, subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont

A, C, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
PER = int(sys.argv[sys.argv.index('--per') + 1]) if '--per' in sys.argv else 20
os.makedirs(OUT, exist_ok=True); CACHE = os.path.join(OUT, 'img'); os.makedirs(CACHE, exist_ok=True)
comps = json.load(open(C))
idx = {f.split('/')[3]: json.load(open(f)) for f in glob.glob('/tmp/eye/fbx-*/index.json')}
F = glob.glob('/usr/share/fonts/**/DejaVuSans.ttf', recursive=True)[0]
font, bold = ImageFont.truetype(F, 15), ImageFont.truetype(F.replace('DejaVuSans.ttf', 'DejaVuSans-Bold.ttf'), 17)

def fetch(url):
    p = os.path.join(CACHE, hashlib.md5(url.encode()).hexdigest() + '.jpg')
    if not os.path.exists(p): subprocess.run(['curl', '-s', '-m', '20', '-o', p, url])
    try: return Image.open(p).convert('RGB')
    except Exception: return None

flags = []
for ln in open(A):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 6 or p[3] != 'id': continue
    run, sh, cell = p[0], p[1], p[2]
    r = idx.get(run, {}).get(f'{sh}:{cell}')
    if not r: continue
    seen, cs = set(), []
    for q in p[5].split('||'):
        for c in comps.get(q.strip(), []):
            if c.get('id') and c['id'] not in seen: seen.add(c['id']); cs.append(dict(c, q=q.strip()))
    cs = cs[:8]
    W, H = 1400, 420 + 230 * ((len(cs) + 3) // 4)
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    lp = Image.open(f'/tmp/eye/{run}/panels/{r["id"]}.jpg').convert('RGB').crop((2, 2, 398, 398))
    im.paste(lp, (10, 10)); d.text((420, 14), 'FACEBOOK LISTING', font=bold, fill='black')
    y = 40
    for line in textwrap.wrap(f'{r["t"]} — ${r["p"]:.0f}', 90)[:3] + ['Stage A: ' + s for s in textwrap.wrap(p[4], 90)[:4]]:
        d.text((420, y), line, font=font, fill='black'); y += 20
    d.text((420, y + 10), f'eBay SOLD comps: {len(cs)} (searched: {p[5]})'[:120], font=bold, fill='#14487a')
    for k, c in enumerate(cs):
        x0, y0 = 10 + (k % 4) * 345, 420 + (k // 4) * 230
        t = fetch(c['img']) if c.get('img', '').startswith('https://i.ebayimg.com/') else None
        if t: t.thumbnail((150, 150)); im.paste(t, (x0, y0))
        d.text((x0 + 155, y0), f'#{k + 1} {c.get("p", "")}', font=bold, fill='#a23b1e')
        d.text((x0 + 155, y0 + 22), c.get('d', '')[:22], font=font, fill='black')
        for j, line in enumerate(textwrap.wrap(c.get('t', ''), 22)[:7]): d.text((x0 + 155, y0 + 44 + j * 18), line, font=font, fill='#333')
    path = os.path.join(OUT, f'panel_{r["id"]}.jpg'); im.save(path, quality=82)
    flags.append(dict(run=run, sheet=sh, cell=cell, id=r['id'], title=r['t'], price=r['p'], url=r['url'],
                      ident=p[4], checks=p[6] if len(p) > 6 else '', panel=path,
                      comps=[{k2: c.get(k2) for k2 in ('t', 'p', 'd', 'id', 'img')} for c in cs]))
json.dump(flags, open(os.path.join(OUT, 'flags.json'), 'w'), indent=1)
for b in range(0, len(flags), PER):
    with open(os.path.join(OUT, f'judge_{b // PER:02d}.md'), 'w') as f:
        for i, x in enumerate(flags[b:b + PER]):
            f.write(f"- n {b + i} | run {x['run']} | sheet {x['sheet']} | cell {x['cell']} | ${x['price']:.0f} | {x['title']} | panel: {x['panel']} | Stage A: {x['ident']} | checks: {x['checks']}\n")
print(len(flags), 'flags,', sum(1 for x in flags if len(x['comps']) >= 2), 'with ≥2 comps;', (len(flags) + PER - 1) // PER, 'batches')
