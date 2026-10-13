#!/usr/bin/env python3
"""Eye-first screening (Oct 13 2026 redo). Replaces "rank by title, review the top 800" with "look at everything".

Why: the title score did not predict leads at all (lead rate ~1.4% in every score quintile, every category, every price
band, Lens or no Lens — docs/improvements.md 2026-10-13). A picker's eye on the photo is the filter titles can't be.

  python3 scripts/eye_screen.py harvest <hours> [cats]     # fresh listings, size/junk/policy filters only, NO ranking
  python3 scripts/eye_screen.py sheets <run>               # 120-thumb contact sheets (12x10) + index.json
  python3 scripts/sgw.py harvest <hours>                  # same pool format from ShopGoodwill auctions (scripts/sgw.py)
  python3 scripts/eye_screen.py ingest <run> <flags.tsv>   # flagged cells -> listings + queued/flagged events

Work dir: /tmp/eye/<run>/ (thumbnails are not committed). flags.tsv lines: sheet<TAB>cell<TAB>why
"""
import os, sys, json, time, concurrent.futures as cf, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import scoring
# Categories that have produced leads (fua/for/pha/bik/mob/rvs/wan/boo/bop/mpo excluded: 0–0.5% and mostly size kills)
CATS = 'ata,atq,cba,clt,jwa,clo,msa,spo,tag,art,hsh,ele,tls,emd,vga,gms,sys'
COLS, ROWS, TH = 12, 10, 150

def wdir(run): d = f'/tmp/eye/{run}'; os.makedirs(d + '/th', exist_ok=True); return d

def harvest(hours, cats=CATS):
    import harvest_cl, db
    rows, fails, jobs = harvest_cl.harvest(cats, hours)
    known = db.known_pids(); seen = set(); pool = []
    for r in sorted(rows, key=lambda r: -r['posted']):
        if str(r['pid']) in known or scoring.score(r) <= -99: continue
        if r['imgs'][0] in seen: continue                 # cross-posts share the first photo
        seen.add(r['imgs'][0]); pool.append(r)
    run = 'eye-' + time.strftime('%Y%m%d-%H%M', time.gmtime())
    json.dump(pool, open(wdir(run) + '/pool.json', 'w'))
    print(run, len(rows), 'listings,', len(pool), 'after filters,', fails, 'failed of', jobs)

def _thumb(d, r):
    p = f"{d}/th/{r['pid']}.jpg"
    if os.path.exists(p): return True
    url = r.get('thumb') or f"https://images.craigslist.org/{r['imgs'][0].split(':')[-1]}_300x300.jpg"
    for t in range(3):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read()
            open(p, 'wb').write(data); return True
        except Exception: time.sleep(1 + t)
    return False

def sheets(run):
    from PIL import Image, ImageDraw, ImageFont
    d = wdir(run); pool = json.load(open(d + '/pool.json'))
    with cf.ThreadPoolExecutor(48) as ex: ok = list(ex.map(lambda r: _thumb(d, r), pool))
    pool = [r for r, k in zip(pool, ok) if k]
    try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    except Exception: font = ImageFont.load_default()
    per = COLS * ROWS; index = {}
    os.makedirs(d + '/sheets', exist_ok=True)
    for s in range(0, len(pool), per):
        n = s // per + 1; sheet = Image.new('RGB', (COLS * TH, ROWS * (TH + 18)), 'white'); dr = ImageDraw.Draw(sheet)
        for k, r in enumerate(pool[s:s + per]):
            x, y = (k % COLS) * TH, (k // COLS) * (TH + 18)
            try:
                im = Image.open(f"{d}/th/{r['pid']}.jpg").convert('RGB'); im.thumbnail((TH - 4, TH - 4))
                sheet.paste(im, (x + 2, y + 2))
            except Exception: pass
            cell = f'{chr(65 + k // COLS)}{k % COLS + 1}'
            # Label ABOVE-LEFT inside the cell's own box (Oct 13: labels under the photo were read as belonging to the
            # next row — ~25% of estate-sale flags pointed at the wrong photo).
            lab = f"{cell} ${r['price']:g}" if r.get('price') else cell
            dr.rectangle([x + 2, y + 2, x + 2 + 9 * len(lab), y + 19], fill='yellow')
            dr.text((x + 4, y + 3), lab, fill='black', font=font)
            index[f'{n}:{cell}'] = r
        sheet.save(f'{d}/sheets/s{n:03d}.jpg', quality=82)
    json.dump(index, open(d + '/index.json', 'w'))
    print(len(pool), 'thumbs ->', (len(pool) + per - 1) // per, 'sheets in', d + '/sheets')

def ingest(run, tsv):
    import db
    d = wdir(run); index = json.load(open(d + '/index.json')); out = []
    for line in open(tsv):
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 2: continue
        r = index.get(f'{int(parts[0])}:{parts[1].strip().upper()}')
        if r: out.append((r, parts[2] if len(parts) > 2 else ''))
    known = db.known_pids(); out = [(r, w) for r, w in out if str(r['pid']) not in known]
    db.append('listings', [{'pid': str(r['pid']), 'source': r.get('source', 'craigslist'), 'harvest_id': run, 'posted': r['posted'], 'price': r['price'],
                            'title': r['title'], 'area': r['area'], 'region': r['region'], 'cat': r['cat'], 'imgs': r['imgs'],
                            'score': None, 'clip': None, 'url': r.get('url') or f"https://www.craigslist.org/view/d/{r['slug']}/{r['uuid']}",
                            'ends': r.get('ends'), 'bids': r.get('bids')} for r, _ in out])
    db.append('events', [{'pid': str(r['pid']), 'stage': 'queued', 'run': run, 'data': {'eye': True}} for r, _ in out])
    db.append('events', [{'pid': str(r['pid']), 'stage': 'flagged', 'run': run, 'by': 'claude', 'note': 'eye screen: ' + w, 'data': {'eye': True}} for r, w in out])
    print(len(out), 'flagged listings ingested from', run)

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == 'harvest': harvest(float(a[1]), a[2] if len(a) > 2 else CATS)
    elif a[0] == 'sheets': sheets(a[1])
    elif a[0] == 'ingest': ingest(a[1], a[2])
