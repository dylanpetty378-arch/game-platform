# Estate-sale readout workbook. Replace SALES / T / SKIP (and the garage list G) each week.
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


import json,sys

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
idx=json.load(open('/home/claude/sweep/esn_idx.json'))
F="Arial"; money='$#,##0;($#,##0);-'; thin=Side(style="thin",color="BFBFBF")
wb=Workbook()
# ---------- Targets ----------
ws=wb.active; ws.title="Targets"
hdr=["#","Sale","City","Dates","What it is","Photo","Company captioned it?","Check before paying","Sold evidence (eBay Terapeak, last 12 mo unless noted)","Resale low ($)","Resale high ($)","Resale mid ($)","Sell channel","Fee %","Ship/supplies ($)","Net @ mid ($)","Pay up to ($)","Profit if bought at 'pay up to' ($)","Confidence","Sale link"]
ws.append(hdr)
rows=sorted(T,key=lambda t:(SALES[t[0]][5],t[0]))
for n,(sid,k,what,cap,chk,ev,lo,hi,ch,fee,ship,conf) in enumerate(rows,1):
    s=SALES[sid]; x=idx[k]
    ws.append([n,s[0],s[2],s[4],what,x['url'],cap,chk,ev,lo,hi,None,ch,fee,ship,None,None,None,conf,x['saleurl']])
N=len(rows)
for i in range(2,N+2):
    ws[f"L{i}"]=f"=AVERAGE(J{i}:K{i})"
    ws[f"P{i}"]=f"=L{i}*(1-N{i})-O{i}"
    ws[f"Q{i}"]=f"=MAX(0,IF(P{i}>=100,P{i}/2,P{i}-50))"   # profit >= max($50, price)
    ws[f"R{i}"]=f"=P{i}-Q{i}"
    for c in "JKLOPQR": ws[f"{c}{i}"].number_format=money
    ws[f"N{i}"].number_format='0.0%'
    for c,label in (("F","Photo"),("T","Open sale")):
        cell=ws[f"{c}{i}"]; cell.hyperlink=cell.value; cell.value=label; cell.font=Font(name=F,size=10,color="0563C1",underline="single")
# ---------- Sale plan ----------
w2=wb.create_sheet("Sale plan",0)
w2.append(["Rank","Sale","Company","City (zip)","Dates","Drive from Keller (min)","Targets","Combined resale mid ($)","Combined 'pay up to' ($)","Top targets","Notes","Sale link"])
by={}
for r in range(2,N+2):
    pass
agg={}
for n,(sid,k,what,*_r) in enumerate(rows,1):
    agg.setdefault(sid,[]).append((n+1,what))
order=sorted(agg,key=lambda sid:-sum((t[6]+t[7])/2 for t in T if t[0]==sid))
for rank,sid in enumerate(order,1):
    s=SALES[sid]; lst=agg[sid]; r=rank+1
    w2.append([rank,s[0],s[1],f"{s[2]} ({s[3]})",s[4],s[5],len(lst),
      f'=SUMIF(Targets!$B$2:$B${N+1},B{r},Targets!$L$2:$L${N+1})',f'=SUMIF(Targets!$B$2:$B${N+1},B{r},Targets!$Q$2:$Q${N+1})',
      "; ".join(w.split(' (')[0].split(' –')[0][:45] for _,w in lst[:4]),s[6],[x for x in idx if x['sale']==sid][0]['saleurl']])
    for c in "HI": w2[f"{c}{r}"].number_format=money
    c=w2[f"L{r}"]; c.hyperlink=c.value; c.value="Open sale"; c.font=Font(name=F,size=10,color="0563C1",underline="single")
tr=len(order)+3
tips=["How to use this readout:",
"• Prices at estate sales aren't posted online. 'Pay up to' is the most you can pay and still make profit ≥ the price (with a $50 floor), based on the eBay sold prices in the Targets tab.",
"• Day 1 (usually Thu/Fri morning) has the best selection; the last day is often 50% off. Uncaptioned items (all of these) are the ones the company is least likely to have researched.",
"• Every target was spotted in the company's own photos (10,191 photos across 57 sales were reviewed). Photo links open the exact picture.",
"• Weatherford (2 sales) is near Dylan's work; Arlington, Bedford and Keller-area sales are closest to home.",
"• Sell channel and fee: FB local 0%, eBay 13.6%. Shipping/supplies is a rough allowance."]
for k,t in enumerate(tips): w2[f"A{tr+k}"]=t
# ---------- Skipped ----------
w3=wb.create_sheet("Seen & skipped")
w3.append(["Sale","Item","Why skipped"])
for sid,item,why in SKIP:
    XN={5085372:"LANN Estate Sales – Plano",5069514:"Out of The Attic – Dallas 75231",5084445:"Fabulous art and antiques – Plano"}
    w3.append([ SALES[sid][0]+" – "+SALES[sid][2] if sid in SALES else XN.get(sid,str(sid)), item, why])
# ---------- Garage sales ----------
w4=wb.create_sheet("Garage sales (gsalr)")
w4.append(["Dates","City","Title","Why it's listed","Link"])
G=[("Fri 9/25 – Sat 9/26","Fort Worth","Garage Sale + Comics","'Tons of comic books… vintage to new, graded and signed' – worth an early look","https://gsalr.com/garage-sale-comics-fort-worth-tx-38931273.html"),
("Fri 9/25 – Sat 9/26","Cross Roads","Retiring teacher's sale","Toys, books, games from a long career – low-info seller","https://gsalr.com/sept-garage-sale-2026-cross-roads-tx-38932113.html"),
("Thu 9/24 – Sat 9/26","Watauga","Multiple neighbors","10 min from Keller; toys and household","https://gsalr.com/multiple-sales-watauga-tx-38931099.html"),
("Fri 10/2 – Sat 10/3","Haslet","'HUGE variety… might as well be an estate sale'","Close to Keller; 9 photos","https://gsalr.com/garage-sale-huge-variety-haslet-tx-38922713.html"),
("Sat 10/3","Plano","Plano Antique Mall parking-lot sale","Many vendors at once; prices vary","https://gsalr.com/fall-2026-plano-antique-plano-tx-38931393.html"),
("Thu 9/24 – Fri 9/25","Fort Worth","Garage sale (29 photos)","Reviewed: costume jewelry lot, Coca-Cola collectibles, art-glass vases – nothing high-value seen","https://gsalr.com/garage-sale-fort-worth-tx-38931593.html")]
for g in G: w4.append(list(g))
for i in range(2,len(G)+2):
    c=w4[f"E{i}"]; c.hyperlink=c.value; c.value="Open"; c.font=Font(name=F,size=10,color="0563C1",underline="single")
# ---------- styling ----------
for sh,widths in ((w2,[6,30,24,18,18,10,8,12,12,48,40,10]),(ws,[4,26,12,17,46,7,10,34,44,9,9,9,16,7,9,9,10,11,9,9]),(w3,[30,44,60]),(w4,[18,14,34,56,8])):
    for row in sh.iter_rows():
        for c in row:
            if c.font.color is None or c.font.color.rgb!="FF0563C1": c.font=Font(name=F,size=10)
            c.alignment=Alignment(wrap_text=True,vertical="top")
    for c in sh[1]:
        c.font=Font(name=F,size=10,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="1F3864"); c.alignment=Alignment(wrap_text=True,vertical="center",horizontal="center")
    for k,wv in enumerate(widths,1): sh.column_dimensions[get_column_letter(k)].width=wv
    sh.freeze_panes="C2" if sh is ws else "B2"; sh.row_dimensions[1].height=40
for i in range(2,N+2):
    ws.row_dimensions[i].height=75
    for c in "JKNO": ws[f"{c}{i}"].font=Font(name=F,size=10,color="0000FF")
    ws[f"Q{i}"].font=Font(name=F,size=10,bold=True); ws[f"Q{i}"].fill=PatternFill("solid",fgColor="E2EFDA")
    for col in range(1,len(hdr)+1): ws.cell(i,col).border=Border(top=thin,bottom=thin,left=thin,right=thin)
for i in range(2,len(order)+2): w2.row_dimensions[i].height=60
w2[f"A{tr}"].font=Font(name=F,size=10,bold=True)
ws.auto_filter.ref=f"A1:T{N+1}"
wb.save("/mnt/user-data/outputs/Estate-Sales-Readout-2026-09-24.xlsx"); print(N,len(order))
