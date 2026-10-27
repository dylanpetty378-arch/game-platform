# Facebook Marketplace distribution & furniture selling — research brief (Oct 27, 2026)

Context: Keller, TX (DFW) seller; two couches, a rug, several furniture pieces listed far under market; zero messages.

**Source-quality warning (read first).** Facebook's own Help Center pages are blocked to automated fetch (robots disallowed: https://www.facebook.com/help/marketplace), so official Meta facts below come from Meta Newsroom (about.fb.com). Most granular "algorithm" numbers come from reseller-tool vendors (Closo, Vendoo, both sell relisting software) and Reddit threads (read via the reddit.sentinel-team.org snapshot mirror). Meta publishes **no** decay curve, ranking formula, or restriction thresholds; any specific number below that isn't from Meta is practitioner folklore and is labeled as such.

---

## 0. The diagnostic that matters most for this case

- **Underpriced + zero messages is almost never a price problem.** Practitioner rule: views with no messages = price/presentation problem; near-zero views = visibility problem. "Hundreds of views" with no messages signals price; "12 views in six weeks" signals visibility. https://closo.co/blogs/platform-specific-guides/does-facebook-marketplace-boost-work
- Underpriced items normally draw a *flood* of messages — r/FacebookMarketplace commenters: "Many messages suggest the price is too low." https://reddit.sentinel-team.org/posts/1qqq3z6/snapshots/2026-01-31T00%3A10%3A09.859599Z
- So the first job is to read the listing's view/click count (section 6) and test visibility from another account (section 2).
- **"Too good to be true" pricing reads as a scam.** The BBB tells buyers an unusually low price is a "big red flag," and names furniture as one of the most-affected Marketplace scam categories. https://www.tmj4.com/news/i-team/fake-listings-and-scam-posts-take-over-facebook-marketplace-bbb-warns (2023). A deep discount on nice furniture with a thin profile can get views and no messages.
- **Buyers now see an AI trust summary of the seller.** Since March 2026 Meta shows an AI-generated overview at the top of a seller's Marketplace profile: Facebook tenure, friend count, listing history, item types sold, ratings. A new or sparse profile is visible to every buyer. https://about.fb.com/news/2026/03/facebook-marketplace-new-meta-ai-tools-make-selling-faster-and-easier/

## 1. How new listings get distribution and how fast it decays

- **No official decay data exists.** Meta has not published how visibility drops with listing age. Even Vendoo, which sells a relisting tool, says it can't quantify the decline. https://blog.vendoo.co/facebook-marketplace-delete-and-relist
- **Practitioner consensus: freshness is ranked heavily.** New listings get the strongest initial exposure. https://blog.vendoo.co/facebook-marketplace-delete-and-relist. One seller relists anything unsold after 72 hours "because Marketplace ranking favours recent listings" (her own observation). https://www.lilachbullock.com/facebook-marketplace-groups-sell-more/
- **Early-life heuristic (Reddit):** delete and relist any listing with fewer than 2 views after 12 hours. https://reddit.sentinel-team.org/posts/1pnswek/snapshots/2025-12-16T21%3A20%3A15.564998Z
- **Renew:**
  - Keeps the listing ID, views and saves, and gives a smaller bump than a new listing.
  - Becomes available about 7 days after posting; usable up to about 5 times.
  - Source: https://blog.vendoo.co/facebook-marketplace-delete-and-relist
  - A 9-month Apartment Therapy case: repeated Renew, photo swaps and price cuts never sold the couch. Deleting and reposting with the *same* photos and text sold it within about a month. https://www.apartmenttherapy.com/how-i-sold-my-couch-on-facebook-marketplace-37410429 (Jul 2024)
- **Delete & relist vs edit:**
  - Delete-and-relist makes a new listing ID and resets the listing's age, but loses its saves.
  - **Delete the old listing first.** Two live copies can be flagged as duplicates, which can reduce visibility.
  - Don't relist the same item every 24 hours. Vendoo suggests a self-imposed cap of about 10 deletes/relists per hour, which it says is not an official limit.
  - Source: https://blog.vendoo.co/facebook-marketplace-delete-and-relist
  - Reddit: delete-and-repost usually fixes single dead listings, but not when every listing is affected (that points to the account). https://reddit.sentinel-team.org/posts/1pt3n9k/snapshots/2025-12-24T08%3A00%3A09.367277Z
- **Price edits:**
  - A price drop may notify shoppers who saved the item.
  - Vendoo rates a drop of 5% or more as a medium boost that keeps the listing's data.
  - If a listing has many saves, cut the price before deleting it.
  - Source: https://blog.vendoo.co/facebook-marketplace-delete-and-relist
  - None of this helps a listing that nobody has seen or saved.
- **Boost (paid):**
  - **Cost:** typical boosts run $5–$30 over 3–7 days, starting around $5. https://closo.co/blogs/platform-specific-guides/does-facebook-marketplace-boost-work
  - **What it does:** boosting "buys reach, not intent." It shows the item to people scrolling, not searching. https://closo.co/blogs/platform-specific-guides/fb-marketplace-boost-listing
  - **Which items:** worth it on local, bulky items over about $150, such as a $400 sectional. Fix the listing and test a roughly 10% price cut first. https://closo.co/blogs/platform-specific-guides/does-facebook-marketplace-boost-work
  - **Reddit:** sellers are skeptical and none reported measured results for a sectional. Boosting raises views but doesn't guarantee local buyers, and there is "ZERO way" to tie a boost to a sale. https://reddit.sentinel-team.org/posts/1rlttmf/snapshots/2026-03-06T02%3A42%3A44.829333Z
  - **Billing warning (Oct 2026):** Meta's new "Cost per Sale" boost applies to shipped listings only and is pitched as 15–30% of the sale price. In a Value Added Resource test, it created continuous campaigns with $400–$600/day budgets that billed on impressions. The local fixed-budget boost is separate. https://www.valueaddedresource.net/facebook-marketplace-cost-per-sale-ads/ ; https://www.selfemployed.com/news/facebook-marketplace-cost-per-sale-ads-billing-sellers-2026/
  - **Rule if you boost:** use only the fixed-budget local boost, and check the daily budget and duration on the confirmation screen.
- **More competition in the feed (2025–2026):**
  - Shipped eBay listings appear in the US Marketplace feed. https://www.ebay.com/sellercenter/news/2025-april/facebook-marketplace
  - Poshmark items and delivery products are now mixed in beside local items. https://www.analyticsinsight.net/technology/what-happened-to-facebook-marketplace-what-changed-and-how-it-works-now
  - One seller's anecdote: sponsored ads take about one in every three rows. https://reddit.sentinel-team.org/posts/1pnswek/snapshots/2025-12-16T21%3A20%3A15.564998Z
  - Volume: more than 3.5M listings posted daily in the US and Canada. https://about.fb.com/news/2026/03/facebook-marketplace-new-meta-ai-tools-make-selling-faster-and-easier/

## 2. Account-level reach limits ("shadow" limits)

- **Meta's model is ranking and trust scores, not a formal shadowban.** Low trust, policy flags, competing paid promotions and weak early engagement cut distribution (r/FacebookMarketplace). https://reddit.sentinel-team.org/posts/1pt3n9k/snapshots/2025-12-24T08%3A00%3A09.367277Z
- **Signs:**
  - Views drop sharply across *all* listings at once. https://www.imarkinfotech.com/lost-your-facebook-marketplace-heres-how-to-get-it-back-use-it-safely-and-start-earning-in-2026/
  - A listing shows zero views for weeks while the same item from another account gets clicks. https://reddit.sentinel-team.org/posts/1pt3n9k/snapshots/2025-12-24T08%3A00%3A09.367277Z
  - Messages fail to arrive.
- **Triggers reported:**
  - Bulk or rapid posting, frequent edits, identical listings, automation tools, stock photos, duplicates. https://www.imarkinfotech.com/lost-your-facebook-marketplace-heres-how-to-get-it-back-use-it-safely-and-start-earning-in-2026/
  - New accounts: messaging may be limited for roughly the first 30 days.
  - Posting 10 items in one hour triggered a bot flag (one author's experience).
  - About 50 copy-pasted replies can trigger a reply restriction.
  - A phone number in the description can trigger spam flags.
  - Source for the last four: https://closo.co/blogs/legal-compliance/the-silence-of-the-scams-why-your-facebook-marketplace-inbox-is-empty
- **How to check:**
  1. Settings → **Account Status**, then **Support Inbox** (Help & Support) for any Marketplace notice. https://www.imarkinfotech.com/lost-your-facebook-marketplace-heres-how-to-get-it-back-use-it-safely-and-start-earning-in-2026/
  2. From a friend's account or a logged-out device near Keller, search the exact title. If it doesn't appear, distribution is the problem. https://reddit.sentinel-team.org/posts/1pt3n9k/snapshots/2025-12-24T08%3A00%3A09.367277Z
  3. Confirm buyers can message you: Settings & Privacy → Privacy → How people find and contact you → Message Requests set to Everyone (an app update may have changed this). Also check whether the listing is marked Pending. https://closo.co/blogs/legal-compliance/the-silence-of-the-scams-why-your-facebook-marketplace-inbox-is-empty
- **Recovery:**
  - Remove or fix any flagged listing, then allow 24–72 hours.
  - Appeal through "Request Review" in the Support Inbox. Reviews take 1–5 business days; don't file repeated appeals.
  - Reported suspensions: about 24 hours to 7 days for minor issues, about 30 days for repeat issues.
  - Source: https://www.imarkinfotech.com/lost-your-facebook-marketplace-heres-how-to-get-it-back-use-it-safely-and-start-earning-in-2026/
  - Reddit: listings returned to normal after about 2 weeks. Another suggestion is to delete all listings, wait 1–2 weeks, then repost slowly. https://reddit.sentinel-team.org/posts/1pt3n9k/snapshots/2025-12-24T08%3A00%3A09.367277Z
  - Closo's in-app reset: Commerce Profile → Settings → turn Vacation Mode on and off, update the Facebook and Messenger apps, and stop using the Lite apps. https://closo.co/blogs/legal-compliance/the-silence-of-the-scams-why-your-facebook-marketplace-inbox-is-empty

## 3. Listing mechanics

- **Photos:**
  - Up to 10 per listing; use 5–10 from different angles.
  - The first photo is the search thumbnail, so make it the cleanest, brightest full shot.
  - Source: https://editthispic.com/guides/facebook-marketplace-photo-guide
  - For couches: shoot in natural light against a clean wall, with close-ups of the fabric, legs and any flaws. https://blog.vendoo.co/how-to-flip-couches-for-cash
- **Title keywords:**
  - Furniture buyers search by brand, material and style: e.g. West Elm, Pottery Barn, Broyhill, Drexel, "mid-century", walnut, teak, velvet, leather, "solid wood". https://stylebyemilyhenderson.com/find-good-furniture-on-facebook-marketplace-for-cheap-the-search-terms-to-use
  - Kaiyo's most-searched brands: Restoration Hardware, West Elm, CB2, Design Within Reach. https://prnewswire.com/news-releases/online-furniture-marketplace-kaiyo-reveals-third-annual-furniture-trend-report-301930789.html
  - Put brand + type + material/color + size in the title (e.g. "West Elm Harmony 3-Seat Sofa – Gray Performance Velvet").
- **Description:** list dimensions, fabric, condition, and pickup details; be honest about flaws. https://blog.vendoo.co/how-to-flip-couches-for-cash
- **Delivery:** offering delivery, even for a fee, helps couches sell, because many buyers can't haul them. https://blog.vendoo.co/how-to-flip-couches-for-cash
- **Pickup vs shipping:** local pickup has no fee. Facebook charges 5% (minimum $0.40) on shipped sales; OfferUp charges 12.9%. https://blog.vendoo.co/facebook-marketplace-vs-offerup. Furniture is a local-pickup category.
- **Groups ("List in more places"):**
  - Posting to local buy/sell groups at the same time widens reach. Use the listing's three-dot menu → "List in more places." https://www.alphr.com/facebook-marketplace-list-in-more-places/
  - One seller's case: 3 enquiries in 10 days on Marketplace alone, then 14 items sold in 9 days after posting to 11 groups.
  - Recommended: 8–12 local and category groups, with the opening line varied for each. Identical text posted fast gets flagged as spam, and some groups cap posts per day.
  - Source for the last two points: https://www.lilachbullock.com/facebook-marketplace-groups-sell-more/
- **Timing:**
  - Post Thursday at 7–8 am or 5–6 pm for weekend-project buyers, or Sunday (visible through Monday). This is sellers' opinion, not data. https://www.aol.com/articles/best-day-list-item-sale-110000173.html (Country Living, Oct 2025)
  - Local groups peaked Sunday afternoon and evening (one author's observation). https://www.lilachbullock.com/facebook-marketplace-groups-sell-more/
- **Category and location:** no reliable 2024–2026 source quantified either. The working assumption is: correct Furniture subcategory, and location set to the actual pickup area (Keller) so radius filters include you.
- **AI auto-reply:** Meta AI can now answer "Is this available?" for you (enabled at listing creation). Turning it on cuts the lag on first replies. https://about.fb.com/news/2026/03/facebook-marketplace-new-meta-ai-tools-make-selling-faster-and-easier/

## 4. Furniture data

- **No public sell-through data for furniture on Marketplace was found.** Meta doesn't publish any, and "statistics" sites recycle unsourced figures.
- **Couch time to sell:** some couches sell in 24–48 hours, others take 1–2 weeks, depending on price and demand. https://blog.vendoo.co/how-to-flip-couches-for-cash
- **General reseller benchmark (non-furniture):** an average of 3.6 days and a median of 2 days to sell; 75% sold within 5 days. https://reddit.sentinel-team.org/posts/1q1hp3w/snapshots/2026-01-02T23%3A21%3A09.49167Z
- **Couch stigma:** odors (pets, smoke, mildew), rips, sagging cushions and dated florals kill sales. https://blog.vendoo.co/how-to-flip-couches-for-cash. State "smoke-free / pet-free" if true.
- **A couch can stall for months even when priced fine.** The Apartment Therapy sectional sat about 9 months until a fresh listing. https://www.apartmenttherapy.com/how-i-sold-my-couch-on-facebook-marketplace-37410429
- **Brand matters for resale value (Kaiyo):** West Elm, CB2, Article, Tov and Urban Outfitters hold value best. A West Elm Eddy sectional resold at about 90% of retail. https://www.domino.com/style-shopping/kaiyo-furniture-report-best-brands-to-sell/ (2023)
- **Seasonality and the economy:** sellers report slower sales since November and buyers pressing harder on price. https://reddit.sentinel-team.org/posts/1pnswek/snapshots/2025-12-16T21%3A20%3A15.564998Z
- **Free vs priced:** no hard data found. Anecdotes say free items get swarmed, while some free items get no views at all. https://reddit.sentinel-team.org/posts/1pnswek/snapshots/2025-12-16T21%3A20%3A15.564998Z

## 5. OfferUp and Nextdoor (DFW)

- **OfferUp:**
  - About 20M+ monthly users and more local-focused than Facebook. https://blog.vendoo.co/facebook-marketplace-vs-offerup
  - Fees: 0% on local sales, 12.9% (minimum $1.99) on shipped sales. https://closo.co/blogs/platform-specific-guides/selling-on-offerup
  - Paid promotion: Promote 1-day and 3-day options that can be stacked, and Promote Plus, a subscription for 30+ days. Prices are shown only in the app; promotions can't be cancelled, and refunds are case-by-case. https://help.offerup.com/hc/en-us/articles/360031994412
  - It suits bulky furniture, and a big metro like Dallas has a deeper buyer pool. https://closo.co/blogs/platform-specific-guides/selling-on-offerup
- **Nextdoor For Sale & Free:**
  - Free to list, with up to 10 photos and an AI listing assistant (Aug 2024). Reaches your verified neighborhood and nearby ones. https://about.nextdoor.com/press-releases/nextdoors-genai-assistant-expands-to-for-sale-free-listings
  - The July 2025 app relaunch for about 100M users centered on news, alerts and AI recommendations, not selling. https://www.axios.com/2025/07/15/nextdoor-app-ai-reboot
  - No fee or reach data for DFW was found. Treat it as a free, trust-rich supplementary channel: verified neighbors and short drives.

## 6. Reading the seller stats (views / clicks / saves / messages)

- **What Meta shows:** the July 2026 Seller app shows views, clicks, message threads and sold listings. https://about.fb.com/news/2026/07/introducing-seller-app/. Metricool notes it does not mention saves. https://metricool.com/seller-facebook-marketplace-app/
- **What counts as "low":**
  - Fewer than 2 views 12 hours after posting means a dead listing; relist it. https://reddit.sentinel-team.org/posts/1pnswek/snapshots/2025-12-16T21%3A20%3A15.564998Z
  - About 12 views over weeks means a visibility problem. https://closo.co/blogs/platform-specific-guides/does-facebook-marketplace-boost-work
- **Clicks to messages:** a rental listing got 483 clicks and 3 chats, about 0.6%. https://www.biggerpockets.com/forums/898/topics/1215230-whats-a-good-rental-listing-view-to-application-ratio-on-fb-marketplace (2024; different category, but it calibrates expectations). So a few dozen clicks with no message isn't alarming. Hundreds of clicks with no message points at price, trust or photos.
- **Decision rule:**

| Views/clicks | Saves | Messages | Diagnosis | Action |
|---|---|---|---|---|
| ~0 after 12–24 h | 0 | 0 | Not distributed | Check Account Status and the second-account search; delete and relist with a new first photo; post to groups |
| Dozens–hundreds | some | 0 | Seen but not trusted or wanted | Real photos (not stock), honest flaws, full profile; price near comps, not suspiciously low |
| Many saves | many | 0 | Interest, no trigger | 5–10% price drop (notifies savers) |
