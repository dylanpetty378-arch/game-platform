# Facebook flag verification (Oct 23 2026) — second stage after FB_EYE_BRIEF.md

You get a list of flagged Facebook Marketplace listings (local pickup near Keller TX). Each has the listing photo in
`panels/<id>.jpg`, the title, price, city/miles, the URL, and the screener's note.

Facebook rules (Dylan): sellers dump things cheap to be rid of them fast; price is a ceiling — offers well under
ask are normal ("best offer", "$1", "free"). Dylan's benchmark: a 14-volume antique book set bought for $50 (best
offer), worth ~$600, recognised from the photo.

For each flag:
1. View the photo. Decide what it really is (maker/model/era/set) — the photo outranks the title.
2. Check value with WebSearch: **sold** prices (eBay sold, auction results, completed sales) for that exact thing in
   similar condition. Never asking prices. 1–2 searches per item; stop as soon as it clearly fails.
3. Verdict:
   - `lead` if conservative resale (local FB, or eBay/Poshmark/Mercari net of fees + shipping) minus a realistic offer
     is ≥ $50 AND resale ≥ 3× that offer. Realistic offer = asking price, or ~50–60% of asking when it says OBO/best offer/negotiable/"need gone",
     or $0 if free.
   - Always `kill`: pianos/organs/TV-radio consoles (almost unsellable), and anything needing 3+ people or a dolly
     (dental chairs, safes, hot tubs) unless conservative value ≥ $500.
   - If WebSearch gives no sold prices, use WebFetch on a sold-results page or say "estimate" in the note.
   - `kill` otherwise (state why in a few words: replica, common, priced at value, condition, too big, etc.).
   Clothes, kids' gear, books and kitchen goods count as much as collectibles (Dylan, Oct 23); judge brand-name items
   by their used sold price for that brand/model.
4. For leads give: value_low (conservative sold value), max_offer (keeps profit ≥ max($50, offer) — local resale has
   no fees), and what Dylan should check or ask at pickup (marks, completeness, working, measurements).

Output one line per flag to your verdicts file, tab-separated:
`<run>\t<sheet>\t<cell>\tlead|kill\t<value_low>\t<max_offer>\t<what it is; evidence (sold comp + source); what to check>`
Reply with only: number of leads and kills.
