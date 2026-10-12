"""Stage 1 → Stage 2.  Joins the FLAGGED list exported from Chrome back to the listings and prints a Stage-2 worklist.

Usage:
  python3 lens_export.py flagged.json [lens_pri.json]      -> prints worklist, writes stage2.json
  python3 lens_export.py --photos stage2.json OUTDIR       -> one contact sheet per flagged listing (first 6 photos, 600px)
  python3 lens_export.py --ledger DONE lens_pri.json seen-pids.txt
                                                           -> appends the pids of the first DONE queue items to the ledger
                                                              (only listings that actually went through Lens)

flagged.json is the text you get from Chrome (Step 5 of the runbook).
Each FLAGGED item has: i (queue position), img (first-photo id), price, ratio, med, n, c (collectible channel),
best (best match title), ai, av, s (sources)
"""
import json,sys,os
if sys.argv[1]=='--photos':
    import st
    S=json.load(open(sys.argv[2])); out=sys.argv[3]; os.makedirs(out,exist_ok=True)
    for r in S:
        p=f"{out}/{r['pid']}.jpg"
        if not os.path.exists(p):
            st.sheet([(f"{i}",f"https://images.craigslist.org/{im}_600x450.jpg","") for i,im in enumerate(r['imgs'][:6])],p,cols=3,cell=600)
        print(p)
    sys.exit()
if sys.argv[1]=='--ledger':
    done=int(sys.argv[2]); P=json.load(open(sys.argv[3])); led=sys.argv[4]
    old=set(open(led).read().split()) if os.path.exists(led) else set()
    new={str(r['pid']) for r in P[:done]}
    open(led,'w').write('\n'.join(sorted(old|new))+'\n')
    print(f'ledger {len(old)} -> {len(old|new)}'); sys.exit()
F=json.load(open(sys.argv[1]))
P=json.load(open(sys.argv[2] if len(sys.argv)>2 else 'lens_pri.json'))
byimg={r['imgs'][0]:r for r in P}
out=[]
for f in F:
    r=P[f['i']] if isinstance(f.get('i'),int) and f['i']<len(P) and P[f['i']]['imgs'][0]==f.get('img') else byimg.get(f.get('img'))
    if not r: continue
    d=dict(r); d.update({k:f.get(k) for k in ('i','ratio','med','n','c','best','ai','av','s')})
    d['url']=f"https://www.craigslist.org/view/d/{r['slug']}/{r['uuid']}"
    out.append(d)
out.sort(key=lambda d:(-(d['ratio'] or 0),-(d['med'] or 0)))
json.dump(out,open('stage2.json','w'),indent=1)
for d in out:
    print(f"${d['price']:<4} {d['area']:<12} ratio {d['ratio'] or '-':<5} med ${d['med'] or '-':<5} n{d['n']} {'COLL ' if d['c'] else ''}| {d['title'][:45]:<45} | Lens: {(d['best'] or '')[:60]}\n      {d['url']}\n      {('AI: '+d['av']) if d['av'] else ''}")
print(len(out),'flagged → stage2.json')
