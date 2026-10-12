"""Usage: python3 lookup.py IDX [IDX...]  -> prints listing details; python3 lookup.py --photos IDX OUT.jpg -> 2x2 sheet of 600x450 photos"""
import json,sys,subprocess,re,html as H
S=json.load(open('/home/claude/sweep/run12_list.json'))
def url(r): return f"https://www.craigslist.org/view/d/{r['slug']}/{r['uuid']}"
if sys.argv[1]=='--photos':
    import st
    r=S[int(sys.argv[2])]
    st.sheet([(f"{r['idx']}-{i}",f"https://images.craigslist.org/{im}_600x450.jpg","") for i,im in enumerate(r['imgs'][:6])],sys.argv[3],cols=3,cell=600)
    print(sys.argv[3]); sys.exit()
for a in sys.argv[1:]:
    r=S[int(a)]
    print(f"[{r['idx']}] ${r['price']} | {r['area']} ({r['region']}) | cat {r['cat']} | {r['title']}\n  {url(r)}\n  photos: {len(r['imgs'])}")
    if '--body' in sys.argv or True:
        h=subprocess.run(["curl","-s","-L","--max-time","20",url(r)],capture_output=True,text=True).stdout
        b=re.search(r'<section id="postingbody">(.*?)</section>',h,re.S)
        t=H.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',b.group(1)))).replace('QR Code Link to This Post','').strip() if b else '(no body / gone)'
        print('  body:',t[:600])
