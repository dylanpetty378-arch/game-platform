// ==UserScript==
// @name         Refurbish Lens worker
// @namespace    refurbish
// @version      2.0.0
// @description  Loader: fetches the current Refurbish Lens worker code from GitHub (re-checked every 10 min) and runs it. Install once; worker updates then arrive by themselves.
// @match        https://www.google.com/robots.txt?refurb*
// @match        https://www.google.com/search*
// @match        https://www.google.com/sorry/*
// @grant        GM_getValue
// @grant        GM_setValue
// @grant        GM_xmlhttpRequest
// @connect      raw.githubusercontent.com
// @connect      api.github.com
// @run-at       document-idle
// @updateURL    https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish/scripts/refurbish-lens.user.js
// @downloadURL  https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish/scripts/refurbish-lens.user.js
// ==/UserScript==
// This loader should never need to change. The worker logic is scripts/lens-worker.js on the same branch.
// On ordinary Google pages it does nothing: only the control page, Lens result pages (udm=26) and Google's rate-limit page.
(function () {
  'use strict';
  const URL = 'https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish/scripts/lens-worker.js';
  const TTL = 10 * 60 * 1000;
  const relevant = location.pathname === '/robots.txt' || location.pathname.startsWith('/sorry') || /[?&]udm=26/.test(location.search);
  if (!relevant) return;
  const run = (code) => {
    if (!code) { console.error('Refurbish worker: no code available'); return; }
    try { new Function('GM_getValue', 'GM_setValue', 'GM_xmlhttpRequest', code)(GM_getValue, GM_setValue, GM_xmlhttpRequest); }
    catch (e) { console.error('Refurbish worker failed', e); }
  };
  const cached = GM_getValue('workerCode', ''), at = GM_getValue('workerCodeAt', 0);
  if (cached && Date.now() - at < TTL) return run(cached);
  GM_xmlhttpRequest({
    method: 'GET', url: URL + '?t=' + Date.now(), timeout: 15000,
    onload: (r) => {
      if (r.status === 200 && r.responseText.length > 2000) { GM_setValue('workerCode', r.responseText); GM_setValue('workerCodeAt', Date.now()); run(r.responseText); }
      else run(cached);
    },
    onerror: () => run(cached), ontimeout: () => run(cached),
  });
})();
