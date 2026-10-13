# Estate-sale golden-egg deep review

Rows are photos from DFW estate sales this week flagged as possible golden eggs (worth $1,000+, likely priced as
ordinary goods). Prices aren't online; Dylan would go in person. For each row:
1. Download the 1200px `photo` (`curl -s -o /tmp/res/esn/img/<pid>.jpg <url>`) and view it with Read. Crop/zoom with
   PIL into the flagged object if needed (save crops in /tmp/res/esn/img/). Look for signatures, marks, glazes, frames,
   period construction, edition numbers, printer's dots.
2. If the company's `caption` already names the valuable thing, it will be priced near value — usually kill.
3. Identify specifically and value with evidence: WebSearch for auction/sold records of that maker/artist/model
   (cite at least one URL for egg or lead). Use the low end.
4. Verdict: `egg` ($1,000+ realistic, specific ID, evidence), `lead` (worth a look: ≥$300 value and likely
   underpriced), `kill` (one specific line). Remember the size rule (passenger seat).
Write one JSON per row (append) to your output file:
`{"pid":"…","verdict":"egg|lead|kill","what":"…","evidence":"… URL","value_low":n,"sale":"…","city":"…","company":"…","sale_url":"…","note":"what to check on site"}`
Final reply: counts, then every egg/lead in full.
