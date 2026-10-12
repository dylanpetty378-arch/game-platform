// Gentle Lens loop v6.
// v6 changes: EVERY Lens result is kept in ALL (one object per listing, f=1 if flagged) – the whole of ALL goes into the database, not just flags;
//   loadQ(url) fetches the queue string from the GitHub branch (no pasting 30 KB strings);
//   progress (STATS, FLAGGED, queue position) is checkpointed to localStorage every 10 items, so a tab reload or
//   Chrome crash loses nothing — re-paste this file and call resume(); CAP is a variable (default 3000).
// v5: showStatus() not status() (window.status is reserved). One hidden iframe, recreated every 25 items or on a stall;
//   memory watchdog MEMLIM (default 2200 MB); 2.5 s pause between items. Never remove the pause.
window.QUEUE=window.QUEUE||[]; window.ALL=window.ALL||[]; window.FLAGGED=window.FLAGGED||[];
window.STATS=Object.assign({done:0,blocked:0,errs:0,flag:0,idx:0,stopped:'',start:Date.now()},window.STATS||{}); STATS.stopped='';
window.MEMLIM=window.MEMLIM||2200; window.CAP=window.CAP||3000; window.RUNNING=false; window.MEMLOG=window.MEMLOG||[];
window.RUNID=window.RUNID||'';
const SECOND=/ebay|etsy|reverb|chairish|1stdibs|worthpoint|mercari|poshmark|liveauctioneers|invaluable|auction|ruby lane|bonanza|depop|grailed|discogs|pricecharting|bricklink|proxibid|hibid|shopgoodwill/i;
const COLLECT=/worthpoint|liveauctioneers|invaluable|1stdibs|chairish|ruby lane|auction|proxibid|hibid/i;
const RETAIL=/amazon|walmart|lowe|home depot|target|best buy|wayfair|michaels|hobby lobby|dick's|bass pro|cabela|academy|harbor freight|ace hardware|zoro|grainger|uline/i;
window.parseLens=(t)=>{const a=t.indexOf('AI Overview'); let ai=''; if(a>=0){ai=t.slice(a+11,a+420).replace(/\n+/g,' ').replace(/AI Mode replied:\s*/,'').trim()}
 const v=t.indexOf('Visual matches'); const rows=[]; if(v>=0){const ls=t.slice(v+14).split('\n').map(x=>x.trim()).filter(x=>x&&!/^(Feedback|Search Results|AI Overview|Exact matches|Visual matches|All|AI Mode|Show all|See more|Thinking|Searching|Thinking a little longer|Shared|0 files|In stock|Out of stock|Related search(es)?)$/.test(x)&&!/^\d\.\d\(/.test(x));
  let price=null,src=null; for(const l of ls.slice(0,60)){const pm=l.match(/^\$([\d,.]+)\*?$/); if(pm){price=parseFloat(pm[1].replace(/,/g,''));continue} if(l.length<=28&&!/[|–—]/.test(l)&&/^[A-Za-z0-9 .&'’\-]+$/.test(l)&&!src){src=l;continue} if(src){rows.push({src,title:l.slice(0,90),price});price=null;src=null}else{price=null}}}
 const sec=rows.filter(r=>SECOND.test(r.src)&&!/craigslist/i.test(r.src)); const prices=sec.map(r=>r.price).filter(p=>p>0).sort((x,y)=>x-y);
 const med=prices.length?prices[Math.floor(prices.length/2)]:null; const best=(rows.find(r=>!/craigslist/i.test(r.src))||rows[0]||{}).title||'';
 const aiVal=(ai.match(/(sell|sold|value|worth|price)[^.]{0,80}?\$[\d,]+(?:\s*(?:to|-|–)\s*\$?[\d,]+)?/i)||[''])[0];
 const collect=rows.some(r=>COLLECT.test(r.src)); const retailOnly=rows.length>0&&rows.every(r=>RETAIL.test(r.src)||/craigslist/i.test(r.src));
 return {ai:ai.slice(0,260),best,med,n:prices.length,collect,retailOnly,aiVal,srcs:[...new Set(rows.map(r=>r.src))].slice(0,5).join(',')}};
window.memMB=()=>performance.memory?Math.round(performance.memory.usedJSHeapSize/1048576):-1;
window.newFrame=()=>{document.querySelectorAll('iframe').forEach(f=>{try{f.onload=null;f.src='about:blank';f.remove()}catch(e){}}); const f=document.createElement('iframe'); f.style.cssText='width:900px;height:700px;position:fixed;top:0;left:0;opacity:0.01;pointer-events:none'; document.body.appendChild(f); window.F=f; return f};
window.lensOne=(img)=>new Promise(res=>{const f=window.F||newFrame(); let t0=Date.now(),fin=false,mo=null,wd=null;
 const finish=()=>{if(fin)return; fin=true; if(mo){mo.disconnect();mo=null} if(wd)clearInterval(wd); f.onload=null; let t=''; try{t=f.contentDocument.body.innerText}catch(e){} res({t,ms:Date.now()-t0,stalled:Date.now()-t0>=30000})};
 f.onload=()=>{let doc; try{doc=f.contentDocument}catch(e){return finish()} if(!doc||!doc.documentElement)return finish();
  const chk=()=>{const t=doc.body?doc.body.innerText:''; if(/unusual traffic/.test(t)||(t.indexOf('Visual matches')>=0&&Date.now()-t0>2500))finish()};
  mo=new MutationObserver(chk); mo.observe(doc.documentElement,{childList:true,subtree:true,characterData:true}); chk();
  wd=setInterval(()=>{if(Date.now()-t0>25000)finish(); else chk()},1500)};
 setTimeout(()=>{if(!fin)finish()},30000);
 f.src='https://lens.google.com/uploadbyurl?url='+encodeURIComponent('https://images.craigslist.org/'+img+'_600x450.jpg')});
window.pushQ=(s)=>{for(const e of s.split(';')){const [im,pr]=e.split(','); if(im)QUEUE.push([im,+pr])} return QUEUE.length};
// loadQ(url, startAt): fetch the whole queue string from the GitHub branch and queue it from position startAt (default STATS.idx)
window.loadQ=async(url,startAt)=>{const s=(await (await fetch(url,{cache:'no-store'})).text()).trim(); const all=s.split(';'); const k=startAt??STATS.idx; QUEUE.length=0; pushQ(all.slice(k).join(';')); STATS.idx=k; window.QURL=url; return 'queued '+QUEUE.length+' from '+k+' of '+all.length};
// checkpoint/resume: survives reloads and Chrome crashes (google.com localStorage, ~1 MB max used)
window.saveState=()=>{try{localStorage.setItem('refurbLens',JSON.stringify({RUNID,QURL:window.QURL,STATS,ALL}))}catch(e){}};
window.resume=async()=>{const s=JSON.parse(localStorage.getItem('refurbLens')||'null'); if(!s)return 'no saved state'; window.RUNID=s.RUNID; Object.assign(STATS,s.STATS); STATS.stopped=''; ALL.length=0; ALL.push(...(s.ALL||[])); FLAGGED.length=0; FLAGGED.push(...ALL.filter(r=>r.f)); const r=await loadQ(s.QURL,STATS.idx); return 'resumed '+RUNID+' done='+STATS.done+' flag='+STATS.flag+' | '+r};
window.exportAll=(from=0,to=1e9)=>{const d=document.getElementById('exp')||document.createElement('pre'); d.id='exp'; const part=ALL.filter(r=>r.i>=from&&r.i<to); d.textContent='EXPORT_START\n'+JSON.stringify(part)+'\nEXPORT_END'; document.body.prepend(d); return 'exported '+part.length+' chars '+d.textContent.length};
const sleep=(ms)=>new Promise(r=>{const mc=new MessageChannel(); mc.port1.onmessage=()=>setTimeout(r,ms); mc.port2.postMessage(0)});
window.showStatus=()=>{const el=document.getElementById('st')||(()=>{const d=document.createElement('pre');d.id='st';d.style.cssText='position:fixed;bottom:0;left:0;background:#fff;color:#000;padding:8px;font:14px monospace;z-index:9';document.body.appendChild(d);return d})(); el.textContent='Refurbish Lens pass '+RUNID+' — done '+STATS.done+' | flagged '+STATS.flag+' | queue '+QUEUE.length+' | blocked '+STATS.blocked+' | mem '+memMB()+'MB'+(STATS.stopped?' | STOPPED: '+STATS.stopped:'')+'\nClose this tab any time to stop it. Progress is saved; it can be resumed.'};
window.runLoop=async()=>{if(RUNNING)return 'already'; RUNNING=true; STATS.stopped=''; let since=0;
 while(RUNNING&&QUEUE.length){
  if(STATS.done>=CAP){STATS.stopped='cap';break}
  const m=memMB(); if(m>MEMLIM){STATS.stopped='memory '+m;break}
  if(since>=25){newFrame(); since=0; MEMLOG.push([STATS.done,m]); await sleep(4000)}
  const [img,price]=QUEUE[0]; const i=STATS.idx;
  try{const {t,stalled}=await lensOne(img); if(stalled){STATS.stalls=(STATS.stalls||0)+1; newFrame(); since=0}
   if(/unusual traffic/.test(t)){STATS.blocked++; showStatus(); if(STATS.blocked>6){STATS.stopped='blocked';break} await sleep(180000); continue}
   QUEUE.shift(); STATS.idx++; since++;
   const p=parseLens(t); const ratio=p.med&&price?+(p.med/price).toFixed(2):null;
   const flag=(ratio!==null&&ratio>=2.5&&p.n>=2&&p.med>=60)||(p.collect&&(p.med===null||p.med>=80))||(!!p.aiVal&&/\$\s?[1-9]\d{2,}/.test(p.aiVal));
   const rec={i,img,price,ratio,med:p.med,n:p.n,c:p.collect?1:0,best:p.best,ai:p.ai,av:p.aiVal,s:p.srcs,f:flag?1:0,ts:Date.now()};
   ALL.push(rec); if(flag){FLAGGED.push(rec);STATS.flag++}
   STATS.done++; STATS.t=Date.now();
  }catch(e){STATS.errs++; STATS.lastErr=String(e); QUEUE.shift(); STATS.idx++}
  if(STATS.done%10===0)saveState();
  try{showStatus()}catch(e){} await sleep(2500)}
 RUNNING=false; saveState(); if(!STATS.stopped&&!QUEUE.length)STATS.stopped='queue empty'; try{showStatus()}catch(e){} return STATS.stopped};
// Start a new run:  RUNID='run14'; STATS.done=0;STATS.idx=0;STATS.flag=0;FLAGGED.length=0; await loadQ('<raw url>/queue.txt',0); newFrame(); runLoop().catch(e=>{STATS.stopped='crash '+e}); 'started'
// Resume after reload: (re-paste this file) await resume(); newFrame(); runLoop().catch(e=>{STATS.stopped='crash '+e}); 'resumed'
'gentle v6 ready mem='+memMB();
