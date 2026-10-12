from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
F="Arial"
TIERS=["Stop Everything And Get This","Great Deal","Good Deal","Just Barely Over The Threshold","Lead – need price/photos"]
wb=Workbook(); ws=wb.active; ws.title="Deals"
hdr=["#","Priority","What it actually is","How identified","Seller knew?","Platform","Seller's title","Link","Location","Drive from Keller","Fits in a car?","Listed ($)","Offer ($)","Resale low ($)","Resale high ($)","Resale mid ($)","Sell channel","Fee %","Ship/supplies ($)","Net @ mid ($)","Profit @ offer ($)","Needed profit ($)","Clears @ offer?","Profit @ full price ($)","Clears @ full price?","Confidence","Price evidence","Risks / condition","Next step","Still live?","Trip"]
# W=needed X=clears@offer Y=profit@listed Z=clears@listed
# L=Listed M=Offer N=low O=high P=mid Q=chan R=fee S=costs T=net U=profit V=clears
# ---- replace these lists each run ----
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
# ------------------------------------------
ws.append(hdr)
for r in rows: ws.append(r)
n=len(rows)
for i in range(2,n+2):
    ws[f"P{i}"]=f"=AVERAGE(N{i}:O{i})"
    ws[f"T{i}"]=f"=P{i}*(1-R{i})-S{i}"
    ws[f"U{i}"]=f"=T{i}-M{i}"
    ws[f"V{i}"]=f"=MAX(50,M{i})"
    ws[f"W{i}"]=f'=IF(U{i}>=V{i},"YES","no")'
    ws[f"X{i}"]=f"=T{i}-L{i}"
    ws[f"Y{i}"]=f'=IF(X{i}>=MAX(50,L{i}),"YES","no")'
tr=n+3
ws[f"A{tr}"]="Rows clearing the rule @ offer (leads use placeholder prices)"; ws[f"L{tr}"]=f'=COUNTIF(W2:W{n+1},"YES")'
ws[f"A{tr+1}"]="Total cash to buy everything @ offer"; ws[f"L{tr+1}"]=f"=SUM(M2:M{n+1})"
notes=["How to read this sheet:",
"• Rule (set Sept 21): profit must be at least what you pay, with a $50 floor – profit ≥ MAX($50, price). Price ≤ $200. Seller doesn't know the value. Fits in a car or ships.",
"• Furniture (updated Sept 21): small pieces that fit in the car are OK if profit ≥ 2× price and they get relisted within a week. Bigger furniture still needs $750+ profit.",
"• Trips: group pickups by the Trip column. A trip should add up to at least $150 profit (see the Trips tab); a lone low-profit item isn't worth its own drive.",
"• Tiers scale with price (profit ÷ needed profit): Stop Everything ≥ 4× and ≥ $300 with high confidence; Great ≥ 2.5×; Good ≥ 1.5×; Just Barely 1–1.5× or low confidence/far. Lead = one fact missing.",
"• Blue numbers are inputs. Profit @ offer = resale mid × (1 − fee) − shipping/supplies − offer. Local FB sales are 0% fee; eBay is 13.6%.",
"• Gas and time aren't counted. Far drives are noted in the 'Drive from Keller' column.",
"• Photo-first: every row was identified from the photos, not the title. Checked Sept 21, 2026. Listings move fast, so confirm before driving."]
for k,t in enumerate(notes): ws[f"A{tr+3+k}"]=t

w2=wb.create_sheet("Checked & passed")
h2=["Item","Link","Listed ($)","Why it looked good","Why it failed"]
w2.append(h2)
for r in d2: w2.append(r)

thin=Side(style="thin",color="BFBFBF"); blue=Font(name=F,size=10,color="0000FF"); money='$#,##0;($#,##0);-'
for sh in (ws,w2):
    for row in sh.iter_rows():
        for c in row: c.font=Font(name=F,size=10); c.alignment=Alignment(wrap_text=True,vertical="top")
    for c in sh[1]:
        c.font=Font(name=F,size=10,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="1F3864")
        c.alignment=Alignment(wrap_text=True,vertical="center",horizontal="center")
    sh.row_dimensions[1].height=42; sh.freeze_panes="C2"
tierfill={"Stop Everything And Get This":"C00000","Great Deal":"70AD47","Good Deal":"A9D08E","Just Barely Over The Threshold":"FFE699","Lead – need price/photos":"D9D9D9"}
for i in range(2,n+2):
    ws.row_dimensions[i].height=110
    for col in range(1,len(hdr)+1): ws.cell(i,col).border=Border(top=thin,bottom=thin,left=thin,right=thin)
    for col in "LMNORS": ws[f"{col}{i}"].font=blue
    for col in "LMNOPSTUVX": ws[f"{col}{i}"].number_format=money
    ws[f"R{i}"].number_format='0.0%'
    link=ws[f"H{i}"].value; ws[f"H{i}"].hyperlink=link; ws[f"H{i}"].value="Open listing"
    ws[f"H{i}"].font=Font(name=F,size=10,color="0563C1",underline="single")
    t=ws[f"B{i}"].value; ws[f"B{i}"].fill=PatternFill("solid",fgColor=tierfill[t])
    ws[f"B{i}"].font=Font(name=F,size=10,bold=True,color="FFFFFF" if t=="Stop Everything And Get This" else "000000")
    for col in "UWXY": ws[f"{col}{i}"].font=Font(name=F,size=10,bold=True)
dv=DataValidation(type="list",formula1='"'+",".join(TIERS)+'"',allow_blank=True); ws.add_data_validation(dv); dv.add(f"B2:B{n+50}")
for r in (tr,tr+1,tr+3): ws[f"A{r}"].font=Font(name=F,size=10,bold=True)
ws[f"L{tr+1}"].number_format=money
widths=[4,18,34,34,14,13,24,11,12,10,18,9,9,9,9,9,18,7,9,9,10,9,9,10,9,12,40,40,28,14,16]
for k,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(k)].width=w
ws.auto_filter.ref=f"A1:{get_column_letter(len(hdr))}{n+1}"
ws.conditional_formatting.add(f"W2:Y{n+1}",CellIsRule(operator="equal",formula=['"YES"'],fill=PatternFill("solid",fgColor="E2EFDA")))
for i in range(2,len(d2)+2):
    w2.row_dimensions[i].height=45
    v=w2[f"B{i}"].value
    if v and str(v).startswith("http"): w2[f"B{i}"].hyperlink=v; w2[f"B{i}"].value="Open listing"; w2[f"B{i}"].font=Font(name=F,size=10,color="0563C1",underline="single")
for k,w in enumerate([36,16,10,34,60],1): w2.column_dimensions[get_column_letter(k)].width=w
w2.freeze_panes="B2"

# ---- Trips tab ----
w3=wb.create_sheet("Trips")
w3.append(["Trip","Items","Profit @ offer ($)","Cash needed ($)","Worth the drive? (≥ $150)"])
tl=sorted(set(r[-1] for r in rows),key=lambda t:[r[-1] for r in rows].index(t))
for k,t in enumerate(tl,2):
    w3.append([t,f'=COUNTIF(Deals!AE2:AE{n+1},A{k})',f'=SUMIF(Deals!AE2:AE{n+1},A{k},Deals!U2:U{n+1})',f'=SUMIF(Deals!AE2:AE{n+1},A{k},Deals!M2:M{n+1})',f'=IF(C{k}>=150,"YES","combine or skip")'])
    for c in "CD": w3[f"{c}{k}"].number_format=money
w3.append([]); w3.append(["Leads use placeholder prices, so trips containing leads are optimistic until the seller answers."])
# ---- Buys & Sales tab ----
w4=wb.create_sheet("Buys & Sales")
w4.append(["Date bought","Item","Deal #","Paid ($)","Est. resale mid ($)","Channel sold","Listed at ($)","Sold for ($)","Fees ($)","Ship/supplies ($)","Date sold","Days to sell","Actual profit ($)","Estimate error ($)","Notes"])
for k in range(2,52):
    w4[f"L{k}"]=f'=IF(AND(A{k}<>"",K{k}<>""),K{k}-A{k},"")'
    w4[f"M{k}"]=f'=IF(H{k}="","",H{k}-I{k}-J{k}-D{k})'
    w4[f"N{k}"]=f'=IF(OR(H{k}="",E{k}=""),"",H{k}-E{k})'
    w4[f"E{k}"]=f'=IF(C{k}="","",INDEX(Deals!P$2:P${n+1},MATCH(C{k},Deals!A$2:A${n+1},0)))'
    for c in "DEGHIJMN": w4[f"{c}{k}"].number_format=money
    for c in "AK": w4[f"{c}{k}"].number_format="mm/dd/yy"
w4["P1"]="How to use: log every buy the day you buy it (enter the Deal # to pull the estimate). Fill the sale columns when it sells. 'Estimate error' = sold price minus our resale estimate – negative means we guessed high."
for sh,wd in ((w3,[24,8,16,14,22]),(w4,[11,34,7,9,12,14,11,11,9,12,11,10,13,13,30])):
    for k,wv in enumerate(wd,1): sh.column_dimensions[get_column_letter(k)].width=wv
    for c in sh[1]:
        c.font=Font(name=F,size=10,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="1F3864"); c.alignment=Alignment(wrap_text=True,vertical="center")
    sh.freeze_panes="A2"
w4["P1"].font=Font(name=F,size=10,italic=True); w4["P1"].fill=PatternFill(fill_type=None); w4.column_dimensions["P"].width=60; w4["P1"].alignment=Alignment(wrap_text=True)

# ---- Estate sales this week ----
w5=wb.create_sheet("Estate sales this week")
w5.append(["Sale","Dates","City","Company","Link","Spotted in the photos (prices not posted – check at the sale)","Worth it if priced under","Notes"])
ES=[
["Granny Chic in Aledo","Thu 9/24 – Sat 9/26","Aledo","Family Legacy Estate Sales","https://www.estatesales.net/TX/Aledo/76008/5084871","1977 Star Wars 'May the Force Be With You' raglan tee (poster art); 1970s Thermos 'Road Runner' metal lunchbox","Tee < $60; lunchbox < $25","Original 1977 Star Wars tees sell ~$100–300; check the tag (Factors Etc. = original). Neither item is captioned."],
["Terrific Time Capsule MCM Items","Thu 9/24 – Sat 9/26","Duncanville","Kitchens To Closets","https://www.estatesales.net/TX/Duncanville/75116/5078532","1974 Aladdin Evel Knievel metal lunchbox; 1976 Bicentennial flag lunchbox; boxed Barbies, Betty Boop","Evel Knievel < $40","Evel Knievel boxes sell ~$60–200 by condition. Cash/Venmo/Zelle only."],
["Anchors, Art & Antiques – Navy, Coast Guard & Vintage","Thu 9/24 – Sun 9/27","Arlington","Fantastic Finds Estate Sales","https://www.estatesales.net/TX/Arlington/76013/5074425","Uncaptioned Dutch-style art pottery vase (possible Gouda); military caps; 1920s banjo-ukulele","Vase < $40 if bottom says Gouda/Holland","Company captioned the military items (they know those). Check the vase bottom."],
["Navigate your way – Air, Land or Sea","Fri 9/25 – Sun 9/27","Weatherford","And Again Estate Sales","https://www.estatesales.net/TX/Weatherford/76087/5072409","1970s National Airlines posters; Soviet medals; oil cans; Singer 99 in bentwood case","Posters < $30 each","Near work (Weatherford). Aviation/advertising collection; Texaco/Phillips signs look like reproductions."],
["Out of The Attic","Fri 9/25 – Sun 9/27","Dallas (75231)","Out Of The Attic","https://www.estatesales.net/TX/Dallas/75231/5069514","Pen collector's estate: Parker Duofold store display clock, large Waterman store display, hundreds of pen items; antique toys","Only if priced low – the company captioned these","Seller knows (captioned). Last-day 50% off could still work."],
["Annabelle's Treasures (warehouse)","Fri 9/25 – Sat 9/26","Keller","Annabelle's Treasures","https://www.estatesales.net/TX/Keller/76244/5081160","Mixed decor/furniture","–","10 minutes away; low effort to look."],
]
for r in ES: w5.append(r)
for k in range(2,len(ES)+2):
    c=w5[f"E{k}"]; c.hyperlink=c.value; c.value="Open sale"; c.font=Font(name=F,size=10,color="0563C1",underline="single")
    w5.row_dimensions[k].height=60
    for col in "ABCDFGH": w5[f"{col}{k}"].alignment=Alignment(wrap_text=True,vertical="top"); w5[f"{col}{k}"].font=Font(name=F,size=10)
for k,wv in enumerate([28,18,12,20,10,48,22,44],1): w5.column_dimensions[get_column_letter(k)].width=wv
for c in w5[1]: c.font=Font(name=F,size=10,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="1F3864"); c.alignment=Alignment(wrap_text=True,vertical="center")
w5.freeze_panes="A2"
import os; os.makedirs("/home/claude/out",exist_ok=True); wb.save("/home/claude/out/Refurbish-Sweep-2026-09-21-v5.xlsx")
