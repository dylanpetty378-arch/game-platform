#!/usr/bin/env python3
"""Title → encyclopedia type classifier, so the harvest can use what the encyclopedia knows about a type's economics.

  python3 scripts/type_model.py build      # train from labelled titles (events with a type slug + research/types.tsv) → research/type_model.json
  python3 scripts/type_model.py "Antique Hampden pocket watch"   # predict

Model: multinomial naive Bayes over title words (pure Python, ~1 MB JSON). Type value comes from each entry's rubric:
value = clamp(expected_profit_typical / 25, -3, 3) + 0.5 × (undervalue_frequency − 3) — positive for types where owners
often under-price and a typical buy clears the rule, negative for types that almost never pay (shipping, low value).
scoring.score() adds value × confidence when the top type clearly beats the runner-up (p1/(p1+p2) ≥ 0.65).
"""
import os, re, sys, json, math, csv, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE); OUT = os.path.join(ROOT, 'research', 'type_model.json')
STOP = set('vintage antique old the a an and of for with in on set lot pair item items great nice good condition sale new used beautiful rare'.split())

def toks(t):
    return [w for w in re.findall(r'[a-z0-9]+', (t or '').lower()) if len(w) > 1 and w not in STOP]

def build():
    import db, enc
    A = enc.aliases(); slugs = {s for s, _ in enc.entries()}
    L = {str(r['pid']): r.get('title') for r in db.read('listings')}
    data = []
    for e in db.read('events'):
        s = A.get(e.get('type') or '', e.get('type'))
        if s in slugs and L.get(str(e['pid'])): data.append((L[str(e['pid'])], s))
    tp = os.path.join(ROOT, 'research', 'types.tsv')
    if os.path.exists(tp):
        for r in csv.DictReader(open(tp), delimiter='\t'):
            s = A.get(r['slug'], r['slug'])
            if s in slugs and L.get(r['pid']): data.append((L[r['pid']], s))
    # entry titles/aliases are weak labelled examples too
    for s, t in enc.entries():
        data.append((enc.title(t) + ' ' + enc.field(t, 'Slug').replace('·', ' '), s))
    cnt = collections.defaultdict(collections.Counter); prior = collections.Counter(); vocab = set()
    for title, s in data:
        tk = toks(title); prior[s] += 1; cnt[s].update(tk); vocab.update(tk)
    V = len(vocab); N = sum(prior.values()); model = {'prior': {}, 'tok': {}, 'unk': {}, 'value': {}}
    for s in prior:
        tot = sum(cnt[s].values())
        model['prior'][s] = math.log(prior[s] / N)
        model['unk'][s] = math.log(1 / (tot + V))
        model['tok'][s] = {w: round(math.log((c + 1) / (tot + V)), 3) for w, c in cnt[s].items()}
    for s, t in enc.entries():
        r = enc.rubric(t) or {}
        try: e = float(r.get('expected_profit_typical'))
        except Exception: e = 0
        try: u = float(r.get('undervalue_frequency'))
        except Exception: u = 3
        model['value'][s] = round(max(-3, min(3, e / 25)) + 0.5 * (u - 3), 2)
    json.dump(model, open(OUT, 'w'), separators=(',', ':'))
    print(f'{len(data)} labelled titles, {len(prior)} types, vocab {V} → {OUT}')

_M = None
def load():
    global _M
    if _M is None:
        _M = json.load(open(OUT)) if os.path.exists(OUT) else {}
    return _M

def predict(title, k=3):
    m = load()
    if not m: return []
    tk = toks(title)
    if not tk: return []
    sc = {}
    for s, p in m['prior'].items():
        tt = m['tok'][s]; u = m['unk'][s]
        sc[s] = p + sum(tt.get(w, u) for w in tk)
    mx = max(sc.values()); z = sum(math.exp(v - mx) for v in sc.values())
    top = sorted(sc.items(), key=lambda x: -x[1])[:k]
    return [(s, round(math.exp(v - mx) / z, 3), m['value'].get(s, 0)) for s, v in top]

def adjustment(title):
    # 600+ classes dilute absolute probabilities, so use the margin over the runner-up as confidence
    p = predict(title, 2)
    if len(p) < 2: return 0.0
    (s, p1, val), (_, p2, _) = p
    conf = p1 / (p1 + p2)
    return round(val * conf, 2) if conf >= 0.65 else 0.0

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'build': build()
    elif a: print(predict(' '.join(a)), adjustment(' '.join(a)))
    else: print(__doc__)
