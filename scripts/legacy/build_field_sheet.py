import json,os,glob,qrcode,datetime as dt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether, PageBreak, Image, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

F=glob.glob('/usr/share/fonts/**/DejaVuSans.ttf',recursive=True)[0]
pdfmetrics.registerFont(TTFont('D',F))
pdfmetrics.registerFont(TTFont('DB',F.replace('DejaVuSans.ttf','DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DI',F.replace('DejaVuSans.ttf','DejaVuSans-Oblique.ttf')))
addMapping('D',0,0,'D'); addMapping('D',1,0,'DB'); addMapping('D',0,1,'DI'); addMapping('D',1,1,'DB')

INK=colors.HexColor('#111111'); BODY=colors.HexColor('#2E2E2E'); MUT=colors.HexColor('#6E6E6E')
HAIR=colors.HexColor('#D8D8D8'); BAND=colors.HexColor('#F4F6F8')
NAVY=colors.HexColor('#14487A'); RUST=colors.HexColor('#A23B1E')
S=lambda n,**k:ParagraphStyle(n,fontName=k.pop('f','D'),textColor=k.pop('textColor',BODY),**k)
TITLE =S('t',f='DB',fontSize=21,leading=24,textColor=INK)
KICKER=S('k',f='DB',fontSize=8.5,leading=11,textColor=NAVY)
LEDE  =S('l',fontSize=9.6,leading=13,textColor=MUT)
H2    =S('h2',f='DB',fontSize=12.5,leading=15,textColor=NAVY,spaceAfter=2)
H2S   =S('h2s',fontSize=8.6,leading=11,textColor=MUT,spaceAfter=6)
ITEM  =S('it',f='DB',fontSize=10.5,leading=13,textColor=INK)
BOD   =S('b',fontSize=9,leading=12)
SMG   =S('smg',fontSize=8,leading=10.5,textColor=MUT)
TH    =S('th',f='DB',fontSize=7.6,leading=9.5,textColor=MUT)
TD    =S('td',fontSize=8.6,leading=11)
TDB   =S('tdb',f='DB',fontSize=8.6,leading=11,textColor=INK)
PAY   =S('pay',f='DB',fontSize=12,leading=13.5,textColor=RUST,alignment=2)
PAYL  =S('payl',fontSize=7.2,leading=8.6,textColor=MUT,alignment=2)
NUMR  =S('nr',fontSize=8.6,leading=11,alignment=2)
BLANK =S('bl',fontSize=8.2,leading=11,textColor=MUT)

os.makedirs('/home/claude/qr2',exist_ok=True)
def qr(url,name,size=1.0):
    p=f'/home/claude/qr2/{name}.png'
    if not os.path.exists(p):
        q=qrcode.QRCode(box_size=12,border=4,error_correction=qrcode.constants.ERROR_CORRECT_L)
        q.add_data(url); q.make(fit=True)
        q.make_image(fill_color="black",back_color="white").save(p)
    return Image(p,size*inch,size*inch)
def clip(txt,n):
    if len(txt)<=n: return txt
    cut=txt[:n]
    if ' ' in cut: cut=cut[:cut.rfind(' ')]
    return cut+'…'
def pretty(d):
    a,b=[dt.date.fromisoformat(x) for x in d.split(' – ')]
    f=lambda x:x.strftime('%a %b %-d')
    return f(a) if a==b else f"{f(a)} – {f(b)}"
def daytag(d):
    a,b=[dt.date.fromisoformat(x) for x in d.split(' – ')]
    return a.strftime('%a') if a==b else f"{a.strftime('%a')}–{b.strftime('%a')}"
def t12(h):
    H,M=int(h[:2]),h[3:]
    ap='am' if H<12 else 'pm'; h12=H%12 or 12
    return f"{h12}{'' if M=='00' else ':'+M}{ap}"
BOX='☐'

MM=json.load(open('/home/claude/master10.json'))
PLAN=json.load(open('/home/claude/plan10.json'))
MARK={"Great Deal":("TOP PICK",RUST),"Good Deal":("STRONG",NAVY),
      "Just Barely Over The Threshold":("BORDERLINE",MUT),"Lead – need price/photos":("ASK FIRST",MUT)}
order={"Great Deal":0,"Good Deal":1,"Just Barely Over The Threshold":2,"Lead – need price/photos":3}
MM=sorted(MM,key=lambda m:(order[m['tier']],-m['profit']))
NOW=[p for p in PLAN if p['dates']<'2026-10-13']; NEXT=[p for p in PLAN if p['dates']>='2026-10-13']
for i,p in enumerate(NOW,1): p['rank']=i
for i,p in enumerate(NEXT,1): p['rank']=i
W=7.3*inch

def deco(c,doc):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0,10.78*inch,8.5*inch,0.22*inch,stroke=0,fill=1)
    c.setFont('DB',7.8); c.setFillColor(MUT)
    c.drawString(0.6*inch,10.46*inch,"DFW RESALE  ·  FIELD SHEET")
    c.drawRightString(7.9*inch,10.46*inch,"October 8–17, 2026")
    c.setStrokeColor(HAIR); c.setLineWidth(.5); c.line(0.6*inch,10.38*inch,7.9*inch,10.38*inch)
    c.setFont('D',7.8); c.setFillColor(MUT); c.drawCentredString(4.25*inch,0.45*inch,str(doc.page))
    c.restoreState()
doc=BaseDocTemplate('/mnt/user-data/outputs/DFW-Resale-Field-Sheet-2026-10-08.pdf',pagesize=letter,
    leftMargin=0.6*inch,rightMargin=0.6*inch,topMargin=0.85*inch,bottomMargin=0.62*inch,
    title="DFW Resale Field Sheet – October 8 2026")
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(0.6*inch,0.62*inch,W,9.6*inch,id='f',
    leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=deco)])
st=[]
def rule(c=HAIR,w=.6,sb=2,sa=6): return HRFlowable(width='100%',thickness=w,color=c,spaceBefore=sb,spaceAfter=sa)
def plain_table(data,widths,aligns=None,zebra=True):
    t=Table(data,colWidths=widths,repeatRows=1)
    sty=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
         ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
         ('LINEBELOW',(0,0),(-1,0),.8,NAVY),('LINEBELOW',(0,1),(-1,-2),.4,HAIR)]
    if zebra:
        for r in range(1,len(data)):
            if r%2==0: sty.append(('BACKGROUND',(0,r),(-1,r),BAND))
    t.setStyle(TableStyle(sty)); return t

# ───────────── page 1 · the plan ─────────────
st+=[Paragraph("THE PLAN",KICKER),Paragraph("Underpriced finds around Dallas–Fort Worth",TITLE),
     Paragraph("Thirteen listings to chase and sixteen estate sales worth walking, ranked by what they could return.",LEDE),
     Spacer(1,14)]
st+=[Paragraph("Estate sales — this weekend",H2),
     Paragraph("Ranked by total profit available across all of their targets.",H2S)]
def plan_rows(src):
    d=[[Paragraph("",TH),Paragraph("DAYS",TH),Paragraph("SALE",TH),Paragraph("WHERE",TH),
        Paragraph("MIN",TH),Paragraph("#",TH),Paragraph("POTENTIAL",TH)]]
    for p in src:
        addr=p['addr'] or "address posted sale morning"
        d.append([Paragraph(BOX,TD),Paragraph(daytag(p['dates']),TD),
                  Paragraph(f"<b>{p['rank']}.</b> {clip(p['sale'],34)}",TD),
                  Paragraph(f"{p['city']} · <font color='#6E6E6E'>{clip(addr,28)}</font>",TD),
                  Paragraph(str(p['drive']),NUMR),Paragraph(str(p['n']),NUMR),
                  Paragraph(f"<b>${p['total']:,}</b>",NUMR)])
    return plain_table(d,[.2*inch,.74*inch,2.26*inch,2.3*inch,.42*inch,.48*inch,.9*inch])
st+=[plan_rows(NOW),Spacer(1,16),
     KeepTogether([Paragraph("Estate sales — next weekend",H2),
     Paragraph("Not open yet; photo sets may still grow.",H2S),plan_rows(NEXT)]),Spacer(1,16)]
callhead=[Paragraph("Listings to contact",H2),
          Paragraph("All confirmed still up the morning of October 8. Details and codes on the following pages.",H2S)]
d=[[Paragraph("",TH),Paragraph("ITEM",TH),Paragraph("ASK",TH),Paragraph("PROFIT",TH),Paragraph("WHERE",TH),Paragraph("PAID",TH)]]
for m in MM:
    lab,col=MARK[m['tier']]
    ask="Free" if m['ask']==0 else f"${m['ask']:g}"
    pr="—" if not m['lo'] else f"${m['profit']:,.0f}"
    d.append([Paragraph(BOX,TD),
              Paragraph(f"{clip(m['what'],48)}  <font size=6.6 color='{'#A23B1E' if col==RUST else '#6E6E6E'}'>{lab}</font>",TD),
              Paragraph(f"<b>{ask}</b>",NUMR),Paragraph(pr,NUMR),
              Paragraph(f"{m['city']} · {m['plat'].replace('Facebook Marketplace','Facebook')}",TD),
              Paragraph("$______",BLANK)])
st+=[KeepTogether(callhead+[plain_table(d,[.2*inch,3.35*inch,.55*inch,.6*inch,1.75*inch,.85*inch])])]

# ───────────── marketplace cards ─────────────
st+=[PageBreak(),Paragraph("LISTINGS",KICKER),Paragraph("What to chase and what to check",TITLE),
     Paragraph("Scan the code with your phone camera to open the listing. Price evidence for every item is in the table at the back.",LEDE),Spacer(1,12)]
for i,m in enumerate(MM):
    lab,col=MARK[m['tier']]
    ask=("Free" if m['ask']==0 else f"${m['ask']:g}")+(f" for the lot" if m['offer']!=m['ask'] else "")
    econ=f"ask <b>{ask}</b>" if not m['lo'] else f"ask <b>{ask}</b> &nbsp;→&nbsp; sells for about <b>${m['mid']:,.0f}</b> &nbsp;→&nbsp; <font color='#A23B1E'><b>~${m['profit']:,.0f} profit</b></font>"
    body=[Paragraph(f"<font color='#{col.hexval()[2:]}' size=7.4><b>{lab}</b></font>",SMG),
          Paragraph(m['what'],ITEM),
          Paragraph(f"{econ}",BOD),
          Paragraph(f"{m['city']} · {m['plat']}",SMG),
          Spacer(1,4),
          Paragraph(f"<b>Check before paying.</b> {m['check']}",BOD),
          Spacer(1,3),
          Paragraph(f"Seller: {m['aware']}",SMG)]
    qcell=[qr(m['link'],f"m{i}",1.15),Spacer(1,3),Paragraph("scan to open",SMG)]
    inner=Table([[body,qcell]],colWidths=[W-1.6*inch,1.4*inch])
    inner.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(1,0),(1,0),'CENTER'),
        ('LEFTPADDING',(0,0),(0,0),0),('RIGHTPADDING',(0,0),(0,0),10),
        ('LEFTPADDING',(1,0),(1,0),0),('RIGHTPADDING',(1,0),(1,0),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    foot=Paragraph("Paid $__________    Notes _____________________________________________________",BLANK)
    outer=Table([[inner],[foot]],colWidths=[W])
    outer.setStyle(TableStyle([('LINEBEFORE',(0,0),(0,-1),2.2,col),
        ('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),2),
        ('TOPPADDING',(0,0),(0,0),4),('BOTTOMPADDING',(0,0),(0,0),6),
        ('TOPPADDING',(0,1),(0,1),0),('BOTTOMPADDING',(0,1),(0,1),4),
        ('LINEBELOW',(0,1),(0,1),.5,HAIR)]))
    st+=[KeepTogether([outer]),Spacer(1,11)]

# ───────────── estate sales ─────────────
def sale_section(p,first_of_page=False):
    head_l=[Paragraph(f"{p['rank']}.  {p['sale']}",S('sh',f='DB',fontSize=12.5,leading=15,textColor=NAVY)),
            Paragraph(f"{(p['addr'] or 'Address posted on the sale page the morning of the sale')}, {p['city']} TX {p['zip']}",BOD),
            Paragraph(f"{pretty(p['dates'])} · opens {t12(p['open'])}, last day ends {t12(p['close'])} · {p['drive']} min · {p['co']} · {p['phone']}",SMG),
            Spacer(1,3),
            Paragraph(f"<b>~${p['total']:,} potential</b> across {p['n']} target{'s' if p['n']>1 else ''} · best: {p['best']} (~${p['bestp']:,})",BOD)]
    hdr=Table([[head_l,[qr(p['url'],f"s{p['rank']}{p['zip']}",1.05),Spacer(1,2),Paragraph("sale page",SMG)]]],
              colWidths=[W-1.45*inch,1.3*inch])
    hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(1,0),(1,0),'CENTER'),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    rows=[[Paragraph("",TH),Paragraph("WHAT TO LOOK FOR",TH),Paragraph("PAY UP TO",S('t2',f='DB',fontSize=7.6,leading=9.5,textColor=MUT,alignment=2)),Paragraph("PAID",TH)]]
    for e in p['items']:
        note=" <i>(captioned by the company — expect it priced)</i>" if e['capt'] else ""
        extra=" · too big to ship, sell locally" if e['ch']=='local' else ""
        cell=[Paragraph(f"{e['what']}{note}",S('i2',f='DB',fontSize=9.6,leading=12,textColor=INK)),
              Paragraph(f"{e['check']}",BOD),
              Paragraph(f"profit ~${e['profit']:,.0f} on a ~${e['mid']:,.0f} resale{extra}",SMG)]
        rows.append([Paragraph(BOX,TD),cell,
                     [Paragraph(f"${e['pay']:,.0f}",PAY)],
                     Paragraph("$______",BLANK)])
    t=Table(rows,colWidths=[.22*inch,5.08*inch,1.1*inch,.9*inch])
    sty=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
         ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
         ('LINEBELOW',(0,0),(-1,0),.8,NAVY),('TOPPADDING',(0,0),(-1,0),3),('BOTTOMPADDING',(0,0),(-1,0),3)]
    for r in range(1,len(rows)-1): sty.append(('LINEBELOW',(0,r),(-1,r),.4,HAIR))
    t.setStyle(TableStyle(sty))
    return KeepTogether([hdr,Spacer(1,6),t,Spacer(1,18)])
st+=[PageBreak(),Paragraph("ESTATE SALES · THIS WEEKEND",KICKER),Paragraph("Thu Oct 8 – Sun Oct 11",TITLE),
     Paragraph("Companies post photos but not prices. Almost everything below was photographed without a caption, which usually means nobody recognised it. "
               "<b>Pay up to</b> is a ceiling — above it the margin is gone. First day has the best pick; last day is often half off.",LEDE),Spacer(1,14)]
for p in NOW: st.append(sale_section(p))
st+=[PageBreak(),Paragraph("ESTATE SALES · NEXT WEEKEND",KICKER),Paragraph("Wed Oct 14 – Sat Oct 17",TITLE),
     Paragraph("Not open yet — worth putting on the calendar now.",LEDE),Spacer(1,14)]
for p in NEXT: st.append(sale_section(p))

# ───────────── pocket card ─────────────
st+=[PageBreak(),Paragraph("POCKET CARD",KICKER),Paragraph("Every ceiling on one page",TITLE),
     Paragraph("Cut this page off and carry it — nothing here needs a phone. Numbers match the plan on page 1; an N prefix means next weekend.",LEDE),Spacer(1,12)]
def pocket_col(items):
    rows=[[Paragraph("SALE",TH),Paragraph("ITEM",TH),Paragraph("PAY",S('t3',f='DB',fontSize=7.4,leading=9,textColor=MUT,alignment=2))]]
    marks=[]
    for sale,item,pay,first in items:
        rows.append([Paragraph(f"<b>{sale}</b>" if first else "",S('pc',fontSize=7.8,leading=10)),
                     Paragraph(f"{BOX} {clip(item,44)}",S('pi',fontSize=7.8,leading=10)),
                     Paragraph(f"<b>${pay:,.0f}</b>",S('pp',fontSize=7.8,leading=10,alignment=2,textColor=RUST))])
        if first: marks.append(len(rows)-1)
    t=Table(rows,colWidths=[.82*inch,2.05*inch,.53*inch],repeatRows=1)
    sty=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
         ('TOPPADDING',(0,0),(-1,-1),2.4),('BOTTOMPADDING',(0,0),(-1,-1),2.4),
         ('LINEBELOW',(0,0),(-1,0),.7,NAVY)]
    for r in marks[1:]: sty.append(('LINEABOVE',(0,r),(-1,r),.4,NAVY))
    t.setStyle(TableStyle(sty)); return t
flat=[]
for p in NOW+NEXT:
    first=True
    for e in p['items']:
        tagp=('N' if p in NEXT else '')+str(p['rank'])
        flat.append((f"{tagp}. {p['city'][:13]}",e['what'],e['pay'],first)); first=False
half=(len(flat)+1)//2
A,B=flat[:half],flat[half:]
if B and not B[0][3]:
    B[0]=(B[0][0],B[0][1],B[0][2],True)
two=Table([[pocket_col(A),pocket_col(B)]],colWidths=[3.5*inch,3.5*inch])
two.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(0,0),0),('RIGHTPADDING',(0,0),(0,0),14),
    ('LEFTPADDING',(1,0),(1,0),0),('RIGHTPADDING',(1,0),(1,0),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
st+=[two]

# ───────────── price evidence ─────────────
st+=[PageBreak(),Paragraph("APPENDIX",KICKER),Paragraph("Price evidence",TITLE),
     Paragraph("Completed eBay sales from the last 12 months, gathered October 8. Carry this only if you want to argue a price.",LEDE),Spacer(1,12)]
rows=[[Paragraph("ITEM",TH),Paragraph("WHAT IT SELLS FOR",TH)]]
for m in MM: rows.append([Paragraph(f"<b>{clip(m['what'],44)}</b>",TD),Paragraph(m['ev'],TD)])
for p in NOW+NEXT:
    for e in p['items']: rows.append([Paragraph(f"<b>{clip(e['what'],42)}</b> <font color='#6E6E6E'>({p['city']})</font>",TD),Paragraph(e['ev'],TD)])
ta=Table(rows,colWidths=[2.5*inch,4.8*inch],repeatRows=1)
sty=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
     ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.8,NAVY)]
for r in range(1,len(rows)):
    if r%2==0: sty.append(('BACKGROUND',(0,r),(-1,r),BAND))
ta.setStyle(TableStyle(sty))
st+=[ta,Spacer(1,10),
     Paragraph("Sold prices are recent completed sales, not guarantees; condition in person moves them either way.",SMG)]
doc.build(st)
print("built")
