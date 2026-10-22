#!/usr/bin/env python3
"""Read the marks (Oct 22 2026): resellers flip it over — so does this.

For every shortlisted row, CLIP picks the photos that look like a mark, stamp, signature, hallmark or label
(not the hero shot), and Tesseract OCR reads them. The text is parsed for metal purity (melt floor) and for maker
names from research/makers.json. A maker read off a PHOTO that the TITLE does not name is exactly the "seller
didn't say it" case — it is scored up and shown to the eye as PHOTO MARK.

Needs the `tesseract` binary (apt-get install tesseract-ocr). Free; runs in the eye-shortlist workflow.
  python3 scripts/ocr.py <image-url> [...]     # test: print OCR text of images
"""
import os, re, io, sys, subprocess, urllib.request, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)

MARK = ['a close-up photo of a hallmark stamped into metal', "a close-up photo of a maker's mark on the bottom of pottery",
        "a close-up photo of an artist's signature on a painting", 'a close-up photo of a stamp on the back of jewelry',
        'a photo of a printed label or sticker with text', 'a close-up photo of engraved letters and numbers',
        'a photo of the underside of a vase showing a mark', 'a close-up photo of a clasp with tiny stamped letters']
OBJ = ['a photo of a whole object on a table', 'a photo of a vase', 'a photo of a ring on a finger', 'a photo of a necklace',
       'a photo of a figurine', 'a photo of a framed picture on a wall', 'a photo of a box', 'a photo of a group of items']
PER_ROW = 2          # photos OCR'd per row
MAX_PHOTOS = 4       # candidate photos per row (after the first); 8 made the daily run too slow on 4 vCPU

def have_tesseract():
    try: subprocess.run(['tesseract', '--version'], capture_output=True, timeout=10); return True
    except Exception: return False

def ocr_url(u):
    from PIL import Image, ImageOps
    try:
        b = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=25).read()
        im = ImageOps.autocontrast(Image.open(io.BytesIO(b)).convert('L'))
        w, h = im.size; s = 1600 / max(w, h)
        if s < 1 or s > 1.5: im = im.resize((int(w * s), int(h * s)))
        buf = io.BytesIO(); im.save(buf, 'PNG')
        out = subprocess.run(['tesseract', 'stdin', 'stdout', '--psm', '11'], input=buf.getvalue(), capture_output=True, timeout=60)
        txt = out.stdout.decode('utf-8', 'ignore')
    except Exception: return ''
    toks = [t for t in re.findall(r"[A-Za-z0-9][A-Za-z0-9.&'/-]*", txt) if len(t) >= 2 and re.search(r'[A-Za-z0-9]{2}', t)]
    return ' '.join(toks)[:400]

def run(rows, clip, makers=None):
    """Sets r['ocr'] = {text, metal, makers, photos} on rows with detail photos. clip = shortlist.Clip instance."""
    import melt
    if not have_tesseract(): print('::warning::tesseract missing — OCR skipped', flush=True); return
    torch = clip.torch
    with torch.no_grad():
        tm = clip.text(MARK); to = clip.text(OBJ)
    cand = []
    for r in rows:
        imgs = ((r.get('det') or {}).get('imgs') or [])[1:1 + MAX_PHOTOS]
        cand += [(r, u) for u in imgs]
    embs = clip.embed_urls([u for _, u in cand])
    best = {}
    for (r, u), e in zip(cand, embs):
        if e is None: continue
        e = e.float(); s = float((e @ tm.T).max() - (e @ to.T).max())
        if s > 0.0: best.setdefault(r['id'], []).append((s, u))
    jobs = [(rid, u) for rid, l in best.items() for s, u in sorted(l, reverse=True)[:PER_ROW]]
    with cf.ThreadPoolExecutor(4) as ex: texts = list(ex.map(lambda j: ocr_url(j[1]), jobs))
    got = {}
    for (rid, u), t in zip(jobs, texts):
        if t: got.setdefault(rid, []).append(t)
    for r in rows:
        if r['id'] not in got: continue
        t = ' | '.join(got[r['id']])
        pu = melt.purity(t)
        mk = sorted(set(m.lower() for m in makers.findall(t))) if makers else []
        mk = [m for m in mk if m not in r['t'].lower()]
        r['ocr'] = {'text': t[:300], 'metal': pu[2] if pu else None, 'makers': mk[:4], 'photos': len(got[r['id']])}
    n = sum('ocr' in r for r in rows)
    print(f"ocr: {len(cand)} candidate photos, {len(jobs)} read, text on {n} rows, "
          f"metal {sum(1 for r in rows if (r.get('ocr') or {}).get('metal'))}, "
          f"maker-not-in-title {sum(1 for r in rows if (r.get('ocr') or {}).get('makers'))}", flush=True)

if __name__ == '__main__':
    for u in sys.argv[1:]: print(u, '->', ocr_url(u))
