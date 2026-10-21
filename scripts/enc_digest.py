#!/usr/bin/env python3
"""Encyclopedia -> compact digest for low-usage screening (Oct 21 2026).

  python3 scripts/enc_digest.py        # writes research/enc_digest.json

For every entry: title, aliases, the value tiers from its Summary line (low and top), the TOP tier text (that segment
names the specific makers/variants that make the money — the golden-egg specifics), and the first photo tells from
"How to recognise it in a photo". Used two ways:
  1. shortlist.py builds a CLIP text prompt per type (title + aliases) and weights matches by top-tier value.
  2. lowuse.py hands each eye agent only the digest lines for the types its sheet's photos resemble, plus the
     highest-value tells overall — the encyclopedia goes into every look without loading 660 entries.
"""
import os, re, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ED = os.path.join(ROOT, 'docs', 'encyclopedia', 'entries')
OUT = os.path.join(ROOT, 'research', 'enc_digest.json')
MONEY = re.compile(r'\$\s?(\d[\d,]*(?:\.\d+)?)\s*(k)?(?:\s*[–-]\s*\$?(\d[\d,]*(?:\.\d+)?)\s*(k)?)?', re.I)

def dollars(s):
    v = []
    for n, k, n2, k2 in MONEY.findall(s):
        for a, b in ((n, k), (n2, k2 or k)):
            if a: x = float(a.replace(',', '')); v.append(x * 1000 if b else x)
    return v

def parse(path):
    t = open(path, encoding='utf-8').read()
    lines = t.splitlines()
    title = lines[0].lstrip('# ').strip() if lines else ''
    short = re.sub(r'\s*\(.*?\)\s*', ' ', title).strip()
    slug = os.path.basename(path)[:-3]
    al = re.search(r'^Slug:.*?Aliases:\s*(.+)$', t, re.M)
    aliases = [a.strip() for a in al.group(1).split(',')][:6] if al else []
    sm = re.search(r'^Summary:\s*(.+)$', t, re.M)
    summ = sm.group(1).strip() if sm else ''
    segs = [s.strip() for s in re.split(r';\s*', summ) if s.strip()]
    tiers = [(max(dollars(s)) if dollars(s) else 0, s) for s in segs]
    top_v, top_s = max(tiers) if tiers else (0, '')
    low_v = min((v for v, _ in tiers if v), default=0)
    br = re.search(r'^Buy rule[^:]*:\s*(.+)$', t, re.M)
    rec = re.search(r'## What it is / how to recognise it in a photo\n(.*?)(?:\n## |\Z)', t, re.S)
    tells = []
    if rec:
        bl = [re.sub(r'\*\*', '', ln.strip()[2:]) for ln in rec.group(1).splitlines() if ln.strip().startswith('- ')]
        # prefer the bullets that describe the money tier (share its maker/variant words), keep entry order otherwise
        kw = set(w.lower() for w in re.findall(r'[A-Z][\w\-]{2,}', top_s))
        bl = sorted(bl, key=lambda b: -len(kw & set(w.lower() for w in re.findall(r'[\w\-]{3,}', b))))
        tells = [b[:260] for b in bl[:3]]
    return slug, {'title': short, 'full': title, 'aliases': aliases, 'top': top_v, 'low': low_v,
                  'money': top_s[:300], 'buy': (br.group(1)[:260] if br else ''), 'tells': tells}

def build():
    d = dict(parse(p) for p in sorted(glob.glob(os.path.join(ED, '*.md'))))
    json.dump(d, open(OUT, 'w'), indent=0, ensure_ascii=False)
    tops = sorted(d.values(), key=lambda e: -e['top'])
    print(len(d), 'types ->', OUT, '| top>=$1000:', sum(e['top'] >= 1000 for e in tops), '| top>=$300:', sum(e['top'] >= 300 for e in tops))
    return d

def line(slug, e, tells=1, width=170):
    s = f"- **{e['title']}** [{slug}] top ${e['top']:,.0f}: {e['money'][:200]}"
    for x in e['tells'][:tells]: s += f"\n  tell: {x[:width]}"
    return s

if __name__ == '__main__':
    build()
