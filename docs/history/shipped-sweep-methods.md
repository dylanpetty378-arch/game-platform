# Shipped-items sweep – methods (built Oct 12, 2026, Run 11)

Companion to `site-access-methods.md`, which covers the local-pickup sources. This file covers sources where the item ships to Keller from anywhere.

## Verdict after Run 11

| Source | Shipped nationwide? | Access | Yield for "seller doesn't know" | Keep? |
|---|---|---|---|---|
| Facebook Marketplace, shipping-only | Yes | Browser (GraphQL replay) | Low – resellers + eBay-syndicated items dominate | Yes, but filter eBay items and skip generic keywords |
| ShopGoodwill (all stores) | Yes | Container API | Very low – Goodwill researches titles; auctions | Only for 0-bid lots ending soon in cameras/instruments/tools |
| OfferUp | App-only shipping search | **Container 403 since Oct 12**; web has no shipping filter | n/a | Parked for shipped; browser-only for local |
| AuctionNinja | Mostly CT/NC shipping-only sales | Container, HTML | Low – estate companies research lots | Not built |
| eBay | Yes – the classic source | Search pages hit a bot challenge; Terapeak works | Would be high (badly titled, few-bid auctions) | **Needs Dylan's eBay developer key (Browse API) – ask** |
| Mercari / Poshmark / Depop / Etsy | Yes | Browser / blocked | Reseller marketplaces – tested Mercari 9/21, nothing | Skip |

## Facebook Marketplace – shipping-only harvest

Same machinery as the local harvest (`site-access-methods.md`), with these differences:

1. **Capture the template from a page loaded with `?deliveryMethod=shipping`**, e.g. `https://www.facebook.com/marketplace/category/antiques?deliveryMethod=shipping&sortBy=creation_time_descend&maxPrice=200` (category template) and `https://www.facebook.com/marketplace/fortworth/search/?query=estate&exact=false&maxPrice=200&deliveryMethod=shipping&daysSinceListed=7` (keyword template). Grab the `queryID`/`variables` pair whose variables contain both `"bqf"` and `"count"`. Doc id on 10/12: 29274780305481097 (same as 10/8).
2. **Shipping-only flags** in `params.browse_request_params`: `commerce_enable_shipping: true`, `commerce_enable_local_pickup: false`. Location/radius are ignored for shipped items – results come from every state.
3. **Category feed** (`SEO(slug)`): `bqf = {callsite:'COMMERCE_MKTPLACE_SEO', query:''}`, `custom_request_params.seo_url = slug`, `serp_landing_settings = {virtual_category_id: slug}`, `surface:'TOPIC_PAGE'`, `commerce_search_and_rp_category_id: null`, `commerce_search_and_rp_ctime_days: null`. Slugs that worked: antiques, toys, instruments, entertainment, jewelry, home-improvements, sports, electronics, home. `hobbies` returned only 25 in 16 pages; `arts-crafts` returned 0.
4. **Keyword search** (`KW(q)`): `bqf = {callsite:'COMMERCE_MKTPLACE_WWW', query:q}`, `surface:'SEARCH'`, and **`commerce_search_and_rp_ctime_days` must be a semicolon list of epoch-day numbers** (`Math.floor(Date.now()/864e5)` and the N days before it, e.g. `20738;20737;…`). Passing `7` returns zero results with no error.
5. Run everything from the `facebook.com/robots.txt` tab. Keep the harvest in `window.FBC` (and `sessionStorage`); **do not rely on `localStorage`** – it was wiped when the tab navigated to a Marketplace page, taking a 1,108-listing harvest with it. Export flags to the container (write them into a `<pre>`, `get_page_text`) before navigating anywhere.
6. Rate limit: 167 GraphQL pages in one session with no `1675004` error on 10/12.
7. Review grid: 16 columns × 72 px thumbnails = 128 listings per screenshot. Every screenshot fails once with a 30 s CDP timeout and succeeds on the retry.

### Filtering eBay-syndicated listings (new, important)
Facebook now injects eBay listings into Marketplace ("New! Discover eBay listings on Marketplace"). They are indistinguishable in the feed JSON we keep, but the item page shows "Summarized by eBay.ai", "See item on eBay" and a "Facebook may receive a commission" line, and there is no seller profile. They cluster by city (a lot of "Citrus Heights, CA" on 10/12). They are priced at eBay market, so they never clear the rule – open and discard, or add a seller-city blacklist once a few are known. Worth checking whether the raw GraphQL node carries an `is_ebay`/`external_listing` flag so they can be dropped at harvest time.

## ShopGoodwill – national ending-soon pull (container)

`st.sg(low=0, high=25, sort="1", page=p, size=100, cat=<id>)` – `size` is ignored (40 per page), `sort="1"` = ending soonest. Category ids: 1 Antiques · 15 Art · 170 Cameras · 4 Collectibles · 14 Glass · 13 Musical Instruments · 12 Sports · 9 Toys · 114 Tools · 8 Crafts · 113 Misc · 2208 Bulk · 364 Science. Times in the response are Pacific. Item detail: `GET /api/ItemDetail/GetItemDetailModelByItemId/<id>` (description, `pickupOnly`, `shippingPrice`). Image URLs use backslashes – replace with `/`. 1,549 lots ≤$25 with ≤1 bid were pulled in ~4 min across 13 categories; three review agents found nothing that clears the rule. Goodwill's own descriptions name the brand and model, so the arbitrage isn't there; a max-bid play on 0-bid lots is the only use.

## OfferUp – status Oct 12
- `offerup.com/search` from the container returns a Cloudflare 403 page now (it worked through Oct 8). Browser `fetch('/search?…')` from an offerup.com tab still returns `__NEXT_DATA__`.
- The web search exposes only DISTANCE / PRICE / SORT / CONDITION filters; every tile carries `flags: ["LOCAL_PICKUP"]`, and none of `DELIVERY_PARAM=s`, `delivery=shipping`, `SHIPPING=true`, `DELIVERY_METHOD=SHIPPING` etc. change the results. Shipping search exists only in the app.

## Next-source candidates for shipped sweeps
1. **eBay Browse API** (`https://api.ebay.com/buy/browse/v1/item_summary/search`, filters: `buyingOptions:{AUCTION}`, `itemEndDate`, `bidCount`, `price`, `itemLocationCountry:US`, sort by `endingSoonest`/`newlyListed`). Needs a free developer account under Dylan's eBay login (application token for Browse, no user consent needed). This is the legitimate path and the one real nationwide source of badly titled, few-bid auctions – the classic shipped arbitrage. Container-friendly, thousands of items per minute, images included.
2. HiBid with `shippingAvailable` lots nationwide (same GraphQL as local; needs an account to bid).
3. Craigslist does not ship as a platform; skip for shipped sweeps.
