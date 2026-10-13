// Refurbish Lens worker — the logic. Executed by the Tampermonkey loader (scripts/refurbish-lens.user.js), which
// passes GM_getValue / GM_setValue / GM_xmlhttpRequest in. EDIT THIS FILE to change the worker: every browser picks up
// the new version within ~10 minutes with no reinstall. Plain JS only. Bump WORKER_VERSION on every change.
const WORKER_VERSION = '2.0.0';

//
// HOW IT WORKS (full doc: docs/lens-worker.md)
//  * Control page: https://www.google.com/robots.txt?refurb  — status panel + Start/Stop + token box.
//  * Start marks THIS tab as the worker (sessionStorage), then the tab navigates itself:
//       Lens URL for item 1 → Google redirects to /search?…udm=26 → script waits for "Visual matches", parses,
//       saves the result to Tampermonkey storage, waits ~2.5 s, navigates to the Lens URL for item 2 → …
//    Every item is a brand-new page, so the browser frees the previous page completely. No memory build-up.
//  * Results are saved after EVERY item (Tampermonkey storage survives crashes/restarts) and uploaded to
//    db/inbox/ on the game-platform `refurbish` branch every UPLOAD_EVERY items (needs a GitHub token; see doc).
//  * When the queue is empty it fetches the cloud worker's newest queue (q/current/queue.txt). If there is
//    nothing new it waits on the control page and checks again every 20 minutes. It never stops on its own
//    except: Stop button, closing the tab, or Google rate-limiting 7 times in an hour (then it pauses 1 hour).
//  * Your own Google searches/Lens in other tabs are never touched — only the tab where Start was pressed.
(function () {
  'use strict';
  const RAW = 'https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish';
  const API = 'https://api.github.com/repos/dylanpetty378-arch/game-platform/contents/';
  const CONTROL = 'https://www.google.com/robots.txt?refurb';
  const PAUSE_MS = 2500, UPLOAD_EVERY = 25, WAIT_MS = 30000, IDLE_MIN = 20, BREAK_EVERY = 200, BREAK_MS = 120000;
  const G = (k, d) => GM_getValue(k, d), S = (k, v) => GM_setValue(k, v);
  const isWorker = () => sessionStorage.getItem('refurbWorker') === '1';
  const now = () => Date.now();
  const stats = () => Object.assign({ done: 0, flag: 0, noresult: 0, blocked: 0, uploaded: 0, started: now() }, G('stats', {}));
  const setStats = (st) => S('stats', st);
  const log = (m) => { const L = G('log', []); L.push(new Date().toISOString().slice(5, 19) + ' ' + m); S('log', L.slice(-40)); };

  // ---------- Lens page parsing (same rules as lens_gentle.js v7) ----------
  const SECOND = /ebay|etsy|reverb|chairish|1stdibs|worthpoint|mercari|poshmark|liveauctioneers|invaluable|auction|ruby lane|bonanza|depop|grailed|discogs|pricecharting|bricklink|proxibid|hibid|shopgoodwill/i;
  const COLLECT = /worthpoint|liveauctioneers|invaluable|1stdibs|chairish|ruby lane|auction|proxibid|hibid/i;
  function parseLens(t) {
    const a = t.indexOf('AI Overview'); let ai = ''; if (a >= 0) ai = t.slice(a + 11, a + 600).replace(/\n+/g, ' ').replace(/AI Mode replied:\s*/, '').trim();
    const v = t.indexOf('Visual matches'); const rows = [];
    if (v >= 0) {
      const ls = t.slice(v + 14).split('\n').map(x => x.trim()).filter(x => x && !/^(Feedback|Search Results|AI Overview|Exact matches|Visual matches|All|AI Mode|Show all|See more|Thinking|Searching|Thinking a little longer|Shared|0 files|In stock|Out of stock|Related search(es)?)$/.test(x) && !/^\d\.\d\(/.test(x) && !/^\+\d+$/.test(x) && !/^s-l\d+\.(jpg|png|webp)$/i.test(x));
      let price = null, src = null;
      for (const l of ls.slice(0, 80)) {
        const pm = l.match(/^\$([\d,.]+)\*?$/); if (pm) { price = parseFloat(pm[1].replace(/,/g, '')); continue; }
        if (l.length <= 28 && !/[|–—]/.test(l) && /^[A-Za-z0-9 .&'’\-]+$/.test(l) && !src) { src = l; continue; }
        if (src) { rows.push({ src, title: l.slice(0, 110), price }); price = null; src = null; } else { price = null; }
      }
    }
    const sec = rows.filter(r => SECOND.test(r.src) && !/craigslist/i.test(r.src));
    const prices = sec.map(r => r.price).filter(p => p > 0).sort((x, y) => x - y);
    const med = prices.length ? prices[Math.floor(prices.length / 2)] : null;
    const best = (rows.find(r => !/craigslist/i.test(r.src) && !/^(\+\d|Key |Key$|Material|Design|Type|Dimensions|Brand|Model|If you|Shared)/.test(r.title)) || rows[0] || {}).title || '';
    const aiVal = (ai.match(/(sell|sold|value|worth|price)[^.]{0,80}?\$[\d,]+(?:\s*(?:to|-|–)\s*\$?[\d,]+)?/i) || [''])[0];
    return { ai: ai.slice(0, 500), best, med, n: prices.length, collect: rows.some(r => COLLECT.test(r.src)), aiVal, srcs: [...new Set(rows.map(r => r.src))].slice(0, 8).join(','), rows: rows.slice(0, 15) };
  }

  // ---------- queue ----------
  function gmGet(url) {
    return new Promise((res, rej) => GM_xmlhttpRequest({ method: 'GET', url: url + (url.includes('?') ? '&' : '?') + 't=' + now(), onload: r => res(r), onerror: rej, ontimeout: rej, timeout: 30000 }));
  }
  async function refillQueue() {
    try {
      const m = JSON.parse((await gmGet(RAW + '/q/current/meta.json')).responseText);
      if (m.id === G('qid', '') && G('queue', []).length) return false;
      const txt = (await gmGet(RAW + '/q/current/queue.txt')).responseText.trim();
      const done = new Set(G('done', []));
      const q = txt.split(';').map(e => e.split(',')).filter(x => x[0] && (x[3] === 'r' || !done.has(x[2]))).map(x => [x[0], +x[1], x[2], x[3] || '']);
      S('queue', q); S('qid', m.id); log('loaded queue ' + m.id + ': ' + q.length + ' new items'); return q.length > 0;
    } catch (e) { log('refill failed ' + e); return false; }
  }

  // ---------- upload ----------
  function upload(force) {
    return new Promise((res) => {
      const buf = G('buf', []); const tok = G('ghToken', '');
      if (!buf.length || !tok || (!force && buf.length < UPLOAD_EVERY)) return res('skip');
      if (!force && now() - G('upFail', 0) < 5 * 60000) return res('backoff');   // after a failure, retry at most every 5 min
      const part = buf.slice(0, 200);
      const name = 'db/inbox/lensworker-' + now() + '-' + part.length + '.json';
      const body = JSON.stringify({ message: 'lens worker: ' + part.length + ' results', branch: 'refurbish', content: btoa(unescape(encodeURIComponent(JSON.stringify(part)))) });
      GM_xmlhttpRequest({ method: 'PUT', url: API + name, data: body, timeout: 30000,
        headers: { Authorization: 'Bearer ' + tok, Accept: 'application/vnd.github+json', 'Content-Type': 'application/json' },
        onload: r => { if (r.status === 201 || r.status === 200) { S('upFail', 0); S('buf', G('buf', []).slice(part.length)); const st = stats(); st.uploaded += part.length; setStats(st); log('uploaded ' + part.length); res('ok'); } else { S('upFail', now()); log('upload HTTP ' + r.status + (r.status === 401 ? ' (token not accepted - paste a new one on the control page)' : '')); res('fail'); } },
        onerror: () => { S('upFail', now()); log('upload network error'); res('fail'); }, ontimeout: () => res('fail') });
    });
  }

  // ---------- step ----------
  function lensUrl(img) { return 'https://lens.google.com/uploadbyurl?url=' + encodeURIComponent('https://images.craigslist.org/' + img + '_600x450.jpg'); }
  async function next(delay) {
    if (!G('active', false)) return showControl();
    const pauseUntil = G('pauseUntil', 0); if (pauseUntil > now()) { location.href = CONTROL; return; }
    let q = G('queue', []);
    // switch to a newer cloud queue as soon as one exists (checked every 40 items): always work the freshest, best-scored listings
    const st0 = stats();
    if (!q.length || (st0.done && st0.done % 40 === 0 && G('lastQCheck', -1) !== st0.done)) { S('lastQCheck', st0.done); await refillQueue(); q = G('queue', []); }
    if (!q.length) { S('idleSince', now()); location.href = CONTROL; return; }
    const st = stats();
    let wait = delay ?? PAUSE_MS + Math.random() * 1500;
    if (st.done && st.done % BREAK_EVERY === 0 && G('lastBreak', 0) !== st.done) { S('lastBreak', st.done); wait = BREAK_MS; log('short break'); }
    const item = q[0]; S('cur', { img: item[0], price: item[1], pid: item[2], t: now(), tries: (G('cur', {}).pid === item[2] ? (G('cur', {}).tries || 0) : 0) });
    setTimeout(() => { location.href = lensUrl(item[0]); }, wait);
  }
  function finishItem(rec) {
    const q = G('queue', []); q.shift(); S('queue', q);
    if (rec) {
      const done = G('done', []); done.push(rec.pid); S('done', done.slice(-100000));
      const buf = G('buf', []); buf.push(rec); S('buf', buf.slice(-20000));
      const st = stats(); st.done++; if (rec.f) st.flag++; st.last = now(); setStats(st);
    }
  }

  // ---------- pages ----------
  function onLensPage() {
    if (!isWorker() || !G('active', false)) return;
    const cur = G('cur', null); if (!cur) return next();
    // Wait until the page is COMPLETE, not just started: (1) "Visual matches" present, (2) at least MIN_PRICES priced
    // matches loaded or VM_GRACE ms since the heading, (3) the AI Overview finished (or AI_GRACE ms since the heading),
    // (4) page text unchanged for STABLE_MS. Hard cap WAIT_MS. v2.0 fix: v1 moved on 1.5 s after the heading appeared,
    // which lost the AI text on ~1/3 of items and returned empty match lists on ~10%.
    const MIN_PRICES = 3, VM_GRACE = 9000, AI_GRACE = 11000, STABLE_MS = 2000;
    const t0 = now(); let fin = false, vmAt = 0, lastLen = -1, stableAt = now(), timer = null;
    const measure = (t) => {
      const v = t.indexOf('Visual matches'); const tail = v >= 0 ? t.slice(v) : '';
      const prices = (tail.match(/^\$[\d,.]+\*?$/gm) || []).length;
      const a = t.indexOf('AI Overview'); const aiSeg = a >= 0 ? t.slice(a + 11, a + 400) : '';
      const aiDone = a >= 0 && aiSeg.replace(/\s+/g, ' ').trim().length > 140 && !/^\s*(Thinking|Searching|Generating)/i.test(aiSeg.trim());
      return { prices, aiDone, hasAI: a >= 0 };
    };
    const done = async (ok, why) => {
      if (fin) return; fin = true; mo.disconnect(); if (timer) clearInterval(timer);
      const t = document.body ? document.body.innerText : '';
      const m = measure(t); const wait = now() - t0;
      const empty = m.prices === 0 && /Results are personalized/.test(t) && !m.hasAI;
      if (ok && !empty) {
        const p = parseLens(t); const ratio = p.med && cur.price ? +(p.med / cur.price).toFixed(2) : null;
        const f = (ratio !== null && ratio >= 2.5 && p.n >= 2 && p.med >= 60) || (p.collect && (p.med === null || p.med >= 80)) || (!!p.aiVal && /\$\s?[1-9]\d{2,}/.test(p.aiVal));
        finishItem({ run: 'lensworker-' + G('qid', ''), pid: cur.pid, img: cur.img, price: cur.price, ratio, med: p.med, n: p.n, c: p.collect ? 1 : 0, best: p.best, ai: p.ai, av: p.aiVal, s: p.srcs, f: f ? 1 : 0, ts: now(), rows: p.rows,
                     q: { v: WORKER_VERSION, wait, prices: m.prices, ai: m.aiDone ? 1 : 0, why } });
      } else if ((cur.tries || 0) < 1) {
        cur.tries = (cur.tries || 0) + 1; S('cur', cur); log('incomplete page (' + why + '), retry ' + cur.pid); return next(5000);
      } else {
        const st = stats(); st.noresult++; setStats(st); log('no result after retry, left in queue for later ' + cur.pid); finishItem(null);
      }
      await upload(false);
      next();
    };
    const chk = () => {
      if (fin) return;
      const t = document.body ? document.body.innerText : '';
      if (t.length !== lastLen) { lastLen = t.length; stableAt = now(); }
      if (!vmAt && t.indexOf('Visual matches') >= 0) vmAt = now();
      if (!vmAt) return;
      const m = measure(t), sinceVm = now() - vmAt, stable = now() - stableAt >= STABLE_MS;
      const matchesReady = m.prices >= MIN_PRICES || sinceVm >= VM_GRACE;
      // AI Overview: Google shows it on only some images. Wait for it only if its heading has appeared (up to AI_GRACE);
      // if no heading 3 s after the matches, move on.
      const aiReady = m.aiDone || (!m.hasAI && sinceVm >= 3000) || sinceVm >= AI_GRACE;
      if (matchesReady && aiReady && stable) done(true, (m.prices >= MIN_PRICES ? 'p' : 'P') + (m.aiDone ? 'a' : (m.hasAI ? 'A' : 'n')));
    };
    const mo = new MutationObserver(chk); mo.observe(document.documentElement, { childList: true, subtree: true, characterData: true });
    timer = setInterval(chk, 500);               // stability is time-based, so also poll (single page, no build-up)
    setTimeout(() => { if (vmAt) done(true, 'cap'); else done(false, 'no matches'); }, WAIT_MS);
  }
  function onSorry() {
    if (!isWorker()) return;
    const st = stats(); st.blocked++; setStats(st);
    const B = G('blocks', []).filter(x => x > now() - 3600e3); B.push(now()); S('blocks', B);
    if (B.length >= 7) { S('pauseUntil', now() + 3600e3); log('rate-limited 7x in an hour: pausing 1 hour'); }
    else log('rate-limited: waiting 3 min');
    setTimeout(() => { location.href = CONTROL; }, B.length >= 7 ? 5000 : 180000);
  }
  function showControl() {
    const st = stats(); const q = G('queue', []); const buf = G('buf', []);
    const active = G('active', false), tok = !!G('ghToken', ''), pu = G('pauseUntil', 0);
    document.body.innerHTML = '';
    const d = document.createElement('div'); d.style.cssText = 'font:15px/1.5 -apple-system,Segoe UI,sans-serif;max-width:760px;margin:24px auto;padding:0 16px;color:#111;background:#fff';
    d.innerHTML = `<h2 style="margin:0 0 8px">Refurbish Lens worker <small style="font-weight:normal;color:#666">v${WORKER_VERSION}</small></h2>
      <div id="rs">Status: <b>${active ? (isWorker() ? 'RUNNING in this tab' : 'running in another tab') : 'stopped'}</b>${pu > now() ? ' — paused (rate limit) until ' + new Date(pu).toLocaleTimeString() : ''}</div>
      <div>Done ${st.done} · flagged ${st.flag} · no result ${st.noresult} · blocked ${st.blocked} · uploaded ${st.uploaded} · waiting to upload ${buf.length}</div>
      <div>Queue ${q.length} (cloud queue id ${G('qid', '-')}) · GitHub token: ${tok ? 'set' : '<b>not set — results stay in this browser until a Claude session exports them</b>'}</div>
      <p><button id="go">Start in this tab</button> <button id="stop">Stop</button> <button id="up">Upload now</button></p>
      <p>GitHub token (fine-grained, game-platform only, Contents read+write): <input id="tok" type="password" size="40"> <button id="savetok">Save token</button></p>
      <p style="color:#555">Leave this tab open (it can be in the background). It moves through Lens pages by itself — one fresh page per listing, so memory never builds up. Close it or press Stop to end.</p>
      <pre id="lg" style="background:#f4f4f4;padding:8px;font-size:12px;white-space:pre-wrap">${G('log', []).slice(-15).join('\n')}</pre>
      <pre id="dump" style="display:none"></pre>`;
    document.body.appendChild(d);
    d.querySelector('#go').onclick = () => { sessionStorage.setItem('refurbWorker', '1'); S('active', true); S('workerHeartbeat', now()); log('started'); next(500); };
    d.querySelector('#stop').onclick = () => { S('active', false); sessionStorage.removeItem('refurbWorker'); log('stopped'); showControl(); };
    d.querySelector('#up').onclick = async () => { await upload(true); showControl(); };
    d.querySelector('#savetok').onclick = () => { const v = d.querySelector('#tok').value.trim(); if (v) { S('ghToken', v); S('upFail', 0); log('token saved'); showControl(); } };
    // ?refurb&dump renders the not-yet-uploaded results so a Claude session can export them without a token
    if (/dump/.test(location.search)) { const p = d.querySelector('#dump'); p.style.display = 'block'; p.textContent = 'EXPORT_START\n' + JSON.stringify(buf.map(({ rows, ...x }) => x)) + '\nEXPORT_END'; }
    if (/clearbuf=/.test(location.search)) { const n = +location.search.match(/clearbuf=(\d+)/)[1]; S('buf', G('buf', []).slice(n)); log('cleared ' + n + ' exported results'); }
    // worker tab idling on the control page: check for new work every IDLE_MIN minutes (or when a pause ends)
    if (active && isWorker()) {
      const waitMs = pu > now() ? pu - now() + 5000 : IDLE_MIN * 60000;
      setTimeout(() => { upload(true).then(() => next(0)); }, G('queue', []).length && pu <= now() ? 1000 : waitMs);
    }
  }

  if (location.pathname === '/robots.txt') showControl();
  else if (location.pathname.startsWith('/sorry')) onSorry();
  else if (location.pathname === '/search' && /[?&]udm=26/.test(location.search)) onLensPage();
})();
