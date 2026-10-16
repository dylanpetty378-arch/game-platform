#!/usr/bin/env python3
"""Hallmark run (Oct 15 2026): one panel image per listing showing EVERY photo, so marks on backs/clasps/case insides can
be read (thumbnails can't show them). Brief: research/HALLMARK_EYE_BRIEF.md.

  python3 scripts/hallmark_panels.py <detail.json> <outdir> [source]
detail.json = {"<id>": {"title":..., "imgs": [urls], "bid":..., "end":..., "url":...}}  (ebay-detail.json or sgw detail dump)
-> <outdir>/panels/p0001.jpg … + <outdir>/index.json {"1": {...row}}
"""
import json, os, sys, urllib.request, concurrent.futures as cf
from PIL import Image, ImageDraw, ImageFont

TILE, COLS, MAXIMG = 520, 4, 12

def fetch(url, path):
    if os.path.exists(path): return path
    url = url.replace('s-l225', 's-l1600').replace('s-l500', 's-l1600')
    for _ in range(3):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).read()
            open(path, 'wb').write(data); return path
        except Exception: pass
    return None

def panel(n, key, row, out, font):
    imgs = [u for u in (row.get('imgs') or []) if u][:MAXIMG]
    paths = [fetch(u, f"{out}/img/{key}_{i}.jpg") for i, u in enumerate(imgs)]
    paths = [p for p in paths if p]
    if not paths: return False
    rows = (len(paths) + COLS - 1) // COLS
    sheet = Image.new('RGB', (COLS * TILE, rows * TILE + 40), 'white'); d = ImageDraw.Draw(sheet)
    d.text((8, 6), f"#{n}  ${row.get('bid')}  {str(row.get('title'))[:110]}", fill='black', font=font)
    for i, p in enumerate(paths):
        try:
            im = Image.open(p).convert('RGB'); im.thumbnail((TILE - 6, TILE - 6))
            sheet.paste(im, ((i % COLS) * TILE + 3, (i // COLS) * TILE + 43))
            d.text(((i % COLS) * TILE + 8, (i // COLS) * TILE + 46), str(i), fill='red', font=font)
        except Exception: pass
    sheet.save(f"{out}/panels/p{n:04d}.jpg", quality=84)
    return True

def main(src, out, source='ebay'):
    D = json.load(open(src)); D = {k: v for k, v in D.items() if not k.startswith('_') and v and v.get('imgs')}
    os.makedirs(out + '/img', exist_ok=True); os.makedirs(out + '/panels', exist_ok=True)
    try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
    except Exception: font = ImageFont.load_default()
    keys = sorted(D); index = {}
    with cf.ThreadPoolExecutor(16) as ex:
        ok = list(ex.map(lambda nk: panel(nk[0], nk[1], D[nk[1]], out, font), list(enumerate(keys, 1))))
    for (n, k), good in zip(enumerate(keys, 1), ok):
        if good: index[str(n)] = dict(D[k], id=k, source=source)
    json.dump(index, open(out + '/index.json', 'w'))
    print(len(index), 'panels in', out + '/panels')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'ebay')
