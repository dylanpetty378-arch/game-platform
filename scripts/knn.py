#!/usr/bin/env python3
"""Similar sold (Oct 22 2026): "ones like this sold for $X" — a picker's memory, built from real outcomes.

Every sold ShopGoodwill lot (scripts/outcomes.py) is embedded with the same CLIP model the shortlist uses and kept in a
rolling store. For each live listing the nearest sold neighbours by photo give a price distribution. SGW buyers are
mostly resellers, so these are picker prices: a conservative floor for resale value, not a retail estimate.

Store: $KNN_DIR (default .cache/knn; the workflow persists it with actions/cache — it is derived data and can be
rebuilt from db/outcomes/sgw if lost). emb.npy = int8 N×512 (unit vectors × 127), meta.jsonl = one row per vector.

  python3 scripts/knn.py stats        # store size and date range
Used from scripts/shortlist.py:  knn.add(clip) after outcomes are pulled; knn.query(rows) for rows carrying '_e'.
"""
import os, sys, json, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
DIR = os.environ.get('KNN_DIR') or os.path.join(ROOT, '.cache', 'knn')
KEEP_DAYS = 120
SIM = 0.75          # calibrated Oct 22 on 4.7k SGW sold lots: 25% coverage, log-price corr 0.43 (category median 0.29); raise as the store grows
K = 15

def _load():
    import numpy as np
    try:
        E = np.load(os.path.join(DIR, 'emb.npy'))
        M = [json.loads(l) for l in open(os.path.join(DIR, 'meta.jsonl'))]
        if len(M) == len(E): return E, M
    except Exception: pass
    return np.zeros((0, 512), dtype='int8'), []

def _save(E, M):
    import numpy as np
    os.makedirs(DIR, exist_ok=True)
    np.save(os.path.join(DIR, 'emb.npy'), E)
    with open(os.path.join(DIR, 'meta.jsonl'), 'w') as f:
        for m in M: f.write(json.dumps(m, ensure_ascii=False) + '\n')

def add(clip, max_new=int(os.environ.get('KNN_MAX_NEW', 15000))):
    """Embed stored SGW outcomes not yet in the store (newest first), drop vectors older than KEEP_DAYS."""
    import numpy as np, outcomes
    E, M = _load(); have = {m['id'] for m in M}
    new = [r for r in reversed(outcomes.recent_sgw(KEEP_DAYS)) if r['id'] not in have and r.get('img')][:max_new]
    if new:
        embs = clip.embed_urls([r['img'] for r in new])
        ok = [(r, e) for r, e in zip(new, embs) if e is not None]
        if ok:
            Q = np.stack([np.round(e.float().numpy() * 127).astype('int8') for _, e in ok])
            E = np.concatenate([E, Q]); M += [{'id': r['id'], 'f': r['final'], 't': r['t'][:70], 'end': r['end'][:10],
                                               'cat': (r.get('cat') or '')[:40]} for r, _ in ok]
    cut = (dt.date.today() - dt.timedelta(days=KEEP_DAYS)).isoformat()
    keep = [i for i, m in enumerate(M) if m['end'] >= cut]
    if len(keep) < len(M): E = E[keep]; M = [M[i] for i in keep]
    _save(E, M)
    print(f'knn store: +{len(new)} embedded, {len(M)} sold lots in store', flush=True)
    return len(M)

def _wmedian(vals, ws):
    s = sorted(zip(vals, ws)); half = sum(ws) / 2; acc = 0
    for v, w in s:
        acc += w
        if acc >= half: return v
    return s[-1][0]

def query(rows):
    """Sets r['knn'] = {n, p50, p75, best:[[final, sim, title]...]} for rows with an embedding in r['_e']."""
    import numpy as np, torch
    E, M = _load()
    if not len(M): print('knn store empty — skipping', flush=True); return
    S = torch.from_numpy(E.astype('float32') / 127.0)
    todo = [r for r in rows if r.get('_e') is not None]
    for i in range(0, len(todo), 512):
        part = todo[i:i + 512]
        Q = torch.stack([r['_e'].float() for r in part])
        sims = Q @ S.T; top = sims.topk(min(K, len(M)), dim=1)
        for r, vs, ix in zip(part, top.values.tolist(), top.indices.tolist()):
            nb = [(M[j]['f'], v, M[j]['t']) for v, j in zip(vs, ix) if v >= SIM]
            if len(nb) < 3: continue
            fs = [f for f, _, _ in nb]; ws = [max(v - SIM + 0.02, 0.01) for _, v, _ in nb]
            q = sorted(fs)
            r['knn'] = {'n': len(nb), 'p50': round(_wmedian(fs, ws)), 'p75': round(q[int(0.75 * (len(q) - 1))]),
                        'best': [[round(f), round(v, 2), t[:50]] for f, v, t in sorted(nb, key=lambda x: -x[1])[:3]]}
    print(f"knn: {sum('knn' in r for r in todo)} of {len(todo)} rows have >=3 sold look-alikes", flush=True)

if __name__ == '__main__':
    E, M = _load()
    print(len(M), 'vectors', (min(m['end'] for m in M), max(m['end'] for m in M)) if M else '')
