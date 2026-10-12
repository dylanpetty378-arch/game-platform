// Gentle Lens loop v7 — runs inside Dylan's Chrome on a https://www.google.com/robots.txt tab.
// Paste the whole file with the Chrome javascript_tool, then start it (bottom of file).
//
// v7: FOLLOW mode — when the queue runs out it fetches the cloud worker's latest queue
//       (q/current/queue.txt on the game-platform `refurbish` branch) and keeps going, forever, until the tab closes.
//     Queue entries are "img,price,pid"; every result carries its pid, so it can be matched to the database directly.
//     DONE pid set in localStorage → a listing is never sent through Lens twice from this browser.
//     Optional uploader: if localStorage.ghToken holds a GitHub fine-grained token (Contents: read/write on game-platform,
//       set by Dylan himself in the DevTools console), every 50 results are written to db/inbox/ on the refurbish branch and
//       the cloud cycle ingests them. Without a token, a Claude session exports with exportAll() + get_page_text.
// v6: every result kept in ALL (f=1 if flagged); checkpoint to localStorage every 10 items; resume() after reload.
// v5: showStatus() not status() (window.status is reserved). One hidden iframe, recreated every 25 items or on a stall;
//     memory watchdog MEMLIM; 2.5 s pause between items. NEVER remove the pause or run two loops — it froze Dylan's PC once.
window.RAW=window.RAW||'https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish';
window.QUEUE=window.QUEUE||[]; window.ALL=window.ALL||[]; window.FLAGGED=window.FLAGGED||[];
window.STATS=Object.assign({done:0,blocked:0,errs:0,flag:0,idx:0,stopped:'',start:Date.now(),uploaded:0},window.STATS||{}); STATS.stopped='';
window.MEMLIM=window.MEMLIM||2200; window.CAP=window.CAP||5000; window.RUNNING=false; window.MEMLOG=window.MEMLOG||[];
window.RUNID=window.RUNID||''; window.FOLLOW=(window.FOLLOW===undefined)?true:window.FOLLOW; window.QID=window.QID||'';
window.DONE=window.DONE||new Set((()=>{try{return JSON.parse(localStorage.getItem('refurbDone')||'[]')}catch(e){return []}})());
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
 return {ai:ai.slice(0,260),best,med,n:prices.length,collect,retailOnly,aiVal,srcs:[...new Set(rows.map(r=>r.src))].slice(0,5).join(','),rows:rows.slice(0,12)}};
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
// queue entries: [img, price, pid|null, position]
window.pushQ=(s,base=0)=>{let k=base; for(const e of s.split(';')){const [im,pr,pid]=e.split(','); if(im)QUEUE.push([im,+pr,pid||null,k]); k++} return QUEUE.length};
window.loadQ=async(url,startAt)=>{const s=(await (await fetch(url,{cache:'no-store'})).text()).trim(); const all=s.split(';'); const k=startAt??STATS.idx; QUEUE.length=0; pushQ(all.slice(k).join(';'),k); STATS.idx=k; window.QURL=url; return 'queued '+QUEUE.length+' from '+k+' of '+all.length};
window.setQ=(str,startAt)=>{str=str.trim(); try{localStorage.setItem('refurbQ',str)}catch(e){} const all=str.split(';'); const k=startAt??STATS.idx; QUEUE.length=0; pushQ(all.slice(k).join(';'),k); STATS.idx=k; window.QURL=''; return 'queued '+QUEUE.length+' from '+k+' of '+all.length};
// follow the cloud worker's queue: returns true if a NEW queue was loaded
window.followQ=async()=>{try{const m=await (await fetch(RAW+'/q/current/meta.json',{cache:'no-store'})).json(); if(m.id===QID)return false;
  const r=await loadQ(RAW+'/q/current/queue.txt',0); QID=m.id; RUNID='cloud-'+m.id; STATS.followed=(STATS.followed||0)+1; STATS.lastFollow=r; return true}catch(e){STATS.lastErr='follow '+e; return false}};
window.saveState=()=>{try{if(ALL.length>4000)ALL.splice(0,ALL.length-4000); localStorage.setItem('refurbLens',JSON.stringify({RUNID,QID,QURL:window.QURL,STATS,ALL})); localStorage.setItem('refurbDone',JSON.stringify([...DONE].slice(-60000)))}catch(e){}};
window.resume=async()=>{const s=JSON.parse(localStorage.getItem('refurbLens')||'null'); if(!s)return 'no saved state'; window.RUNID=s.RUNID; window.QID=s.QID||''; Object.assign(STATS,s.STATS); STATS.stopped=''; ALL.length=0; ALL.push(...(s.ALL||[])); FLAGGED.length=0; FLAGGED.push(...ALL.filter(r=>r.f)); const r=s.QURL?await loadQ(s.QURL,s.QID?0:STATS.idx):setQ(localStorage.getItem('refurbQ')||'',STATS.idx); return 'resumed '+RUNID+' done='+STATS.done+' flag='+STATS.flag+' | '+r};
window.exportAll=(fromTs=0)=>{const d=document.getElementById('exp')||document.createElement('pre'); d.id='exp'; const part=ALL.filter(r=>(r.ts||0)>fromTs).map(({rows,...x})=>x); d.textContent='EXPORT_START\n'+JSON.stringify(part)+'\nEXPORT_END'; document.body.prepend(d); return 'exported '+part.length+' chars '+d.textContent.length};
// optional direct upload to the database inbox (only if Dylan set localStorage.ghToken himself)
window.upload=async()=>{const tok=localStorage.getItem('ghToken'); if(!tok)return 'no token'; const from=STATS.uploaded||0; const part=ALL.filter(r=>r.seq>from); if(!part.length)return 'nothing';
 const name='db/inbox/'+(RUNID||'chrome')+'-'+Date.now()+'.json'; const body={message:'lens inbox '+part.length,branch:'refurbish',content:btoa(unescape(encodeURIComponent(JSON.stringify(part))))};
 const r=await fetch('https://api.github.com/repos/dylanpetty378-arch/game-platform/contents/'+name,{method:'PUT',headers:{Authorization:'Bearer '+tok,Accept:'application/vnd.github+json'},body:JSON.stringify(body)});
 if(r.ok){STATS.uploaded=part[part.length-1].seq; saveState(); return 'uploaded '+part.length} STATS.lastErr='upload '+r.status; return 'upload failed '+r.status};
window.sleep=(ms)=>new Promise(r=>{const mc=new MessageChannel(); mc.port1.onmessage=()=>setTimeout(r,ms); mc.port2.postMessage(0)});
window.showStatus=()=>{const el=document.getElementById('st')||(()=>{const d=document.createElement('pre');d.id='st';d.style.cssText='position:fixed;bottom:0;left:0;background:#fff;color:#000;padding:8px;font:14px monospace;z-index:9';document.body.appendChild(d);return d})(); el.textContent='Refurbish Lens pass '+RUNID+' — done '+STATS.done+' | flagged '+STATS.flag+' | queue '+QUEUE.length+' | blocked '+STATS.blocked+' | uploaded '+(STATS.uploaded||0)+' | mem '+memMB()+'MB'+(STATS.stopped?' | STOPPED: '+STATS.stopped:'')+(STATS.waiting?' | waiting for new cloud queue':'')+'\nClose this tab any time to stop it. Progress is saved; it can be resumed.'};
window.runLoop=async()=>{if(RUNNING)return 'already'; RUNNING=true; STATS.stopped=''; let since=0; STATS.seq=STATS.seq||0;
 while(RUNNING){
  if(!QUEUE.length){ if(!FOLLOW)break; STATS.waiting=1; showStatus(); if(await followQ()){STATS.waiting=0; continue} await sleep(20*60*1000); continue }
  if(STATS.done>=CAP){STATS.stopped='cap';break}
  const m=memMB(); if(m>MEMLIM&&!window.AUTORELOAD){STATS.stopped='memory '+m+' (reload the tab, re-paste, resume())';break}
  const [img,price,pid,pos]=QUEUE[0];
  if(pid&&DONE.has(pid)){QUEUE.shift(); STATS.idx++; continue}
  if(since>=25){newFrame(); since=0; MEMLOG.push([STATS.done,m]); await sleep(4000)}
  try{const {t,stalled}=await lensOne(img); if(stalled){STATS.stalls=(STATS.stalls||0)+1; newFrame(); since=0}
   if(/unusual traffic/.test(t)){STATS.blocked++; showStatus(); if(STATS.blocked>6){STATS.stopped='blocked';break} await sleep(180000); continue}
   // bad read: empty page, no "Visual matches", or the SAME text as the previous item (stale frame after a stall).
   const sig=t.slice(0,1500); const bad=!t||t.indexOf('Visual matches')<0||sig===window.LASTSIG;
   if(bad){ window.RETRY=(window.RETRY||0)+1; newFrame(); since=0; await sleep(3000);
     if(window.RETRY<=1)continue;                       // one retry with a fresh frame
     window.RETRY=0; STATS.noresult=(STATS.noresult||0)+1; QUEUE.shift(); STATS.idx++; continue }  // give up: not recorded, stays queued in the DB
   window.RETRY=0; window.LASTSIG=sig;
   QUEUE.shift(); STATS.idx++; since++; window.SINCE_RELOAD=(window.SINCE_RELOAD||0)+1;
   const p=parseLens(t); const ratio=p.med&&price?+(p.med/price).toFixed(2):null;
   const flag=(ratio!==null&&ratio>=2.5&&p.n>=2&&p.med>=60)||(p.collect&&(p.med===null||p.med>=80))||(!!p.aiVal&&/\$\s?[1-9]\d{2,}/.test(p.aiVal));
   const rec={seq:++STATS.seq,run:RUNID,i:pos,pid,img,price,ratio,med:p.med,n:p.n,c:p.collect?1:0,best:p.best,ai:p.ai,av:p.aiVal,s:p.srcs,f:flag?1:0,ts:Date.now(),rows:p.rows};
   ALL.push(rec); if(flag){FLAGGED.push(rec);STATS.flag++} if(pid)DONE.add(pid);
   STATS.done++; STATS.t=Date.now();
  }catch(e){STATS.errs++; STATS.lastErr=String(e); QUEUE.shift(); STATS.idx++}
  if(STATS.done%10===0)saveState();
  // memory leak guard: Lens pages leak ~20 MB each inside this tab. With AUTORELOAD (set by the userscript) the tab
  // checkpoints and reloads itself every RELOAD_EVERY items or when memory passes MEMLIM; the userscript resumes it.
  if(window.AUTORELOAD&&(window.SINCE_RELOAD>=(window.RELOAD_EVERY||40)||memMB()>MEMLIM*0.9)){saveState(); STATS.reloads=(STATS.reloads||0)+1; saveState(); location.reload(); return 'reloading'}
  if(STATS.done%50===0&&localStorage.getItem('ghToken')){try{await upload()}catch(e){STATS.lastErr='upload '+e}}
  try{showStatus()}catch(e){} await sleep(2500)}
 RUNNING=false; saveState(); if(!STATS.stopped&&!QUEUE.length)STATS.stopped='queue empty'; try{showStatus()}catch(e){} return STATS.stopped};
// ---- Start (fresh browser): paste this file, then:
//   FOLLOW=true; await followQ(); newFrame(); runLoop().catch(e=>{STATS.stopped='crash '+e}); 'started '+QUEUE.length
// ---- Resume after a reload: paste this file, then:
//   await resume(); newFrame(); runLoop().catch(e=>{STATS.stopped='crash '+e}); 'resumed'
// ---- Check:  JSON.stringify({done:STATS.done,flag:STATS.flag,blocked:STATS.blocked,errs:STATS.errs,stalls:STATS.stalls,stopped:STATS.stopped,q:QUEUE.length,run:RUNID,mem:memMB()})
'gentle v7 ready mem='+memMB();
