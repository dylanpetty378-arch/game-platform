// Refurbish Watcher — background service worker (Oct 22 2026).
// One sweep: open a Marketplace category page in a background tab, capture Facebook's own search query template and
// session tokens from it (the method that worked in the Sept/Oct 2026 browser sweeps — docs/facebook.md), move the tab
// to facebook.com/robots.txt (light page, doesn't freeze), then replay the query one page at a time for each category
// feed, newest first, within the radius of Keller. Pauses happen here, not in the tab (background tabs throttle timers).
// A feed stops as soon as a whole page is listings we've already saved. New listings are pushed to GitHub as JSON
// files under db/fb/inbox/ on branch refurbish; the free fb-score workflow scores them; a Claude chat reviews later.
// Only listing data is kept (id, title, price, city, photo, category) — never seller names or profiles.

const KELLER = {lat: 32.934, lon: -97.229};
const DEFAULTS = {
  token: '', repo: 'dylanpetty378-arch/game-platform', branch: 'refurbish',
  radiusMiles: 50, maxPrice: 400, pageBudget: 120, perFeedMax: 40, repeatHours: 0,
  feeds: ['antiques', 'jewelry', 'instruments', 'hobbies', 'free', 'toys', 'entertainment', 'sports', 'home-improvements'],
};
const START_URL = 'https://www.facebook.com/marketplace/category/antiques?sortBy=creation_time_descend';
const SEEN_DAYS = 30;
const CHUNK = 800;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const today = () => Math.floor(Date.now() / 864e5);
async function cfg() { return Object.assign({}, DEFAULTS, (await chrome.storage.local.get('cfg')).cfg || {}); }
async function setStatus(patch) {
  const s = (await chrome.storage.local.get('status')).status || {};
  await chrome.storage.local.set({status: Object.assign(s, patch, {updated: new Date().toISOString()})});
}

// ---- runs inside the Facebook page (MAIN world): find the Marketplace search query + session tokens
function captureKit() {
  try {
    const html = document.documentElement.innerHTML;
    const re = /"queryID":"(\d+)","variables":/g; let m;
    while ((m = re.exec(html))) {
      let j = m.index + m[0].length, d = 0, k = j;
      for (; k < html.length; k++) { const c = html[k]; if (c === '{') d++; else if (c === '}') { d--; if (!d) { k++; break; } } }
      const v = html.slice(j, k);
      if (v.includes('"bqf"') && v.includes('"count"')) {
        return {ok: true, doc: m[1], cv: JSON.parse(v), dtsg: require('DTSGInitialData').token, lsd: require('LSD').token,
                uid: require('CurrentUserInitialData').USER_ID};
      }
    }
    return {ok: false, err: 'No Marketplace query found on the page — are you logged in to Facebook in this browser?'};
  } catch (e) { return {ok: false, err: 'capture failed: ' + String(e).slice(0, 200)}; }
}

// ---- runs inside facebook.com/robots.txt (MAIN world, same origin): fetch ONE page of a feed
async function fetchPage(kit, vars) {
  try {
    const b = new URLSearchParams({av: kit.uid, __user: kit.uid, __a: '1', fb_dtsg: kit.dtsg, lsd: kit.lsd,
      fb_api_caller_class: 'RelayModern', fb_api_req_friendly_name: 'CometMarketplaceSearchContentContainerQuery',
      variables: JSON.stringify(vars), server_timestamps: 'true', doc_id: kit.doc});
    const t = await (await fetch('/api/graphql/', {method: 'POST', body: b,
      headers: {'content-type': 'application/x-www-form-urlencoded', 'x-fb-lsd': kit.lsd}})).text();
    const j = JSON.parse(t.split('\n')[0]);
    if (j.errors && j.errors.length) return {err: (j.errors[0].message || 'error') + ' ' + (j.errors[0].code || ''), rate: j.errors[0].code === 1675004};
    const f = j && j.data && j.data.marketplace_search && j.data.marketplace_search.feed_units;
    if (!f) return {err: 'no feed_units in response'};
    const rows = [];
    for (const e of f.edges || []) {
      const L = e.node && e.node.listing; if (!L || !L.id) continue;
      const g = (L.location && L.location.reverse_geocode) || {};
      rows.push({id: L.id, t: L.marketplace_listing_title || '', p: +((L.listing_price && L.listing_price.amount) || 0),
                 city: g.city || '', st: g.state || '', img: (L.primary_listing_photo && L.primary_listing_photo.image &&
                 L.primary_listing_photo.image.uri) || '', sold: !!(L.is_sold || L.is_pending)});
    }
    return {rows, next: f.page_info && f.page_info.has_next_page ? f.page_info.end_cursor : null};
  } catch (e) { return {err: 'page failed: ' + String(e).slice(0, 200)}; }
}

function feedVars(kit, c, slug, cursor) {
  const V = JSON.parse(JSON.stringify(kit.cv));
  V.buyLocation = {latitude: KELLER.lat, longitude: KELLER.lon};
  const B = V.params.browse_request_params;
  Object.assign(B, {commerce_search_and_rp_category_id: null, commerce_enable_shipping: false, commerce_enable_local_pickup: true,
    filter_location_latitude: KELLER.lat, filter_location_longitude: KELLER.lon, filter_radius_km: Math.round(c.radiusMiles * 1.609),
    filter_price_upper_bound: c.maxPrice * 100, commerce_search_and_rp_ctime_days: null, commerce_search_sort_by: 'CREATION_TIME_DESCEND'});
  V.params.custom_request_params.seo_url = slug;
  V.params.custom_request_params.serp_landing_settings = {virtual_category_id: slug};
  V.count = 24; V.cursor = cursor || null;
  return V;
}

function waitLoaded(tabId) {
  return new Promise((resolve) => {
    const done = () => { chrome.tabs.onUpdated.removeListener(l); resolve(); };
    const l = (id, info) => { if (id === tabId && info.status === 'complete') done(); };
    chrome.tabs.onUpdated.addListener(l); setTimeout(done, 45000);
  });
}
async function inPage(tabId, func, args) {
  const [r] = await chrome.scripting.executeScript({target: {tabId}, world: 'MAIN', func, args: args || []});
  return r && r.result;
}

async function pushRows(c, rows, meta) {
  for (let i = 0; i < rows.length; i += CHUNK) {
    const part = rows.slice(i, i + CHUNK);
    const name = new Date().toISOString().replace(/[:.]/g, '-') + `-${i / CHUNK}.json`;
    const body = JSON.stringify({sweep: meta, rows: part});
    const content = btoa(unescape(encodeURIComponent(body)));
    const r = await fetch(`https://api.github.com/repos/${c.repo}/contents/db/fb/inbox/${name}`, {method: 'PUT',
      headers: {Authorization: `Bearer ${c.token}`, Accept: 'application/vnd.github+json'},
      body: JSON.stringify({message: `fb sweep: ${part.length} listings`, content, branch: c.branch})});
    if (!r.ok) throw new Error(`GitHub ${r.status}: ${(await r.text()).slice(0, 160)}`);
  }
}

async function retryPending() {
  const c = await cfg(); const {pending} = await chrome.storage.local.get('pending');
  if (!pending || !pending.rows || !pending.rows.length) return 0;
  await pushRows(c, pending.rows, pending.meta); await chrome.storage.local.remove('pending');
  return pending.rows.length;
}

let running = false;
async function sweep() {
  if (running) return; running = true;
  const c = await cfg(); let tabId = null;
  await setStatus({state: 'starting', err: '', feed: '', pages: 0, found: 0, fresh: 0, pushed: 0, started: new Date().toISOString()});
  try {
    if (!c.token) throw new Error('Add your GitHub token in the extension first.');
    try { const n = await retryPending(); if (n) await setStatus({note: `uploaded ${n} listings left over from last time`}); } catch (e) {}
    const st = await chrome.storage.local.get('seen'); const seen = st.seen || {};
    const cut = today() - SEEN_DAYS; for (const k in seen) if (seen[k] < cut) delete seen[k];
    const tab = await chrome.tabs.create({url: START_URL, active: false}); tabId = tab.id;
    await waitLoaded(tabId); await sleep(5000);
    const kit = await inPage(tabId, captureKit);
    if (!kit || !kit.ok) throw new Error((kit && kit.err) || 'could not read the Marketplace page');
    await chrome.tabs.update(tabId, {url: 'https://www.facebook.com/robots.txt'}); await waitLoaded(tabId); await sleep(1500);
    const fresh = []; const perFeed = {}; const done = []; let pages = 0, found = 0, stop = '';
    const fill0 = (await chrome.storage.local.get('fill')).fill || {};
    // "Cover all" mode: visit the categories not yet covered first, then the rest.
    const order = fill0.on ? c.feeds.filter((f) => !(fill0.cover || {})[f]).concat(c.feeds.filter((f) => (fill0.cover || {})[f])) : c.feeds;
    for (const slug of order) {
      if (pages >= c.pageBudget || stop) break;
      let cursor = null, n = 0, fp = 0, ended = false;
      while (true) {
        if (fp >= c.perFeedMax) { ended = true; break; }
        if (pages >= c.pageBudget) break;
        const r = await inPage(tabId, fetchPage, [kit, feedVars(kit, c, slug, cursor)]);
        pages++; fp++;
        if (!r || r.err) { if (r && r.rate) stop = 'Facebook rate limit reached — the rest waits for the next run'; else { perFeed[slug + '_err'] = r ? r.err : 'no result'; ended = true; } break; }
        let newOnPage = 0;
        for (const x of r.rows) {
          found++; if (seen[x.id]) continue;
          seen[x.id] = today(); newOnPage++; n++;
          if (!x.sold) fresh.push(Object.assign(x, {cat: slug, ts: new Date().toISOString()}));
        }
        await setStatus({state: 'sweeping', feed: slug, pages, found, fresh: fresh.length});
        if (!r.next || newOnPage === 0) { ended = true; break; }   // end of feed, or caught up with what we already have
        cursor = r.next; await sleep(900 + Math.random() * 900);
      }
      perFeed[slug] = n; if (ended) done.push(slug); await sleep(2000 + Math.random() * 2000);
    }
    await chrome.storage.local.set({seen});
    const fill = (await chrome.storage.local.get('fill')).fill || {};
    let fillNote = '';
    if (fill.on) {
      fill.cover = fill.cover || {}; for (const f of done) fill.cover[f] = true;
      fill.left = c.feeds.filter((f) => !fill.cover[f]);
      if (!fill.left.length) { fill.on = false; fill.finished = new Date().toISOString(); fillNote = 'All categories covered.'; }
      else { const wait = stop ? 60 : 10; chrome.alarms.create('fill', {delayInMinutes: wait});
             fillNote = `Cover-all: ${fill.left.length} categories left (${fill.left.join(', ')}) — next sweep in ${wait} min.`; }
      await chrome.storage.local.set({fill});
    }
    const meta = {ts: new Date().toISOString(), pages, found, feeds: perFeed, radius_mi: c.radiusMiles, max_price: c.maxPrice, doc: kit.doc, note: stop,
                  fill: fill.on !== undefined ? {on: !!fill.on, left: fill.left || []} : undefined};
    if (fresh.length) {
      await chrome.storage.local.set({pending: {rows: fresh, meta}});
      await pushRows(c, fresh, meta); await chrome.storage.local.remove('pending');
    }
    await setStatus({state: 'done', pushed: fresh.length, err: stop, last: meta.ts, feeds: perFeed, note: fillNote});
  } catch (e) {
    await setStatus({state: 'error', err: String(e.message || e).slice(0, 300)});
  } finally {
    if (tabId) try { await chrome.tabs.remove(tabId); } catch (e) {}
    running = false;
  }
}

chrome.runtime.onMessage.addListener((msg, _s, reply) => {
  if (msg === 'start') { sweep(); reply('started'); }
  else if (msg === 'fill') { chrome.storage.local.set({fill: {on: true, cover: {}, started: new Date().toISOString()}})
                               .then(() => setStatus({note: 'Cover-all started: sweeps repeat (10 min apart) until every category is covered.'}))
                               .then(() => sweep()); reply('filling'); }
  else if (msg === 'stopfill') { chrome.alarms.clear('fill'); chrome.storage.local.get('fill').then(({fill}) =>
                               chrome.storage.local.set({fill: Object.assign(fill || {}, {on: false})})).then(() => setStatus({note: 'Cover-all stopped.'})); reply('ok'); }
  else if (msg === 'retry') { retryPending().then((n) => setStatus({note: `uploaded ${n} pending listings`, err: ''}))
                                         .catch((e) => setStatus({err: String(e.message || e)})); reply('retrying'); }
  else if (msg === 'schedule') { schedule().then(() => reply('ok')); return true; }
});
async function schedule() {
  const c = await cfg(); await chrome.alarms.clear('sweep');
  if (c.repeatHours > 0) chrome.alarms.create('sweep', {periodInMinutes: Math.max(120, c.repeatHours * 60), delayInMinutes: 1});
}
chrome.alarms.onAlarm.addListener((a) => { if (a.name === 'sweep' || a.name === 'fill') sweep(); });
chrome.runtime.onStartup.addListener(schedule);
