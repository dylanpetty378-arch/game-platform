const F = ['token', 'radiusMiles', 'maxPrice', 'pageBudget', 'repeatHours', 'feeds'];
const D = {radiusMiles: 50, maxPrice: 400, pageBudget: 120, repeatHours: 0,
  feeds: ['antiques', 'jewelry', 'instruments', 'hobbies', 'free', 'toys', 'entertainment', 'sports', 'home-improvements', 'apparel', 'family', 'home']};
const $ = (id) => document.getElementById(id);

async function load() {
  const c = Object.assign({}, D, (await chrome.storage.local.get('cfg')).cfg || {});
  for (const k of F) $(k).value = k === 'feeds' ? c.feeds.join('\n') : (c[k] ?? '');
  if (!c.token) document.querySelector('details').open = true;
}

async function save() {
  const c = {feedsV: 2};
  for (const k of F) c[k] = k === 'feeds' ? $(k).value.split('\n').map((s) => s.trim()).filter(Boolean)
                    : k === 'token' ? $(k).value.trim() : Number($(k).value);
  await chrome.storage.local.set({cfg: c});
  await chrome.runtime.sendMessage('schedule');
  show();
}

async function show() {
  const {status, pending, fill} = await chrome.storage.local.get(['status', 'pending', 'fill']); const s = status || {};
  let t = `state: ${s.state || 'idle'}${s.feed ? '  (' + s.feed + ')' : ''}\n` +
          `pages ${s.pages || 0} · seen ${s.found || 0} · new ${s.fresh || 0} · saved ${s.pushed || 0}`;
  if (s.last) t += `\nlast sweep: ${new Date(s.last).toLocaleString()}`;
  if (s.feeds) t += '\n' + Object.entries(s.feeds).map(([k, v]) => `${k}: ${v}`).join(', ');
  if (pending && pending.rows) t += `\n⚠ ${pending.rows.length} listings waiting to upload — press Retry upload`;
  if (fill && fill.on) t += `\ncover-all ON — left: ${(fill.left || ['(first sweep running)']).join(', ')}`;
  if (s.note) t += `\n${s.note}`;
  if (s.err) t += `\n⚠ ${s.err}`;
  $('status').textContent = t;
}

$('go').onclick = async () => { await chrome.runtime.sendMessage('start'); setTimeout(show, 500); };
$('retry').onclick = async () => { await chrome.runtime.sendMessage('retry'); setTimeout(show, 1500); };
$('fill').onclick = async () => { await chrome.runtime.sendMessage('fill'); setTimeout(show, 500); };
$('stopfill').onclick = async () => { await chrome.runtime.sendMessage('stopfill'); setTimeout(show, 500); };
$('save').onclick = save;
load(); show(); setInterval(show, 1500);
