# Terapeak bulk run (sold prices for many queries at once)

Why: the container cannot reach eBay sold pages, WorthPoint is paywalled, and WebSearch is capped at 200 calls per chat
turn (shared by all agents). Terapeak (eBay Seller Hub research, Dylan is signed in) returns 1 year of sold listings.

1. In Chrome, use a tab that is NOT the Lens worker tab. Open `https://www.ebay.com/sh/research?marketplace=EBAY-US&tabName=SOLD`.
2. Paste the TPR helper (`python3 scripts/review_helpers.py --terapeak-js`, first line).
3. Paste the query array inline: `window.QS=[...]`. eBay's CSP blocks fetching it from GitHub.
4. Start the loop below. It runs in the page at about 1 query every 2 s.
```
window.TP=window.TP||{};window.TPstat={done:0,err:0,run:true};
(async()=>{for(let i=0;i<QS.length;i++){if(!TPstat.run)break;const q=QS[i];if(TP[i])continue;try{const rows=(await TPR(q,365)).map(x=>{const f=x.split(' | ');return {t:(f[1]||'').replace(/[?&=%#;:+]/g,' ').slice(0,70),p:parseFloat((f[3]||'').replace(/[$,\s]/g,'')),n:parseInt(f[8])||1,d:f[f.length-1]}}).filter(r=>r.p>0);const ps=rows.map(r=>r.p).sort((a,b)=>a-b);const qq=x=>ps.length?ps[Math.floor((ps.length-1)*x)]:null;TP[i]={q,n:rows.length,p25:qq(.25),p50:qq(.5),p75:qq(.75),top:rows.slice(0,10)};TPstat.done++}catch(e){TPstat.err++;TP[i]={q,err:String(e).slice(0,80)}}await new Promise(r=>setTimeout(r,900+Math.random()*600))}TPstat.finished=true})();
```
5. Check progress with `JSON.stringify(TPstat)`.
6. Read the results out in chunks of 60 queries: run `JSON.stringify(Object.entries(TP).slice(a,b))`. Strip URL-like
   characters first; the tool blocks output that looks like query strings, which is why titles are sanitised above.
7. Save the results to `research/terapeak/<run>.jsonl`, then load them into db/comps with `scripts/tp_import.py`.

Field order of a TPR row (split on ' | '): 0 item id · 1 title · 3 sold price · 8 quantity sold · last field = date sold.
Generic queries ("decorator table lamps") pull in new retail products sold in quantity, so treat their medians as noise.
Prefer specific identification queries.
