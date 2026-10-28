#!/usr/bin/env python3
"""stage.py — turn phone photos into honest, consistent listing photos (Pillow + numpy, no AI).

  python3 scripts/stage.py prep  <in_dir|files…> -o <out_dir> [--long 1600] [--q 88] [--wb] [--levels] [--rotate N]
        HEIC/JPG/PNG in → JPG out, EXIF orientation applied, GPS/EXIF stripped, auto-levels (0.5% clip), optional
        gray-world white balance, optional rotation, resized to --long px on the long edge. One file per input.
  python3 scripts/stage.py crop  <file> -o <out> --box x0,y0,x1,y1 [--pad 0.06] [--ar 4:3|1:1|none]
        Crop to the item (pixel box from a `sheet` or a guess), pad by a fraction, then expand to the aspect ratio.
  python3 scripts/stage.py fix   <file> -o <out> [--bright 1.08] [--contrast 1.05] [--sharpen 0.6] [--straighten DEG]
        Small, declared adjustments only. Straighten rotates ±DEG and crops the wedge.
  python3 scripts/stage.py sheet <in_dir|files…> -o <sheet.jpg> [--h 500]
        Contact sheet with filenames and pixel size, to pick the hero and read crop boxes.
  python3 scripts/stage.py order <in_dir> -o <out_dir> hero.jpg angle.jpg … flaw.jpg
        Copies files as 01-hero.jpg, 02-…, so the upload order is the listing order (hero → angles → details → flaws → label).

Rules (docs/selling/photos.md): correct light, colour, crop, tilt; never hide or soften a flaw on the item, never change
its colour, never add anything. Every output is a new file; inputs are untouched.
"""
import sys, os, glob, argparse, shutil
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw, ImageFont
try:
    import pillow_heif; pillow_heif.register_heif_opener()
except Exception:
    pass

EXT = ('.jpg', '.jpeg', '.png', '.heic', '.heif', '.webp', '.tif', '.tiff')

def inputs(args):
    out = []
    for a in args:
        if os.path.isdir(a): out += sorted(p for p in glob.glob(os.path.join(a, '*')) if p.lower().endswith(EXT))
        else: out.append(a)
    return out

def load(p):
    im = Image.open(p); im = ImageOps.exif_transpose(im)
    return im.convert('RGB')

def auto_levels(im, clip=0.005):
    a = np.asarray(im).astype(np.float32)
    lo = np.percentile(a, clip * 100); hi = np.percentile(a, 100 - clip * 100)
    if hi <= lo: return im
    a = np.clip((a - lo) * (255.0 / (hi - lo)), 0, 255)
    return Image.fromarray(a.astype(np.uint8))

def gray_world(im, strength=0.7):
    a = np.asarray(im).astype(np.float32)
    means = a.reshape(-1, 3).mean(0); g = means.mean()
    gain = 1 + strength * (g / np.maximum(means, 1) - 1)
    gain = np.clip(gain, 0.8, 1.25)              # never a dramatic colour shift — the fabric must stay its colour
    return Image.fromarray(np.clip(a * gain, 0, 255).astype(np.uint8))

def resize_long(im, long):
    w, h = im.size
    if max(w, h) <= long: return im
    s = long / max(w, h)
    return im.resize((round(w * s), round(h * s)), Image.LANCZOS)

def save(im, out, q=88):
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    im.save(out, 'JPEG', quality=q, optimize=True)        # no EXIF → no GPS, no device info
    print(out, im.size)

def cmd_prep(a):
    ap = argparse.ArgumentParser(); ap.add_argument('src', nargs='+'); ap.add_argument('-o', required=True)
    ap.add_argument('--long', type=int, default=1600); ap.add_argument('--q', type=int, default=88)
    ap.add_argument('--wb', action='store_true'); ap.add_argument('--levels', action='store_true', default=True)
    ap.add_argument('--no-levels', dest='levels', action='store_false'); ap.add_argument('--rotate', type=float, default=0)
    o = ap.parse_args(a)
    for p in inputs(o.src):
        im = load(p)
        if o.levels: im = auto_levels(im)
        if o.wb: im = gray_world(im)
        if o.rotate: im = im.rotate(o.rotate, resample=Image.BICUBIC, expand=True)
        im = resize_long(im, o.long)
        save(im, os.path.join(o.o, os.path.splitext(os.path.basename(p))[0] + '.jpg'), o.q)

def expand_ar(box, ar, W, H):
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    if not ar or ar == 'none': return box
    aw, ah = (4, 3) if ar == '4:3' else (1, 1) if ar == '1:1' else tuple(int(v) for v in ar.split(':'))
    target = aw / ah
    if w / h < target: nw = h * target; x0 -= (nw - w) / 2; x1 = x0 + nw
    else: nh = w / target; y0 -= (nh - h) / 2; y1 = y0 + nh
    # slide inside the image rather than clip
    if x0 < 0: x1 -= x0; x0 = 0
    if y0 < 0: y1 -= y0; y0 = 0
    if x1 > W: x0 -= x1 - W; x1 = W
    if y1 > H: y0 -= y1 - H; y1 = H
    return [max(0, x0), max(0, y0), min(W, x1), min(H, y1)]

def cmd_crop(a):
    ap = argparse.ArgumentParser(); ap.add_argument('src'); ap.add_argument('-o', required=True)
    ap.add_argument('--box', required=True); ap.add_argument('--pad', type=float, default=0.06); ap.add_argument('--ar', default='4:3')
    ap.add_argument('--q', type=int, default=88)
    o = ap.parse_args(a)
    im = load(o.src); W, H = im.size
    x0, y0, x1, y1 = [float(v) for v in o.box.split(',')]
    pw, ph = (x1 - x0) * o.pad, (y1 - y0) * o.pad
    box = expand_ar([x0 - pw, y0 - ph, x1 + pw, y1 + ph], o.ar, W, H)
    save(im.crop(tuple(int(round(v)) for v in box)), o.o, o.q)

def cmd_fix(a):
    ap = argparse.ArgumentParser(); ap.add_argument('src'); ap.add_argument('-o', required=True)
    ap.add_argument('--bright', type=float, default=1.0); ap.add_argument('--contrast', type=float, default=1.0)
    ap.add_argument('--sharpen', type=float, default=0.0); ap.add_argument('--straighten', type=float, default=0.0)
    ap.add_argument('--q', type=int, default=88)
    o = ap.parse_args(a)
    im = load(o.src)
    if o.straighten:
        W, H = im.size
        im = im.rotate(o.straighten, resample=Image.BICUBIC, expand=False)
        t = abs(np.tan(np.radians(o.straighten))); cx, cy = int(H * t) + 2, int(W * t) + 2
        im = im.crop((cx, cy, W - cx, H - cy))
    if abs(o.bright - 1) > 0.001: im = ImageEnhance.Brightness(im).enhance(min(max(o.bright, 0.8), 1.25))
    if abs(o.contrast - 1) > 0.001: im = ImageEnhance.Contrast(im).enhance(min(max(o.contrast, 0.85), 1.2))
    if o.sharpen: im = im.filter(ImageFilter.UnsharpMask(radius=1, percent=int(60 * o.sharpen), threshold=3))
    save(im, o.o, o.q)

def cmd_sheet(a):
    ap = argparse.ArgumentParser(); ap.add_argument('src', nargs='+'); ap.add_argument('-o', required=True); ap.add_argument('--h', type=int, default=500)
    o = ap.parse_args(a)
    files = inputs(o.src); ims = []
    for p in files:
        im = load(p); orig = im.size; im = im.resize((round(im.width * o.h / im.height), o.h))
        d = ImageDraw.Draw(im); label = f'{os.path.basename(p)}  {orig[0]}x{orig[1]}'
        d.rectangle((0, 0, 8 + 7 * len(label), 18), fill=(0, 0, 0)); d.text((4, 3), label, fill=(255, 255, 255))
        ims.append(im)
    cols = 5 if len(ims) > 5 else len(ims); rows = (len(ims) + cols - 1) // cols
    cw = max(i.width for i in ims); sheet = Image.new('RGB', (cw * cols, o.h * rows), (40, 40, 40))
    for k, im in enumerate(ims): sheet.paste(im, ((k % cols) * cw, (k // cols) * o.h))
    save(sheet, o.o, 85)

def cmd_order(a):
    ap = argparse.ArgumentParser(); ap.add_argument('src'); ap.add_argument('-o', required=True); ap.add_argument('names', nargs='+')
    o = ap.parse_args(a); os.makedirs(o.o, exist_ok=True)
    roles = ['hero', 'angle', 'angle', 'detail', 'detail', 'detail', 'flaw', 'flaw', 'label', 'extra']
    for i, n in enumerate(o.names):
        src = n if os.path.exists(n) else os.path.join(o.src, n)
        dst = os.path.join(o.o, f'{i+1:02d}-{roles[min(i, len(roles)-1)]}.jpg'); shutil.copy(src, dst); print(dst)

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    {'prep': cmd_prep, 'crop': cmd_crop, 'fix': cmd_fix, 'sheet': cmd_sheet, 'order': cmd_order}.get(a[0], lambda _: print(__doc__))(a[1:])
