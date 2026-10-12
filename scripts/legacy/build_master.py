# Master list builder (workbook + plan9.json for the PDF). Data inlined below.
import json,sys

# sale_id: (short name, company, city, zip, dates, days_label, drive_min, notes)
SALES={
5072409:("Air, Land or Sea (pilot's estate)","And Again Estate Sales","Weatherford","76087","Fri 9/25 – Sun 9/27",45,"Near Dylan's work. Aviation/airline collection + audio."),
5087100:("High-End Equestrian & Western","Unique Estate Sales","Weatherford","76088","Sat 9/26 – Sun 9/27",50,"Western wear room: ~30 pairs of boots, hats, jewelry."),
5078532:("Time Capsule MCM","Kitchens To Closets","Duncanville","75116","Thu 9/24 – Sat 9/26",45,"Cash/Venmo/Zelle only. Comics + lunchboxes are uncaptioned."),
5086461:("Delightful Sale","Southern Revival","Duncanville","75137","Wed 9/23 – Sat 9/26",45,""),
5084871:("Granny Chic","Family Legacy Estate Sales","Aledo","76008","Thu 9/24 – Sat 9/26",45,""),
5074425:("Anchors, Art & Antiques","Fantastic Finds Estate Sales","Arlington","76013","Thu 9/24 – Sun 9/27",30,"Military items are captioned (company knows them)."),
5083770:("Arlington: Unbeatable Deals","Dayspring Estate Sales","Arlington","76018","Thu 9/24 – Sat 9/26",35,"Big sale (950 photos). Strongest single stop in Arlington."),
5072352:("Preston Hollow Demolition Sale","Dayspring Estate Sales","Dallas","75220","Thu 9/24 – Sat 9/26",35,"Demolition = everything goes; rugs rolled up."),
5080236:("About The House – Windmill Hill","About The House","Desoto","75115","Thu 9/24 – Sat 9/26",50,"Most uncaptioned finds of any sale."),
5047674:("Garland: Unbeatable Deals","Dayspring Estate Sales","Garland","75040","Thu 9/24 – Sat 9/26",45,"Designer bags present (skipped – need authentication)."),
5085255:("Preston Hollow Fine Furnishings","Discovery Estate Sales","Dallas","75229","Thu 9/24 – Sat 9/26",35,""),
5084379:("Room to Room","Forget Me Not Estate Sales","Lancaster","75146","Thu 9/24 – Sun 9/27",50,"Hobby room with HO trains."),
5044686:("Brilliant Bedford","Rustrial Renovations","Bedford","76021","Thu 9/24 – Sat 9/26",20,"Close to Keller."),
5082942:("Motorcycle, Lladros, Collectibles","Annice Antiques","Midlothian","76065","Thu 9/24 – Sun 9/27",55,"Antique dealer runs it – expect sharper prices."),
5018778:("Multi Generational","Ambrosia & Co.","Dallas","75287","Fri 9/25 – Sat 9/26",35,""),
5083080:("Positively Perfect","Chickadee Lane","Plano","75074","Thu 9/24 – Sat 9/26",45,""),
5082645:("Vintage Character Meets Classic","Full House Estate Sales","Mansfield","76063","Thu 9/24 – Sun 9/27",40,""),
5086653:("Eclectic home, Windsor Park","At A Glance Estate Sales","Dallas","75225","Fri 9/25 – Sun 9/27",40,""),
}
# (sale, photo idx, item, captioned, check, sold evidence, low, high, channel, fee, ship, confidence)
T=[
(5072409,1856,"TEAC A-3340S 4-channel reel-to-reel deck (plus a second TEAC/Akai deck below it)","N","Plug in: reels turn in play/FF/rewind, meters move. Skip if it won't power on.","Terapeak 12 mo: TEAC A-3340S median $400 (p25 $250, p75 $785); tested units $350–420",250,420,"FB local / eBay",0.136,40,"M"),
(5072409,1937,"Akai 4000D-series reel-to-reel deck","N","Same power/transport test.","Terapeak: Akai 4000D/DS median $217 (p25 $160); $180 for a plain working unit",150,220,"FB local",0,0,"M"),
(5072409,1842,"1970s National Airlines 'Watch us shine' posters (several) + Pan Am A300 operating manuals + Delta counter displays","N","Posters original (not reprints): printer line at bottom, period paper. Manuals complete.","Terapeak: National Airlines posters median $120 (range $41–300); Pan Am manuals median $83, lots $280–500",150,400,"eBay",0.136,25,"M"),
(5072409,1843,"Gulf Supreme + Pennzoil metal oil cans (original)","N","Original litho, no 'reproduction' stamp; dents OK.","Terapeak: Gulf Supreme cans median $52 (quarts $75–115)",60,130,"eBay",0.136,15,"M"),
(5072409,1804,"Classic rock LP collection (Skynyrd Second Helping, Early Beatles on Capitol, Springsteen, Nugent…)","N","Pull only clean, early pressings; check vinyl for scratches.","No Terapeak run; typical $5–25 each for these titles",100,250,"FB local bulk / eBay singles",0,0,"L"),
(5087100,9915,"Pendleton Glacier National Park wool blanket (label + GNP patch)","N","Wool, no moth holes; tag says Pendleton.","Terapeak: Pendleton Glacier NP blanket median $137 (p75 $195); vintage wool $125–250",120,200,"eBay / FB local",0.136,15,"H"),
(5087100,9884,"~30 pairs of cowboy boots incl. exotic leathers + Resistol hats","N","Look inside for Lucchese / Tony Lama / Justin / Rios of Mercedes; skip unbranded.","Terapeak: Lucchese men's median $200 (p75 $315, exotic caiman $780); Tony Lama median $139",150,450,"eBay",0.136,20,"M"),
(5087100,9838,"Southwest sterling & turquoise jewelry (cuff, naja pendant, coral/turquoise pendant)","N","Must be stamped 'Sterling' or '925' + artist hallmark; magnet test (silver isn't magnetic).","Terapeak: Navajo sterling turquoise cuffs median $205 (p25 $135)",150,400,"eBay",0.136,10,"M"),
(5087100,9917,"Gibson hardshell acoustic case – guitar may be inside","N","Open it: Gibson label/serial inside the soundhole. Case alone is still resale.","No Terapeak run; Gibson acoustic cases $100–200, guitars $1,000+",100,200,"FB local",0,0,"L"),
(5078532,983,"1960s comic lot (~40 bagged: Action Comics 12¢/15¢, Superman, Daredevil, Flash, Doom Patrol, Dr. Strange, Marvel Tales Spider-Man)","N","Count issues; look for key numbers; covers attached; no water damage.","Terapeak: silver-age 12¢ comic lots median $128 (p75 $185); Daredevil 28-issue lot $174",200,500,"eBay (lot or singles)",0.136,15,"H"),
(5078532,1037,"1974 Aladdin Evel Knievel metal lunchbox (+ Bicentennial flag box)","N","Metal (not tin repro); rust level; thermos is a bonus.","Terapeak: Evel Knievel 1974 Aladdin median $125 (p25 $75, p75 $199)",80,150,"eBay",0.136,15,"H"),
(5078532,1224,"Antique silver-plated baritone horn + brass trombone in original cases","N","Maker name on the bell (Conn, King, Holton, York = better). Valves move.","No Terapeak run; antique baritones $75–250 each",100,300,"FB local / eBay",0,0,"M"),
(5086461,3247,"Vintage sunburst archtop acoustic guitar (Kay/Harmony type, f-holes)","N","Label inside f-hole; neck straight; no cracks.","Terapeak: vintage Kay archtops median $225 (p25 $168)",150,250,"FB local",0,0,"M"),
(5084871,782,"1977-style Star Wars 'May the Force Be With You' raglan nightshirt","N","Tag: 'Factors Etc.' or '1977 Twentieth Century Fox' = original.","Terapeak: 1977 Star Wars tees median $55; Factors originals up to $200",50,150,"eBay",0.136,6,"L"),
(5084871,780,"1970s Thermos 'Road Runner' metal lunchbox","N","Paint wear and rust.","Terapeak: Road Runner lunchbox median $70 (p75 $90)",50,90,"eBay",0.136,15,"M"),
(5084871,849,"Two vintage Penn saltwater reels (Senator type) in wood box","N","Model on the side plate (Senator 4/0–9/0); handle turns.","Terapeak (parts-heavy): Senator reels $50–140",70,140,"eBay",0.136,15,"M"),
(5074425,306,"Dutch Gouda-style hand-painted art pottery vase (1920s–30s look)","N","Bottom must say Gouda / Zuid-Holland / Plazuid with a house mark.","Terapeak: Gouda vases median $60 (p75 $99; 1920s pieces $110–129)",60,120,"eBay",0.136,15,"M"),
(5083770,3943,"American Girl dolls in original boxes (Josefina, Kaya) + boxed accessories + Bitty Babies","N","Doll inside each box; retired pieces (Pleasant Company era = better).","Terapeak: boxed Josefina doll $225; Kaya boxed $120; accessory sets $57–165",250,600,"eBay",0.136,25,"H"),
(5083770,4136,"1950s–60s women's closet: Lilli Ann coats (one 'Tissé à Paris'), Bill De Natale dress, Alice Polynesian dress, mink-collar suede","N","Labels intact; no moth holes or underarm stains.","Terapeak: Lilli Ann coats median $136 (p75 $289, rare swing coats $395)",200,600,"eBay / Etsy",0.136,20,"H"),
(5083770,4006,"1960s–70s rock LPs: Yes Fragile, Stones Exile on Main St, The Band Music From Big Pink, Mothers of Invention, Kinks, Bowie","N","Original pressings (labels, inserts); vinyl condition.","No Terapeak run; originals of key titles $25–60 each",150,400,"eBay singles",0.136,10,"M"),
(5083770,4579,"Vintage Pyrex: blue refrigerator dishes w/ lids, turquoise Butterprint, primary bowls","N","No dishwasher dulling; lids present.","Terapeak: Pyrex refrigerator sets median $90; turquoise Butterprint bowls median $39 (4-bowl set $270)",80,200,"FB local",0,0,"M"),
(5072352,4870,"Rolled hand-knotted Persian rugs & runners (Bijar/Tabriz type)","N","Flip the corner: knots visible on the back = hand-knotted; fringe is the warp.","No Terapeak run; hand-knotted runners $200–1,500",200,800,"FB local / eBay",0,40,"M"),
(5072352,4943,"Easton Press leather-bound books (several)","N","Count them; gilt edges clean.","Terapeak: Easton Press lots median $145 (8-book lots $188–228)",100,250,"eBay",0.136,20,"M"),
(5080236,7263,"January 1935 nude pin-up calendar – 'Cannon Ball Linen Supply Co., Dallas TX'","N","Full calendar pad attached; no big tears.","Terapeak: 1935 pin-up calendars $50–450 (Earl Moran example $450); Dallas advertising adds local appeal",100,250,"eBay",0.136,15,"M"),
(5080236,7747,"1970s lighted ceramic Christmas trees (green and white, several)","N","Base lights up; plastic bulbs mostly present.","Terapeak: vintage large ceramic trees median $120 (p75 $190)",100,300,"FB local (Oct–Dec peak)",0,0,"H"),
(5080236,7507,"Le Creuset Dutch oven + skillet/saucepan","N","'Le Creuset' cast on the lid/bottom; no enamel chips inside.","Terapeak: Le Creuset Dutch ovens median $224 (p25 $132)",130,280,"FB local",0,0,"H"),
(5080236,7366,"1930s wood tombstone/cathedral tube radio (Philco-style)","N","Back label for brand/model; cabinet intact. Sell as-is.","Working/nice sets $100–250",80,200,"FB local",0,0,"M"),
(5080236,7199,"Silvertone (Sears) banjo","N","Head intact, neck straight.","Terapeak: Silvertone banjos median $120",90,150,"FB local / eBay",0,0,"M"),
(5080236,7813,"Antique Robbins & Myers 'Junior' desk fan (c. 1905–20)","N (price tag)","Blades/cage intact; spins by hand.","Terapeak: Robbins & Myers antique fans median $125 (Junior working $52; 8\" oscillating $150)",60,150,"eBay",0.136,20,"M"),
(5080236,7801,"Board of ~150 railroad date nails / ID tags","N","Read the stamped numbers/letters; loose and complete.","No Terapeak run; date-nail lots typically $100–300",100,300,"eBay",0.136,15,"M"),
(5047674,5875,"Jay Strongwater jeweled glass ornaments in original boxes","N","Box says Jay Strongwater; tag/number on ornament.","Terapeak: Jay Strongwater ornaments median $300 each (p25 $213)",200,500,"eBay",0.136,12,"M"),
(5047674,6072,"Tony Lama men's cowboy boots, boxed (~11.5D) + Stetson hat new in box","N","Tony Lama stamp inside; minimal wear.","Terapeak: Tony Lama men's median $139; Stetson NIB $60–150",120,250,"eBay",0.136,20,"M"),
(5085255,8319,"Rek-O-Kut Rondine Jr. L-34 transcription turntable with tonearm (1950s hi-fi)","N (price sign nearby)","Platter spins; tonearm present.","Terapeak: Rondine Jr. L-34 $62–495, median $225 (working $248)",150,300,"eBay",0.136,35,"H"),
(5085255,8339,"1960s–70s board games incl. 1968 Dark Shadows","N (price sign)","Pieces complete.","No Terapeak run; Dark Shadows game $40–100",60,150,"eBay",0.136,15,"L"),
(5084379,8550,"HO model train collection: ~15 locomotives + cars in display case, boxed Tyco piggyback set","N","Brand on the bottoms (Athearn, Atlas, Kato, Bachmann Spectrum = better than Tyco/Life-Like).","Terapeak: Tyco piggyback sets median $40; brand-name HO locos $40–150 each",300,800,"eBay",0.136,30,"M"),
(5044686,8801,"Commodore color monitor (1702-type) + Hayes modems, boxed software","N","Model on the back (1702/1802/1084); powers on.","Terapeak: Commodore 1702 median $366 (tested $325–550)",250,450,"eBay",0.136,45,"H"),
(5044686,8775,"Shirley Temple doll – likely 1930s Ideal composition","N","Composition (hard, not vinyl); 'Shirley Temple' mark on neck.","Terapeak: Shirley Temple composition dolls median $99 (1930s Ideal $175–618)",100,250,"eBay",0.136,15,"M"),
(5044686,8799,"1960s Rosko 'Bartender' battery tin toy","N (price tag)","Works with batteries; box is a bonus.","Terapeak: Rosko Bartender median $43 (boxed $50–75)",40,75,"eBay",0.136,12,"M"),
(5082942,3643,"Large drawer set of Cutco knives in Cutco trays (brown classic handles, cleaver)","N","Count pieces; blades not chipped.","Terapeak: Cutco sets median $162 (p75 $195); big sets more",150,350,"eBay / FB local",0,0,"H"),
(5082942,3769,"Antique engraved brass alto/tenor horn + brass trombone","N","Maker stamp; engraving.","No Terapeak run; $150–400 together",150,350,"FB local / eBay",0,0,"M"),
(5018778,2268,"Rock LP lot: Doors L.A. Woman, Led Zeppelin II, Blind Faith, Runaways, Steely Dan, R.E.M.","N","Original pressings; condition.","No Terapeak run; $100–300 for the lot",100,250,"eBay singles",0.136,10,"M"),
(5083080,6858,"Royal Quiet De Luxe typewriter with case (+ Smith-Corona Galaxie)","N","Keys strike, carriage moves.","Terapeak: Royal Quiet De Luxe median $120 (p75 $150; working 1950s $275)",90,150,"FB local / eBay",0,0,"M"),
(5082645,1465,"Vintage Pyrex nesting mixing bowls (primary colors)","N","Complete set of 4; no dulling.","Terapeak: primary-color sets $60–125",60,120,"FB local",0,0,"M"),
(5082645,1558,"1946 Texas vs Missouri football program (pin-up cover)","N","Complete, cover attached.","Terapeak: 1940s Longhorns programs ~$65",50,120,"eBay",0.136,6,"M"),
(5086653,2494,"Antique brass-blade electric fan (GE/Emerson type, 1910s–30s)","N","Brand tag on motor; blades straight.","Antique brass-blade desk fans typically $100–300",100,250,"eBay / FB local",0,20,"M"),
]
SKIP=[
(5047674,"Louis Vuitton Speedy, Chanel-style flap bag, Burberry scarf","Designer goods – value depends on authentication (out of scope)."),
(5085372,"Louis Vuitton flap bag","Authentication required."),
(5072352,"Cartier box, Lucchese box (contents unknown)","Ask to see inside; box alone is low value."),
(5082942,"'14K Italy' chains and pendants","Gold claims need testing; pendants look like costume pieces in the photo."),
(5072409,"Soviet orders and medals","Fakes are very common; can't verify from photos."),
(5072409,"Round Delta/Pan Am porcelain signs; Texaco/Phillips 66 signs","Reproductions."),
(5085372,"Louisville Slugger Jackie Robinson R17 bat","Terapeak median $50 – too thin."),
(5074425,"Military caps and hats","Company already captioned and researched them."),
(5069514,"Parker Duofold store display clock, Waterman store display (pen collector's estate)","Company captioned them – expect full prices. Worth a look only on the last-day discount."),
(5084445,"Fine art (Plano)","Heavily researched and captioned by the company."),
]

# New estate sales/photos found Sept 22 (run 9). Photo indexes refer to esn9_idx.json.
SALES9={
5088765:("A Geologist's Treasures","Pranton Estate Sales","Flower Mound","75028","Fri 9/25 – Sun 9/27",30,"New this week. Garage has a Honda inverter generator."),
5082459:("NASA & Collectibles Galore","Dusty Gold Estate Sales","Flower Mound","75022","Fri 9/25 – Sun 9/27",30,"Big NASA/military collection – company captioned most of it; targets below are uncaptioned."),
5089257:("Collector's Estate","Texoma Auctions & Estate Sales","Fort Worth","76179","Fri 9/25 – Sun 9/27",20,"Close to Keller."),
5084217:("Wedgwood Fort Worth","Annie's Estate Sales","Fort Worth","76133","Fri 9/25 – Sun 9/27",35,"Photos grew from 60 to 167 since yesterday."),
5082837:("Bits and Pieces in Bedford","Bits And Pieces Estate Sales","Bedford","76022","Thu 9/24 – Sat 9/26",20,"Photos grew from 71 to 235 since yesterday."),
}
T9=[
(5088765,889,"Honda EU2000i inverter generator (clean, in the garage)","N","Pull-start it; check hours meter/oil. Estate companies often price these $300+ – only buy under the ceiling.","Terapeak 12 mo: EU2000i median $585 (p25 $500, p75 $675), 45 sold",500,675,"FB local",0,0,"H"),
(5082459,496,"Bernina Virtuosa 153 Quilter's Edition sewing machine + accessory case","N","Power on, stitch a line; foot pedal and power cord present.","Terapeak: Virtuosa 153 QE median $570 (p25 $450, p75 $600)",450,600,"FB local / eBay",0,40,"H"),
(5082459,436,"Atari 2600 lot: ~20 games in a wood rack, Sears Tele-Games box, joysticks & paddles (+ NES console, SNES pads)","N","Count carts; check for the console itself (not visible in this photo).","Terapeak: Atari 2600 lots median $188 (p25 $105, p75 $220)",120,220,"eBay",0.136,20,"M"),
(5082459,447,"Stack of ~15–20 unbuilt Monogram/Revell aircraft model kits","N","Sealed or complete (parts on sprues).","Terapeak: aircraft kit lots median $61 (p75 $110); single 1/48 kits $80–115",60,150,"eBay",0.136,20,"M"),
(5088765,797,"Pair of iridescent pulled-feather studio art-glass vases (Robert Held / Correia style)","N","Signature on the bottom (Held, Correia, Lotton). Unsigned = pass.","Terapeak: Robert Held vases median $100 each (p75 $150)",150,300,"eBay",0.136,30,"M"),
(5084217,1278,"Yashica-Mat EM twin-lens reflex camera (+ Polaroid folding camera)","N","Shutter fires at several speeds; lens clear (no haze/fungus).","Terapeak: Yashica-Mat EM median $100 (p75 $135, clean $215–235)",90,150,"eBay",0.136,15,"M"),
(5084217,1280,"Boxed Accutron by Bulova watch (+ boxed Swiss Army watch)","N","Model and whether it runs; gold-filled vs solid gold stamp.","Terapeak: Accutron with box median $150 (p25 $103)",100,200,"eBay",0.136,10,"M"),
(5082837,978,"Apple iMac G4 'lamp' computer – boots to the desktop","N","Screen size (15/17/20in); power cord present.","Typical working G4 iMac $150–300 (collector model) – Terapeak query returned unrelated items, re-check",150,250,"eBay / FB local",0.136,45,"L"),
]
SKIP9=[
(5084217,"1946 Sugar Bowl program","Terapeak: one sale at $49 – too thin."),
(5089257,"Pyrex Fireside boxed sets","Terapeak median $33."),
(5084217,"Fujica AX-5 kit","Terapeak median $75 – too thin."),
(5082459,"Signed Michael Collins 'Carrying the Fire'","Company flagged signed books – expect full price; signature unverified."),
(5088765,"Inuit-style stone carvings","Can't tell authentic from tourist pieces in photos; check for igloo tag if attending anyway."),
]

FB="https://www.facebook.com/marketplace/item/%s/"
rows=[
[1,"Great Deal","Ekornes Stressless Consul (small) recliner + ottoman, black leather","Photo ID: Stressless badge and Consul base visible. Priced as a damaged chair ($50).","Brand yes, value no","FB Marketplace","Ekornes stressless small chair",FB%"28819451134345367","Mansfield","~40 min","Yes – seat lifts off the base (small furniture)",50,50,300,450,None,"FB local",0,15,None,None,None,None,None,None,"MEDIUM-HIGH","eBay sold Stressless chair + ottoman $800–1,900; local used small Consul sets $300–600.","Furniture – your $750 furniture rule would skip it, but it fits in an SUV and resells fast. Arm tear (disclosed); patching counts as repair, so sell as-is.","Message now; pay $50."],
[2,"Good Deal","Singer 221K Featherweight with case and pedal","Photo ID: title only says 'Vintage Singer'. Featherweight shape + UK motor tag = 221K.","No","OfferUp","Vintage Singer Manufacturing Co. Sewing Machine","https://offerup.com/item/detail/bda0b634-b9c1-3cdd-a1d3-11d6341393cf","Dallas","~40–50 min","Yes – carry case",200,160,340,500,None,"FB local / eBay",0,15,None,None,None,None,None,None,"MEDIUM","eBay sold 221/221K with case: $341–500.","Test that it runs and stitches; bobbin case must be present.","Offer $150–160. At full $200 it only just clears."],
[3,"Good Deal","Vintage fishing lot incl. boxed Creek Chub + Heddon lures, Penn Peer 209, fly reels, tin boxes","Photo ID: generic title; the boxed lures carry the value.","Partly","Craigslist","Large LOT Vintage Fishing Rods Reels Lures Tackle Boxes Gear","https://www.craigslist.org/view/d/fort-worth-large-lot-vintage-fishing/3Ny6BYLx4rtfYTPsHS1wja","Fort Worth","~25 min","Yes – rods on a diagonal",200,150,380,650,None,"eBay piece-out",0.136,45,None,None,None,None,None,None,"MEDIUM","eBay sold similar lots $258–431; boxed Creek Chub $30–80 each.","Hours to piece out. Skip the tackle-box hinge repair.","Offer $150 cash."],
[4,"Good Deal","Star Wars CCG (Decipher, 1995–98) – 5 boxes of original-trilogy Limited/Unlimited cards","Photo ID: black-border Decipher card backs and set symbols in the photos.","No – 'Star Wars cards'","OfferUp","Star Wars cards",'https://offerup.com/item/detail/8620a05e-1fe3-3e55-9292-91813516dbce',"Dallas","~45 min","Yes – 5 boxes",50,50,150,300,None,"eBay (bulk lots)",0.136,20,None,None,None,None,None,None,"MEDIUM","eBay sold: 3,000+ card bulk $128.50; 700+ Premiere $120; 500+ $120.","Card count unknown; rares may have been pulled. Check for binders of rares.","Ask for a count or photos of any binder; pay $50."],
[5,"Just Barely Over The Threshold","Lane walnut cube end table / storage cabinet, 26×25×22, serial 2084270","Photo ID: Lane stamp + serial inside the drawer.","Yes – titled 'Vintage Lane Cube End Table'","FB Marketplace","Vintage Lane Cube End Table",FB%"28460368930264731","Fort Worth","~25 min","Yes – 26×25×22 (small furniture)",75,75,200,300,None,"FB local (list as 'Lane MCM walnut')",0,0,None,None,None,None,None,None,"MEDIUM","eBay sold Lane walnut end tables $171–378; 'Lane walnut cube end table w/ storage 1975' $299.","Seller knows it's Lane; dropped $150→$75 after 2 weeks unsold locally. Only edge: listing it as mid-century walnut with the stamp photo. Weak price-drop case.","Offer $60–75."],
[6,"Good Deal","Eames fiberglass side shell chair, yellow","Photo ID: fiberglass shell + base type.","Yes – titled 'Vintage Herman Miller Eames Yellow Fiberglass Chair'","FB Marketplace","Vintage Herman Miller Eames Yellow Fiberglass Chair Mid Century",FB%"1574262364433783","Plano","~50 min","Yes – one chair",75,75,225,325,None,"FB local",0,0,None,None,None,None,None,None,"MEDIUM","Local and eBay Herman Miller fiberglass side shells $200–350.","Needs the Herman Miller/Zenith label under the seat, or it's a copy. Furniture (one chair).","Ask for a photo under the seat."],
[7,"Just Barely Over The Threshold","Eames rope-edge fiberglass armshell (1st-gen Zenith)","Photo ID: rolled 'rope' edge = 1950–51 Zenith production.","Yes – 'Early Herman Miller'; was $175, listed 4 weeks","FB Marketplace","Early Herman Miller Fiberglass Molded Chair",FB%"1404427988253058","Coppell","~35 min","Yes – one chair",100,100,225,300,None,"FB local / eBay",0,0,None,None,None,None,None,None,"MEDIUM-LOW","Rope-edge armshells $225–600 depending on base and cracks.","Check for cracks and the base type. Furniture (one chair).","Ask for photos of the shell mounts and underside."],
[8,"Just Barely Over The Threshold","Nikonos V underwater camera body","Model is in the title.","Yes – was $120, listed 13 weeks","FB Marketplace","Nikon Nikonos V 35mm Point & Shoot Film Camera",FB%"977121448457611","Fort Worth","~25 min","Yes",80,80,200,300,None,"eBay",0.136,15,None,None,None,None,None,None,"MEDIUM","eBay sold Nikonos V bodies $200–300.","Price drop is OK here: local FB has few divers; eBay reaches them nationally. Electronic shutter – test before paying.","Test the shutter and meter; pay $80."],
[9,"Just Barely Over The Threshold","Singer 15-91 sewing machine head (gear-driven, potted motor)","Photo ID: potted motor on the back and gingerbread decals = 15-91. Title just says 'Singer sewing machine'.","No","FB Marketplace","Singer sewing machine",FB%"26238600912504049","Frisco","~45 min","Yes – head only",20,20,70,130,None,"FB local",0,5,None,None,None,None,None,None,"MEDIUM-LOW","Singer 15-91 heads typically $70–150 locally; working with a cord more.","No cord; the seller used it as decor. Sell as 'untested, no cord' unless a cord is borrowed to test.","Pay $20; bring a spare Singer cord to test if you have one."],
[10,"Just Barely Over The Threshold","~75 lb loose Lego + 25 lb instructions and boxes (Ninjago, Star Wars, Atlantis, Super Heroes)","Photo ID: themes visible in the photos; minifigs present.","Partly","OfferUp","Lego lot",'https://offerup.com/item/detail/548482b2-ce76-3ae6-85d1-9693662769c3',"Keller","~5 min","Yes – several bins",200,200,375,525,None,"FB local / eBay by the pound",0,0,None,None,None,None,None,None,"MEDIUM","Bulk Lego $5–10/lb (Bamgoodbricks, Brickem 2026 guides); instructions/boxes add some.","Clears only at full value; buy-by-the-pound stores pay $3–5/lb. Sorting complete sets would raise it.","Offer $150–175. At $200 it barely clears."],
[11,"Lead – need price/photos","381 LP records, 'lots of big star names'","One photo of the stacks.","Yes, sort of","FB Marketplace","381 records",FB%"39425707730361878","Newark","~35 min","Yes – boxes",5,5,100,300,None,"FB local bulk / pick the keepers for eBay",0,0,None,None,None,None,None,None,"LOW","Bulk LPs roughly $0.50–2 each; better titles more.","Condition unknown (mold, warps). Only one photo.","Ask for photos of the spines and a few sleeves."],
[12,"Lead – need price/photos","Antique tombstone/cathedral-style tube radio (seller says it works)","Photo ID: 1930s tombstone cabinet; no model tag shown.","No","FB Marketplace","Antique radio",FB%"29256010280653061","Fort Worth","~25 min","Yes",50,50,100,250,None,"FB local",0,0,None,None,None,None,None,None,"LOW","Working tombstone sets $100–250; Philco/Zenith models more.","Model unknown. 'Works' is a claim, and running old radios without service can damage them.","Ask for a photo of the back label or dial."],
[13,"Lead – need price/photos","G.I. Joe ARAH lot incl. Defiant pieces, ~40 figures, ~20 vehicles","Photo ID from 15 photos. $1 placeholder price.","Partly","Craigslist","Vintage G.I. Joe & Power Ranger Figures & Vehicles","https://www.craigslist.org/view/d/dallas-vintage-gi-joe-power-ranger/xkFP7E19VchkSi7cffsbRg","Dallas","~45 min","Yes – totes",200,150,600,1000,None,"eBay piece-out",0.136,60,None,None,None,None,None,None,"LOW-MEDIUM","eBay sold: Defiant incomplete $520–700; ARAH lots $140–700.","Price unknown.","Ask the price. At ≤$200 it's Stop Everything."],
[14,"Lead – need price/photos","Southwest pottery group (~9 pcs): possible Pueblo, Tarahumara, carved gourd","Photo ID; title only 'Vintage Pottery'.","No","FB Marketplace","Vintage Pottery",FB%"28402405612731893","Dallas","~45 min","Yes – boxes",180,150,300,550,None,"eBay / Etsy",0.136,50,None,None,None,None,None,None,"LOW","Signed Pueblo $80–300 each; Tarahumara/Mata Ortiz-style $30–80.","Signatures unreadable; could be tourist ware.","Ask for close-ups of every signature."],
]
d2=[
["Singer 500A 'Rocketeer' in cabinet",FB%"29012100448478172",100,"Photo ID – 500A heads sell $150–350.","Seller says the machine needs work (repair = out of scope)."],
["Signed 'RML' sgraffito studio vase",FB%"27799394733071993",25,"Mid-century studio look.","Unknown initials; studio vases like this sell $20–60."],
["Coca-Cola neon clock, new in box",FB%"28741285958830395",10,"Watauga, 10 min away.","Current retail product (Trademark Gameroom), sells $40–60 used."],
["Seiko alarm-chronograph LCD watch",FB%"28394676910152738",90,"Vintage Seiko digital.","A914-type sell $35–100. Needs $180+ to clear at $90."],
["Pelikan M200 / Waterman / Mont Blanc pens","FB – DFW","100–200","Fountain pens.","Sellers name the brands and price at market; Mont Blanc needs authentication."],
["Decanter of vintage marbles (seller claims moss agates, Peltier, uranium)",FB%"28653741614257207",85,"Collector marbles can be $5–50 each.","Comps mixed and claims can't be confirmed from photos."],
["Antique sewing machines, 'not working', $50 each",FB%"28138258195867089",50,"Tan machines in cabinets.","Not working = repair."],
["'Navajo Two Gray Hills' rug 49x35","https://www.facebook.com/marketplace/item/38961281176789346/",200,"Real ones $1,000+.","Warp fringe – Mexican copy."],
["Antique J&P Coats floss cabinet","https://www.facebook.com/marketplace/item/28212130335095349/",195,"Store display.","Sold $200–325."],
["Tackle box of ~100 1970s–80s crankbaits","https://www.facebook.com/marketplace/item/38610383111909801/",100,"Big lot.","Common plastics $2–6 each."],
["Herend 'collection'","https://www.facebook.com/marketplace/item/28888684070723564/",125,"Herend $100–500 each.","Dealer, priced at retail."],
["IGC MS70 'gold rounds'","https://www.facebook.com/marketplace/item/28640044072362674/",65,"Graded gold.","1/500 oz each."],
["14K rope chains","https://www.facebook.com/marketplace/item/28144215138521392/",100,"Below melt if solid.","Gold plated."],
["Airline parlor guitar","FB – DFW","","Vintage Valco.","Loose bridge = repair."],
["Mexican silver bracelet","FB – DFW",150,"Taxco silver.","Sold $33–125."],
["Larry Mahan boots","FB – DFW",25,"Handmade western boots.","Sold $60–130; fails after fees."],
["'Swatch x Omega' MoonSwatch",'FB – DFW',50,"Retail $270.","Fakes at that price."],
["Lionel Penn Flyer / AHM Big Boy","FB – DFW","80–160","Trains.","Sold at or below asking."],
["Vought Zippos x4","FB – DFW",75,"Aviation Zippos.","Weak comps."],
["IKEA PS 2014 lamp / Blåsverk","FB – DFW","","Design-collector IKEA.","Comps too low."],
["Brutalist 'Kim' pendant; Tony Paul lamp; Beacon House lamp; Dazor lamp","FB – DFW","","Designer lighting.","Comps $10–70, or seller knows value."],
["Estate jewelry lots (Monet/Trifari, 5 lb bag, 800 silver bangle, silverplate)","FB – DFW","","Jewelry lots.","Costume-brand values; silver claims need testing."],
["Pioneer PL-740, flamenco LPs, Brelco telegraph, Gibson Vibrola, Pepsi rack, McMartin amp","CL/FB – DFW","","Various.","Sold comps under the needed profit."],
]

TRIPS={1: 'Mansfield', 2: 'Dallas', 3: 'Fort Worth', 4: 'Dallas', 5: 'Fort Worth', 6: 'Plano/Coppell/Frisco', 7: 'Plano/Coppell/Frisco', 8: 'Fort Worth', 9: 'Plano/Coppell/Frisco', 10: 'Keller/Newark', 11: 'Keller/Newark', 12: 'Fort Worth', 13: 'Dallas', 14: 'Dallas'}
LIVE={i:"LIVE 9/21 11pm" for i in range(1,15)}
for r in rows: r.extend([LIVE[r[0]],TRIPS[r[0]]])

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
SALES={**SALES,**SALES9}
idx8=json.load(open('/home/claude/sweep/esn_idx.json')); idx9=json.load(open('/home/claude/sweep/esn9_idx.json'))
F="Arial"; money='$#,##0;($#,##0);-'; thin=Side(style="thin",color="BFBFBF")
LINK=Font(name=F,size=10,color="0563C1",underline="single")
wb=Workbook()
# ================= Marketplace =================
ws=wb.active; ws.title="Marketplace listings"
H=["#","Priority","Status (9/22)","First found","What it is","Asking ($)","Offer / pay up to ($)","Resale low ($)","Resale high ($)","Resale mid ($)","Fee %","Ship/supplies ($)","Profit @ offer ($)","Needed profit ($)","Clears?","City","Drive (min)","Platform","Does the seller know?","Sold evidence","Check before paying","Link"]
ws.append(H)
status={1:"Live",2:"Live",3:"Live",4:"Live",5:"Live",6:"Live",7:"Live",8:"Live",9:"Live",10:"Live",11:"Live",12:"Live",13:"Live – price still not listed",14:"SOLD"}
drive={"Mansfield":40,"Dallas":45,"Fort Worth":25,"Plano":50,"Coppell":35,"Frisco":45,"Keller":5,"Newark":35}
M=[]
for r in rows:
    n,tier,what,how,aware,plat,title,link,city,dr,fit,listed,offer,lo,hi=r[:15]; fee,ship=r[17],r[18]; conf,ev,risk,nxt=r[24],r[25],r[26],r[27]
    M.append([tier,status[n],"9/21",what,listed,offer,lo,hi,fee,ship,city,drive.get(city,""),plat,aware,ev,risk+" "+nxt,link])
NEW=[
["Lead – need price/photos","Live","9/22","Box of mixed vintage & costume jewelry (bead strands that look like turquoise, pearls, bangles, brooches)",15,15,40,120,0.136,8,"Dallas area","","OfferUp","No – titled 'Jewelry box'","Costume lots $40–80; more if any sterling/turquoise is real","Ask for close-ups of clasps (925 stamps) and the turquoise pieces.","https://offerup.com/item/detail/4cc9930b-9efc-3292-9b98-63e4a973708f"],
["Lead – need price/photos","Live","9/22","Box of ~50+ LP records, titles not visible",20,20,50,200,0,0,"DFW","","OfferUp","No – titled 'Vinyl records'","Bulk LPs $0.50–2 each; classic rock/jazz more","Ask for photos of the spines.","https://offerup.com/item/detail/39c03455-82f7-3367-8b20-155c9c94aa24"],
["Lead – need price/photos","Live","9/22","~60 boxed men's fragrances (mostly Middle-Eastern 'inspired-by' brands)",35,35,150,400,0.136,40,"DFW","","OfferUp","No brands named","Full bottles $12–30 each on eBay/Mercari","Ask whether bottles are full/new or empty boxes.","https://offerup.com/item/detail/e50e1fc8-0343-3858-bfe6-fafbf1c0ea09"],
]
M+=NEW
order={"Great Deal":0,"Good Deal":1,"Just Barely Over The Threshold":2,"Lead – need price/photos":3}
M.sort(key=lambda r:(r[1]=="SOLD",order.get(r[0],9)))
for i,m in enumerate(M,1):
    tier,st,first,what,listed,offer,lo,hi,fee,ship,city,dr,plat,aware,ev,chk,link=m
    ws.append([i,tier,st,first,what,listed,offer,lo,hi,None,fee,ship,None,None,None,city,dr,plat,aware,ev,chk,link])
    r=i+1
    ws[f"J{r}"]=f"=AVERAGE(H{r}:I{r})"; ws[f"M{r}"]=f"=J{r}*(1-K{r})-L{r}-G{r}"; ws[f"N{r}"]=f"=MAX(50,G{r})"; ws[f"O{r}"]=f'=IF(M{r}>=N{r},"YES","no")'
    for c in "FGHIJLMN": ws[f"{c}{r}"].number_format=money
    ws[f"K{r}"].number_format='0.0%'
    c=ws[f"V{r}"]; c.hyperlink=c.value; c.value="Open listing"
NM=len(M)
# ================= Estate targets =================
w2=wb.create_sheet("Estate sale targets")
H2=["#","Sale","City","Dates","Drive (min)","First found","What it is","Captioned by company?","Check before paying","Sold evidence (eBay Terapeak, 12 mo)","Resale low ($)","Resale high ($)","Resale mid ($)","Fee %","Ship/supplies ($)","Net @ mid ($)","Pay up to ($)","Profit if bought at 'pay up to' ($)","Confidence","Photo","Sale page"]
w2.append(H2)
E=[(t,idx8,"9/21") for t in T]+[(t,idx9,"9/22") for t in T9]
E.sort(key=lambda e:(SALES[e[0][0]][5],e[0][0]))
for i,((sid,k,what,cap,chk,ev,lo,hi,ch,fee,ship,conf),ix,first) in enumerate(E,1):
    s=SALES[sid]; x=ix[k]; r=i+1
    w2.append([i,s[0],s[2],s[4],s[5],first,what,cap,chk,ev,lo,hi,None,fee,ship,None,None,None,conf,x['url'],x['saleurl']])
    w2[f"M{r}"]=f"=AVERAGE(K{r}:L{r})"; w2[f"P{r}"]=f"=M{r}*(1-N{r})-O{r}"; w2[f"Q{r}"]=f"=MIN(200,MAX(0,IF(P{r}>=100,P{r}/2,P{r}-50)))"; w2[f"R{r}"]=f"=P{r}-Q{r}"
    for c in "KLMOPQR": w2[f"{c}{r}"].number_format=money
    w2[f"N{r}"].number_format='0.0%'
    for c,l in (("T","Photo"),("U","Open sale")):
        cc=w2[f"{c}{r}"]; cc.hyperlink=cc.value; cc.value=l
NE=len(E)
# ================= Sale plan =================
W={"H":1.0,"M":0.7,"L":0.4}
def calc(t):
    sid,k,what,cap,chk,ev,lo,hi,ch,fee,ship,conf=t
    mid=(lo+hi)/2; net=mid*(1-fee)-ship; pay=min(200,max(0,net/2 if net>=100 else net-50)); return net-pay,pay,mid
w3=wb.create_sheet("Estate sale plan",0)
w3.append(["Rank","Sale","Company","City (zip)","Dates","Drive (min)","Targets","Total potential profit ($)","Best item","Best item profit ($)","Confidence-weighted score","Summary","Sale page"])
agg={}
for (t,ix,f) in E: agg.setdefault(t[0],[]).append((t,ix))
def score(sid): return sum(calc(t)[0]*W.get(str(t[11])[0],0.5) for t,_ in agg[sid])
rk=sorted(agg,key=lambda sid:-score(sid))
PLAN=[]
for n,sid in enumerate(rk,1):
    s=SALES[sid]; r=n+1; lst=agg[sid]
    prof=[(calc(t)[0],t) for t,_ in lst]; tot=sum(p for p,_ in prof); best=max(prof,key=lambda x:x[0])
    bname=best[1][2].split(' (')[0].split(' –')[0][:60]
    others=[t[2].split(' (')[0].split(' –')[0][:35] for p,t in sorted(prof,key=lambda x:-x[0])[1:4]]
    summ=f"{len(lst)} target{'s' if len(lst)>1 else ''}. Best bet: {bname} (~${best[0]:,.0f} profit if bought at the ceiling)."+(f" Also: {', '.join(others)}." if others else "")+(f" {s[6]}" if s[6] else "")
    w3.append([n,s[0],s[1],f"{s[2]} ({s[3]})",s[4],s[5],len(lst),round(tot),bname,round(best[0]),round(score(sid)),summ,lst[0][1][lst[0][0][1]]['saleurl']])
    for c in "HJK": w3[f"{c}{r}"].number_format=money
    cc=w3[f"M{r}"]; cc.hyperlink=cc.value; cc.value="Open sale"
    PLAN.append(dict(rank=n,sale=s[0],co=s[1],city=f"{s[2]} ({s[3]})",dates=s[4],drive=s[5],n=len(lst),total=round(tot),best=bname,bestp=round(best[0]),summary=summ,url=lst[0][1][lst[0][0][1]]['saleurl'],items=[dict(what=t[2],check=t[4],ev=t[5],mid=calc(t)[2],pay=calc(t)[1],profit=calc(t)[0],conf=t[11],first=f,photo=ix[t[1]]['url']) for (t,ix,f) in E if t[0]==sid]))
json.dump(PLAN,open('/home/claude/plan9.json','w'))
tr=len(rk)+3
for k,t in enumerate(["How to read this workbook:",
"• 'Estate sale plan' ranks this week's estate sales (Thu 9/24 – Sun 9/27) by potential profit, weighted by how confident the identification is (High 100%, Medium 70%, Low 40%). Total potential = profit on every target if bought at its ceiling. 'Estate sale targets' lists each item with a 'pay up to' ceiling.",
"• Estate sales don't post prices. 'Pay up to' = the most you can pay and still make profit ≥ the price ($50 floor), after eBay fees and shipping, using real eBay sold prices.",
"• Day 1 has the best selection; the last day is often 50% off. Items the company didn't caption are the ones they're least likely to have researched.",
"• 'Marketplace listings' = everything found on Facebook, OfferUp and Craigslist since Sept 21, with live status checked the morning of 9/22.",
"• Rule: profit ≥ max($50, price); price ≤ $200; fits in a car or ships. Local FB sales 0% fee; eBay 13.6%."]):
    w3[f"A{tr+k}"]=t
# ================= Passed =================
w4=wb.create_sheet("Checked & passed")
w4.append(["Found","Source","Item","Why it was passed"])
PASSED=[("9/21","FB Dallas","Southwest pottery group ($180)","Sold before we got to it."),
("9/22","CL Fort Worth","Star Wars figure lot with Landspeeder ($30)","Figures look modern; vintage Landspeeder sells ~$40 (Terapeak)."),
("9/22","OfferUp","Brass military bugle ($50)","Terapeak median $49."),
("9/21","FB","Hunter Zephair fan ($100)","Terapeak median $73."),("9/21","FB","Lot of 3 vintage Bach mouthpieces ($149)","~$75 each – too thin."),
("9/21","FB","1960s Airline acoustic guitar ($60)","Terapeak median $110."),("9/21","FB","Roland U-110 ($80)","Terapeak median $109."),
("9/21","FB","Olds trombone ($125)","Terapeak median $155 – too thin."),("9/21","FB","Schilke 51D mouthpiece ($70)","Median $65."),
("9/21","Mercari","3,367 items reviewed","Reseller marketplace – nothing underpriced."),
("9/21","HiBid","'Kelvin & Hughes' sextant ($6 bid)","Matches common reproduction.")]
for p in PASSED: w4.append(list(p))
for sid,item,why in SKIP+SKIP9:
    nm=SALES[sid][0]+" – "+SALES[sid][2] if sid in SALES else f"Estate sale {sid}"
    w4.append(["9/21–22","Estate: "+nm,item,why])
# ================= Buys & Sales =================
w5=wb.create_sheet("Buys & Sales")
w5.append(["Date bought","Item","From tab / row","Paid ($)","Est. resale mid ($)","Channel sold","Sold for ($)","Fees ($)","Ship/supplies ($)","Date sold","Days to sell","Actual profit ($)","Notes"])
for k in range(2,52):
    w5[f"K{k}"]=f'=IF(AND(A{k}<>"",J{k}<>""),J{k}-A{k},"")'; w5[f"L{k}"]=f'=IF(G{k}="","",G{k}-H{k}-I{k}-D{k})'
# ================= styling =================
for sh,wd in ((ws,[4,18,12,8,42,8,9,8,8,8,6,8,9,9,7,12,7,11,30,40,44,10]),(w2,[4,24,12,16,7,7,44,9,36,40,8,8,8,6,8,9,9,10,8,7,9]),(w3,[5,28,22,18,18,7,7,12,34,11,11,70,9]),(w4,[8,26,48,60]),(w5,[11,34,12,9,11,12,10,8,10,10,9,11,30])):
    for row in sh.iter_rows():
        for c in row:
            lk=c.hyperlink is not None
            c.font=LINK if lk else Font(name=F,size=10); c.alignment=Alignment(wrap_text=True,vertical="top")
    for c in sh[1]:
        c.font=Font(name=F,size=10,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="1F3864"); c.alignment=Alignment(wrap_text=True,vertical="center",horizontal="center")
    for k,wv in enumerate(wd,1): sh.column_dimensions[get_column_letter(k)].width=wv
    sh.freeze_panes="B2"; sh.row_dimensions[1].height=40
tierfill={"Stop Everything And Get This":"C00000","Great Deal":"70AD47","Good Deal":"A9D08E","Just Barely Over The Threshold":"FFE699","Lead – need price/photos":"D9D9D9"}
for i in range(2,NM+2):
    ws[f"B{i}"].fill=PatternFill("solid",fgColor=tierfill.get(ws[f"B{i}"].value,"FFFFFF")); ws.row_dimensions[i].height=70
    if ws[f"C{i}"].value=="SOLD":
        for col in range(1,len(H)+1): ws.cell(i,col).font=Font(name=F,size=10,color="999999",strike=True)
for i in range(2,NE+2):
    w2.row_dimensions[i].height=60; w2[f"Q{i}"].font=Font(name=F,size=10,bold=True); w2[f"Q{i}"].fill=PatternFill("solid",fgColor="E2EFDA")
    if w2[f"F{i}"].value=="9/22": w2[f"F{i}"].fill=PatternFill("solid",fgColor="FFF2CC")
w3[f"A{tr}"].font=Font(name=F,size=10,bold=True)
for i in range(2,len(rk)+2): w3.row_dimensions[i].height=70
ws.auto_filter.ref=f"A1:V{NM+1}"; w2.auto_filter.ref=f"A1:U{NE+1}"
out="/mnt/user-data/outputs/Refurbish-Master-List-2026-09-22.xlsx"; wb.save(out); print(NM,NE,len(rk))
