# Branding Research for an Original TTRPG-as-Web-Platform

**Prepared:** August 2026
**Subject:** Original tabletop RPG system, played through a purpose-built web application. Base ruleset plus purchasable Components, Adventures and Asset instances, with user-authored Settings free. Asynchronous play across a week is a core feature. No AI-generated prose or art in the product. Solo developer, Fort Worth TX, nights and weekends, full-time job, no audience, no company.

---

## How to read this

This document is organised by **decision**, not by topic, because the topics interleave. The name constrains the trademark strategy, the trademark strategy constrains the product architecture, the product architecture constrains the positioning, and the positioning constrains which channels are worth your nights.

Every factual claim that came from a source carries an inline URL. Where I am reasoning rather than reporting, I say so. Where the public data is thin or the source is weak, there is a **[THIN]** flag — those claims should not be load-bearing.

A note on evidence quality generally: the tabletop RPG industry publishes almost no reliable market data. There is no NPD/Circana equivalent that covers hobby RPGs cleanly, publishers do not report unit sales, and the "TTRPG market size" reports that dominate search results are template-generated SEO content with fabricated CAGRs. I have deliberately avoided those and preferred: primary legal sources (USPTO, TTAB, licence texts), publisher-reported crowdfunding figures, first-party platform data (Foundry install stats, Gen Con event catalogues), and named practitioners writing about their own numbers. Where I use a secondary aggregator I flag it.

---

# Part 1 — The Name

## 1.1 The structural fact that should drive your naming strategy

Start here, because it is counter-intuitive and it is the single most actionable legal finding in this document.

**The title of a single creative work cannot be registered as a trademark in the United States.** This is settled law, codified in TMEP §1202.08. A book title, standing alone, does not function as a source identifier — it identifies the work, not who made it.

The tabletop-specific precedent is directly on point and is *about a TTRPG book*. In 2022 the Trademark Trial and Appeal Board issued a **precedential** decision affirming refusal of **STRONGHOLDS & FOLLOWERS**, filed by **MCDM Productions, LLC** for "role playing game equipment in the nature of game book manuals." The Board held the mark was the title of a single creative work; that selling it in both print and PDF did not make it a series; and — the critical line — that "the publication of a single book cannot create, as a matter of law, an association between a book's title (the alleged mark) and the source of the book." ([TTABlog, March 2022](https://thettablog.blogspot.com/2022/03/precedential-no-6-title-of-single-work.html))

Now the good news, and it is very good news for your specific project.

TMEP §1202.08(b) lists what is **not** treated as a single creative work. The list explicitly includes: works in a series ("volume 1," "book 1"); works with subsequent editions where content changes significantly; periodically issued publications whose content varies each release; and — verbatim — **"computer software, computer games, coloring books, and activity books are not treated as single creative works."** ([BitLaw, TMEP 1202.08(b)](https://www.bitlaw.com/source/tmep/1202_08_b.html))

**Consequence for you:** the thing you are building is, in trademark terms, on the *right* side of this line in three separate ways simultaneously.

1. It is **computer software** (the web app). Software names are registrable.
2. It is an **ongoing service** (asynchronous campaign hosting). Services are registrable.
3. It is an **explicit series** — a base ruleset plus a continuing line of purchasable Components, Adventures and Asset instances, with user-authored Settings free, published under one house mark. That is exactly the "evidence of a series" fact pattern that rescues a title from the §1202.08 refusal.

MCDM got refused because they filed the title of one book, as one book. You are structurally not in that position — provided you file the right way. This is a real, concrete advantage of the platform architecture that you should not squander by filing the *rulebook title* alone in Class 016.

## 1.2 What kind of name is actually registrable

US trademark strength runs on a five-step spectrum, and only the top three categories get onto the Principal Register without first proving acquired distinctiveness:

| Category | Definition | Examples | Registrable immediately? |
|---|---|---|---|
| **Fanciful** | Invented words with no prior meaning | EXXON, KODAK, XEROX | Yes — strongest |
| **Arbitrary** | Real words unrelated to the goods | APPLE for computers, LOTUS for software | Yes |
| **Suggestive** | Hints at a quality; requires imagination | MICROSOFT, NETSCAPE | Yes |
| **Descriptive** | Directly describes the product | — | Only with secondary meaning |
| **Generic** | Names the product category itself | — | Never |

([BitLaw, Strength of Trademarks](https://www.bitlaw.com/trademark/degrees.html))

This maps almost perfectly onto the aesthetic advice from the tabletop design world. Clayton Notestine (Explorers Design, the most-cited working graphic designer in indie TTRPG) argues that the failure modes for RPG titles are: **meme names** (undermine a serious game), **knock-off names** (live permanently in the shadow of their referent), and **boilerplate formulas** — "The ___ of ___" — which he says are so interchangeable that "if an AI could generate your title, reconsider it." His positive criteria are sharpness and phonetic pleasure (*Necronautilus*, *FIST*, *Mothership*, *Troika!*, *Honey Heist*), scene-setting (*The Quiet Year*, *Deathmatch Island*), and a distinct voice that connects to actual content. His overarching rule: "Bad titles are arbitrary or irrelevant." ([Explorers Design — Killing Good Games with Bad Titles](https://explorersdesign.substack.com/p/killing-good-games-with-bad-titles))

Note the tension worth naming explicitly: **Notestine's "arbitrary" is the trademark lawyer's "arbitrary," and they mean opposite things.** He means *disconnected from the game* (bad). The lawyer means *a real word with no descriptive relationship to the goods* (strong). The overlap you want is a name that is legally arbitrary-or-fanciful but emotionally *evocative of the fiction or the feeling* — APPLE is arbitrary for computers, but it is not random; it was chosen for warmth and approachability. That is the target zone.

**Patterns that recur in successful tabletop names**, observed across the corpus:

- **Compound of two concrete nouns/adjectives, one of which is unexpected**: *Mörk Borg* ("dark fort", Swedish, deliberately non-English so it reads as a proper noun to anglophones), *Shadowdark*, *Blades in the Dark*, *Mothership*, *Dolmenwood*.
- **Single invented or quasi-invented word**: *Chaosium*, *Numenera*, *Troika!*, *Vaesen*. These are the strongest trademarks and the hardest to seed — you must teach the market the word, but once taught, you own it outright.
- **Arbitrary real word used as a proper noun**: *Pathfinder*, *Delta Green*, *Ironsworn*, *Spire*. Legally strong in the relevant classes, cheap to teach, but crowded — search results fight you forever.
- **Company names that are arbitrary-whimsical and deliberately non-descriptive**: Wizards of the Coast, Evil Hat Productions, Free League / Fria Ligan, Necrotic Gnome, Rowan Rook & Decard, Tuesday Knight Games, Magpie Games, Stonemaier Games. Note that essentially none of these describe the goods. That is not an accident; a descriptive publisher name ("Tabletop RPG Publishing LLC") is unregistrable *and* unmemorable.

**A pattern to avoid: reviving a dead name.** More on this in the anti-patterns section, but as a naming principle: dead trademarks in this hobby are dead for reasons, and their ghosts are litigious. See §7.2.

## 1.3 Which classes, what it costs, how long it takes

**Classes.** For a product that is simultaneously a book, a piece of software, a service, and a set of downloadable goods, the relevant International Classes are:

- **IC 009** — downloadable software; downloadable electronic publications. This is where a downloadable rulebook PDF and any downloadable client live.
- **IC 028** — games and playthings; role-playing game equipment; dice; card games. This is the traditional tabletop class.
- **IC 041** — entertainment services; providing online non-downloadable games; providing online publications. Historically the class for "providing an online game."
- **IC 042** — SaaS; providing temporary use of non-downloadable software. Increasingly the correct class for a hosted web application, and often filed alongside 041.
- **IC 016** — printed matter (physical books), if and only if you print.

For a hosted, subscription/purchase-based web platform, **009 + 041 is the classic pair and 042 is the modern addition**; 028 matters the moment you sell any physical component or want to block someone selling a boxed game under your name. Trademark practitioners consistently recommend 009 and 041 as the core pair for games with a digital delivery model ([Revision Legal — What Trademark Class Is a Video Game?](https://revisionlegal.com/trademark/what-trademark-class-is-a-video-game/); [Gerben IP — Trademark Classes for Software Applications](https://www.gerbenlaw.com/blog/trademark-search-for-an-app-or-name-of-a-software-program/)). **[THIN]** — these are law-firm marketing pages, not primary authority. The class choice should be confirmed by whoever files, against the actual USPTO ID Manual entries you use.

**Cost (USPTO, current fee schedule).** The January 2025 restructure eliminated the old TEAS Plus / TEAS Standard split and replaced it with one base fee plus behavioural surcharges:

| Item | Fee |
|---|---|
| Base application, **per class** | **$350** |
| Surcharge: insufficient information | +$100 |
| Surcharge: free-form (custom) goods/services text, per class | +$100 |
| Surcharge: lengthy identification, per additional 1,000 characters | +$200 |
| Statement of Use (intent-to-use path), per class | $200 |
| Extension of time to file SOU, per class, per 6 months (max 5) | $150 |
| §8 Declaration of Use (years 5–6), per class | $200 |
| Combined §8 & §9 renewal, per class | $350 |

([USPTO Fee Schedule](https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule))

The $100 free-form surcharge is the one that catches self-filers. **If you write your own goods description instead of picking pre-approved entries from the USPTO ID Manual, you pay an extra $100 per class.** For a project like yours where the goods are genuinely novel ("downloadable software for asynchronous tabletop role-playing game campaign management" is not a stock entry), you will likely eat this. Budget for it.

**Realistic all-in cost.** Two classes, self-filed, with free-form text: 2 × ($350 + $100) = **$900** in government fees. With an attorney: flat fees for a single-class filing run **$400–$800** in the regional-firm market, comprehensive clearance searches **$200–$500** standalone, and office action responses **$500–$1,500** depending on complexity. One firm quotes a total realistic budget of **$750–$1,150** for a small business filing one class with clearance included, and notes the probability of receiving an office action at over 40%. ([Michael Meyer Law — Trademark Attorney Fees 2026](https://www.michaelmeyerlaw.com/blog/trademark-attorney-fees/)) **[THIN — law-firm self-published pricing; treat as order-of-magnitude.]**

**Timeline.** This has improved dramatically and is now a genuine argument for filing early rather than waiting. First-action pendency was **4.5 months as of Q1 2026**, down from 8.5 months in early 2023. Total pending applications stood at **953,003 as of 14 April 2026**, with an unexamined backlog of **346,378 classes** at end of FY2025. Back-end services have gotten *worse*: Statement of Use review has stretched from 53 to 118 days, renewals from 86 to 129 days. ([TrademarKraft — USPTO Processing Times, April 2026](https://trademarkraft.com/blogs/news/uspto-processing-times-and-backlog-at-a-glance-april-2026)) **[THIN — a domain-industry blog aggregating USPTO dashboard data. The USPTO's own dashboard at https://www.uspto.gov/dashboard/trademarks/ is the authority but did not render cleanly for extraction; verify the current figures there before relying on them.]**

Practical reading: **filing to registration realistically runs 9–18 months** on the use-based path, longer on intent-to-use because you must then file a Statement of Use and wait ~4 months for it to be reviewed.

**The intent-to-use path is the right one for you.** You have no product in commerce yet. A §1(b) intent-to-use application lets you claim priority from the filing date, and you have up to 3 years (six 6-month extensions at $150/class each) to actually launch. That is exactly the shape of a nights-and-weekends project. Note TMEP §1202.08(f): a single-work refusal can be *deferred* in an intent-to-use application until you file specimens — meaning the single-work trap is something you can still walk into at SOU time if your specimen is just a book cover. ([BitLaw, TMEP 1202.08(f)](https://www.bitlaw.com/source/tmep/1202_08_f.html))

**Entity formation, since it interacts with naming.** Texas: certificate of formation **$300** (waived for veterans), state-level assumed name certificate **$25**, annual franchise tax report due 15 May with a **no-tax-due threshold of $2.47 million** in annual revenue. ([ZenBusiness — Texas Filing Fees](https://www.zenbusiness.com/texas-filing-fees/)) **[THIN — formation-service marketing page; confirm against the Texas SOS fee schedule.]** The relevant branding point: an LLC name registration in Texas gives you *nothing* nationally. It stops another Texas entity registering an identical entity name and that is all. Do not mistake it for trademark rights.

## 1.4 Clearance: what to actually search, and in what order

The order matters because each step is cheaper than the next and can kill the name before you spend on the one after.

1. **USPTO search** (free, `tmsearch.uspto.gov`) — live and dead marks in 009, 028, 041, 042, 016. Dead marks matter: they tell you someone tried, and sometimes tell you why they stopped.
2. **Common-law search** — itch.io, DriveThruRPG, BoardGameGeek, RPGGeek, Steam, Kickstarter, Google. In tabletop, *unregistered* prior use is the dominant risk because almost nobody registers. A game with 400 itch downloads and no trademark can still generate a Lanham Act §43(a) claim and, more practically, can generate a search-results collision that costs you more than a lawsuit would.
3. **Domain and handle sweep** — see below.
4. **International** — EUIPO and UKIPO if you intend to sell in Europe, which a web platform does by default the moment someone in Berlin signs up.

## 1.5 Domains and handles

The blunt strategic reality in 2026 is that **the exact-match .com is usually gone and usually not worth what it costs**, and the handle namespace is more constrained than the domain namespace. Practical strategy, in rough priority order:

- **Prefer a name where you can get a coherent set** rather than a "perfect" name where you cannot. Consistency of `@name` across Bluesky, Discord vanity, itch, GitHub, YouTube and a domain is worth more than the specific TLD.
- **Two-word and compound-word .coms are the realistic target zone.** Invented single words (the strongest trademarks) are also the most likely to have a free .com — this is a rare case where the legal optimum and the availability optimum coincide.
- **Be cautious with `.io`.** The UK's transfer of the Chagos Archipelago to Mauritius put the `.io` ccTLD's long-term status into genuine question, because ccTLDs are delegated to territories and IANA policy allows for retirement of a ccTLD within roughly five years of the underlying country code being withdrawn. Industry consensus is that immediate shutdown is unlikely and ICANN prioritises DNS stability, and precedent (.su, .yu) shows retirements are drawn-out — but the risk is real and non-zero, and it is a bad risk to take on the *canonical* domain for a platform you intend to run for a decade. ([CircleID — Future of .io Domain Uncertain](https://circleid.com/posts/future-of-dot-io-domain-uncertain-as-uk-relinquishes-chagos-islands); [The Register, Oct 2024](https://www.theregister.com/2024/10/10/io_domain_uk_mauritius/)) A 2026 hosting-industry piece frames the general principle well — with any ccTLD "you rent a country's politics." ([webhosting.today, July 2026](https://webhosting.today/2026/07/02/you-dont-own-your-io-or-ai-you-rent-a-countrys-politics/)) **[THIN — opinion piece, but the underlying delegation mechanics are accurate.]**
- **`.games`, `.gg`, `.app`, `.co` are all live options** for a game platform and read as intentional rather than second-best in 2026, in a way they did not in 2015. `.app` has the side benefit of being HSTS-preloaded (HTTPS enforced at the TLD level).
- **Defensive registrations are mostly a waste of money for you.** Register the .com and one alternate. Do not buy fifteen TLDs; nobody is typosquatting a product with zero users.

## 1.6 Names that had to change, and what it cost

These are the cautionary cases worth internalising. Note that in **every** one, the party that changed was the smaller one, and in none of them did the merits decide it.

**Prey for the Gods → Praey for the Gods (May 2017).** ZeniMax Media, owner of the *Prey* trademark in video games, objected to indie developer No Matter Studios' Kickstarter-funded game. The studio abandoned its trademark filing and changed the name rather than fight — the rename landing in the same month ZeniMax shipped its own *Prey*. The game shipped and was fine; the brand carried a permanent, slightly silly spelling scar. ([Wikipedia — Praey for the Gods](https://en.wikipedia.org/wiki/Praey_for_the_Gods); [MCV/Develop](https://mcvuk.com/business-news/publishing/no-prey-for-no-matter-studios-after-zenimax-trademark-claim/))

**Bethesda v. Mojang, "Scrolls" (2011–2012).** Bethesda claimed Mojang's card game *Scrolls* would confuse consumers with *The Elder Scrolls*. Mojang won an interim injunction, then settled in March 2012: Mojang would not register *Scrolls* as a trademark, and Bethesda would not contest the name provided the game did not compete with theirs. The game was later released as *Caller's Bane* (2018) — a full rename after development had ceased. Both companies are now Microsoft subsidiaries, which is its own commentary on how much this mattered. ([Wikipedia — Caller's Bane](https://en.wikipedia.org/wiki/Caller%27s_Bane); [Forbes, March 2012](https://www.forbes.com/sites/alexknapp/2012/03/16/bethesda-and-mojang-settle-scrolls-lawsuit/))

**Games Workshop v. M.C.A. Hogarth, "Spots the Space Marine" (2013).** GW asserted trademark rights in "space marine" and Amazon removed Hogarth's novel. The term had appeared in science fiction since the 1930s and GW's registration covered *games*, not books. Amazon restored the book only after EFF intervened and the story went viral. The structural lesson is the one that should worry you: **a takedown at a platform intermediary does not require the claim to be valid.** The burden lands entirely on the accused. ([EFF, February 2013](https://www.eff.org/deeplinks/2013/02/trademark-bully-thwarted-spots-space-marine-back-online))

**B/X Essentials → Old-School Essentials.** Widely reported in OSR circles as a rename driven by trademark caution around "B/X" as a designation associated with TSR/Wizards D&D editions. **[THIN — I could not verify the publisher's stated reason from a primary source; the Wikipedia entry does not explain the rename, and Gavin Norman's original blog post was not retrievable. Do not cite this as established fact.]**

**The general principle these cases teach:** you will not be sued for infringement by a giant. You will be *emailed*, or your storefront listing will simply vanish. The cost of a name collision is not litigation; it is a Tuesday where DriveThruRPG or Apple delists you and you have no leverage.

---

# Part 2 — Identity and Visual Language Without an Art Budget

## 2.1 What modern RPG identity looks like, versus legacy

The legacy model — TSR, White Wolf, 1990s–2000s Wizards — was **illustration-led**: a painted cover establishing genre, interior spot art establishing tone, and typography as a neutral container. That model requires an art director and five figures of commissioned work per book. It is not available to you and, importantly, it is no longer the prestige position.

The modern indie model is **design-led**: typography, colour, paper stock, grid, and information architecture carry the identity, and illustration is deployed sparsely and pointedly. Two proofs:

**Mörk Borg (2020).** Designed by Pelle Nilsson with all art and layout by **one person**, Johan Nohr. The book is deliberately hard to navigate — "chaotic font choices and gnarly splatter art," foil, varied paper stocks — described by its makers as "beautifully ugly." It swept the 2020 ENnies with **Gold for Product of the Year, Best Writing, and Best Layout and Design**, plus Silver for Best Game, and further golds in 2021 and 2022. ([Wikipedia — Mörk Borg](https://en.wikipedia.org/wiki/M%C3%B6rk_Borg)) This is the canonical demonstration that *graphic design alone* can be the entire brand.

**Mothership (2018–2021).** Sean McCoy's visual identity — watercolour and Sharpie — came out of constraint, not preference. His formulation is the single most useful sentence in this whole section: **"Style is all about accentuating your strengths and distracting from your weaknesses."** The first release was a 41-page *Player's Survival Guide*; McCoy brought 50 copies to Origins 2018. Three years later the 1e boxed set Kickstarter raised **$1,676,936 from 17,719 backers**. ([The Companion — Inside the Million Dollar Sci-Fi Horror RPG](https://www.thecompanion.app/mothership-inside-the-million-dollar-sci-fi-horror-rpg/))

**Shadowdark (2023).** Kelsey Dionne, solo. Reviewers specifically praised *production* rather than art: "thick, durable paper; library-sewn binding; clear, readable font selections." It won four Gold ENNIEs in 2024 including **Best Layout and Design** and Product of the Year, off a Kickstarter of roughly **$1.3–1.4 million**. ([Wikipedia — Shadowdark](https://en.wikipedia.org/wiki/Shadowdark); [Forbes, March 2025](https://www.forbes.com/sites/robwieland/2025/03/19/shadowdarks-second-million-dollar-kickstarer-creates-a-full-setting/))

Note what all three have in common: **the identity is executable by one person**, it is *legible at thumbnail size*, and it is instantly parodiable — which is to say, instantly recognisable.

## 2.2 What art actually costs, so you can decide what not to buy

Ballpark commissioning rates, from a working small publisher (Chris Bissette, Loot the Room): **$50–100 per spot illustration, ~$200 for a full-page interior, $500 to several thousand for cover art.** He models a 40-page zine at roughly **$2,350 in art alone**, which after DriveThruRPG's ~35% cut requires around **360 digital sales just to break even on art**. He notes that even Jason Bulmahn — the creator of Pathfinder — needed 600+ sales to recoup a $2,500 art budget on a recent adventure. ([Loot the Room — RPGs and the High Cost of Art](https://loottheroom.uk/rpgs-and-the-high-cost-of-art))

A more granular 2019 rate survey, still broadly the working reference:

| Item | Rate |
|---|---|
| RPG full-page colour illustration | $200–500 (industry typical) |
| Half-page | 50–60% of full page |
| Quarter-page | 25–35% of full page |
| Black & white | roughly half the colour rate |
| Spot filler, b/w (Dean Spencer's published rates) | $40+ |
| Spot filler, colour | $60+ |
| Full-page b/w | $255+ |
| PDF layout | $2–5 per page |
| Print layout (EFA guideline) | $4–14 per page |
| Hand-drawn b/w map | from $50/page; Dyson Logos $250/page |
| Full-colour map | comparable to a full-page illustration |

([EN World — A Guide to RPG Freelance Rates, Part 2](https://www.enworld.org/threads/a-guide-to-rpg-freelance-rates-part-2-layout-illustration-and-cartography.666262/) — dated April 2019; **treat as a floor, not current**. General inflation since 2019 plus the anti-AI-driven premium on human illustration means real 2026 rates are meaningfully higher.)

For comparison and calibration: Magic: The Gathering pays roughly **$400–600 per card** to typical artists, up to triple that for name artists; a full-page colour illustration at a major trade publisher runs **$3,000+**. (same source)

**Consequence:** a fully-illustrated core rulebook is a $10,000–40,000 proposition. That is not a nights-and-weekends number. Plan on **zero to eight commissioned pieces total** for launch, deployed where they do the most work: one cover/hero image, and one image per major Setting.

## 2.3 The four things that actually work when you cannot buy art

### (a) Typography-led identity

This is the highest-leverage option for a software-first product, because **your product is mostly text and interface anyway**. Notestine's Typography 101 is the practical primer: six essentials (body text, point size, line spacing, line length, functionality, type choice), with RPG-specific adjustments — he recommends larger sizes for screen reading (15–25px) than print standards would suggest. His central argument is that **every typeface carries historical and functional baggage that communicates before a single word is read**, which makes type selection an identity decision rather than a styling one. Crucially, he argues *against* using extreme typefaces to compensate for weak content: "let your game stand out with its mechanics, writing, and art." ([Explorers Design — Typography 101](https://www.explorersdesign.com/typography-101/))

He recommends robust families that can carry an entire layout alone — **IBM Plex, Noto, Fira** (all open-licensed) — plus EB Garamond for classical weight. On licensing, he warns explicitly against grabbing fonts from "random websites" and insists on licences that grant commercial rights.

**The licensing detail that matters for a web app**, and which most designers get wrong: fonts under the **SIL Open Font License** may be used commercially, modified, embedded in documents under any terms, and **bundled inside software sold commercially**. The two constraints are that (i) OFL fonts cannot be sold *on their own*, and (ii) the **Reserved Font Name** clause means a modified version cannot carry the original name. ([Wikipedia — SIL Open Font License](https://en.wikipedia.org/wiki/SIL_Open_Font_License)) This means IBM Plex, Fira, EB Garamond, Inter, and the whole Google Fonts OFL corpus are legally clean for a paid web platform, for the PDF exports it generates, and for print — at zero cost. A distinctive *paid* display face for the wordmark alone (typically $30–200 for a single weight, desktop licence) is a very cheap way to buy uniqueness on top of an open body-text foundation. Verify the licence permits logo use; some foundries restrict it.

### (b) Public domain sources, with real scale

These are not scraps. The available corpus is enormous and legally clean:

- **The Metropolitan Museum of Art** — over **492,000** public-domain artworks released under **CC0** since February 2017, explicitly free to "download, share, and remix." ([Met Open Access](https://www.metmuseum.org/hubs/open-access))
- **Smithsonian Institution** — **2.8 million** images and associated data released under CC0 in 2020, across 19 museums and research centres. ([Creative Commons, Feb 2020](https://creativecommons.org/2020/02/27/smithsonian-releases-2-8-million-images-data-into-the-public-domain-using-cc0/))
- **Public Domain Day, 1 January 2026** — US works published in **1930** and sound recordings from **1925** entered the public domain. The rolling rule is 95 years from publication, so each January adds another year. ([Copyright Lately — Public Domain Day 2026](https://copyrightlately.com/public-domain-2026/); [Internet Archive](https://blog.archive.org/public-domain-day-2026/)) For a project launching in 2027–2028, this means 1931–1932 material — the peak of Art Deco graphic design, technical illustration, and pulp-magazine layout — becomes available on schedule.
- Also standard: NYPL Digital Collections, Biodiversity Heritage Library (scientific plates), Wellcome Collection (medical and anatomical), Old Book Illustrations, Rawpixel, and the Public Domain Review's curated collections. ([Inkwell Ideas — Free/Open Fantasy Art Sources](https://inkwellideas.com/2013/01/13-free-open-fantasy-art-sources/) — dated 2013, links may have rotted, but the category list is still the right one.)

**The catch, and it is a real one:** Bissette calls public-domain art "always a compromise." The compromise is *coherence*. A book of 19th-century engravings from twelve different sources looks like a scrapbook unless you impose a unifying treatment — one duotone, one halftone screen, one crop discipline, one consistent placement rule. **The treatment is the brand, not the images.** Mörk Borg is the proof: much of its power comes from processing, not sourcing.

### (c) Generative and procedural visuals, made by you, not by a model

This is the option that is underexploited and that fits your specific skills. You are building a web app; you can write code that makes pictures. Algorithmic/parametric visual systems — p5.js, SVG generation, plotter aesthetics, Voronoi/flow-field/reaction-diffusion structures, procedural sigils, procedural heraldry, procedural star charts — are **not generative AI**. They are deterministic programs you wrote. They are:

- Free at the margin. Once written, you have infinite assets.
- Perfectly on-brand by construction, because the parameters *are* the brand.
- Trivially defensible against the anti-AI scrutiny discussed in §3.3, because you can publish the source.
- Genuinely distinctive, because almost nobody in tabletop does it.

There is also a thematic fit worth noticing: your system's own vocabulary is mathematical (Vectors, Channels, Dimension Spaces, Thresholds, Layers). A visual language built from vectors and fields is not decoration bolted on — it is the mechanics rendered. **[This is my synthesis, not a sourced claim.]** The risk is that procedural work reads as cold or as programmer-art; mitigate by pairing it with warm typography and by hand-curating rather than dumping generator output.

### (d) Sparse, high-impact commissioning

Given the rates above, a defensible launch art budget is **$800–2,500 total**: one cover/key art piece at $500–1,500, plus three to six spot pieces at $75–150. Commission from one artist so the pieces cohere. Pay properly and credit prominently — in the current climate (§3.3) the artist's name is itself a brand asset.

## 2.4 The specific opportunity: your product is a UI

Every point above is about books. Yours is not primarily a book — it is a **web application people will look at for an hour a day, five days a week, for months**. This inverts the usual indie-RPG identity problem in your favour.

Nobody's brand memory of Notion, Linear or Figma is driven by illustration. It is driven by a colour, a typeface, a density, a motion language, and a small number of distinctive interface gestures. A tabletop system delivered as software gets to build identity out of the parts you are already building — and interface craft is a thing you can actually produce alone, unlike illustration.

The corollary is a warning: **the app cannot look like a generic SaaS dashboard.** The default aesthetic of "web app built by a solo developer in 2026" is Tailwind grey with an Inter heading and a lot of cards, and it will read as an admin panel for the game rather than the game. The identity work is in resisting that default.

---

# Part 3 — Positioning

## 3.1 The actual size and shape of the thing you are positioning against

Three independent 2025–2026 datasets converge on the same rank order, which is useful because each has different biases:

**Foundry VTT 2025 Year in Review** (install share among licence owners — biased toward technically-inclined, VTT-using players): D&D 5e **64.28%**, Pathfinder 2e **30.52%**, Pathfinder 1e **4.32%**.

**Gen Con 2026 scheduled events** (biased toward convention-organised play): D&D **1,751** events, Pathfinder **320**, Starfinder **267**, Call of Cthulhu **247**, out of 6,700+ sessions across 500+ systems.

**Bob World Builder May 2026 player poll**, ~**27,500 votes** (biased toward YouTube audiences): D&D 5e (2014) 3,267, Pathfinder all editions 3,081, D&D 5e (2024) 2,553.

Resulting 2026 top ten: D&D 5e (2024), Pathfinder 2e, **Daggerheart**, Call of Cthulhu 7e, Starfinder 2e, Blades in the Dark, Shadowdark, Vampire: The Masquerade 5e, Cosmere RPG, OSR systems. ([ScriptoriumGM — Most Popular TTRPG Systems 2026](https://www.scriptoriumgm.com/blog/most-popular-ttrpg-systems)) **[Secondary aggregation of three primary sources; the underlying datasets are real but each is a convenience sample.]**

A matchmaking platform's April 2026 data is starker on the demand side: of 1,560 active players and 688 active groups, **~60% of groups looking for players are D&D games, and 90% of player-side posts are looking for a D&D game.** ([Groupfinder, April 2026](https://groupfinder.gg/library/is-dnd-still-king-a-deep-dive-into-groupfinders-2026-matchmaking-data)) **[Small sample, one platform, self-selected. Directionally useful, not a market share estimate.]**

**Read all of this as follows:** D&D is not a competitor you can take share from. It is the *weather*. The relevant question is never "how do I beat D&D," it is "what is the second game these people play, and what makes them play it."

Note also that the number three slot — **Daggerheart**, launched 2025 — was achieved by Critical Role, the largest actual-play brand in existence, leveraging an audience it had spent a decade building. That is what it takes to enter the top three from outside. It is not a strategy available to you and you should not model on it.

## 3.2 What "not D&D" positioning works, and what fails

**What works: positioning against a specific, nameable frustration — never against the brand.**

*Draw Steel* (MCDM) raised **$4.6 million against an $800,000 goal on BackerKit**, positioning as a heroic fantasy RPG "unburdened" by D&D's legacy and as a "direct competitor with modern innovations." Critically, the pitch was **mechanically specific**: every attack hits (no whiffed turns), players choose their own action order (no initiative roll), all in service of "teamwork and drama without wasted turns." ([TechRadar](https://www.techradar.com/gaming/indie-tabletop-rpg-raises-over-dollar46-million-on-backerkit-in-effort-to-create-fantasy-title-unburdened-by-dungeons-and-dragons))

The pattern generalises. Every successful "alternative" of the last five years names a *feeling*, not an enemy:

- *Shadowdark* — "old-school danger for a modern audience": OSR lethality without OSR's usability problems.
- *Mothership* — sci-fi horror; the pitch is Stress and Panic, not "unlike D&D."
- *Blades in the Dark* — heist fiction; the pitch is flashbacks and the score structure.
- *Mörk Borg* — doom metal apocalypse; the pitch is an *object*.

**What fails:**

1. **"D&D but better."** This is a comparison you cannot win because the customer's switching cost is not the rules — it is their group, their character, their DM's prep, and their D&D Beyond purchase history. A system that is D&D-shaped gives them no reason to pay that cost.
2. **"5e compatible" as a strategy rather than a tactic.** Building on 5e compatibility permanently subordinates your brand to someone else's roadmap and puts you in the most crowded aisle in the hobby. It also makes you legible only as an *accessory*. **[THIN — I could not find a rigorous quantitative source on 5e-compatible market saturation; this is a widely-held practitioner view and my own synthesis rather than a sourced finding.]**
3. **Negative-space identity generally.** "Not D&D" is not a positioning, it is a hole. It tells a prospect what they will not get.

**For your product specifically, the natural positioning is not about D&D at all.** Your differentiator is a *mode of play* — asynchronous, week-long, server-resolved — which D&D structurally cannot deliver because D&D is a synchronous-table game with a human referee. That is a positioning against a **constraint in the customer's life** ("we cannot get five adults in a room every week") rather than against a product. Constraint-based positioning is far more durable than competitor-based positioning, because the constraint does not release a new edition.

## 3.3 The AI question is a positioning asset, and it is bigger than you may realise

This is the strongest tailwind available to you and it is worth being loud about.

**The list of publishers and institutions with formal anti-generative-AI policies now includes:** Paizo, Chaosium, Stonemaier Games, Wizards of the Coast, Renegade Game Studios, Free League, Kobold Press (a formal "No AI Pledge" in late 2024), Magpie Games, Monte Cook Games, Modiphius, Rowan Rook & Decard (who amended their licences to forbid using their games for AI training), the **ENNIE Awards** (total ban for the 2025–2026 cycle), and **DriveThruRPG** (banned standalone AI-art products and AI-generated text). ([Geek Native — The Growing List of Tabletop Companies Banning AI](https://www.geeknative.com/221420/the-human-touch-the-growing-list-of-tabletop-companies-banning-ai/); [ENNIE Awards — Revised Policy on Generative AI Usage](https://ennie-awards.com/revised-policy-on-generative-ai-usage/))

At **UK Games Expo 2026**, the con's refusal to take a public position became the story of the show. Designer Steph Windross produced "**Human Made**" signs that were distributed across the floor, funded by Rowan Rook & Decard and Modiphius. Publishers including RR&D called the silence "disappointing." The consumer-attitude datapoint in that piece is the one to note: at a panel, when attendees were asked whether they would buy from a company using AI, **few raised their hands** — but almost everyone was fine with AI in *back-end logistics*. ([Wargamer — Tabletop creators push back against AI at UK Games Expo 2026](https://www.wargamer.com/tabletop-ai-ukge))

**Three consequences:**

1. **"No AI" is a credential in this market, not a limitation.** It is worth a prominent, specific, dated policy page — not a vague statement. Specificity is what makes it credible.
2. **Note the asymmetry attendees expressed.** Front-of-house (art, prose, the things players consume) is where the line is. Back-office is not. A policy that says exactly this — "no generative AI in any published art, text, or game content; we use ordinary developer tooling internally" — is both honest and matches where the audience's actual line sits. A blanket "we never touch AI" claim from a software developer in 2026 will read as either naive or dishonest and is a hostage to fortune.
3. **The 2025 crowdfunding data suggests AI is polluting the low end.** The RPG crowdfunding tracker's 2025 report notes the record project *count* alongside a collapse in medians, and hypothesises that low-goal AI-generated submissions are a driver. ([2025 Year End RPG-related Crowdfunding Report](https://skalchemist.cloud/mediawiki/index.php/2025_Year_End_RPG-related_Crowdfunding_Report)) If true, the signal value of "verifiably human" *rises* as the noise floor rises.

## 3.4 The hard problem: being a system AND a platform

There is no clean, encouraging precedent here. Let me lay out what the evidence actually shows.

**Platforms that are not systems have consolidated.** Roll20 acquired Demiplane in June 2024 ([Roll20 blog](https://blog.roll20.net/posts/roll20-has-acquired-demiplane/); [Blizzard Watch](https://blizzardwatch.com/2024/06/04/roll20-acquires-demiplane/)). Astral Tabletop — which launched as PowerVTT in 2017, grew through the pandemic and had a OneBookShelf partnership — halted development because, in its founder's words, "even with the growth that Astral has experienced, it has not attracted an audience large enough to be a thriving business," and the VTT landscape was becoming "even more competitive." ([Geek Native](https://www.geeknative.com/135941/astral-tabletop-halts-development/))

**The richest company in the hobby could not make a platform work.** Wizards shut down **Sigil**, the D&D Beyond 3D VTT, on **18 March 2025**, laying off roughly **30 developers — about 90% of the team** — one month after a rocky public playtest. ([Rascal News](https://www.rascal.news/wizards-of-the-coast-shutters-sigil-virtual-tabletop-project-lays-off-30-staff/)) This is worth sitting with. Sigil had Hasbro's balance sheet, the D&D brand, and D&D Beyond's existing subscriber base, and it still died.

**The one clearly successful system-plus-tool in indie tabletop is COMP/CON, for Lancer** (Massif Press). It is free, open-source, purpose-built for exactly one system, and does not attempt to be a virtual tabletop. ([COMP/CON on GitHub](https://github.com/massif-press/compcon); [Massif Press](https://massifpress.com/lancer)) Lancer's rules are also available free. The tool is not a business; it is a **retention and onboarding mechanism for the book business**.

**The board-game analogue is instructive and cautionary.** App-mandatory board games (Fantasy Flight's *Mansions of Madness* 2e, *Descent: Legends of the Dark*) reliably generate consumer anxiety about **app obsolescence** — the game becomes unplayable if the app is retired. This concern has been a persistent thread in the hobby since 2016. ([BoardGameGeek — "Game now tied to app obsolescence"](https://boardgamegeek.com/thread/1611826/game-now-tied-to-app-obsolescence)) **[Forum discussion, not research — but the sentiment is real, durable, and will be aimed at you.]**

**The brand consequences of all this, which are the actionable part:**

- **You will be read as a VTT unless you actively prevent it.** VTT is a category with brutal incumbents, a consolidating market, a demonstrated inability to sustain new entrants, and a customer expectation of "supports all systems." If your first sentence lets someone file you under "VTT," you inherit all of that. **Your framing must foreground the *system* and the *asynchronous mode*, with the software as the medium, not the product.** "It is a game you play in a browser over a week" is a different category from "it is a tool for playing games."
- **The obsolescence objection will be raised on day one, by someone with 4,000 Bluesky followers.** Prepare a real answer before launch, not a reassuring one. Options: an offline/print fallback ruleset; a documented Ledger export format; a published commitment that the rules are readable and playable without the server; open-sourcing the fold engine. Something *structural*, because the audience will not accept a promise. Your architecture already gives you the strongest possible version of this answer — an append-only per-Campaign Ledger with a deterministic fold is, by construction, an exportable, replayable, self-describing artefact. **Say that out loud, in the marketing.** It is the single best brand-trust asset in your design and it costs nothing to communicate.
- **The single-product platform is a brand advantage, not a limitation.** Every general-purpose VTT is drowning in the requirement to support everything. A platform that does one system perfectly and cannot do anything else is *legible*, and legibility is the scarce resource.

---

# Part 4 — The Invented Vocabulary

Your lexicon — Substrate, Socket, Vector, Moment, Channel, Threshold, Allocation Points, Ledger, Fold, Facet, Noun, Verb, Layer, Lens, Almanac, Dispatch, Chronicle — is unusually large and unusually *systems-engineering-flavoured*. This section is about when that becomes an asset and when it becomes a wall.

## 4.1 When a lexicon is an asset

**Blades in the Dark** is the clearest tabletop case. John Harper's terms — *playbook*, *score*, *stress*, *trauma*, *devil's bargain*, *position and effect*, *clock*, *flashback*, *downtime* — became so portable that Harper released a Creative Commons SRD in December 2017 and the vocabulary propagated into an entire genre. As of April 2023 itch.io listed **over 300 products tagged "Forged in the Dark."** The Kickstarter itself was modest — **$179,280 from 3,925 backers** in 2015 — so the vocabulary's spread is not an artefact of scale; it is an artefact of the words being *good*. ([Wikipedia — Blades in the Dark](https://en.wikipedia.org/wiki/Blades_in_the_Dark))

Note *why* those words work. Every one is (a) a common English word, (b) used in a slightly displaced sense, (c) that names a thing the player does or feels. "Clock" is not a new word; it is an old word doing a new job, and the job is visible the first time you see the diagram.

**Magic: The Gathering** is the commercial-maximum case. "Tap" was chosen as a plain English verb meaning "to draw out, from, or upon." The mechanic was covered by US patent **5,662,332** ("Trading card game method of play"), and the tap symbol went through several redesigns — the original tilted "T" failed internationally because "tap" does not begin with T in other languages. ([MTG Wiki — Tap](https://mtg.fandom.com/wiki/Tap)) **[Fandom wiki; treat the narrative as community-sourced, though the patent number is independently verifiable.]** The lesson: the strongest game vocabulary is *short, verbal, and physical*.

**Games Workshop is the cautionary version of "lexicon as asset."** GW systematically renamed generic terms to proprietary ones specifically to make them trademarkable — Imperial Guard → **Astra Militarum**, Eldar → **Aeldari**. One analysis found that in the very codex that introduced "Astra Militarum," the phrase appeared **17 times in prose while "Imperial Guard" appeared 111 times** — GW's own writers would not use it. The author's argument: the names sacrifice usability for legal protection, and fail even at that, because "everyone is still going to use 'Imperial Guard.'" ([Variance Hammer, May 2014](https://variancehammer.com/2014/05/07/astra-militarum-is-a-silly-name-and-games-workshop-knows-it/)) **[Opinion blog. But the word-count evidence is checkable and the pattern of GW renamings is a matter of public record.]**

**This is directly your risk.** A word chosen because it is ownable, rather than because it is right, will be quietly replaced by the community with the word it displaced — and then you have two vocabularies, one in the book and one at the table, and the one at the table wins.

## 4.2 When a lexicon is a barrier — the actual research

The best experimental evidence is not from games; it is from science communication, and it is unusually clean.

Bullock, Colón Amill, Shulman & Dixon (2019) ran a 2×2 design with **650 US participants**, who read paragraphs about emerging technologies in either jargon-heavy or plain-language form, with or without inline definitions. Findings:

- Jargon **significantly impaired processing fluency** — the felt ease of understanding — independent of actual comprehension. Jargon condition mean fluency **4.57** vs **5.27** for plain language.
- Reduced fluency produced **greater motivated resistance to persuasion** and **higher risk perception**, via a serial mediation path.
- Lower fluency and higher resistance produced **reduced willingness to adopt** the technology described.
- **Providing inline definitions did not mitigate the effect.** No significant interaction. Defining your terms does not rescue you.

([Bullock et al., *Public Understanding of Science*, 2019 — full text PDF](https://comm.osu.edu/sites/comm.osu.edu/files/PUS%202019-%20Bullock%20et%20al..pdf); [journal listing](https://journals.sagepub.com/doi/abs/10.1177/0963662519865687))

**That last finding is the important one and it is bad news for the obvious mitigation.** A glossary does not fix jargon. The effect operates on *fluency*, not comprehension — it is about how hard the text *feels*, and a definition adds text.

The counterweight is a real one, from the software world. The CNCF argues that Kubernetes' reputation for terminological complexity is misattributed: the new vocabulary (Pod, Deployment, Ingress) is not the barrier; the *distributed-systems domain* is. "This power and versatility do not come without complexity." ([CNCF — Too Complex: It's Not Kubernetes, It's What It Does](https://www.cncf.io/blog/2025/03/06/too-complex-its-not-kubernetes-its-what-it-does/)) The honest synthesis: **jargon that names irreducible complexity is defensible; jargon that renames familiar things is pure cost.**

Applying that test to your list, and this is my judgement rather than a sourced finding:

| Term | Verdict |
|---|---|
| **Ledger, Record, Fold, Substrate, Socket, Layer, Component, Facet, Noun, Verb, Edition, Bundle, Lens, Delivery** | **Architecture vocabulary.** Names things only you and third-party Component authors touch. Precision matters more than accessibility. Keep. These belong in developer docs, not in player onboarding. |
| **Vector, Channel, Dimension, Modifier, Guard, Threshold, Capacity, Allocation Points, Moment, Tick** | **The contested middle.** These are the words a *player* has to hold in their head to take a turn. This is where the jargon tax is levied. |
| **Moment, Threshold, Channel, Capacity, Standing Order, Almanac, Dispatch, Chronicle, Session, Campaign** | **Already good.** Common English, displaced meaning, evokes the fiction. These are Blades-shaped words. |
| **Substrate, Vector, Socket, Facet, Fold** | **Engineering register.** Correct, but they smell like a compiler. To a player, "Vector" is a maths class. |

**The specific structural risk:** you have *both* an architecture lexicon and a play lexicon, and they currently share a register. A reader cannot tell from the words alone which layer they are in. Blades avoids this because it only has a play lexicon. Magic avoids it because its rules-engine vocabulary ("the stack," "state-based actions") is explicitly quarantined in the Comprehensive Rules, which no casual player ever opens.

**The mitigation that the research supports** — since definitions do not work — is **not defining less, but exposing less.** Reduce the number of terms a player must encounter *before their first successful action*. The Bullock result is about fluency at first contact. A player who has already taken three satisfying turns has a completely different relationship to the word "Vector" than one who met it in paragraph two of the rulebook. Your software gives you a weapon here that a book does not: **progressive disclosure**. You can literally not show a term until the player needs it.

## 4.3 The trademark upside of an invented lexicon

Worth naming, since it partially offsets the cost. Fanciful and arbitrary terms are the strongest trademarks (§1.2). A proprietary term that becomes genuinely associated with your game — "Allocation Points," an Almanac, a Dispatch — is a registrable asset in a way that "hit points" never could be. Games Workshop's strategy is correct in the abstract; it fails only in execution, when the ownable word is worse than the word it replaced.

**Test to apply to every term:** *if this word were not ownable, would I still choose it?* If no, it is an Astra Militarum and it will lose to whatever players call it instead.

---

# Part 5 — Licensing and Openness as Brand Strategy

## 5.1 Where the landscape actually stands in 2026

**The OGL crisis and its resolution.** In January 2023 Wizards' plan to replace and deauthorise the Open Game License 1.0a — in place since 2000 and universally understood as perpetual — triggered the largest community revolt in the hobby's history. Over 15,000 fans responded to WotC's survey. On **27 January 2023** Wizards announced OGL 1.0a would remain "in place, as is. Untouched," and released the entire SRD 5.1 under Creative Commons, with an executive stating: "This Creative Commons license makes the content freely available for any use. We don't control that license, and cannot alter or revoke it." Commentators immediately identified this as "a one-way door." ([GameSpot](https://www.gamespot.com/articles/dungeons-dragons-backtracks-on-ogl-deauthorization-adds-creative-commons-license/1100-6510953/); [GeekWire](https://www.geekwire.com/2023/after-fan-outcry-wizards-of-the-coast-will-leave-its-original-open-license-in-place/); [Hipsters of the Coast](https://www.hipstersofthecoast.com/2023/01/wizards-withdraws-open-gaming-license-moves-srd-5-1-to-a-creative-commons-license/))

**Three years on**, the assessment from EN World is that the OGL is now "barely used," having been superseded by Creative Commons Attribution, which is legally stronger; SRD 5.1 and 5.2 are both CC BY across five languages. The commercial coda is important: WotC ultimately got what it wanted — reduced OGL dependency — by pivoting to **monetising third-party content through D&D Beyond platform fees rather than through licence terms**. A carrot, after the stick failed. WotC's reputation, per the same discussion, has not recovered. ([EN World — We All Won: The OGL Three Years Later](https://www.enworld.org/threads/we-all-won-%E2%80%93-the-ogl-three-years-later.717946/)) **[Community discussion thread with a named columnist; no market data.]**

**The ORC License** (Open RPG Creative), driven by Paizo in response to the crisis, is now the system-neutral open standard. Its architecture is deliberately unrevocable: the licence text is held by Azora Law but **dedicated to the public domain**, registered with the Library of Congress (**TX 9-307-067**), and **cannot be amended, revoked or updated — ever**. It permits use of mechanics in any medium royalty-free, including video games and podcasts; it requires an ORC Notice crediting upstream licensors, identification of your Reserved Material (art, story, characters, setting), and share-alike **on mechanics only**. This is its key distinction from both the OGL (share-alike on everything, ambiguous reserved rights, revocable in practice) and CC BY-SA (share-alike on the whole work). ([Paizo — ORC License](https://paizo.com/orclicense))

**The bespoke third-party licence has become the indie norm.** Mörk Borg's is the template: creators may make and sell content commercially without permission, **the publisher takes 0%**, creators may not use the publishers' logos but are encouraged to use a compatibility logo, may not claim to be official, and may not reuse art or text — but may freely use the system mechanics. ([Geek Native — Mörk Borg launches 0% cut license](https://www.geeknative.com/93298/doom-metal-osr-rpg-mork-borg-launches-0-cut-license/))

## 5.2 What licence choices signal

This is a semiotics question as much as a legal one, and in this hobby the signals are unusually well-established:

| Choice | What it signals in 2026 |
|---|---|
| **Fully proprietary, no third-party licence** | "Corporate." Post-OGL, this is read as a risk to anyone considering building on you. Costs you the most valuable free marketing available: other people's products with your name on the cover. |
| **CC BY on an SRD** | Maximum openness, maximum trust, zero control. Blades in the Dark's route. Generated 300+ derivative products. |
| **ORC** | "I am on the community's side, and I have thought about this." Signals alignment with Paizo/Free League/Kobold. Irrevocability is the whole point of the signal. |
| **Bespoke compatibility licence, 0% cut, logo-controlled** | The indie default. Mörk Borg, Mothership, Shadowdark, Draw Steel. Gives you brand control (the compatibility logo) while giving away the mechanics. |
| **Revenue-share or approval-gated licence** | Reads as the DMs Guild model. Acceptable if the platform genuinely adds distribution value; corrosive if it reads as a tax. |

**The specific tension in your business model, stated plainly:** you sell **Components** as products, and a Component is *code and data*, not prose. An open licence on the *mechanics* costs you nothing — nobody can build a competing Component without your Substrate. An open licence on the *Component interface* is different: it invites third parties to build Components for your platform, which is enormous distribution leverage *and* direct competition for the thing you sell.

The resolution used by every successful platform is the layered one, and your architecture already anticipates it:

- **Substrate, Verb set, Ledger format, Record schema, Noun kinds** — publish openly, permissively (CC BY or ORC or a plain MIT-style grant on the schemas). This is your *standard*. Standards want to be free; a standard nobody can implement is not a standard.
- **First-party Components, Settings, Adventures** — proprietary, sold.
- **Third-party Components** — permitted under a compatibility licence with a compatibility mark, sold through your platform, with you taking a distribution cut *only* if you provide distribution. The Mörk Borg 0% model is the trust-maximal version; a marketplace cut is defensible if the marketplace is real.
- **The name and the compatibility logo** — retained absolutely. This is what the trademark is *for*. The licence gives away mechanics; the trademark keeps the brand. That is precisely how Mörk Borg's licence is drafted.

**Two warnings.**

First: **your CLAUDE.md rule that "users author instances, never types" is a licensing statement as much as an architectural one**, and the community will read it that way. "The authoring tool must make this structurally impossible" is going to be experienced by some fraction of your audience as a walled garden. You need a public answer for "so how do I make a new Component?" The good answer is a documented Component SDK with a real path to publication. The bad answer is silence, because in this hobby, silence about openness now defaults to suspicion.

Second: **whatever you promise, promise it irrevocably or not at all.** The single loudest lesson of 2023 is that a licence people believed was perpetual, and which was then threatened, cost Wizards more reputation than a restrictive licence would have cost them from the start. ORC's design — public-domain text, Library of Congress registration, no amendment mechanism — is a *brand statement about irrevocability*, and that is why it works.

---

# Part 6 — Community as Brand: Channels, Timelines, Costs

## 6.1 The honest economics

Start with the base rates, because everything else is a rounding error against them.

**RPG crowdfunding, calendar 2025:** **US$66.99 million** across **2,331 projects**. Mean project **$28,738** — the lowest since 2014. **Median project $3,640** — the lowest on record since tracking began in 2013. Excluding blockbuster outliers, total value fell from $44M to $16M year over year. BackerKit rose to 13% of projects and 25% of funding; Kickstarter remains dominant. ([2025 Year End RPG-related Crowdfunding Report](https://skalchemist.cloud/mediawiki/index.php/2025_Year_End_RPG-related_Crowdfunding_Report))

Read that median again: **half of all RPG crowdfunding projects raise under $3,640.** The distribution is savagely right-skewed. Mothership's $1.67M and Draw Steel's $4.6M are not the top of a curve; they are a different phenomenon entirely, driven by audiences built over years before the campaign.

**Product-level base rates:** a practitioner guide puts it at "most products sell under 200 copies lifetime," with creators earning "$2–5K per product at best," and recommends **500+ engaged followers as the minimum before attempting Kickstarter**, with 10–15% of raise consumed by platform fees, processing and tax. Its phased timeline: months 0–6 build foundation with free content, 6–18 develop a first real product (20–50 pages), 18–24 launch, year 2+ scale. It calls email "the most valuable marketing asset you'll own" and professional editing "the most important investment you'll make," and advises keeping the day job. ([RPG Drop — How to "Make It" in the TTRPG Industry](https://www.rpgdrop.com/how-to-make-it-in-the-ttrpg-industry-comprehensive-strategy-for-small-indie-creators/)) **[THIN — practitioner blog, no methodology behind the "under 200 copies" figure. But it is consistent with the crowdfunding median and with everything else in this section.]**

**The 18–24 month timeline before a launch is the realistic one for a nights-and-weekends project, and it should be understood as a marketing timeline, not just a development one.** The audience has to be built *during* development, not after.

## 6.2 The channels, honestly assessed for 2026

**Discord — alive, essential, and the wrong place to start.** Every successful indie RPG of the last five years has a Discord. Mothership used Google+ then Discord ([The Companion](https://www.thecompanion.app/mothership-inside-the-million-dollar-sci-fi-horror-rpg/)). MCDM's entire design process runs through community feedback. Kelsey Dionne describes the Shadowdark community as "players in a huge Shadowdark campaign" whose enthusiasm directly shapes what she writes next ([Forbes](https://www.forbes.com/sites/robwieland/2025/03/19/shadowdarks-second-million-dollar-kickstarer-creates-a-full-setting/)).

But Discord is a **retention** channel, not an acquisition channel. An empty Discord is worse than no Discord — it is a public advertisement that nobody cares. Do not open one until you have something for people to talk about and roughly 50–100 people who want to. **[My judgement; the community-building content available on this is uniformly low-quality SEO material and I would not cite any of it.]**

**Bluesky — alive, and the centre of gravity for tabletop.** The tabletop creator migration from X happened in a concentrated burst in November 2024, alongside comics, game dev and comedy; Bluesky was at 21.2 million users at the time, and the stated drivers were functional moderation, block lists with teeth, and a trust-and-safety function. ([EN World, Nov 2024](https://www.enworld.org/threads/tabletop-creators-leave-x-for-bluesky-in-droves.708055/)) Clayton Notestine, the most-referenced designer in §2, posts primarily on Bluesky. **[I could not find 2026 engagement data specific to the TTRPG segment on any platform. The claim that Bluesky is where tabletop lives is well-supported for late 2024 and is my inference for 2026 — flagging that explicitly.]**

**X/Twitter — effectively dead for this audience.** The tabletop creator class left. Staying is not neutral; for a segment this politically legible it reads as a position.

**Mastodon — alive but small, and a poor primary.** Best treated as a cross-post.

**Reddit — alive, high-reach, hostile to self-promotion.** r/rpg and r/RPGdesign are among the largest concentrations of the target audience anywhere, and both have self-promotion rules that will get a launch post removed. The workable pattern is a year of genuine participation before you have any standing. High cost, high ceiling.

**itch.io — alive, and structurally the friendliest storefront in existence.** Listing is free and itch uses **open revenue sharing**: *you* choose what percentage of your sales goes to itch. ([itch.io Creator FAQ](https://itch.io/docs/creators/faq)) Compare DriveThruRPG's ~35% ([Loot the Room](https://loottheroom.uk/rpgs-and-the-high-cost-of-art)). For a free ashcan/quickstart used as a top-of-funnel, itch is the obvious host.

**Newsletter — alive, and the only channel you own.** Benchmarks for creator newsletters in 2026: 35–50% open rates for creator lists, 45–60% for niche authority lists, versus 22–32% for general business email; healthy CTR 3–8%; organic list growth 2–5%/month. The essential caveat: Apple Mail Privacy Protection inflates reported opens, so "real read rates are probably 50–70% of reported open rates." ([Heist Brain — Newsletter Open Rate Benchmarks 2026](https://heistbrain.com/benchmarks/newsletter-open-rate.html)) **[THIN — SEO benchmark aggregator with no stated methodology. Directional only. The MPP caveat is independently well-established.]**

The strategic point stands regardless of the exact numbers: it is the only list you carry across platform collapses, and platform collapses now happen roughly every three years.

**Kickstarter/BackerKit — alive, but as a *launch* mechanism, not a discovery mechanism.** The 2025 medians make this unambiguous. Crowdfunding converts an existing audience; it does not create one. BackerKit's rise to 25% of RPG funding dollars, and MCDM raising $4.6M there, means it now merits equal consideration to Kickstarter for tabletop.

**Actual play — the hardest call, and I think the answer is: not for you, not yet.**

The historical evidence for actual play as a discovery engine is genuinely extraordinary. Wizards' own research in 2020: "For the first time in our research, it used to be that friends and family were the number one reason someone joined D&D. Now, the number one reason is 'I saw someone playing online and I joined.'" 150 million hours of D&D content viewed on Twitch and YouTube, up ~50% year on year; Critical Role's Kickstarter raised **$11.3 million from 88,000+ backers**. ([CNBC, March 2020](https://www.cnbc.com/2020/03/14/critical-role-helped-spark-a-dungeons-dragons-renaissance.html))

The 2026 picture is much less encouraging for a new entrant. In October 2025, the Twitch D&D category averaged roughly **623 viewers across 65 streams**; the general tabletop RPG category roughly **1,501 viewers across 27 streams**. At least **1,000 actual play shows** are listed on RPGAP.com, many inactive. Academic work on microstreaming finds **99.5% of creators earn below monetisation thresholds**. Practitioners in the piece frame AP as being in its "silent film era" — genuinely early as an art form — while acknowledging that advertising dollars and Patreon sustainability are the binding constraint. ([TTRPG Insider — Are There Too Many Actual Plays?](https://www.ttrpginsider.news/p/are-there-too-many-actual-plays-a-closer-look))

Averaging ~600 concurrent viewers across an entire category means the marginal new show reaches approximately nobody. **Actual play is now a channel you buy access to (by getting an existing show to play your game), not one you build.** Sending free copies plus real GM support to three mid-sized existing shows is a far better use of your time than producing your own.

**A distinct and better-fitting opportunity for you: your game is asynchronous, which means it produces text.** A week-long campaign generates a readable transcript — a Chronicle, in your own vocabulary. That is *natively* shareable content in a way a four-hour video is not. This is a genuine structural advantage over synchronous games in the content-marketing dimension and I have not seen anyone exploit it. **[My synthesis; no source.]**

**Broader discovery data, with a caveat.** A May 2024 survey of 1,009 US *video game* players found YouTube at 64%, TikTok 38%, Instagram 36%, Facebook 35%, friends/acquaintances 34%, ads 32% as discovery channels; 40% would try a game because it is a new instalment of a favourite franchise, 25% because a developer they like made it. ([Big Games Machine via Game Dev Reports, May 2024](https://gamedevreports.substack.com/p/big-games-machine-how-people-discover)) **[This is video games, not tabletop. The tabletop audience skews older, more text-oriented and more forum-based. Use it only as a rough shape.]** The one transferable finding is the last: **a quarter of players will try something because of who made it.** For someone with no franchise, the *maker* is the only available franchise. Which argues for building a personal, named public presence in parallel with the product.

## 6.3 A realistic brand-track sequence and what it costs in money

**These are brand-track stages, not product phases.** The product sequence is `phase-map.md`, which deliberately carries no dates. The months below are the *external* clocks this track runs against — trademark pendency, audience growth — and they line up against the product roughly as shown.

| Brand stage | Months on the external clock | Runs alongside | Activity | Cash |
|---|---|---|---|---|
| **1 · Foundation** | 0–6 | Phases 0–1 | Name + clearance + intent-to-use filing; domain; newsletter live; build in public; free playable ashcan | ~$1,200–1,600 (TM filing 2 classes + domain + LLC) |
| **2 · Build** | 6–18 | Phases 2–4 | Alpha with a private playtest cohort; Discord opens once there is something to discuss; monthly newsletter; commission cover art | ~$800–2,500 (art) + ~$200/yr (hosting, email) |
| **3 · Launch** | 18+ | Phases 7–8 | Crowdfunding or direct launch; seed existing AP shows; SOU filing | ~$400 (SOU 2 classes) + campaign fees 10–15% of raise |

**Total cash: roughly $3,000–5,500**, dominated by trademark and art.

**The one place these two clocks collide, and it matters.** An intent-to-use filing gives priority for three years maximum, with extensions. `issues-and-ideas.md` A22 puts Phases 0 through 3 alone at multiple years at six to twelve hours a week. **File when the name is chosen and defensible — not the moment it is merely liked** — or the priority window can lapse before there is anything to launch under it.

---

# Part 7 — Anti-Patterns

## 7.1 Rebrands that hurt

**Warhammer Fantasy Battle → Age of Sigmar (2015).** Games Workshop destroyed a decades-old setting and replaced its flagship fantasy game with one shipping **four pages of rules and no points system**, requiring players to re-base entire armies from square to round and abandoning rank-and-flank play. Some rules were jokes ("re-roll any failed hit rolls... so long as you have a bigger and more impressive moustache than your opponent"). One retrospective: "The release was an utter disaster." Players filmed themselves burning armies. Recovery took three years and was substantially driven by *fans* building competitive rulesets, which GW eventually adopted — hiring community members and shipping the General's Handbook in 2016, then AoS 2.0 in 2018. ([Age of Sigmar: A 5 Year Retrospective](https://www.tabletopbattles.com/age-of-sigmar-a-5-year-retrospective), originally Goonhammer) **Lesson: a rebrand that discards accumulated player investment — characters, armies, campaigns, knowledge — is not a rebrand, it is a launch with negative goodwill.** For you: never break a Campaign. Your Conversion mechanism is a brand feature.

**Unity Runtime Fee (2023–2024).** Announced as a per-install charge above revenue thresholds; triggered a developer revolt, threats of mass migration, and, within roughly two weeks, the departure of CEO John Riccitiello, followed by Unity Create's head. The fee was **cancelled on 12 September 2024** by incoming CEO Matthew Bromberg, who framed the reversal in terms of partnerships "built on trust." Terraria's Re-Logic donated $200,000 to open-source engines in response. ([Game Developer](https://www.gamedeveloper.com/business/unity-is-killing-its-controversial-runtime-fee); [TechRadar](https://www.techradar.com/gaming/terraria-developer-re-logic-responds-to-unity-runtime-fee-by-donating-dollar200000-to-open-source-engines)) **Lesson: for a platform, pricing terms *are* brand. A retroactive change to the deal is the fastest way to destroy a developer-facing brand, and reversing it does not restore the position.** Directly relevant to you, because you will run a Component marketplace with third-party sellers.

**OGL 1.1 (2023).** Covered in §5.1. **Lesson: the cost of *threatening* to close something open exceeded the cost of never opening it.** Wizards ended up more open than before, with a permanently damaged reputation, and only achieved its commercial goal afterwards via a carrot.

## 7.2 Names that aged badly, and names that should have stayed dead

**Reviving a defunct name: the TSR case.** After the TSR trademark lapsed, a new entity was formed in 2021 by a North Carolina tattooist and Gary Gygax's son. Litigation with Wizards began in December 2021; Wizards countersued alleging, among other things, trademark fraud regarding the TSR logo, and in 2022 sought an injunction against *Star Frontiers: New Genesis*, claiming reputational damage over reportedly racist and homophobic content. On **12 June 2023** the new TSR filed Chapter 7. Its filings showed **$621.93 in revenue for 2023 to date against $384,941.99 in liabilities.** ([Wargamer](https://www.wargamer.com/dnd/wizards-of-the-coast-tsr-bankruptcy); [GeekWire](https://www.geekwire.com/2022/wizards-of-the-coast-files-lawsuit-to-stop-publication-of-tabletop-game-alleging-trademark-violation-and-reprehensible-content/)) **Lesson: an available name is not a free name. Nostalgia brands carry the original owner's enemies, the original owner's baggage, and an active party with a legal budget.**

**Product names that aged badly.** D&D's *Oriental Adventures* is the standing example: in 2020 Wizards applied a sensitivity disclaimer to legacy products on DMs Guild, and campaigns followed to have the product delisted entirely. ([EN World](https://www.enworld.org/threads/dungeons-dragons-fans-seek-removal-of-oriental-adventures-from-online-marketplace.672989/); [HuffPost](https://www.huffpost.com/entry/dungeons-and-dragons-oriental-adventures-disclaimer_n_5f089048c5b6480493cf760f)) **Lesson for a system with an invented vocabulary: any term that encodes a real-world ethnic, national or religious frame is a liability with a 20-year fuse.** Your vocabulary is abstract and mechanical, which entirely sidesteps this. That is worth preserving deliberately when you name Settings later — the *Settings* are where this risk lives, not the Substrate.

**Names that trap.** A name that encodes a specific technology, edition number, scope or year constrains everything after it. "One D&D" was a working name during the playtest that Wizards abandoned; the eventual products were branded by year (2024 Player's Handbook), and the community settled on "5.5e" anyway — a naming outcome nobody chose. ([EN World discussion](https://www.enworld.org/threads/d-d-2024-is-now-officially-called-5-5e.718185/)) **[Community thread; treat the "officially" framing as loose.]** **Lesson: the community names your editions, not you. Give them something short and good to say, or they will invent something worse.**

## 7.3 Positioning that trapped a product

**The VTT category trap.** Astral Tabletop grew, then died, because the category demands universality and universality is expensive; its founder's own diagnosis was that growth never reached "an audience large enough to be a thriving business" in a market getting "even more competitive." ([Geek Native](https://www.geeknative.com/135941/astral-tabletop-halts-development/)) Sigil died with Hasbro's money behind it ([Rascal News](https://www.rascal.news/wizards-of-the-coast-shutters-sigil-virtual-tabletop-project-lays-off-30-staff/)). Roll20 consolidated Demiplane ([Roll20](https://blog.roll20.net/posts/roll20-has-acquired-demiplane/)). **If your positioning lets anyone file you under VTT, you have inherited a category with a demonstrated inability to sustain new entrants.**

**The "compatible with X" trap.** Building your identity on compatibility with a bigger system means your ceiling is set by their roadmap and your shelf space is in the accessories aisle. It is a fine *tactic* for a supplement and a fatal *strategy* for a platform.

**The single-book trap.** Legally covered in §1.1. Commercially it is the same problem: a product that is one book is a product with one sale per customer.

## 7.4 Failure modes specific to a solo-developer platform brand

These are inference from the cases above rather than documented incidents, flagged as such:

- **The abandonment signal.** For a *platform*, unlike a book, silence reads as death. A book that stops updating is finished; an app that stops updating is dying. A public changelog is a brand artefact, not an engineering one.
- **The bus factor question.** People will ask what happens to their Campaigns if you stop. Answer structurally (export format, offline rules, escrowed source) rather than reassuringly.
- **Pricing architecture as brand.** Your Components/Settings/Adventures model reads as either "expansions" (good, familiar, board-game-shaped) or "microtransactions" (bad, mobile-game-shaped). The framing, the price points and the packaging decide which — and the decision is essentially irreversible after launch. See Unity.
- **The founder-as-brand trap.** For a solo developer with no audience, being personally visible is the cheapest acquisition channel available (see §6.2 on the 25% who try a game because of who made it). But a brand fused to a person cannot be sold, cannot be delegated, and cannot survive you needing a year off. Build the product brand as the primary and the personal account as the amplifier, not the reverse.

---

# Part 8 — Recommendations for This Project

Ranked by consequence and by how early the decision locks in.

**1. File a house mark, not a book title, and file it intent-to-use, soon.**
The single-work refusal (§1.1) is the trap that caught MCDM. Avoid it by filing the **name of the platform/system** in **IC 009 + IC 042 (and/or 041)** with software and online-service identifications, where the single-work doctrine explicitly does not apply. Add **IC 028** if physical goods are ever likely. Intent-to-use costs $350–450 per class now and buys you three years of priority — which is roughly your development timeline. Budget **$900–1,600** self-filed for two classes, or **$1,500–2,500** with an attorney. Do a clearance sweep across USPTO, itch.io, DriveThruRPG, BGG, Steam and Kickstarter *before* you spend anything.

**2. Choose a fanciful or arbitrary name, one or two words, phonetically pleasant, with a clean handle set.**
Fanciful/arbitrary is the only zone where legal strength, availability and Notestine's aesthetic criteria all coincide. Avoid: "The ___ of ___," anything containing "RPG," "Tabletop," "Engine," "Forge," "Nexus," "Realm," "Quest," "Saga" — all of which are both descriptive-tending and hopelessly crowded. Avoid dead names entirely (§7.2). Prefer a name where `.com` + Bluesky + Discord + GitHub + itch are all consistently available over a "better" name where they are not. Prefer `.com`; treat `.io` as carrying a live sovereignty risk (§1.5).

**3. Do not let the name describe the technology or the mode.**
"Async," "Web," "Play-by-Post," "Server," "Cloud" in the name are descriptive (weak trademark), date-stamped, and cap the product at its launch feature set. The *tagline* should carry the mode; the *name* should carry the feeling.

**4. Build a typography-and-system-led visual identity, and treat the app UI as the primary brand surface.**
One open-licensed body family (IBM Plex / Fira / EB Garamond — commercially clean under OFL, including embedded in paid software), one distinctive display face bought for the wordmark, one disciplined colour system, one grid. Then invest your differentiation budget in **procedural, code-generated visual systems** — you can write them, they cost nothing at the margin, they are provably not AI, they are on-theme with a vector/field/threshold mechanical language, and essentially nobody in tabletop is doing it. Commission **$800–2,500** of human art total for launch: one hero piece plus a handful of spots, from one artist, credited loudly.

**5. Position on the constraint, not on D&D.**
The pitch is "a real RPG for people who cannot get five adults in a room every week" — or however you say that in your own voice. Positioning against a life constraint outlasts positioning against a competitor. Never say "not D&D," never say "D&D but," never say "5e compatible."

**6. Actively refuse the VTT frame in the first sentence of every description.**
"A tabletop RPG you play across a week, in your browser" is a category of one. "A virtual tabletop for asynchronous play" is a category with corpses in it. This is a copywriting decision with strategic consequences and it should be made once, written down, and enforced everywhere.

**7. Publish a specific, dated no-AI policy, and make it precise rather than absolute.**
The market credential is real and growing (Paizo, Chaosium, Free League, Kobold Press, Magpie, MCG, Modiphius, RR&D, the ENNIEs, DriveThruRPG — §3.3). Be exact: no generative AI in any published art, prose, or game content; state your position on internal tooling honestly. The UKGE 2026 evidence shows the audience's line is at what they consume, not at your build process, and a claim broader than you can defend is a liability.

**8. Make the Ledger's exportability a headline brand promise, not an engineering footnote.**
The app-obsolescence objection is certain to arrive (§3.4). Your architecture answers it better than any competitor's: an append-only, per-Campaign, deterministically-foldable Record log is by construction a portable, replayable, self-describing artefact. Publish the format. Ship the export button on day one. Consider open-sourcing the fold engine — it is the highest-trust, lowest-cost signal available to you, and it does not give away the Components, which are what you sell.

**9. Layer the licence: open standard, proprietary Components, controlled mark.**
Publish the Substrate, Verb set, Record schema and Noun kinds under a permissive, irrevocable licence — ORC or CC BY. Sell first-party Components. Permit third-party Components under a compatibility licence with a compatibility logo and a 0% or clearly-justified cut (the Mörk Borg model). **Retain the name and logo absolutely** — that is what the trademark is for, and it is exactly how Mörk Borg's licence is drafted. Whatever you promise, make it structurally irrevocable, because 2023 proved that a revocable promise is worth less than no promise.

**10. Split your vocabulary into two registers and expose the play register only.**
Substrate, Socket, Fold, Facet, Ledger, Layer, Noun, Verb belong in developer documentation and should never appear in player-facing onboarding. Moment, Threshold, Channel, Capacity, Standing Order, Almanac, Dispatch, Chronicle are already excellent player words. The Bullock et al. finding is that **glossaries do not fix jargon** — only reduced exposure at first contact does. Use progressive disclosure in the software: do not show a term until the player needs it to act. Apply the Astra Militarum test to every term: *would I still choose this word if it were not ownable?*

**11. Rename "Vector" for players, keep it in the engine.**
It is the one contested-middle term that most clearly reads as mathematics rather than fiction, and it sits at the exact point of first contact — it is what a player *does on their turn*. The engine can keep Vector forever. **[This is a judgement call, not a sourced finding, and it may be wrong — if the word is doing real disambiguating work for players, the cost of two names for one thing may exceed the jargon cost.]**

**12. Newsletter from month one; Bluesky from month one; Discord from month nine.**
Email is the only asset you own across platform collapses. Bluesky is where the tabletop creator class went. Discord opened too early is a public advertisement that nobody cares.

**13. Ship a free playable ashcan on itch.io twelve months before launch.**
itch is free to list and lets you set the revenue share yourself. A free, playable, print-and-play-or-browser subset is the cheapest possible proof that the system is real and fun — and it is the artefact that gets you the 500 followers you need before crowdfunding is viable.

**14. Do not start an actual play show. Do seed three existing ones, and publish Chronicles instead.**
The Twitch tabletop category averages a few hundred concurrent viewers across the whole category; 1,000+ AP shows already exist; 99.5% of microstreamers earn below monetisation thresholds. Your asynchronous format's native output is *readable text*, which is a shareable artefact no synchronous game produces. That is a content-marketing advantage nobody is using.

**15. Plan for 18–24 months and ~$3,000–5,500 in cash before launch.**
That is what the evidence supports, and knowing it up front is worth more than optimism.

---

# Part 9 — Open Questions Only Dylan Can Answer

These are the decisions where no amount of research substitutes for your judgement, and where I would want your answer before going further on any of them.

**On the name**

1. Is the brand name **the system**, **the platform**, or **the company** — and are those one thing or three? Wizards of the Coast / Dungeons & Dragons / D&D Beyond is three. Mörk Borg is one. Three is more flexible and three times the trademark cost. This decision determines everything in Part 1.
2. Do you want a name that is **pronounceable and spellable on first hearing**? The Mörk Borg umlaut is a brand asset in print and a permanent tax in search, voice, and word-of-mouth. Which cost are you willing to carry?
3. Do you have a **shortlist**? Everything in §1.4 is executable in an evening once there are candidates, and the clearance result may kill several.

**On the product's shape**

4. **Is the ruleset ever a book?** If a printed or PDF core book exists as a saleable object, you inherit the whole art-cost structure of §2.2 and the single-work trademark problem of §1.1. If it is only ever software and web documentation, both problems largely dissolve. This is the highest-consequence unanswered question in this document.
5. **Can the game be played without your server?** Not "would anyone," but *can it*. This determines whether you can answer the obsolescence objection structurally or only rhetorically, and it is an architecture decision, not a marketing one.
6. **What exactly is a Component to a customer?** An expansion, a subscription tier, a class, a rules module, a DLC? The mental model you choose determines the price point, and the price point is close to irreversible after launch.

**On openness**

7. **Do you want third-party Component authors — genuinely?** "Users author instances, never types" is a hard architectural line. If it holds absolutely, you have no third-party ecosystem, which removes the most powerful free marketing available in this hobby (see Mörk Borg's 300+ third-party products) and will read to some of the audience as a closed platform. If there is a sanctioned path for a *developer* to author types, what is it, who is eligible, and what does it cost them?
8. **Are you willing to make an irrevocable licence promise?** ORC's power is that it cannot be taken back. Are you prepared to commit at that level before you know your business model?

**On you**

9. **Are you willing to be personally visible?** A named human building in public is the cheapest acquisition channel you have and the single strongest counter-signal against AI-slop suspicion. It is also exposure you may not want, and it fuses the brand to you in a way that is hard to undo.
10. **What is your actual weekly hour budget, and does it survive month 14?** The 18–24 month timeline is real. Most solo projects die between months 9 and 15, when the novelty is gone and the launch is not close. Knowing your own answer to this changes what scope you should commit to publicly.
11. **What happens if it works?** If 3,000 people are playing asynchronously and generating support load while you have a full-time job — what is the plan? This is a brand question, not an ops question, because the failure mode is visible: an unanswered Discord and a stale changelog are how a platform brand dies in public.

**On the vocabulary**

12. **Which terms are load-bearing for players versus for you?** You know which ones a player must actually hold in their head to take a turn. That list is the only one where the jargon research applies. Everything else is documentation and can be as precise as you like.
13. **Would you accept the community renaming things?** They will. Blades' players say "clock." Warhammer's players still say "Imperial Guard." If you would find that intolerable, the vocabulary needs to be *good* rather than merely *correct* — because "correct" loses to "sayable" every time.

---

# Appendix — Source Quality Notes

**Strong (primary or first-party):**
USPTO fee schedule · TMEP via BitLaw · TTABlog on *Strongholds & Followers* (precedential TTAB) · Paizo ORC licence text · itch.io creator FAQ · Met Museum Open Access · Creative Commons on Smithsonian · Bullock et al. 2019 (peer-reviewed) · Roll20 acquisition announcement · Massif Press / COMP/CON repository · Wikipedia entries for Mörk Borg, Blades in the Dark, Shadowdark, Caller's Bane, Praey for the Gods, SIL OFL.

**Good (reported journalism, named authors):**
EFF on *Spots the Space Marine* · Rascal News on Sigil · Wargamer on TSR bankruptcy and on UKGE 2026 · Game Developer on Unity · CNBC on Critical Role · Forbes on Shadowdark · TechRadar on Draw Steel · GameSpot / GeekWire / Hipsters of the Coast on the OGL · Geek Native on the AI-policy list, the Mörk Borg licence and Astral Tabletop · The Companion on Mothership · TTRPG Insider on actual-play saturation · Explorers Design (Notestine) · Loot the Room (Bissette).

**Weak — do not make load-bearing:**
TrademarKraft (USPTO figures — verify against the USPTO dashboard) · Michael Meyer Law and ZenBusiness (self-published pricing) · ScriptoriumGM and Groupfinder (aggregation and small convenience samples, though the underlying datasets are real) · RPG Drop (no methodology) · Heist Brain (SEO benchmark aggregator) · Variance Hammer and the EN World threads (opinion/community) · MTG Fandom wiki · Big Games Machine survey (video games, not tabletop).

**Gaps I could not close:**
- No reliable 2026 engagement data for TTRPG communities on Bluesky specifically.
- No rigorous quantitative source on 5e-compatible market saturation.
- No usable market-size figures for tabletop RPGs from any credible source; the entire "TTRPG market report" search space is machine-generated.
- Could not verify the B/X Essentials → Old-School Essentials rename rationale from a primary source.
- No research at all, academic or industry, on jargon load specifically in tabletop RPG onboarding. The Bullock et al. science-communication work is the closest transferable evidence and the transfer is an inference.
- No comparable precedent for a commercial single-system asynchronous RPG platform. The closest analogues (COMP/CON, play-by-post forums, app-driven board games) each differ in a way that matters. This is genuinely new territory, which is both the opportunity and the risk.
