from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import glob
reg=glob.glob('/usr/share/fonts/**/DejaVuSans.ttf',recursive=True)[0]; bold=reg.replace('DejaVuSans.ttf','DejaVuSans-Bold.ttf')
pdfmetrics.registerFont(TTFont('D',reg)); pdfmetrics.registerFont(TTFont('DB',bold)); from reportlab.lib.fonts import addMapping; addMapping('D',0,0,'D'); addMapping('D',1,0,'DB'); addMapping('D',0,1,'D'); addMapping('D',1,1,'DB')
S=lambda n,**k:ParagraphStyle(n,fontName=k.pop('f','D'),**k)
H1=S('h1',f='DB',fontSize=20,leading=24,spaceAfter=4); SUB=S('s',fontSize=10.5,leading=14,textColor=colors.HexColor('#444444'))
H2=S('h2',f='DB',fontSize=14,leading=18,spaceBefore=10,spaceAfter=4); B=S('b',fontSize=10.5,leading=14)
T=S('t',f='DB',fontSize=12,leading=15); SM=S('sm',fontSize=9.5,leading=12.5)
FB="https://www.facebook.com/marketplace/item/%s/"
def L(u,txt="Open listing"): return f'<link href="{u}" color="#0563C1"><u>{txt}</u></link>'
tiers={"GET FIRST":"#C00000","GOOD":"#548235","WORTH IT":"#BF8F00","ASK FIRST":"#7F7F7F"}
items=[
("TOP PICK","Stressless recliner + ottoman (Ekornes)","$50","Mansfield","FB Marketplace",FB%"28819451134345367",
 "Stressless is a Norwegian recliner brand that sells new for $2,000+. This is the small Consul model in black leather, with its ottoman. There's a small tear on one arm, which is shown in the photos.",
 "Used Stressless chairs with ottomans have sold on eBay for $800–1,900. Small Consul sets usually go for $300–600 locally.",
 "Partly. The brand is in the title, but $50 is a damaged-chair price, not a Stressless price.",
 "The swivel base and ottoman are both included. The seat lifts off the base, so it fits in an SUV."),
("STRONG","Singer Featherweight 221K sewing machine","$200 (likely takes ~$160)","Dallas","OfferUp","https://offerup.com/item/detail/bda0b634-b9c1-3cdd-a1d3-11d6341393cf",
 "The Featherweight is the most collected Singer ever made. Quilters seek it out. This is the UK-built 221K version with its carry case and foot pedal.",
 "Recent eBay sales with the case: $341, $380, $395, $399, $400, $425 and $500.",
 "Probably not. The listing just says 'Vintage Singer Manufacturing Co. Sewing Machine' and never uses the word Featherweight.",
 "Whether it runs and stitches, and whether the bobbin case is inside."),
("STRONG","Vintage fishing lot with boxed Creek Chub and Heddon lures","$200 (likely takes ~$150)","Fort Worth","Craigslist","https://www.craigslist.org/view/d/fort-worth-large-lot-vintage-fishing/3Ny6BYLx4rtfYTPsHS1wja",
 "A big mixed lot of rods, reels, lures and old tackle boxes. Most of the value is in the older lures still in their original boxes, plus a Penn reel.",
 "Similar lots have sold on eBay for $258–431. Boxed Creek Chub lures alone sell for $30–80 each.",
 "Partly. The seller mentions it's good for reselling but doesn't call out the boxed lures.",
 "Whether the boxed lures from the photos are still in the lot. Selling it piece by piece takes some time."),
("STRONG","Star Wars trading card game cards (Decipher, 1995–98), 5 boxes","$50","Dallas","OfferUp","https://offerup.com/item/detail/8620a05e-1fe3-3e55-9292-91813516dbce",
 "Decipher made the original Star Wars card game in the late '90s. The photos show five boxes of original-trilogy cards, which have a steady collector market.",
 "Bulk lots on eBay: 3,000+ cards sold for $128.50; 700+ Premiere cards for $120; 500+ cards for $120. Rare cards sell separately for more.",
 "No. It's listed as 'Star Wars cards' with no mention of Decipher or the game.",
 "Roughly how many cards there are, and whether any rare cards were pulled out."),
("BORDERLINE","Lane mid-century walnut cube end table with storage","$75 (was $150)","Fort Worth","FB Marketplace",FB%"28460368930264731",
 "Lane made popular mid-century furniture. The Lane stamp and serial number are inside the drawer, and it's small: 26 × 25 × 22 inches.",
 "Lane walnut end tables have sold on eBay for $171–378. A 1975 Lane walnut cube end table with storage sold for $299.",
 "Yes. It's titled 'Vintage Lane Cube End Table'. It dropped from $150 to $75 after two weeks, so local demand at that price looks soft.",
 "The stamp inside the drawer, water rings on top, and any wobble."),
("STRONG","Eames fiberglass side chair, yellow","$75","Plano","FB Marketplace",FB%"1574262364433783",
 "Charles and Ray Eames designed these fiberglass shell chairs for Herman Miller. Real ones are valuable, but copies are everywhere.",
 "Authentic Herman Miller fiberglass side shells usually sell for $200–350.",
 "Yes. It's titled 'Vintage Herman Miller Eames Yellow Fiberglass Chair', but $75 is still well under what authentic ones sell for.",
 "The deciding check: a Herman Miller or Zenith label or stamp under the seat. Without one, it's probably a copy. Also look for cracks."),
("GOOD","Eames 'rope edge' fiberglass armchair (1950s)","$100","Coppell","FB Marketplace",FB%"1404427988253058",
 "The rolled 'rope' edge marks the earliest production run (about 1950–51), made by Zenith. It's the most collectible version of the chair.",
 "Rope-edge armshells sell for $225–600 depending on condition and base.",
 "Mostly. It's titled 'Early Herman Miller Fiberglass Molded Chair', and the price was cut from $175 after four weeks. The rope edge itself isn't mentioned.",
 "Cracks around the mounting points under the seat, and what kind of base it's on."),
("GOOD","Nikonos V underwater camera","$80","Fort Worth","FB Marketplace",FB%"977121448457611",
 "A Nikon film camera built for diving. It's still popular with divers and film photographers.",
 "Camera bodies have sold on eBay for $200–300.",
 "Yes, the model is in the title. It dropped from $120 after 13 weeks, likely because few local buyers want an underwater film camera. eBay reaches divers nationally.",
 "The shutter fires and the light meter works (it needs batteries). No corrosion."),
("GOOD","Singer 15-91 sewing machine (head only, no cord)","$20","Frisco","FB Marketplace",FB%"26238600912504049",
 "A heavy-duty 1950s Singer, recognizable by the bulge of the motor on the back and the gold scroll decals. People still use these for sewing leather and heavy fabric.",
 "Heads typically sell locally for $70–150, and more when tested with a cord.",
 "No. It's titled 'Singer sewing machine', and the seller says they used it as decor.",
 "The handwheel should turn smoothly by hand. It has no cord, so it's untested."),
("BORDERLINE","About 75 lb of Lego, plus 25 lb of instructions and boxes","$200","Keller","OfferUp","https://offerup.com/item/detail/548482b2-ce76-3ae6-85d1-9693662769c3",
 "A big bulk lot with Ninjago, Star Wars, Atlantis and Super Heroes pieces, minifigures, and the original instructions and boxes.",
 "Bulk Lego sells for about $5–10 per pound (2026 price guides). Lego resale stores pay about $3–5 per pound.",
 "Mostly. The price is close to fair bulk value, so it only pays off below $200 or if complete sets can be rebuilt.",
 "That it's real Lego (LEGO is stamped on the studs), and how many minifigures there are."),
]
leads=[
("381 LP records","$5","Newark","FB Marketplace",FB%"39425707730361878","Bulk vinyl typically goes for $0.50–2 a record, more for good titles. There's only one photo, so condition is unknown.","Photos of the spines and a few covers; any mold or warping."),
("Antique tube radio (1930s 'tombstone' style)","$50","Fort Worth","FB Marketplace",FB%"29256010280653061","Working sets like this sell for $100–250, more for Philco or Zenith. No brand or model is shown.","A photo of the back panel or label."),
("1980s G.I. Joe lot with vehicles","Price not listed","Dallas","Craigslist","https://www.craigslist.org/view/d/dallas-vintage-gi-joe-power-ranger/xkFP7E19VchkSi7cffsbRg","It includes pieces of the Defiant space shuttle set, which alone has sold for $520–700 incomplete. Mixed lots sell for $140–700. The seller names the Defiant.","The asking price. At $200 or less it would be the best find on this list."),
("Southwest pottery group (~9 pieces)","$180","Dallas","FB Marketplace",FB%"28402405612731893","It may include Pueblo pieces, which sell for $80–300 each when signed, but it could be tourist pottery. The title only says 'Vintage Pottery'.","Close-ups of the signatures on the bottoms."),
]
tiers={"TOP PICK":"#C00000","STRONG":"#548235","GOOD":"#2F5597","BORDERLINE":"#BF8F00"}
_o={'TOP PICK':0,'STRONG':1,'GOOD':2,'BORDERLINE':3}; items.sort(key=lambda x:_o[x[0]])
doc=SimpleDocTemplate('/mnt/user-data/outputs/DFW-Resale-Finds.pdf',pagesize=letter,leftMargin=40,rightMargin=40,topMargin=36,bottomMargin=36,title="DFW Resale Finds")
st=[Paragraph("Underpriced finds around Dallas–Fort Worth",H1),
Paragraph("September 21, 2026 · every listing was confirmed still up that night",SUB),Spacer(1,6),
Paragraph("These are secondhand listings on Facebook Marketplace, OfferUp and Craigslist that look underpriced. In most cases the photos show a brand or model the listing doesn't mention. Each entry covers what the item is, what similar items have sold for, whether the seller seems to know what they have, and what's worth checking in person. Prices are the asking prices on the date above. Listings sell fast, so some may be gone.",B),
Spacer(1,4),
Paragraph("<b>Ratings</b> reflect how much room there is between the asking price and recent sale prices, and how sure the identification is: <font color='#C00000'><b>Top pick</b></font> › <font color='#548235'><b>Strong</b></font> › <font color='#2F5597'><b>Good</b></font> › <font color='#BF8F00'><b>Borderline</b></font>. Sold prices come from eBay sold listings and 2026 price guides.",SM),
Paragraph("The finds",H2)]
for i,(tier,what,ask,city,plat,url,ctx,sold,aware,check) in enumerate(items,1):
    rows=[[Paragraph(f'<font color="{tiers[tier]}"><b>{tier}</b></font> &nbsp; {what}',T)],
          [Paragraph(f"<b>{ask}</b> &nbsp;·&nbsp; {city} &nbsp;·&nbsp; {plat} &nbsp;·&nbsp; {L(url,'View listing')}",B)],
          [Paragraph(f"{ctx}",SM)],
          [Paragraph(f"<b>Selling elsewhere:</b> {sold}",SM)],
          [Paragraph(f"<b>Does the seller know?</b> {aware}",SM)],
          [Paragraph(f"<b>Worth checking:</b> {check}",SM)]]
    t=Table(rows,colWidths=[532]); t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.HexColor(tiers[tier])),('LINEBEFORE',(0,0),(0,-1),5,colors.HexColor(tiers[tier])),
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#F2F2F2')),('LEFTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
    st+= [KeepTogether([t]),Spacer(1,7)]
st.append(Paragraph("Promising, but missing a key detail",H2))
st.append(Paragraph("Each of these could be good, but one thing needs to come from the seller first.",SM)); st.append(Spacer(1,4))
for what,ask,city,plat,url,ctx,need in leads:
    t=Table([[Paragraph(f"<b>{what}</b> &nbsp;·&nbsp; {ask} &nbsp;·&nbsp; {city} &nbsp;·&nbsp; {plat} &nbsp;·&nbsp; {L(url,'View listing')}",B)],[Paragraph(ctx,SM)],[Paragraph(f"<b>Missing:</b> {need}",SM)]],colWidths=[532])
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.75,colors.HexColor('#7F7F7F')),('LEFTPADDING',(0,0),(-1,-1),9)]))
    st+=[KeepTogether([t]),Spacer(1,6)]
st+=[Spacer(1,6),Paragraph("Sale prices are recent examples, not guarantees. Condition in person can change the value either way.",SUB)]
doc.build(st)
