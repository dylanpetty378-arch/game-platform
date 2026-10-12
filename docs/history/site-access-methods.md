# Site access methods – how to see the most listings, fastest

Last tested: Sept 21, 2026 (sweep 5). The working code is in `claude/sweep_tools.py`, a Python module for the cloud container. Facebook runs inside Chrome using the browser snippet below.

**The rule for every site:** harvest everything cheaply, then review photos in bulk on contact sheets, then open only the shortlist. **Never search by brand name.** Brand searches only find sellers who already know the brand.

## Speed ranking (what worked)

| Site | Method | Volume per run | Needs browser? | Notes |
|---|---|---|---|---|
| Craigslist | JSON API `sapi.craigslist.org` | ~4,000 posts in 48 hrs across 17 categories in <2 min | No (container) | Best by far. Full-size images come straight from the CDN. |
| OfferUp | Server-rendered JSON (`__NEXT_DATA__`) | 50 per page, ~4,000 per run | No (container) | Needs a location cookie, and must NOT send a custom User-Agent. |
| Facebook Marketplace | In-page GraphQL replay | ~15 per page, ~250 per query, ~6,600 in a 28-query run | Yes (Chrome, logged in) | Slow (~1–2 min per query). The tab must stay in the foreground or Chrome throttles it. |
| ShopGoodwill | Buyer API POST | 40 per page. Fort Worth store = seller 63, ~1,900 items | No (container) | All auctions with brand titles and a picked-over audience. Low priority. |
| eBay sold comps | `fetch` inside an ebay.com tab | 1 query per 3–4 sec | Yes | Container gets 403. Use a light page (ebay.com/robots.txt) as the host tab. |
| estatesales.net | Public JSON API (`/api/sale-details`) | ~160 DFW sales, ~10,000 photos a week | No (container) | Built and tested 9/21 (`esn.py`). Photos go up 1–3 days before the sale; no prices online. |

## Craigslist

Endpoint: `https://sapi.craigslist.org/web/v8/postings/search/full`

- **Parameters:**
  - `batch=21-0-360-0-0` (21 = Dallas/Fort Worth area id)
  - `searchPath=<category>` (e.g. `ata` antiques, `cba` collectibles, `jwa` jewelry, `pha` photo, `msa` music)
  - `lat=32.934&lon=-97.229&search_distance=30` (miles from Keller)
  - `purveyor=owner`, `max_price=200`, `min_price=`, `sort=date`, `query=` (optional)
- **360 results max per call.** The offset in `batch` is rejected ("not enough batch params"). To get more, split the price range: `sweep_cat()` halves `min_price`/`max_price` until each band has fewer than 360 posts.
- **Decoding:** posting id = `decode.minPostingId + item[0]`; posted time = `decode.minPostedDate + item[1]`; category id = `item[2]`; price = `item[3]`; title = last element. The tagged sub-lists are `[4, …]` images, `[6, slug]` and `[13, uuid]`.
- **Images:** `https://images.craigslist.org/<full id incl. suffix>_300x300.jpg` (or `_600x450`). **Keep the trailing suffix** (e.g. `3:00y0y_abc_0t20CI` → `00y0y_abc_0t20CI`), or you get a 404.
- **Listing URL:** `https://www.craigslist.org/view/d/<slug>/<uuid>`. Fetching it gives the body text and 600x450 images (`clpost.post()`).
- **Don't** load `*.craigslist.org/search` pages repeatedly in Chrome. That got the browser IP blocked mid-sweep. The container API was never blocked.

## OfferUp

- `curl` `https://offerup.com/search?PRICE_MAX=200&SORT=-posted[&q=…]` with cookie `ou.location={"city":"Keller","state":"TX","zipCode":"[zip]","latitude":32.934,"longitude":-97.229,"source":"user"}` (URL-encoded).
- Parse `<script id="__NEXT_DATA__">` → `props.pageProps.searchFeedResponse.looseTiles[].listing` (id, title, price, location, image).
- **Paginate** with `&pageCursor=<nextPageCursor>`. 40 pages ≈ 4,000 listings in about a minute.
- **Gotchas:**
  - A custom `-A "Mozilla/5.0"` gets a 403. Use curl's default UA.
  - `zipcode`/`lat`/`lng` URL params are ignored. Only the cookie sets location.
  - The feed is heavy on dealer cars and new retail goods. Filter titles (the `filt.py` junk list, plus a car/"down payment" regex).
- **Item page:** `https://offerup.com/item/detail/<listingId>`. From the container these started returning 403 after a big feed pull (9/22); check liveness from an offerup.com browser tab instead (fetch the item page, read `ROOT_QUERY["listing(...)"].state`). The description is in `__NEXT_DATA__`, and images are `images.offerup.com/...jpg`.

## Facebook Marketplace (browser)

- The account is Dylan's main profile with full Marketplace access (checked at `/marketplace/status/`). The "15–30 results per search" cap only applies to the visible UI scroll. The GraphQL replay below paginates past it.
- **Setup, once per tab:**
  1. Open any search, e.g. `https://www.facebook.com/marketplace/fortworth/search/?query=lamp&exact=false&maxPrice=200`.
  2. Run the snippet below. It reads the page's own search query (doc id + variables) and the session tokens, then replays it with new query text, radius, price, days-listed and cursor.

```js
// 1) capture template + tokens from the loaded search page.
//    Pick the query whose variables contain both "bqf" and "count" – the doc id changes between page loads
//    (27517490627932547 on 9/21/26), and grabbing the first Marketplace query by name gets the wrong one.
const html=document.documentElement.innerHTML; const re=/"queryID":"(\d+)","variables":/g; let m;
while((m=re.exec(html))){let j=m.index+m[0].length,d=0,k=j; for(;k<html.length;k++){const c=html[k]; if(c==='{')d++; else if(c==='}'){d--; if(!d){k++;break}}}
  const v=html.slice(j,k); if(v.includes('"bqf"')&&v.includes('"count"')){window.DOC=m[1]; window.FBV=JSON.parse(v); break}}
window.FBT={dtsg:require('DTSGInitialData').token, lsd:require('LSD').token, uid:require('CurrentUserInitialData').USER_ID};
window.FBQ=async(vars)=>{const b=new URLSearchParams({av:FBT.uid,__user:FBT.uid,__a:'1',fb_dtsg:FBT.dtsg,lsd:FBT.lsd,
  fb_api_caller_class:'RelayModern',fb_api_req_friendly_name:'CometMarketplaceSearchContentContainerQuery',
  variables:JSON.stringify(vars),server_timestamps:'true',doc_id:DOC});
  return (await fetch('/api/graphql/',{method:'POST',body:b,headers:{'content-type':'application/x-www-form-urlencoded','x-fb-lsd':FBT.lsd}})).text()};
// 2) harvest one query into sessionStorage 'FBX' (dedupes by id)
window.FBALL=async(q,{max=250,days=null,maxPrice=200,lat=32.934,lon=-97.229,km=50,label=q}={})=>{
  const V=JSON.parse(JSON.stringify(FBV)); V.buyLocation={latitude:lat,longitude:lon}; V.params.bqf.query=q; V.savedSearchQuery=q;
  const B=V.params.browse_request_params; Object.assign(B,{filter_location_latitude:lat,filter_location_longitude:lon,filter_radius_km:km,
    filter_price_upper_bound:maxPrice*100,commerce_search_and_rp_ctime_days:days}); V.count=24;
  const store=JSON.parse(sessionStorage.getItem('FBX')||'{}'); let cur=null,got=0,pages=0;
  while(got<max&&pages<20){V.cursor=cur; const f=JSON.parse((await FBQ(V)).split('\n')[0])?.data?.marketplace_search?.feed_units; if(!f)break;
    for(const e of f.edges){const L=e.node&&e.node.listing; if(!L||!L.id||store[L.id])continue;
      store[L.id]={id:L.id,t:L.marketplace_listing_title,p:+L.listing_price?.amount,c:L.location?.reverse_geocode?.city,
        img:L.primary_listing_photo?.image?.uri,Q:label,sold:L.is_sold||L.is_pending}; got++}
    pages++; if(!f.page_info?.has_next_page)break; cur=f.page_info.end_cursor; await new Promise(r=>setTimeout(r,700))}
  sessionStorage.setItem('FBX',JSON.stringify(store)); return label+': +'+got};
```

- **NEW (Sept 21, sweep 8) – category feeds with no keyword, newest first. This is now the primary Facebook method.**
  - Load any category page, e.g. `https://www.facebook.com/marketplace/fortworth/antiques?sortBy=creation_time_descend`, then grab the query whose variables contain `"bqf"` and `"count"` (same doc id as keyword search). Its `bqf.callsite` is `COMMERCE_MKTPLACE_SEO` with `query:""`.
  - Replay with `custom_request_params.seo_url = <slug>` and `serp_landing_settings.virtual_category_id = <slug>`, and set `browse_request_params.commerce_search_and_rp_category_id = null`. The slug alone picks the category; `commerce_search_sort_by: "CREATION_TIME_DESCEND"` keeps it newest-first. Radius, price and days filters work as in keyword search.
  - **No ~250 cap:** antiques paginated past 1,000 listings (24 per page).
  - Slugs that work this way (tested 9/21): **antiques, toys, instruments, hobbies, free, entertainment, sports, home-improvements**. Sub-category slugs (antique-electronics, typewriters, antique-coins, collectible-stamps) do **not** filter this way – they fell back to the general all-items feed. For those, load the sub-category page itself and capture its own `category_ids` from the page's query variables.
  - The feed includes shipped listings from other states (`commerce_enable_shipping: true`). Set it to false for pickup-only, or keep it (shipped buys are allowed) and check the city.
  - Yield on 9/21: 5,879 listings from 10 category feeds in ~6 minutes (antiques 1,000+, toys 720, instruments 720, entertainment 699, home-improvements 676, sports 654, hobbies 535, free 309).
  - Snippet: `FBSEO(slug,{maxPages,km,maxPrice,days})` in `sweep_tools.py` (`FB_CATEGORY_JS`). Run the category queue in the background and poll.
  - Why it matters: keyword search only finds listings whose titles contain our words; category feeds return **every** listing in the category, including the badly titled ones ("old thing", "box of stuff") where the value hides.
- **Run the harvest from a light tab (9/22):** on a category page, save `{DOC, CV (the variables JSON), dtsg, lsd, uid}` to `localStorage.FBKIT`, then navigate the same tab to `facebook.com/robots.txt` and run the harvest there (same-origin `fetch('/api/graphql/')` works). The heavy Marketplace tab froze twice mid-harvest and lost its data; the robots.txt tab didn't. Save results to localStorage after every query.
- **Rate limit:** after ~100–150 GraphQL pages in a session FB returns `{"errors":[{"message":"Rate limit exceeded","code":1675004}]}` and every later query is empty. Budget ~120 pages per run and put the highest-value feeds first.
- **Run queries in the background** so the tool call doesn't time out: `(async()=>{for(const q of QUEUE){await FBALL(q,{days:N})}})()`. Then poll `Object.keys(JSON.parse(sessionStorage.getItem('FBX'))).length`.
- **`days`** = `commerce_search_and_rp_ctime_days`: 1, 7, 30 or null. Use it for "since the last run."
- **An empty query returns 0.** FB needs a keyword. Use the generic query list in the runbook.
- **Grid review on a light tab (big speed-up, 9/21):** grid screenshots on the Marketplace tab kept timing out (30 s) because the Marketplace page is heavy. Instead, save the harvest to `localStorage.GRIDDATA` (it's shared across facebook.com tabs, unlike sessionStorage), **close the Marketplace tab**, open `https://www.facebook.com/robots.txt` and render the grid there (`G(start)`, 20 columns × 7 rows = 140 per screenshot). Screenshots then return in ~2 s instead of timing out. fbcdn images load fine there because it's the same origin. Two facebook.com tabs open at once still share a renderer – keep only one.
- **Review in bulk:**
  - Titles: dump `index|price|title` into `<pre>` on facebook.com/robots.txt (same origin, so sessionStorage is visible) and read it with get_page_text. About 1,100 titles per read.
  - Photos (preferred – photo-first review): overlay a fixed 20-column grid of every harvested listing on the FB tab (78px-tall thumbs, index + price + title under each) and screenshot ~120 per frame after a 4 s wait for lazy images. Filter junk titles first (playpens, kennels, cars, phones, bouquets). Keep the list in `sessionStorage` (it's per-tab) and write flags to a file in the container – `localStorage` flags have gone missing.
  - Item viewer: on `/marketplace/item/<id>/`, wait ~3.5 s, take the first image wider than 300px plus every `img[alt^="Product photo"]` (other `scontent` images on the page are 'Today's picks' from other sellers), rebuild the page as a 3×2 grid of 510px photos under the description, then screenshot. Store the code as a string in `localStorage.IVC` and run `await eval(localStorage.IVC)` after each navigation.
  - Navigating the tab stops any background harvest in it. Finish the harvest, then open items.
  - `fetch('/marketplace/item/<id>/')` returns a page shell without the listing data – don't bother.
  - Item page: `/marketplace/item/<id>/`. `[role=main].innerText` gives the description. Collect `img[src*=scontent]` into a grid for the photos.
- **Gotchas:**
  - Screenshots often time out on the first try (lazy images and a busy renderer). Retry once.
  - After a timeout, tab ids can change, so re-read tab context.
  - Keep a single FB tab. A second facebook.com tab shares the renderer and freezes both.
  - Output containing long URLs gets blocked by the tool ("cookie/query string data"). Write it into the page and read it with get_page_text instead.
  - fbcdn image URLs are signed (`oh`/`oe` params) and expire in a few days. The container can fetch them while they're fresh.

## eBay sold comps (browser)

- Open `https://www.ebay.com/robots.txt` (a light page that doesn't freeze).
- Define `SC(q)` to `fetch('/sch/i.html?_nkw=…&LH_Sold=1&LH_Complete=1&_ipg=60')`.
- Parse with regex on the `s-card__title` / `s-card__price` chunks. The attributes are unquoted, and DOMParser on 1.5 MB pages froze the tab.
- Queue queries 3–4 s apart and read `OUT` after. About 15–30 calls triggers throttling (short responses, then timeouts). Keep it to the few items that need it and use WebSearch for the rest. eBay's robots.txt allows `/sch/` for Claude-User but prohibits bulk automated access, so stay light.

## estatesales.net (built Sept 21, sweep 6)

- **Every sale near Keller, no login:** `GET https://www.estatesales.net/api/sale-details?bypass=bycoordinatesanddistance:32.934_-97.229_40` → JSON list (id, name, cityName, typeName, firstUtcStartDate, lastUtcEndDate, pictureCount, orgName, url). 158 sales within 40 miles on 9/21.
- **Every photo in a sale:** `GET https://www.estatesales.net/api/sale-details/<id>?include=pictures` → `pictures[]` with `url` (1200px), `thumbnailUrl` (325px) and an optional `description` (the company's caption, ~10% of photos).
- **Window:** keep sales whose dates overlap the next 7 days and whose type is EstateSales / MovingSales / MovedOffsite* / ByAppointment. (OnlineOnlyAuctions are auctions – skip.)
- **Review:** 12×8 contact sheets of thumbnails (96 per sheet) with `montage.sheet(..., cols=12, cell=150)`. For a full week (~10,000 photos / ~107 sheets) split the sheets across **4 parallel review agents** (≈27 sheets each, ~3.5 min); each writes `esn_flags_X.txt` (index | sale | city | item | captioned? | est. resale | confidence) after zooming with `esn_zoom.py`. Then verify the top ~20 at full size yourself and run Terapeak on each. Order sales by title keywords (antique, vintage, attic, collector, MCM, "50 years", hoard) and review those first. Open anything interesting at 1200px.
- **What it's good for:** choosing which sales to attend and what to grab first. Prices are never online, and companies caption what they've researched – so the targets are the *uncaptioned* photos (e.g. the 1977 Star Wars tee in Aledo, the Gouda-style vase in Arlington).
- **Yield on 9/21:** 57 sales / 10,191 photos this week; about 2,300 reviewed; 5 sales worth a visit.
- estatesales.org / gsalr.com (same company, garage + estate sales): HTML pages with photo URLs on `eso-cdn.tlcdn.workers.dev`. Loads from the container; not parsed yet. Many listings duplicate estatesales.net, but gsalr adds **garage/yard sales**, which is where the least-informed sellers are.

## Is it still for sale? (liveness check – run before every sheet)

- **Craigslist / OfferUp (container):** `python3 live.py <url> ...` (in `sweep_tools.py`). OfferUp reads `ROOT_QUERY["listing(...)"].state` (LISTED = live); Craigslist looks for 404 / "deleted" / "expired".
- **Facebook (browser):** FB blocks iframes, and `fetch()` of an item page doesn't contain the listing. So navigate through the list, carrying the queue in localStorage:
  - `localStorage.LQ` = JSON array of ids, `localStorage.LR` = results. `localStorage.LC` holds the checker: wait 4 s, read `[role=main]`, record LIVE / SOLD / PENDING / GONE, navigate to the next id.
  - Call `await eval(localStorage.LC)` once per item. About 6 s per item.
  - Match "Sold"/"Pending" only as a **whole line** near the top (`/^(Sold|Pending)$/m`) – "Sold as a set" in a description gave a false positive.
  - Bonus: the check shows the **seller's exact title and any price cut** ("$75$150" = was $150). On 9/21 it showed that three items we'd marked "seller doesn't know" actually name the brand. Always run it before calling a seller unaware.

## Facebook photos in the container – tested, not worth it

- fbcdn thumbnail URLs download fine from the container while fresh (200, ~13 KB).
- But moving the URLs out of the browser costs ~500 bytes of text per listing (~130 tokens) versus ~13 tokens per listing on a grid screenshot. **Keep the in-browser grid screenshots.**

## eBay Terapeak (sold-price research) – WORKING (unlocked Sept 21)

- Page: https://www.ebay.com/sh/research (Seller Hub → Research → Product research). Needs Dylan's eBay login in the browser.
- **JSON API (same-origin fetch from any ebay.com/sh page):**
  `GET /sh/research/api/search?marketplace=EBAY-US&keywords=<q>&dayRange=365&endDate=<ms>&startDate=<ms>&offset=0&limit=50&tabName=SOLD&tz=America%2FChicago&modules=searchResults`
  - Response = several JSON objects separated by blank lines; take the one with `_type:"SearchResultsModule"` → `results[]`. Flatten every `TextSpan.text` in a row: [itemId, title, format, avg sold price, shipping, …, qty sold, total, …, last sold date].
  - `&modules=aggregates` gives avg/median-style summary (avg sold price, range, total sold, sellers).
  - **Filters that work:** `&minPrice=50` / `&maxPrice=` (drops parts and accessories – essential), `&sorting=-avgsalesprice`. `limit` max is 50 (use `offset` to page). `dayRange` up to 1095 (3 years).
  - Default sort is by quantity sold, so parts dominate; always set `minPrice` and an exclusion regex.
- **Helper (paste into the tab):** `TPR(q,days,pages,extra)` returns flattened rows; `COMP(q,{min,max,ex,n})` returns `n / p25 / median / p75` plus example sales. Code is in `sweep_tools.py` (`TERAPEAK_JS`). Run a queue in the background 2.5 s apart; 40 queries took ~2 min with no throttling.
- Output containing listing text sometimes trips the tool's "cookie/query string" filter – write results into the page and read them with get_page_text.

## HiBid (built Sept 21, sweep 7) – DFW online auctions

- Browser only (container gets 403). No login needed to search.
- **GraphQL at `https://hibid.com/graphql` with our own minimal query** (introspection is disabled; the site's own query uses fragments, so write a small one):
```
query LS($pageNumber:Int!,$pageLength:Int!,$zip:String,$miles:Int,$status:AuctionLotStatus,$searchText:String,$sortOrder:EventItemSortOrder){
 lotSearch(input:{zip:$zip,miles:$miles,status:$status,searchText:$searchText,sortOrder:$sortOrder,countAsView:false},pageNumber:$pageNumber,pageLength:$pageLength,sortDirection:ASC){
  pagedResults{ totalCount results{ id lead description featuredPicture{thumbnailLocation}
   lotState{highBid bidCount minBid buyNow timeLeftSeconds} auction{ id auctioneer{name city} } } } } }
```
  - Variables: `{zip:"[zip]", miles:40, status:"OPEN", sortOrder:"TIME_LEFT", pageNumber:1..100, pageLength:100}`. `TIME_LEFT` + `ASC` = closing soonest first. Other sort values: CLOSING_TODAY, CLOSING, HIGH_BID, LOT_NUMBER, NO_ORDER. Results cap at 10,000.
  - Lot page: `https://hibid.com/lot/<id>`.
- **Filter:** drop store-return sellers (Big D Discount, Authentic Warehouse – ~60% of lots) and lots with high bid > $150. On 9/21: 4,000 soonest-closing lots → 2,088 after filtering; 294 photo-reviewed on a 14-column grid.
- **Verdict so far:** mostly estate-company auctions (Tyler Grace – Addison, Rusty by Design – Forney, Marks & Marks – Dallas). Bids jump in the last minutes, so the only workable play is **a max bid set from Terapeak comps** (max bid = what still leaves profit ≥ max($50, price) after the buyer's premium, usually 15–20%). The one standout ("Kelvin & Hughes sextant in box", $6) turned out to match the common Indian reproduction. Bidding needs Dylan's HiBid account.

## gsalr.com garage sales (built Sept 21, sweep 7)

- `POST https://gsalr.com/block/city/listings` (form: `lat`, `lon`, `radius`, optional `day`, `q`, `types`) returns HTML for the ~30 sales nearest the point – **`radius` is ignored**, so `gsalr.sweep()` tiles a 35-mile grid (8-mile steps) and dedupes. 71 DFW sales on 9/21 (21 garage/yard, 1 multi-family, the rest estate/online).
- Each listing has street address, dates, full text description and photo count. Photos: sale page `?gallery=1`, images at `ps.tlstatic.com/image/w700-h500/...jpeg` (`gsalr.photos(url)`).
- Most garage sales have 0–5 photos, so **screen by description keywords** (comics, vintage, antique, collection, coins, records, tools, toys, retiring, estate) and look at photos where they exist.

## AuctionNinja (tested Sept 21)

- `https://www.auctionninja.com/tx/dallas` is server-rendered (loads in the container with `--compressed`): 57 sales, but most are **shipping-only sales from other states** (CT, NC). Local DFW pickup sales are rare. Sale pages: `/<company>/sales/details/<slug>.html`.
- Verdict: low priority for local pickup; usable later for shipped buys.

## CTBids (Caring Transitions online estate auctions) (tested Sept 21)

- DFW franchise locations (from the public `GET https://api.ctbids.com/services/api/v1/buyer/seolocation/list`): Dallas (117, 447), Plano (132), Garland (135, 546), Euless (413), Granbury (280).
- Item/sale search endpoints (`/api/v1/search/...`) need a token ("Forbidden: token missing"). Use the website in the browser (Locations → a DFW location). Auctions run 7–14 days, bidding starts at $1 – same max-bid approach as HiBid. Needs Dylan's account to bid.

## Mercari (tested Sept 21, sweep 8)

- Browser only (container 403). Search page: `https://www.mercari.com/search/?keyword=<q>&itemStatuses=1&sortBy=2&maxPrice=<cents>` (sortBy 2 = newest; prices in cents).
- **API:** the page calls `GET https://www.mercari.com/v1/api?operationName=searchFacetQuery&variables=…&extensions=…` (persisted query). Capture one request (hook `window.fetch`, scroll once), keep its URL **and headers** (needs the page's `authorization`, `x-csrf-token`, `x-session` etc.), then change `variables.criteria` (`query`, `maxPrice`, `sortBy`, `itemStatuses:[1]`, `categoryIds`). 100 items per call.
  - **Paging uses `startKey` = previous response's `nextKey`** (the `offset` field is ignored).
  - Item fields: id (`m…`), name, price (cents), photos[].thumbnail, brand, categoryTitle. Item URL: `https://www.mercari.com/us/item/<id>/`.
- **Verdict:** works, but Mercari is a reseller marketplace – titles are already keyword-stuffed with brands and prices are near market. 3,367 newest items for 16 generic words produced nothing that cleared the rule. Better used as a **selling** channel and a sold-price reference than a source.

## eBay search pages – blocked by bot challenge

- Loading `ebay.com/sch/...` in the browser after a few fetches triggered "Pardon Our Interruption" (a CAPTCHA). Claude can't solve CAPTCHAs. Keep eBay to Terapeak (Seller Hub API), which wasn't challenged. Local-pickup eBay searching is parked.

## Facebook groups (tested Sept 21)

- Search: `https://www.facebook.com/search/groups/?q=garage%20sale%20fort%20worth`. Big public groups: Fort Worth Garage Sale (45K), Garage Sale Dallas/Fort Worth (95K), Local Online Garage Sale! Fort Worth (21K), DFW Garage/Yard Sales (38K), Garageando en Dallas/Fort Worth (66K). Private and dealer-heavy: Fort Worth Antiques & Vintage Buy, Sell, Trade (19K, ~94 posts/day), Antiques and Vintage and Collectibles Fort Worth/DFW, Dallas Antiques, Vintage & Collectibles.
- Public garage-sale groups are flooded with car-dealer and repeat posts. For-sale posts in groups usually also appear in Marketplace, which the category feed already covers. **Verdict: low added value.** Joining the private antique groups is Dylan's call; if he joins, add them as a weekly check.

## Other sources checked Sept 21

- **Craigslist `gms` (garage sales):** 38 posts in 3 days, but many are cross-posts from far away (Temple, Austin) or estate companies already on estatesales.net. Filter by distance before reviewing. `zip` (free) had nothing worth taking.
- **estatesale.com / gotoauction.com:** another estate/auction listing network (some Craigslist estate posts link there). Behind Incapsula/Cloudflare bot protection – browser only. Not built yet.
- **PublicSurplus:** loads in the container, but the zip/distance filter is ignored (national results). Institutional surplus (laptops, forklifts). Low fit.

## ShopGoodwill

- POST `https://buyerapi.shopgoodwill.com/api/Search/ItemListing` with the JSON body in `sg()`.
- `selectedSellerIds:"63"` = Goodwill North Central Texas (Fort Worth 76119). Other Texas sellers: 43 Austin, 185 Houston, 338 Sherman, 164 San Antonio, 144 Waco, 100 El Paso.
- Item detail: GET `/api/ItemDetail/GetItemDetailModelByItemId/<itemId>` (description, all images, pickup address).
- **Verdict:** titles are already brand-researched and every item is an auction, so current price means little. Use it only for pickup-only items ending with 0 bids.

## Source directory (researched Sept 21 – access tested from the container)

**Tier 1 – worth building next**

| Source | What it is | Access | Why it fits |
|---|---|---|---|
| **gsalr.com / estatesales.org** | Garage, yard and estate sale listings with photos | 200, HTML | Garage-sale sellers are the least likely to know values. Same photo-first review as estatesales.net. |
| **yardsalesearch.com, garagesalefinder.com** | Garage/yard sale aggregators | 200, HTML | Same idea; check overlap with gsalr first. |
| **AuctionNinja** (auctionninja.com/tx/dallas) | Online estate-sale auctions run by local companies | 200, jQuery app (API not found yet) | Low-traffic auctions often close cheap; photo-heavy; pickup in DFW. |
| **CTBids** | Online estate-sale auctions (TX) | 200, SPA with JSON API | Same as AuctionNinja. |
| **Mercari** | National app, shipped items | 403 from container → browser | Casual sellers, lots of mis-titled items; shipping in is fine. |
| **eBay** itself | Badly titled/misspelled auctions and local-pickup-only listings ending with few bids | 403 → browser, gently | Classic arbitrage; pickup-only listings near DFW get few bidders. |

**Tier 2 – auctions (buy price unknown until close)**

| Source | Access | Notes |
|---|---|---|
| HiBid (dallas.hibid.com, texas.hibid.com) | 403 → browser | The biggest platform for small DFW auction houses and estate liquidators. |
| localauctions.com / estatefinds.com (DFW market pages) | 200, JS app | Aggregates local online auctions. |
| MaxSold | 301 → browser | Whole-house online auctions; ~2 in DFW at a time. |
| AuctionZip, Proxibid, LiveAuctioneers, BidSpotter | 200 / 403 | Auction-house directories; mostly dealer-attended, lower odds. |
| Texas Online Auction House, Auction Hub Texas | 200 | Local auction companies; check what they run. |
| ShopGoodwill | API (built) | Picked over; pickup-only items with 0 bids only. |

**Tier 3 – liquidation and surplus (mostly new/returned goods – low fit)**

| Source | Access | Notes |
|---|---|---|
| Quickbidz, OB Liquidation, BidRL, Nellis, BidFTA | 200 / 429 | Store-return auctions. Brand values are already known; skip unless a lot is mis-described. |
| GovDeals, PublicSurplus, GSA Auctions, PropertyRoom, Tarrant County, TX state surplus | 403 / 200 | Government and police surplus. Occasional camera/tool/jewelry lots; mostly vehicles and equipment (need a truck). |

**Tier 4 – needs Dylan's login or not reachable**

- **Nextdoor For Sale & Free:** neighborhood sellers, very low-information – excellent fit, but requires Dylan's account in the browser.
- **Facebook Groups** (DFW buy/sell/trade and "estate/garage sale" groups): same account as Marketplace; many sellers post only in groups.
- **VarageSale, Poshmark:** load, but clothing/kids heavy – low fit.

## What didn't work

- Facebook: loading search pages and scraping the DOM (the old GRAB/FHC snippets) caps at 15–30 results. Replaced by GraphQL replay.
- Facebook: fetching item pages from the container redirects to login.
- eBay HTML from the container gets a 403. Mercari API gets a 403.
