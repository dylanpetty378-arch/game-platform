#!/usr/bin/env python3
"""Import a Terapeak bulk-run result file into the database.

  python3 scripts/tp_import.py research/terapeak/<run>.jsonl <queries.json> [run-id]

The result file holds one JSON object per line: {i, q, n, p25, p50, p75, top:[{t,p,n,d}]}, as read out of the page (see
research/terapeak-bulk.md). <queries.json> is the [[slug, query], ...] list that was run, so each comp gets its type.
Writes one `searches` row per query (site=terapeak) and one `comps` row per query (all prices, median, top rows in note).
"""
import sys, os, json, statistics
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import db

def main(res, qfile, run=None):
    Q = json.load(open(qfile)); run = run or 'terapeak-' + os.path.basename(res).split('.')[0]
    S, C = [], []
    for line in open(res):
        if not line.strip(): continue
        r = json.loads(line); i = int(r['i']); slug = Q[i][0] if i < len(Q) else None
        top = r.get('top') or []; prices = [x['p'] for x in top if x.get('p')]
        S.append({'site': 'terapeak', 'query': r['q'], 'purpose': f'type research: {slug}', 'results': r.get('n'), 'run': run})
        if r.get('n'):
            C.append({'type': slug, 'query': r['q'], 'source': 'terapeak-365d', 'prices': prices,
                      'median': r.get('p50'), 'n': r.get('n'), 'pid': None, 'run': run,
                      'note': json.dumps({'p25': r.get('p25'), 'p75': r.get('p75'),
                                          'top': [f"${x['p']} {x['t'][:60]} ({x['d']})" for x in top[:8]]})})
    db.append('searches', S); db.append('comps', C); print(len(S), 'searches,', len(C), 'comps')

if __name__ == '__main__':
    main(*sys.argv[1:4])
