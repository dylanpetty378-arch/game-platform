import os,glob,qrcode
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, Image, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
F=glob.glob('/usr/share/fonts/**/DejaVuSans.ttf',recursive=True)[0]
pdfmetrics.registerFont(TTFont('D',F)); pdfmetrics.registerFont(TTFont('DB',F.replace('DejaVuSans.ttf','DejaVuSans-Bold.ttf'))); pdfmetrics.registerFont(TTFont('DI',F.replace('DejaVuSans.ttf','DejaVuSans-Oblique.ttf')))
addMapping('D',0,0,'D'); addMapping('D',1,0,'DB'); addMapping('D',0,1,'DI'); addMapping('D',1,1,'DB')
INK=colors.HexColor('#111111'); BODY=colors.HexColor('#2E2E2E'); MUT=colors.HexColor('#6E6E6E'); HAIR=colors.HexColor('#D8D8D8'); BAND=colors.HexColor('#F4F6F8'); NAVY=colors.HexColor('#14487A'); RUST=colors.HexColor('#A23B1E')
S=lambda n,**k:ParagraphStyle(n,fontName=k.pop('f','D'),textColor=k.pop('textColor',BODY),**k)
TITLE=S('t',f='DB',fontSize=21,leading=24,textColor=INK); KICKER=S('k',f='DB',fontSize=8.5,leading=11,textColor=NAVY); LEDE=S('l',fontSize=9.6,leading=13,textColor=MUT)
H2=S('h2',f='DB',fontSize=12.5,leading=15,textColor=NAVY,spaceAfter=2); H2S=S('h2s',fontSize=8.6,leading=11,textColor=MUT,spaceAfter=6)
ITEM=S('it',f='DB',fontSize=10.5,leading=13,textColor=INK); BOD=S('b',fontSize=9,leading=12); SMG=S('smg',fontSize=8,leading=10.5,textColor=MUT)
TH=S('th',f='DB',fontSize=7.6,leading=9.5,textColor=MUT); TD=S('td',fontSize=8.6,leading=11); NUMR=S('nr',fontSize=8.6,leading=11,alignment=2); BLANK=S('bl',fontSize=8.2,leading=11,textColor=MUT)
os.makedirs('/home/claude/qr12',exist_ok=True)
def qr(url,name,size=1.0):
    p=f'/home/claude/qr12/{name}.png'
    if not os.path.exists(p):
        q=qrcode.QRCode(box_size=12,border=4,error_correction=qrcode.constants.ERROR_CORRECT_L); q.add_data(url); q.make(fit=True); q.make_image(fill_color="black",back_color="white").save(p)
    return Image(p,size*inch,size*inch)
def clip(t,n): return t if len(t)<=n else t[:n].rsplit(' ',1)[0]+'…'
BOX='☐'
MARK={"Great Deal":("TOP PICK",RUST),"Good Deal":("STRONG",NAVY),"Just Barely Over The Threshold":("BORDERLINE",MUT),"Lead – need price/photos":("ASK FIRST",MUT)}
MM=[
 dict(tier="Great Deal",what="Camera lot from a lifetime photographer – black Nikon F2 Photomic with Nikkor zoom, Polaroid SX-70 Sonar OneStep, Falcon Special, two Brownies, Spartus Full-Vue, Spectra Candela meter, folding camera, Brownie 8mm projector in box, screen, 'lots of high-end lenses'",
      ask=100,mid=550,profit=375,city="Mesquite, TX (local pickup – fits in the car)",plat="Craigslist Dallas",link="https://www.craigslist.org/view/d/mesquite-vintage-film-cameras-and/7x4ZFmPnkJhVbbwvcVbYEe",
      check="The black F2 alone sells for $175–280 and the SX-70 Sonar for $100–180, so the lot pays for itself twice before the rest. Ask Don which lenses are in the 'high-end lenses' pile (any Nikkor prime adds $50–150 each). Fire the F2 shutter at a few speeds and check the meter needle moves; press the SX-70 red button and listen for the motor. Phone number is in the listing; 'reasonable offers considered'.",
      aware="Title says 'Vintage Film Cameras'; the body says 'Nikon' but never F2, and never mentions the SX-70 model. Priced as a box of old cameras.",
      ev="Nikon F2 black body: 45 sold in 12 months, median $228 (p25 $175, p75 $280) – e.g. $185 Nov 2025, $196 Mar 2026, $205 Nov 2025. Polaroid SX-70 Sonar OneStep: 41 sold, median $125 (p25 $101, p75 $180). Falcon Special, Brownies, Spartus, Candela meter: $20–45 each."),
 dict(tier="Great Deal",what="Hoyt UltraTec compound bow with a spare set of XT3000 limbs (70 lb), sights, stabilizer, release and soft case – needs new strings",
      ask=40,mid=280,profit=140,city="Carthage, NY (ask to ship – ~$35)",plat="Craigslist Albany",link="https://www.craigslist.org/view/d/carthage-hoyt-ultratec-with-xt-sets-and/9n79s9LCanPoJx7v1z19fx",
      check="Working UltraTecs sell $150–235, and the spare limb set is $60–120 on its own. A new string set is ~$30 and a pro shop fits it in minutes – that's a consumable, not a repair, but it's the one thing to budget. Ask for a photo of the limb stickers (draw weight) and that the cams and cables aren't frayed. Seller says cash only and 'can deliver within commuting area of Carthage' – offer to pay for a shipped box.",
      aware="Title names the Hoyt UltraTec; the seller just prices it like a junk bow because the strings are shot.",
      ev="Hoyt UltraTec / XT2000: 15 sold in 12 months, median $200 (p25 $150, p75 $235) – e.g. $220 Sep 2026, $185 Sep 2026, $230 Aug 2026. Spare Hoyt limb sets $60–120."),
 dict(tier="Good Deal",what="Eight 1998 Tiger Electronics Furbys (model 70-800), never out of the box – teal/yellow, dalmatian, tuxedo, giraffe, brown/tan, snowball",
      ask=80,mid=400,profit=130,city="Grants Pass, OR (ask to ship – one carton, ~$50)",plat="Craigslist Humboldt",link="https://www.craigslist.org/view/d/grants-pass-original-full-size-furbys/93SwfT4ki1d2wQ4Q26MpEg",
      check="Boxed first-generation Furbys sell $40–65 each, so eight at $10 is a $400 lot for $80. Sell them one at a time, not as a lot. Ask for a photo of each box front (colour/edition) and whether the boxes are crushed – box condition moves these $15 either way. Phone number is in the listing (Fergie). Batteries will have been removed or dead; that's expected for NIB.",
      aware="Seller knows they're original Furbys and prices them at what they cost in 1998 – no idea boxed ones are collected.",
      ev="Furby 1998 Tiger 70-800 new in box: 50 sold in 12 months, median $50 (p25 $40, p75 $65) – e.g. $50 Jul 2026, $50 Nov 2025, $48 Dec 2025."),
 dict(tier="Good Deal",what="Paul Flato jewelled compact with matching lipstick tube, in the original Paul Flato box, c. 1950",
      ask=25,mid=130,profit=85,city="Medford, MN (seller meets at Medford Outlet Center; ask to ship – ~$8)",plat="Craigslist Ames",link="https://www.craigslist.org/view/d/medford-vintage-paul-flato-jeweled/wqfqMe54njMZ3BQEoFektf",
      check="Signed Flato compacts sell $75–140 and the lipstick-tube sets $120–220. Ask for a photo of the signature inside the lid and whether all the stones are present (one missing stone halves it). Listing says 'no shipping, meet at the outlet center 9–3' – offer $25 plus $8 postage; most sellers say yes once the money is in hand.",
      aware="Names Paul Flato in the title but prices it as an old compact.",
      ev="Paul Flato compact: 16 sold in 12 months, median $108 (p25 $75, p75 $140) – e.g. $140 compact+lipstick Mar 2026, $130 Nov 2025, $102 Mar 2026, $260 carriage set Mar 2026."),
 dict(tier="Lead – need price/photos",what="Cymbal bundle – Zildjian A 23\" Sweet Ride, A 18\" Medium Ride, Oriental Trash Splash 11\", Paiste 502 18\" China, PST5 splash, Sabian B8 Pro 16\", B8 14\", B8 hats",
      ask=123,mid=700,profit=290,city="Kahului, Maui, HI (ask to ship – ~$100 from Hawaii)",plat="Craigslist Honolulu",link="https://www.craigslist.org/view/d/kahului-huge-cymbal-bundle-zildjian/2zX6xaXdRmJoPkPGehbNkg",
      check="One fact decides it: is $123 the price for the whole bundle (the body itemises each cymbal with its own 'value', totalling ~$900) and will they ship? The 23\" A Sweet Ride alone sells $285–450. If $123 is the lot and they'll box it (cymbals ship fine flat, ~25 lb), this is the best spread of the week; if $123 is a placeholder, walk away. Body says 'local cash'.",
      aware="Very aware – lists every cymbal and its market value, and says 'below market price'. The spread exists only because of the odd $123 figure.",
      ev="Zildjian 23\" A Sweet Ride: 19 sold in 12 months, median $380 (p25 $285, p75 $450). 18\" A Medium Ride $120–180; Paiste 502 China $60–90; B8/PST pieces $20–50 each."),
 dict(tier="Lead – need price/photos",what="Yamaha A-series cutaway acoustic-electric (A1M or A3M) with hard case and stand – listed as just 'Guitar'",
      ask=100,mid=325,profit=120,city="Sweet Home, AR (ask to ship – ~$60 each way)",plat="Craigslist Memphis",link="https://www.craigslist.org/view/d/sweet-home-guitar/k2yUbJnAqJsTJfcZaBkpFv",
      check="Ask for a photo of the label inside the soundhole. A1M sells $200–460 (median $325) – clears if the buyer pays outbound shipping, which is normal on eBay. A3M sells $400–600 and clears easily. Check the neck is straight and the preamp powers on. Two photos only; seller wrote four words.",
      aware="Not at all – title 'Guitar', body 'Guitar with case and stand'.",
      ev="Yamaha A1M: 18 sold in 12 months, median $325 (p25 $218, p75 $462). Yamaha A3M: $400 Feb 2026, $600 May 2026."),
 dict(tier="Lead – need price/photos",what="Signed costume jewellery – Sherman (Canada) rhodium 'wave' brooch $50, Boucher pearl starfish brooch + earrings $40, Marboux pearl leaf set $40",
      ask=90,mid=210,profit=75,city="Whistler, BC, Canada (ask to ship – ~$15; customs-free under $800)",plat="Craigslist Bellingham",link="https://www.craigslist.org/view/d/whistler-jewelryvintage-assorted/xaCakn5UvEV5bwd97MTDCz",
      check="Sherman brooches sell $74–135 and Boucher sets $70–180, so at the asking $90 for both the profit is ~$75 – just short of the $90 the rule needs. Offer $65 for the Sherman and Boucher together and it clears. Ask for back-mark photos (Sherman script, 'Boucher' with a number).",
      aware="Names every maker; just priced from an old price book.",
      ev="Sherman brooch: 49 sold, median $92 (p25 $74, p75 $135). Boucher brooch & earring sets: 50 sold, median $115 (p25 $70, p75 $180)."),
 dict(tier="Lead – need price/photos",what="Two 3-piece bamboo fly rods with spare tips, aluminium tubes and cloth bags, plus two L.L.Bean pack rods and a reel – maker not stated",
      ask=200,mid=0,profit=0,city="Houghton, MI (ask to ship – ~$40)",plat="Craigslist Upper Peninsula",link="https://www.craigslist.org/view/d/houghton-old-fly-rods-fly-rods-bamboo/1eDhUTFzFtmMd7p8QNq6Xc",
      check="Everything rides on the stamp on the flat above the cork grip. Montague/South Bend rods sell $70–150 (median $90) – then it's a pass at any price near $200. Heddon, Granger, Phillipson or Orvis sell $250–700 each – then $200 for the pair clears. Ask for a close photo of both butt stamps before talking price; seller says 'make an offer'.",
      aware="Doesn't name a maker.",
      ev="Montague bamboo fly rod: 49 sold, median $90 (p25 $68, p75 $150). Heddon/Granger/Phillipson 3/2 rods with tube $250–700 (encyclopedia: bamboo-fly-rods)."),
 dict(tier="Just Barely Over The Threshold",what="Thorens AD30 4.5\" disc music box in an inlaid Sorrento case with 23 discs – listed as 'Vintage Music Box'",
      ask=100,mid=280,profit=75,city="Quakertown, PA (ask to ship – ~$30)",plat="Craigslist Elmira",link="https://www.craigslist.org/view/d/quakertown-vintage-music-box/g2Y8F45bgtRGDckZ8ABVTs",
      check="The box sells $85–200 (median $130) and a stack of 20+ discs about $150 on its own, so selling the two separately brings ~$280. At $100 that's ~$75 profit, below the $100 the rule needs; at $75 it clears. Seller offers a video of it playing – get it, and count the discs. Cash only / meet to pick up, so ask about shipping first.",
      aware="Doesn't know it's a Thorens; the discs are the tell.",
      ev="Thorens AD30: 50 sold, median $130 (p25 $85, p75 $200) – e.g. $200 with 20 discs May 2026, $125 Mar 2026. Thorens disc lots: 21 discs $150 Aug 2026."),
]
W=7.3*inch
def deco(c,doc):
    c.saveState(); c.setFillColor(NAVY); c.rect(0,10.78*inch,8.5*inch,0.22*inch,stroke=0,fill=1)
    c.setFont('DB',7.8); c.setFillColor(MUT); c.drawString(0.6*inch,10.46*inch,"RESALE FINDS  ·  NATIONWIDE  ·  RUN 12"); c.drawRightString(7.9*inch,10.46*inch,"October 12, 2026")
    c.setStrokeColor(HAIR); c.setLineWidth(.5); c.line(0.6*inch,10.38*inch,7.9*inch,10.38*inch)
    c.setFont('D',7.8); c.setFillColor(MUT); c.drawCentredString(4.25*inch,0.45*inch,str(doc.page)); c.restoreState()
OUT='/mnt/user-data/outputs/Resale-Finds-Nationwide-2026-10-12.pdf'; os.makedirs('/mnt/user-data/outputs',exist_ok=True)
doc=BaseDocTemplate(OUT,pagesize=letter,leftMargin=0.6*inch,rightMargin=0.6*inch,topMargin=0.85*inch,bottomMargin=0.62*inch,title="Resale Finds – Nationwide – October 12 2026")
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(0.6*inch,0.62*inch,W,9.6*inch,id='f',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=deco)])
st=[]
def plain_table(data,widths):
    t=Table(data,colWidths=widths,repeatRows=1)
    sty=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,0),.8,NAVY),('LINEBELOW',(0,1),(-1,-2),.4,HAIR)]
    for r in range(1,len(data)):
        if r%2==0: sty.append(('BACKGROUND',(0,r),(-1,r),BAND))
    t.setStyle(TableStyle(sty)); return t
st+=[Paragraph("THE LIST",KICKER),Paragraph("Underpriced finds, anywhere in the country",TITLE),
     Paragraph("9,600 Craigslist listings from 282 cities were identified one by one and researched on October 12. These nine survived eBay sold-price checks. Out-of-town sellers are asked to ship; the shipping estimate is already in each profit figure. All were still posted at 1 pm.",LEDE),Spacer(1,14)]
d=[[Paragraph("",TH),Paragraph("ITEM",TH),Paragraph("ASK",TH),Paragraph("PROFIT",TH),Paragraph("WHERE",TH),Paragraph("PAID",TH)]]
for m in MM:
    lab,col=MARK[m['tier']]
    d.append([Paragraph(BOX,TD),Paragraph(f"{clip(m['what'],52)}  <font size=6.6 color='{'#A23B1E' if col==RUST else '#6E6E6E'}'>{lab}</font>",TD),Paragraph(f"<b>${m['ask']:g}</b>",NUMR),Paragraph("—" if not m['profit'] else f"~${m['profit']:,}",NUMR),Paragraph(clip(m['city'].split(' (')[0],22),TD),Paragraph("$______",BLANK)])
st+=[plain_table(d,[.2*inch,3.4*inch,.55*inch,.65*inch,1.65*inch,.85*inch]),Spacer(1,14),
     Paragraph("How to read it",H2),Paragraph("TOP PICK and STRONG clear the rule as listed (profit at least equal to the price, $50 minimum, after eBay fees and shipping both ways). ASK FIRST items need one fact from the seller before the number is real. BORDERLINE clears only at the offer price shown. Scan a code with the phone camera to open the listing; the price evidence is on the last page.",BOD)]
st+=[PageBreak(),Paragraph("LISTINGS",KICKER),Paragraph("What to chase and what to check",TITLE),Spacer(1,12)]
for i,m in enumerate(MM):
    lab,col=MARK[m['tier']]
    econ=f"ask <b>${m['ask']:g}</b>"+(f" &nbsp;→&nbsp; sells for about <b>${m['mid']:,}</b> &nbsp;→&nbsp; <font color='#A23B1E'><b>~${m['profit']:,} profit</b></font>" if m['profit'] else " &nbsp;→&nbsp; value depends on the answer below")
    body=[Paragraph(f"<font color='#{col.hexval()[2:]}' size=7.4><b>{lab}</b></font>",SMG),Paragraph(m['what'],ITEM),Paragraph(econ,BOD),Paragraph(f"{m['city']} · {m['plat']}",SMG),Spacer(1,4),
          Paragraph(f"<b>Check before paying.</b> {m['check']}",BOD),Spacer(1,3),Paragraph(f"Seller: {m['aware']}",SMG)]
    qcell=[qr(m['link'],f"m{i}",1.15),Spacer(1,3),Paragraph("scan to open",SMG)]
    inner=Table([[body,qcell]],colWidths=[W-1.6*inch,1.4*inch])
    inner.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(1,0),(1,0),'CENTER'),('LEFTPADDING',(0,0),(0,0),0),('RIGHTPADDING',(0,0),(0,0),10),('LEFTPADDING',(1,0),(1,0),0),('RIGHTPADDING',(1,0),(1,0),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    foot=Paragraph("Asked seller ☐    Paid $__________    Notes _______________________________________",BLANK)
    outer=Table([[inner],[foot]],colWidths=[W])
    outer.setStyle(TableStyle([('LINEBEFORE',(0,0),(0,-1),2.2,col),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),2),('TOPPADDING',(0,0),(0,0),4),('BOTTOMPADDING',(0,0),(0,0),6),('TOPPADDING',(0,1),(0,1),0),('BOTTOMPADDING',(0,1),(0,1),4),('LINEBELOW',(0,1),(0,1),.5,HAIR)]))
    st+=[KeepTogether([outer]),Spacer(1,11)]
st+=[PageBreak(),Paragraph("APPENDIX",KICKER),Paragraph("Price evidence",TITLE),Paragraph("Completed eBay sales from the last 12 months (Terapeak), gathered October 12. Medians are what half of them sold above.",LEDE),Spacer(1,12)]
rows=[[Paragraph("ITEM",TH),Paragraph("WHAT IT SELLS FOR",TH)]]
for m in MM: rows.append([Paragraph(f"<b>{clip(m['what'],44)}</b>",TD),Paragraph(m['ev'],TD)])
ta=Table(rows,colWidths=[2.5*inch,4.8*inch],repeatRows=1)
sty=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.8,NAVY)]
for r in range(1,len(rows)):
    if r%2==0: sty.append(('BACKGROUND',(0,r),(-1,r),BAND))
ta.setStyle(TableStyle(sty))
st+=[ta,Spacer(1,10),Paragraph("Checked and passed on the same day, for the record: Kowa 16-D anamorphic $200 (sells $185–200), Rode NT2 $75 (sells ~$170, profit short), MXR Carbon Copy $40 (sells ~$86), G&S Fibreflex $200 (sells ~$204), 1978 Kenner 12\" Leia lot $80 (sells ~$99 + extras), Japanese bronze vase $40 (one comp, $120), Bauer ringware bowls $35 (sell $36 each), two old duck decoys $70 (sell $45–80 each), DeArmond M-75 rig $180 (no sold comps), Onewheel+ $100 (scam pattern), 'Martin' acoustic $12 (scam pattern).",SMG)]
doc.build(st); print("built",OUT)
