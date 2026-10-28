#!/usr/bin/env python3
"""Encyclopedia tool — one Markdown file per item type in docs/encyclopedia/entries/<slug>.md.

  python3 scripts/enc.py find <words…>        # which entries mention these words (slug, title, index summary)
  python3 scripts/enc.py show <slug|alias>    # print an entry
  python3 scripts/enc.py seen <slug> "<line>"  # append a dated line to the entry's "Seen in sweeps"
  python3 scripts/enc.py add <file.md> [...]  # add/replace entries written elsewhere (slug from the file's "Slug:" line or name)
  python3 scripts/enc.py index                # rebuild docs/encyclopedia/index.md from the entries
  python3 scripts/enc.py sync                 # write every entry's type rubric into db/item_types.jsonl (only changed ones)
  python3 scripts/enc.py volumes  # (no longer uploaded to the claude.ai project since Oct 13 — the website serves entries) <out_dir>    # bundle entries into A-B … T-Z volumes (for the claude.ai project copy)
  python3 scripts/enc.py lint                 # entries missing required sections / rubric fields (--tells, --thin)
  python3 scripts/enc.py sell <slug>          # print just the "Selling it" section (title words, platform, price position, photos, packing)

Entry format: docs/encyclopedia/README.md. Rubric fields: docs/rubric.md. The rubric is a ```json block under
"## Rubric" so it can be read by code.
"""
import os, re, sys, json, glob, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
ED = os.path.join(ROOT, 'docs', 'encyclopedia', 'entries')
IDX = os.path.join(ROOT, 'docs', 'encyclopedia', 'index.md')
REQUIRED = ['## What it is', '## Value ladder', '## What sellers usually miss', '## Shipping', '## Buy rule', '## Rubric', '## Seen in sweeps']
RUBRIC_KEYS = ['size_class', 'weight_lb', 'shape', 'fragility', 'transit_damage_risk', 'hidden_defect_risk', 'testability', 'repro_risk',
               'id_difficulty', 'rarity', 'sold_per_month', 'sell_through', 'days_to_sell', 'price_p25_p50_p75', 'price_spread',
               'condition_sensitivity', 'seasonality', 'best_platform', 'fees_pct', 'ship_cost_to_buyer', 'undervalue_frequency',
               'bust_probability', 'expected_profit_typical', 'confidence']

def aliases():
    p = os.path.join(ED, '_aliases.json')
    return json.load(open(p)) if os.path.exists(p) else {}

def resolve(slug):
    return aliases().get(slug, slug)

def path(slug): return os.path.join(ED, resolve(slug) + '.md')

def entries():
    for p in sorted(glob.glob(os.path.join(ED, '*.md'))):
        yield os.path.basename(p)[:-3], open(p).read()

def title(text): return (re.match(r'# (.+)', text) or [None, ''])[1].strip()

def field(text, name):
    m = re.search(rf'(?m)^{name}:\s*(.+)$', text); return m.group(1).strip() if m else ''

def rubric(text):
    m = re.search(r'## Rubric.*?```json\s*(\{.*?\})\s*```', text, re.S)
    if not m: return None
    try: return json.loads(m.group(1))
    except Exception: return None

def index_rows():
    rows = {}
    if os.path.exists(IDX):
        for l in open(IDX):
            if l.startswith('| ') and not l.startswith('| Type') and not l.startswith('|---'):
                c = [x.strip() for x in l.strip().strip('|').split('|')]
                if len(c) >= 5: rows[c[1]] = c
    return rows

def cmd_find(words):
    words = [w.lower() for w in words]; rows = index_rows(); A = aliases(); hits = []
    for slug, t in entries():
        low = (slug + ' ' + t).lower()
        n = sum(low.count(w) for w in words)
        if all(w in low for w in words): hits.append((n + (50 if all(w in slug for w in words) else 0), slug, title(t)))
    for al, sl in A.items():
        if all(w in al for w in words): hits.append((100, sl, f'(alias {al})'))
    for n, slug, ttl in sorted(hits, reverse=True)[:25]:
        r = rows.get(slug); print(f'{slug:40} {ttl[:70]}' + (f'\n    {r[2][:150]}\n    buy: {r[3][:150]}' if r else ''))
    if not hits: print('no entry — research it and write one (docs/encyclopedia/README.md)')

def cmd_seen(slug, line):
    p = path(slug); t = open(p).read(); d = datetime.date.today().isoformat()
    line = line if line.startswith('- ') else f'- {d} – {line}'
    if '## Seen in sweeps' not in t: t = t.rstrip() + '\n\n## Seen in sweeps\n'
    i = t.index('## Seen in sweeps'); j = t.find('\n## ', i + 5)
    t = (t.rstrip() + '\n' + line + '\n') if j < 0 else (t[:j].rstrip() + '\n' + line + '\n' + t[j:])
    open(p, 'w').write(t); print('ok', os.path.relpath(p, ROOT))

def cmd_add(files):
    for f in files:
        t = open(f).read().strip() + '\n'
        slug = field(t, 'Slug') or os.path.basename(f)[:-3]
        slug = re.sub(r'[^a-z0-9-]', '', slug.split()[0].lower())
        p = os.path.join(ED, slug + '.md')
        if os.path.exists(p) and '--replace' not in sys.argv:
            old = open(p).read()
            if old.strip() != t.strip():
                h = title(t); body = t.split('\n', 1)[1] if '\n' in t else ''
                t = old.rstrip() + f'\n\n---\n\n## Additional research ({datetime.date.today().isoformat()}: {h})\n' + re.sub(r'(?m)^## ', '### ', body)
                # keep the newest rubric machine-readable at the top level
                r = rubric(open(f).read())
                if r: t = re.sub(r'(## Rubric.*?```json\s*)\{.*?\}(\s*```)', lambda m: m.group(1) + json.dumps(r, indent=1) + m.group(2), t, count=1, flags=re.S)
        open(p, 'w').write(t); print('wrote', slug)

def cmd_makers():
    # research/makers.json: maker/brand/model names from every entry's Makers section, for scoring.mismatch (Oct 13)
    import collections
    generic=set('hand painted|clear glass|art nouveau|art deco|mid-century|hand tools|general|american|english|german|french|italian|japanese|chinese|victorian|vintage|antique|unmarked|unsigned|reproduction|modern|contemporary|sterling|silver plate|silverplate|cast iron|brass|bronze|copper|pewter|wood|glass|ceramic|porcelain|pottery|stoneware|crystal|leather|cotton|wool|plastic|bakelite|lucite|celluloid|gold tone|gold-tone|gold filled|rolled gold|common|rare|scarce|early|late|other|others|various|misc|unknown|japan|china|germany|england|france|italy|usa|mexico|india|taiwan|korea|hong kong|occupied japan|made in japan|made in china|made in germany|made in england|made in usa|made in italy|made in france|west germany|east germany|limited edition|signed|numbered|first edition|original|style|type|model|pattern|series|edition|version|set|lot|pair|collection'.split('|'))
    words=set()
    if os.path.exists('/usr/share/dict/words'): words={w.strip().lower() for w in open('/usr/share/dict/words')}
    docfreq=collections.Counter(); boldfreq=collections.Counter()
    for s, t in entries():
        m=re.search(r'## Makers.*?(?=\n## )',t,re.S); sec=m.group(0) if m else ''
        bold=set(b.strip(' .:;,"“”\'’-') for b in re.findall(r'\*\*([^*\n]{3,40})\*\*',sec))
        for b in bold: boldfreq[b]+=1
        names=set(re.findall(r'\*\*([^*\n]{3,40})\*\*',sec))|set(re.findall(r'^\|\s*([^|\n]{3,40}?)\s*\|',sec,re.M))
        cl=set()
        for n in names:
            n=re.sub(r'\s*[\(\[].*$','',n).strip(' .:;,"“”\'’-'); n=re.split(r'\s*[/,;–—]\s*',n)[0].strip()
            if not (3<=len(n)<=35) or n.lower() in generic or not re.search(r'[A-Z]',n): continue
            if re.match(r'^[\d$#]',n) or (re.search(r'\d{4}s?\b',n) and len(n.split())<=2): continue
            if re.match(r'^(Maker|Brand|Tier|Variant|Model|Line|Mark|Marks|Note|Notes|Value|Date|Dates|Price|Top|Mid|Low|High|Example|Examples|Quick ID checklist|Golden-egg tells|Common|Rare|What|How|Where|When|Why|Who)\b',n,re.I): continue
            if all(w.lower() in generic for w in n.split()): continue
            cl.add(n)
        for n in cl: docfreq[n]+=1
    keep=[]
    for m,c in docfreq.items():
        ws=m.split()
        if c>15 and boldfreq[m]<3: continue
        if len(ws)>=2:
            if words and len(ws)==2 and all(w.lower() in words for w in ws if w.isalpha()): continue
            keep.append(m)
        elif (not (words and m.lower() in words) and c<=3) or boldfreq[m]>=2: keep.append(m)   # dictionary-word makers (Fender, Champion) survive when bolded in 2+ entries
    json.dump(sorted(keep), open(os.path.join(ROOT,'research','makers.json'),'w')); print(len(keep),'maker names → research/makers.json')

def cmd_index():
    rows = index_rows(); out = []
    for slug, t in entries():
        old = rows.get(slug)
        summ = field(t, 'Summary') or (old[2] if old else '')
        buy = field(t, 'Buy rule \\(short\\)') or (old[3] if old else '')
        upd = (re.search(r'Updated:\s*([\d-]+)', t) or [None, old[4] if old else ''])[1]
        out.append(f"| {title(t)[:90]} | {slug} | {summ} | {buy} | {upd} |")
    A = aliases()
    hdr = ['# Encyclopedia index', '', f'{len(out)} entries, one file each in `entries/<slug>.md` (raw: '
           '`https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish/docs/encyclopedia/entries/<slug>.md`). '
           'Search: `python3 scripts/enc.py find <words>`. Aliases: ' + ', '.join(f'{a}→{s}' for a, s in A.items()) + '.', '',
           '| Type | Slug | Value summary (sold) | Buy rule | Updated |', '|---|---|---|---|---|']
    open(IDX, 'w').write('\n'.join(hdr + out) + '\n'); print(len(out), 'rows')

def cmd_sync():
    import db
    have = {}
    for r in db.read('item_types'): have[r['slug']] = r
    new = []
    for slug, t in entries():
        r = rubric(t)
        row = {'ts': db.now(), 'slug': slug, 'name': title(t), 'volume': 'entries', 'aliases': ','.join(a for a, s in aliases().items() if s == slug),
               'note': field(t, 'Summary')[:300], 'rubric': r}
        o = have.get(slug)
        if not o or o.get('name') != row['name'] or o.get('rubric') != r or o.get('note') != row['note']: new.append(row)
    db.append('item_types', new); print(len(new), 'item_types rows written')

def cmd_volumes(out):
    os.makedirs(out, exist_ok=True)
    groups = [('a-b', 'ab'), ('c-d', 'cd'), ('e-h', 'efgh'), ('i-m', 'ijklm'), ('n-r', 'nopqr'), ('s', 's'), ('t-z', 'tuvwxyz0123456789')]
    E = list(entries())
    for name, letters in groups:
        sel = [(s, t) for s, t in E if s[0] in letters]
        txt = f'# Resale encyclopedia – volume {name.upper()}\n\nEntries in this file: ' + ', '.join(s for s, _ in sel) + \
              '\n\nGenerated from docs/encyclopedia/entries/ by scripts/enc.py volumes — edit the entry files, not this.\n'
        for s, t in sel: txt += f'\n---\n\n<!-- slug: {s} -->\n' + t.strip() + '\n'
        open(os.path.join(out, f'encyclopedia-{name}.md'), 'w').write(txt)
    print('volumes written to', out)

def cmd_lint():
    bad = 0
    for slug, t in entries():
        miss = [s for s in REQUIRED if s not in t]; r = rubric(t)
        rk = [k for k in RUBRIC_KEYS if not r or k not in r]
        if miss or rk:
            bad += 1; print(f'{slug:40} missing sections: {len(miss)}  rubric fields missing: {len(rk)}')
    gen = [slug for slug, t in entries() if '### Golden-egg tells' not in t]
    thin = [slug for slug, t in entries() if len(selling(t).split()) < 60]
    print(bad, 'entries need work;', len(gen), 'without "### Golden-egg tells" (no-generalization rule, Oct 13) — see `enc.py lint --tells`;',
          len(thin), 'with a "Selling it" section under 60 words (sell-side template, Oct 28) — see `enc.py lint --thin`')
    if '--tells' in sys.argv:
        for g in gen: print(g)
    if '--thin' in sys.argv:
        for g in thin: print(g)

def selling(t):
    m = re.search(r'## Selling it[^\n]*\n(.*?)(?=\n## |\Z)', t, re.S)
    return m.group(1).strip() if m else ''

def cmd_sell(slug):
    t = open(path(slug)).read()
    print(title(t)); print(selling(t) or '(no Selling it section)')

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    c = a[0]
    if c == 'find': cmd_find(a[1:])
    elif c == 'show': print(open(path(a[1])).read())
    elif c == 'seen': cmd_seen(a[1], a[2])
    elif c == 'add': cmd_add([x for x in a[1:] if not x.startswith('--')])
    elif c == 'index': cmd_index(); cmd_makers()
    elif c == 'sync': cmd_sync()
    elif c == 'volumes': cmd_volumes(a[1])
    elif c == 'lint': cmd_lint()
    elif c == 'sell': cmd_sell(a[1]) if len(a) > 1 else print('usage: enc.py sell <slug>')
    else: print(__doc__)
