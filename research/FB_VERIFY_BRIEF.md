# Facebook flag verification — v3 (Dylan's Q&A, Oct 24 2026; second stage after FB_EYE_BRIEF.md v3)

Dylan resells locally on Facebook and shipped on eBay. He is not an expert in most categories, so **a lead reaches him
only with proof**: real sold listings of the same item, a plain explanation, real-or-fake checks, and a resale plan.
Read FB_EYE_BRIEF.md first (never-flag list, Civic size limit, hidden-value types, money rule).

## Stage A — identify (agents, per flag)
1. View the photo. Decide exactly what it is: brand + model/line/pattern/title/era. The photo outranks the title.
2. Kill at once if it's on the never-flag list, won't fit a Civic's trunk/back seat, is a replica, is only a generic
   description ("vintage chair"), or obviously fails the money rule.
3. Otherwise write **1–2 eBay sold-search queries** that would find the same item (specific: brand + model words,
   not category words), and the real-or-fake checks for this item.
Output, tab-separated: `<run>\t<sheet>\t<cell>\tid|kill\t<identification or kill reason>\t<query1>||<query2>\t<checks>`

## Stage B — sold comps (main session, in Dylan's Chrome)
The main session runs every query against eBay **sold** results in Dylan's logged-in Chrome (one in-page script for
the whole batch) and saves title, price, sold date, photo and link for up to 10 sales per query to `comps.json`.
WebSearch is not used for comps (its budget runs out and eBay sold pages are blocked to WebFetch).

## Stage C — judge (agents, per identified flag, with comps.json)
1. Compare the listing photo to each sold comp's photo and title; keep only true matches (same item, similar
   condition). Need **≥ 2 true matches** unless the ask is under $20 (then a strong ID alone is enough; say "hunch").
2. value_low = a conservative figure from the matched sales (lower-middle, net ~15% eBay fees + shipping, or the local
   FB price if better). Realistic offer = ask, or ~50–60% of ask if OBO/"need gone", $0 if free.
3. `lead` if value_low − offer ≥ $50 and, for asks over $50, value_low ≥ 2× ask. Else `kill`.
4. For leads write: the 2–3 best matching comps (link + price + date), a two-sentence plain explainer (what it is, who
   buys it and why), real-or-fake checks for pickup, and a resale plan (platform, listing title, list price).
Output, tab-separated: `<run>\t<sheet>\t<cell>\tlead|kill\t<value_low>\t<max_offer>\t<json: comps[], explainer, checks[], plan>`
Reply with only: number of leads and kills.
