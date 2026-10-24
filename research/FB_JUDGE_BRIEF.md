# Facebook v3 Stage C — judge with real sold comps and write the lead (Oct 24 2026)

Read research/FB_EYE_BRIEF.md first (who Dylan is, never-flag list, Civic size, hidden-value types, money rule).
Dylan is **not an expert** in most categories: a lead must show him it's real. Your input is a list of flags; each has a
**panel image**: the Facebook listing photo top-left, and below it up to 8 real eBay **SOLD** listings (photo, price,
sold date, title) found by searching for Stage A's identification. View every panel.

For each flag:
1. **Match.** Which comps (by #) are truly the same item — same brand/model/pattern/edition, similar condition and
   completeness (a lot vs a single, boxed vs loose, size, new vs used)? Ignore non-matches. Also re-check the listing
   photo: is Stage A's identification actually supported by what is visible?
2. **Value.** value_low = a conservative resale from the true matches (lower-middle sold price; for eBay subtract ~15%
   fees and shipping, or use a local Facebook price if that's clearly better). Realistic offer = ask; ~60% of ask if it
   says OBO / "need gone" / "make offer"; $0 if free; for $0/$1 placeholder asks assume ~$20.
3. **Verdict.** `lead` only if: ≥ 2 true matches (or ask ≤ $20 with a strong, specific ID — mark it "hunch"); and
   value_low − offer ≥ $50; and for asks over $50, value_low ≥ 2× ask; and it's not on the never-flag list and fits a
   Civic. Otherwise `kill` with a short reason. Be strict: Dylan said the last report's values weren't believable.
4. For **leads**, write the card (plain English, no hype, no seller names).

Write ONE JSON array to your output file: one object per flag, in order:
```
{"n": <n from input>, "verdict": "lead"|"kill", "reason": "<kill reason or 'ok'>",
 "match": [<comp numbers that truly match>],
 "value": <value_low int>, "max_offer": <int, keeps profit ≥ $50 at value_low>,
 "name": "<plain name: brand + model>",
 "category": "Clothing & Shoes"|"Books & Media"|"Toys & Kids"|"Kitchen & Home"|"Jewelry & Silver"|"Tools"|"Antiques & Art"|"Collectibles"|"Other",
 "tier": "A" (≥3 tight matches, big margin) | "B" (2 matches or modest margin) | "C" (hunch / needs an answer first),
 "confidence": "high"|"medium"|"low", "size": "carry"|"car",
 "price_note": "<what the listed price likely means>",
 "what": "<explainer, 2 sentences: what it is, who buys it and why it's worth money>",
 "evidence": "<what the matched sold listings show, e.g. '3 sold Oct 2026 for $95–155 (#2,#3,#5)'>",
 "resale": "<where to sell>",
 "plan": {"platform": "eBay"|"Facebook local"|..., "title": "<ready-to-paste listing title>", "price": "<list price, e.g. $129 or best offer>"},
 "checks": ["3-5 real-or-fake and condition checks at pickup"],
 "message": "<short friendly first message to the seller with the key question>",
 "offer_plan": "Open at $X, walk away above $Y.",
 "risks": "<main way this loses money>"}
```
For kills only n, verdict, reason, match are needed. Reply only: leads N, kills N.
