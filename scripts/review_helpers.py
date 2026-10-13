#!/usr/bin/env python3
"""Helpers for the review cycle (docs/review-cycle.md).
  python3 scripts/review_helpers.py --flagged              # TSV of every listing whose latest stage is 'flagged', best Lens ratio first
  python3 scripts/review_helpers.py --body <url> [...]     # listing title / price / body / still-live for Craigslist URLs
  python3 scripts/review_helpers.py --shortlist pid,pid,…  # writes shortlist.json (listing rows) for lens_export.py --photos
  python3 scripts/review_helpers.py --terapeak-js          # prints the Terapeak TPR/COMP helper to paste into an ebay.com/sh tab
"""
import sys, os, re, json, html, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import db

TERAPEAK_JS = r"""window.TPR=async(q,days=365,extra='')=>{const now=Date.now(); const u='/sh/research/api/search?marketplace=EBAY-US&keywords='+encodeURIComponent(q)+'&dayRange='+days+'&endDate='+now+'&startDate='+(now-days*864e5)+'&offset=0&limit=50&tabName=SOLD&tz=America%2FChicago&modules=searchResults'+extra; const ms=(await (await fetch(u)).text()).split('\n\n').filter(Boolean).map(s=>{try{return JSON.parse(s)}catch(e){return null}}).filter(Boolean); const sr=ms.find(m=>m._type==='SearchResultsModule'); if(!sr||!sr.results)return []; const flat=o=>{let a=[];(function w(x){if(!x)return; if(x._type==='TextSpan'&&x.text)a.push(x.text); if(typeof x==='object')for(const k in x)w(x[k])})(o);return a}; return sr.results.map(r=>flat(r).join(' | '))};
window.COMP=async(q,{days=365,min=0,ex=null,n=8}={})=>{const rows=(await TPR(q,days,(min?'&minPrice='+min:''))).map(s=>{const f=s.split(' | '); const p=parseFloat((f[3]||'').replace(/[$,\s]/g,'')); return {t:f[1]||'',p,d:f[f.length-1]}}).filter(r=>!ex||!new RegExp(ex,'i').test(r.t)); const ps=rows.map(r=>r.p).filter(x=>x>0).sort((a,b)=>a-b); const q_=x=>ps[Math.floor(ps.length*x)]; return q+' | n='+rows.length+' | p25 $'+q_(.25)+' | median $'+q_(.5)+' | p75 $'+q_(.75)+'\n  '+rows.slice(0,n).map(r=>'$'+r.p+' '+r.t.replace(/[?&=%#;:+]/g,' ').slice(0,60)+' ('+r.d+')').join('\n  ')};
// usage (one call; the tool times out at 45 s but the page keeps working — then read with get_page_text):
// const out=[]; for(const [q,o] of [['query',{min:20,ex:'parts|repro'}]]){out.push(await COMP(q,o)); await new Promise(r=>setTimeout(r,1200))}
// document.body.innerHTML='<pre id=cmp></pre>'; document.getElementById('cmp').textContent=out.join('\n'); 'ok'
"""

def body(url):
    h = subprocess.run(['curl', '-s', '-L', '-m', '25', '-A', 'Mozilla/5.0 (Macintosh)', url], capture_output=True, text=True).stdout
    live = 'postingbody' in h and not re.search(r'has been deleted|has expired|flagged for removal', h)
    m = re.search(r'<section id="postingbody">(.*?)</section>', h, re.S)
    b = html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', m.group(1)))).replace('QR Code Link to This Post', '').strip() if m else ''
    t = re.search(r'<span id="titletextonly">(.*?)</span>', h, re.S); pr = re.search(r'<span class="price">\$?([\d,]+)', h)
    return {'url': url, 'live': live, 'title': html.unescape(t.group(1)) if t else '', 'price': pr.group(1) if pr else None, 'body': b}

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    if a[0] == '--flagged':
        con = db.build_sqlite()
        q = '''SELECT s.pid, s.price, l.cat, s.area, s.title, lens.ratio, lens.med, lens.collect, lens.best, lens.ai_value, substr(lens.ai,1,160), l.clip, s.url
               FROM listing_status s JOIN listings l ON l.pid=s.pid JOIN lens ON lens.pid=s.pid WHERE s.stage='flagged' GROUP BY s.pid ORDER BY lens.ratio DESC'''
        print('pid\tprice\tcat\tarea\ttitle\tratio\tmed\tcollect\tbest\tai_value\tai\tclip\turl')
        for r in con.execute(q): print('\t'.join('' if v is None else str(v).replace('\t', ' ').replace('\n', ' ') for v in r))
    elif a[0] == '--body':
        for u in a[1:]: print(json.dumps(body(u), ensure_ascii=False))
    elif a[0] == '--shortlist':
        want = a[1].split(','); L = {str(r['pid']): r for r in db.read('listings')}
        json.dump([L[p] for p in want if p in L], open('shortlist.json', 'w')); print('shortlist.json', len(want))
    elif a[0] == '--terapeak-js':
        print(TERAPEAK_JS)
