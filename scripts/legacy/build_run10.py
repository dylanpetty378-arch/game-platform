import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import glob
reg=glob.glob('/usr/share/fonts/**/DejaVuSans.ttf',recursive=True)[0]; bold=reg.replace('DejaVuSans.ttf','DejaVuSans-Bold.ttf')
pdfmetrics.registerFont(TTFont('D',reg)); pdfmetrics.registerFont(TTFont('DB',bold))
for b in (0,1):
    for i in (0,1): addMapping('D',b,i,'DB' if b else 'D')
S=lambda n,**k:ParagraphStyle(n,fontName=k.pop('f','D'),**k)
H1=S('h1',f='DB',fontSize=20,leading=24,spaceAfter=4); SUB=S('s',fontSize=10,leading=13,textColor=colors.HexColor('#444444'))
H2=S('h2',f='DB',fontSize=14,leading=18,spaceBefore=10,spaceAfter=4); B=S('b',fontSize=10,leading=13.5)
T=S('t',f='DB',fontSize=11.5,leading=14.5); SM=S('sm',fontSize=9.2,leading=12)
def L(u,t="View listing"): return f'<link href="{u}" color="#0563C1"><u>{t}</u></link>'
MM=json.load(open('/home/claude/master10.json')); PLAN=json.load(open('/home/claude/plan10.json'))
tiermap={"Great Deal":("TOP PICK","#C00000"),"Good Deal":("STRONG","#548235"),
         "Just Barely Over The Threshold":("BORDERLINE","#BF8F00"),"Lead – need price/photos":("NEEDS ONE ANSWER","#7F7F7F")}
def card(head,color,lines):
    rows=[[Paragraph(head,T)]]+[[Paragraph(x,SM if i else B)] for i,x in enumerate(lines)]
    t=Table(rows,colWidths=[532]); t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.HexColor(color)),
      ('LINEBEFORE',(0,0),(0,-1),5,colors.HexColor(color)),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#F2F2F2')),
      ('LEFTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
    return [KeepTogether([t]),Spacer(1,6)]
st=[Paragraph("Underpriced finds around Dallas–Fort Worth",H1),
Paragraph("October 8, 2026 · a fresh sweep of Craigslist, OfferUp and Facebook Marketplace (16,000+ listings) plus every estate sale within 20 miles of north Fort Worth",SUB),Spacer(1,6),
Paragraph("This list has two parts. <b>Part 1</b> is secondhand listings that look underpriced – usually because the photos show a brand or model the listing itself doesn't mention. Every one was confirmed still up on the morning of October 8. <b>Part 2</b> is the estate sales running now and next weekend: estate-sale companies post photos but not prices, so each item carries a <b>“pay up to”</b> ceiling instead – the most it is worth paying and still leave a worthwhile margin. Sold prices throughout come from completed eBay sales in the last 12 months.",B),
Spacer(1,4),
Paragraph("Ratings: <font color='#C00000'><b>Top pick</b></font> › <font color='#548235'><b>Strong</b></font> › <font color='#BF8F00'><b>Borderline</b></font> › <font color='#7F7F7F'><b>Needs one answer</b></font> (a question for the seller first). Ratings reflect the gap between the asking price and recent sale prices, and how certain the identification is from photos alone.",SM),
Paragraph("Part 1 · Marketplace listings",H2)]
order={"Great Deal":0,"Good Deal":1,"Just Barely Over The Threshold":2,"Lead – need price/photos":3}
for m in sorted(MM,key=lambda m:(order[m['tier']],-m['profit'])):
    lab,col=tiermap[m['tier']]
    ask=("Free" if m['ask']==0 else f"${m['ask']:g}")+(f" (treat as ~${m['offer']:g} for the lot)" if m['offer']!=m['ask'] else "")
    prof=f"resale ~${m['mid']:,.0f} · profit ~${m['profit']:,.0f}" if m['lo'] else "value unknown until verified"
    st+=card(f'<font color="{col}"><b>{lab}</b></font> &nbsp; {m["what"]}',col,[
      f"<b>{ask}</b> · {prof} · {m['city']} · {m['plat']} · {L(m['link'])}",
      f"<b>Selling elsewhere:</b> {m['ev']}",
      f"<b>Does the seller know?</b> {m['aware']}",
      f"<b>Worth checking:</b> {m['check']}"])
NOW=[p for p in PLAN if p['dates'] < '2026-10-13']
NEXT=[p for p in PLAN if p['dates'] >= '2026-10-13']
def sales_block(plans,title,intro):
    out=[Paragraph(title,H2),Paragraph(intro,SM),Spacer(1,6)]
    for p in plans:
        summ=Table([[Paragraph(f"<b>Total potential:</b> ~${p['total']:,} profit across {p['n']} target{'s' if p['n']>1 else ''}",SM),
                     Paragraph(f"<b>Best item:</b> {p['best']} – ~${p['bestp']:,}",SM)]],colWidths=[230,284])
        summ.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#E2EFDA')),('LEFTPADDING',(0,0),(-1,-1),6),
          ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('VALIGN',(0,0),(-1,-1),'TOP')]))
        rows=[[Paragraph(f"#{p['rank']} &nbsp; {p['sale']}",T)],
              [Paragraph(f"<b>{p['dates']}</b> · {p['city']} · ~{p['drive']} min from Keller · run by {p['co']} · {p['pics']} photos posted · {L(p['url'],'Open sale page')}",B)],
              [summ]]
        for e in p['items']:
            tag=" <font color='#777777'>(the company captioned this one, so expect it priced)</font>" if e['capt'] else ""
            ch=" · sell locally, too big to ship" if e['ch']=='local' else ""
            rows.append([Paragraph(f"• <b>{e['what']}</b>{tag} — pay up to <b>${e['pay']:,.0f}</b> · resale ~${e['mid']:,.0f} · profit ~${e['profit']:,.0f}{ch} · {L(e['photo'],'photo')}<br/>&nbsp;&nbsp;<i>Check:</i> {e['check']} &nbsp;<i>Sold:</i> {e['ev']}",SM)])
        t=Table(rows,colWidths=[532]); t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.HexColor('#2F5597')),
          ('LINEBEFORE',(0,0),(0,-1),5,colors.HexColor('#2F5597')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#F2F2F2')),
          ('LEFTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
        out+=[KeepTogether([t]),Spacer(1,6)]
    return out
st+=[PageBreak()]
st+=sales_block(NOW,"Part 2 · Estate sales running now (Thu Oct 8 – Sun Oct 11)",
 "Sales are ranked by how much profit is available across all of their targets, weighted by how certain each identification is. Items below are drawn from the company's own photos; most were posted without a caption, which usually means the company didn't recognise what it was. The first day has the best selection and the last day is often half price. <b>“Pay up to”</b> is a ceiling, not a prediction of the tag – if it's marked higher, wait for the discount day or walk.")
st+=[PageBreak()]
st+=sales_block(NEXT,"Part 2b · Estate sales next weekend (Wed Oct 14 – Sat Oct 17)",
 "These haven't opened yet, so photo sets may still grow. Worth putting on the calendar now.")
st+=[Spacer(1,8),Paragraph("Sold prices are recent completed sales, not guarantees, and condition in person moves them either way. Marketplace listings and estate-sale items both move fast – some of this will already be gone.",SUB)]
doc=SimpleDocTemplate('/mnt/user-data/outputs/DFW-Resale-Finds-Full-List-2026-10-08.pdf',pagesize=letter,
  leftMargin=40,rightMargin=40,topMargin=36,bottomMargin=36,title="DFW Resale Finds – Full List – October 8 2026")
doc.build(st)
print("ok")
