import json,glob
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
reg=glob.glob('/usr/share/fonts/**/DejaVuSans.ttf',recursive=True)[0]; bold=reg.replace('DejaVuSans.ttf','DejaVuSans-Bold.ttf')
pdfmetrics.registerFont(TTFont('D',reg)); pdfmetrics.registerFont(TTFont('DB',bold))
for b in (0,1):
    for i in (0,1): addMapping('D',b,i,'DB' if b else 'D')
S=lambda n,**k:ParagraphStyle(n,fontName=k.pop('f','D'),**k)
H1=S('h1',f='DB',fontSize=20,leading=24,spaceAfter=4); SUB=S('s',fontSize=10,leading=13,textColor=colors.HexColor('#444444'))
H2=S('h2',f='DB',fontSize=14,leading=18,spaceBefore=10,spaceAfter=4); B=S('b',fontSize=10,leading=13.5); T=S('t',f='DB',fontSize=11.5,leading=14.5); SM=S('sm',fontSize=9.2,leading=12)
def L(u,t="View listing"): return f'<link href="{u}" color="#0563C1"><u>{t}</u></link>'
D=json.load(open('/home/claude/master9.json'))
tiermap={"Great Deal":("TOP PICK","#C00000"),"Good Deal":("STRONG","#548235"),"Just Barely Over The Threshold":("BORDERLINE","#BF8F00"),"Lead – need price/photos":("NEEDS ONE ANSWER","#7F7F7F")}
def card(head,color,lines):
    rows=[[Paragraph(head,T)]]+[[Paragraph(x,SM if i else B)] for i,x in enumerate(lines)]
    t=Table(rows,colWidths=[532]); t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.HexColor(color)),('LINEBEFORE',(0,0),(0,-1),5,colors.HexColor(color)),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#F2F2F2')),('LEFTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
    return [KeepTogether([t]),Spacer(1,6)]
st=[Paragraph("Underpriced finds around Dallas–Fort Worth – full list",H1),
Paragraph("September 22, 2026 · everything found since September 21 · marketplace listings confirmed still up that morning",SUB),Spacer(1,6),
Paragraph("This list has two parts. <b>Part 1</b> is secondhand listings on Facebook Marketplace, OfferUp and Craigslist that look underpriced – usually because the photos show a brand or model the listing doesn't mention. <b>Part 2</b> is this week's estate sales (Thursday 9/24 – Sunday 9/27): estate sale companies post photos but not prices, so each item has a <b>“pay up to”</b> ceiling instead – the most it's worth paying and still leave room to resell. Sold prices come from eBay sold listings over the last 12 months. Listings and estate-sale items sell fast, so some will be gone.",B),
Spacer(1,4),Paragraph("Ratings: <font color='#C00000'><b>Top pick</b></font> › <font color='#548235'><b>Strong</b></font> › <font color='#BF8F00'><b>Borderline</b></font> › <font color='#7F7F7F'><b>Needs one answer</b></font> (a missing price or photo from the seller). Ratings reflect the gap between the asking price and recent sale prices, and how sure the identification is.",SM),
Paragraph("Part 1 · Marketplace listings",H2)]
for m in D['M']:
    if m['status']=='SOLD': continue
    lab,col=tiermap.get(m['tier'],("",'#7F7F7F'))
    ask=f"${m['ask']:g}"+(f" (likely takes ~${m['offer']:g})" if m['offer']!=m['ask'] else "")
    st+=card(f'<font color="{col}"><b>{lab}</b></font> &nbsp; {m["what"]}',col,[
      f"<b>{ask}</b> · {m['city']} · {m['plat']} · {L(m['link'])} · <i>first seen {m['first']}</i>",
      f"<b>Selling elsewhere:</b> {m['ev']}",f"<b>Does the seller know?</b> {m['aware']}",f"<b>Worth checking:</b> {m['check']}"])
st+=[PageBreak(),Paragraph("Part 2 · Estate sales this week (Thu 9/24 – Sun 9/27)",H2),
Paragraph("Sales are ranked by how good they could be: the profit available on every target if bought at its ceiling, weighted by how sure the identification is. Each sale opens with its total potential and its single best item. Every item below appeared in the company's own photos without a caption, which usually means they haven't researched it. The first day has the best selection; the last day is often half off. <b>“Pay up to”</b> is a ceiling, not a guess at the tag price – if it's tagged higher, skip it or wait for the discount day.",SM),Spacer(1,6)]
PLAN=json.load(open('/home/claude/plan9.json'))
for p in PLAN:
    summ=Table([[Paragraph(f"<b>Total potential:</b> ~${p['total']:,} profit across {p['n']} target{'s' if p['n']>1 else ''}",SM),Paragraph(f"<b>Best item:</b> {p['best']} – ~${p['bestp']:,}",SM)]],colWidths=[230,284])
    summ.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#E2EFDA')),('LEFTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('VALIGN',(0,0),(-1,-1),'TOP')]))
    rows=[[Paragraph(f"#{p['rank']} &nbsp; {p['sale']}",T)],
          [Paragraph(f"<b>{p['dates']}</b> · {p['city']} · ~{p['drive']} min from Keller · run by {p['co']} · {L(p['url'],'Open sale page')}",B)],
          [summ],[Paragraph(__import__('re').sub(r'^\d+ targets?\. Best bet: .*? profit if bought at the ceiling\)\.\s*','',p['summary']) or ' ',SM)]]
    for e in sorted(p['items'],key=lambda e:-e['profit']):
        new=" <font color='#C55A11'><b>NEW 9/22</b></font>" if e['first']=='9/22' else ""
        rows.append([Paragraph(f"• <b>{e['what']}</b>{new} — pay up to <b>${e['pay']:,.0f}</b> · resale ~${e['mid']:,.0f} · profit ~${e['profit']:,.0f} · {L(e['photo'],'photo')}<br/>&nbsp;&nbsp;<i>Check:</i> {e['check']} &nbsp;<i>Sold:</i> {e['ev']}",SM)])
    t=Table(rows,colWidths=[532]); t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.HexColor('#2F5597')),('LINEBEFORE',(0,0),(0,-1),5,colors.HexColor('#2F5597')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#F2F2F2')),('LEFTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
    st+=[KeepTogether([t]),Spacer(1,6)]
st+=[Spacer(1,6),Paragraph("Sale prices are recent examples, not guarantees. Condition in person can change the value either way.",SUB)]
doc=SimpleDocTemplate('/mnt/user-data/outputs/DFW-Resale-Finds-Full-List-2026-09-22.pdf',pagesize=letter,leftMargin=40,rightMargin=40,topMargin=36,bottomMargin=36,title="DFW Resale Finds – Full List")
doc.build(st)
