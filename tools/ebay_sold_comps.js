// eBay SOLD comps, run inside any www.ebay.com tab in Dylan's Chrome (Claude in Chrome javascript_tool).
// Why: WebSearch budgets run out and eBay sold pages are blocked to WebFetch; a same-origin fetch from an ebay.com tab
// returns the real sold-results HTML. (Oct 24 2026, research/FB_VERIFY_BRIEF.md Stage B.)
//
// Usage: paste this file, then  await soldComps(['query one', 'query two', ...])  — results land in window.__comps
// as {query: [{t, p, d, id, img}]}. Read them back with  JSON.stringify(window.__comps)  in chunks; item links are
// https://www.ebay.com/itm/<id> (ids/urls carry no query strings, so the tool output isn't filtered).
async function soldComps(queries, perQuery = 10) {
  window.__comps = window.__comps || {};
  for (const q of queries) {
    if (window.__comps[q]) continue;
    try {
      const h = await (await fetch('/sch/i.html?_nkw=' + encodeURIComponent(q) + '&LH_Sold=1&LH_Complete=1&_ipg=60')).text();
      const d = new DOMParser().parseFromString(h, 'text/html');
      window.__comps[q] = [...d.querySelectorAll('li.s-card, li.s-item')].map((li) => {
        const a = li.querySelector('a[href*="/itm/"]'); const im = li.querySelector('img');
        return {
          t: ((li.querySelector('.s-card__title, .s-item__title') || {}).textContent || '').replace(/Opens in a new window or tab/i, '').trim(),
          p: ((li.querySelector('.s-card__price, .s-item__price') || {}).textContent || '').trim(),
          d: ((li.querySelector('.s-card__caption, .s-item__caption, .POSITIVE') || {}).textContent || '').replace(/^\s*Sold\s*/, '').trim(),
          id: ((a && a.href) || '').match(/itm\/(\d+)/)?.[1] || '',
          img: ((im && (im.getAttribute('data-defer-load') || im.getAttribute('src'))) || '').replace(/\?.*/, ''),
        };
      }).filter((x) => x.t && x.id && x.id !== '123456' && !/^Shop on eBay$/.test(x.t)).slice(0, perQuery);
    } catch (e) { window.__comps[q] = [{ err: String(e).slice(0, 100) }]; }
    await new Promise((r) => setTimeout(r, 700 + Math.random() * 700));
  }
  return Object.keys(window.__comps).length;
}
