# Hallmark eye brief: read the marks sellers didn't

Dylan (Oct 15 2026): find valuable things through the way cultures MARK them. Example that started this: eBay 128137081948, a
"gold tone" brooch. Its back shows an oval assay mark with numbers, a drilled assay dot and a rectangular Cyrillic maker
mark in rose-red metal, which points to Russian 56 or Soviet 583 (14k) gold.

Each image is ONE listing: every photo the seller posted, tiled, with the listing number top-left. Look at every tile,
especially backs, clasps, pin stems, ring shanks, bails, watch case insides, bases and undersides. Zoom into any tile that
shows a stamp (PIL crop/resize into your crop folder).

Reference (read the reading guide first, then use the rest as needed), all in /home/claude/gp/docs/encyclopedia/entries/:
precious-metal-marks-reading-guide.md · russian-and-soviet-hallmarks.md · british-and-irish-hallmarks.md ·
french-hallmarks.md · continental-european-hallmarks.md · scandinavian-hallmarks.md · watch-case-marks.md ·
american-precious-metal-marks.md · latin-american-and-caribbean-hallmarks.md · east-and-southeast-asian-gold-silver-marks.md ·
south-asian-and-middle-eastern-gold-silver-marks.md · platinum-and-palladium-marks.md · ceramic-and-glass-marks-that-multiply-value.md

## Flag when
- A solid precious-metal mark is visible or likely: karat numbers (10K, 14K, 18K, 9ct, 15ct, K18, 375, 585, 583, 750, 916,
  56, 72, 足金, ٧٥٠, ٢١), silver fineness on something sold as "metal" or "tone" (800, 830, 875, 925, 950, 84, Minerva,
  lion passant, crescent and crown), platinum (PLAT, PT, IRIDPLAT, dog's head), or an official assay set (state mark + maker
  + fineness, assay scrape or drill).
- A maker mark that multiplies value (Jensen, Spratling, Fahrner, David-Andersen, Liberty, Murrle Bennett, Loloma, etc.).
- A watch case whose inside shows 14K/18K/0.585/0.750, Helvetia, squirrel or a British gold date-letter set, while the
  title says "gold?", "gold tone" or nothing.
- A lot or grab bag where one piece in the photos shows any of the above.

## Do NOT flag
- Plated or filled: GF, RGP, 1/20, GE, HGE, GP, KGP, EP, EPNS, "18K GP", "Alpaca", "German silver", "silver plate", "Siam"
  without "sterling", or a bare "925" on a modern import chain (melt only, low value).
- Marks you can't read at all where nothing else suggests gold. Write it as "unreadable" only if color and construction
  strongly suggest gold (rose-red Russian or Soviet, deep yellow 22K Asian).
- Anything already titled with the mark and bid near value.

## Output, one line per flag, appended to your flags file
`<listing number>\t<mark read, e.g. "oval 56 kokoshnik + Cyrillic maker, rose metal">\t<what it means + est. weight g + rough $>`
Aim for precision: most listings have no marks. A real read beats a hopeful guess.
