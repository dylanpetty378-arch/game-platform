"""Printable finds report (Dylan prints these and works from paper) — one summary page + one card per find with
photo, economics, sold-price evidence, what to check, a drafted seller message and a QR code to the listing.

  python3 scripts/build_report.py spec.json out.pdf

spec.json = {"title": "...", "subtitle": "...", "date": "October 13, 2026", "intro": "...",
             "items": [{"rank":1, "tier":"A"|"B"|"C", "name":"...", "ask":100, "pay":100, "resale":550, "profit":375,
                        "where":"Mesquite, TX (local pickup)", "img":"<craigslist image id>", "url":"https://...",
                        "what":"...", "evidence":"...", "check":"...", "seller":"...", "message":"..."}],
             "passed": "one paragraph of what was checked and rejected"}
Seller contact details go in the spec/PDF only (never in the public repo). Format rules: docs/history/report-format.md.
"""
import os, sys, json, glob, hashlib, subprocess, qrcode
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether,
                                PageBreak, Image)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from PIL import Image as PImage

F = glob.glob('/usr/share/fonts/**/DejaVuSans.ttf', recursive=True)[0]
pdfmetrics.registerFont(TTFont('D', F)); pdfmetrics.registerFont(TTFont('DB', F.replace('DejaVuSans.ttf', 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DI', F.replace('DejaVuSans.ttf', 'DejaVuSans-Oblique.ttf')))
addMapping('D', 0, 0, 'D'); addMapping('D', 1, 0, 'DB'); addMapping('D', 0, 1, 'DI'); addMapping('D', 1, 1, 'DB')
INK = colors.HexColor('#111111'); BODY = colors.HexColor('#2E2E2E'); MUT = colors.HexColor('#6E6E6E'); HAIR = colors.HexColor('#D8D8D8')
BAND = colors.HexColor('#F4F6F8'); NAVY = colors.HexColor('#14487A'); RUST = colors.HexColor('#A23B1E'); GOLD = colors.HexColor('#9A6B00')
TIER = {'A': ('TOP PICK', RUST), 'B': ('STRONG', NAVY), 'C': ('NEEDS AN ANSWER / OFFER', GOLD), 'EGG': ('GOLDEN EGG', RUST), 'LEAD': ('CHECK ON SITE', NAVY)}
S = lambda n, **k: ParagraphStyle(n, fontName=k.pop('f', 'D'), textColor=k.pop('textColor', BODY), **k)
TITLE = S('t', f='DB', fontSize=21, leading=24, textColor=INK); KICK = S('k', f='DB', fontSize=8.5, leading=11, textColor=NAVY)
LEDE = S('l', fontSize=9.6, leading=13, textColor=MUT); H2 = S('h2', f='DB', fontSize=12.5, leading=15, textColor=NAVY)
ITEM = S('it', f='DB', fontSize=11, leading=13.5, textColor=INK); BOD = S('b', fontSize=8.9, leading=11.8)
SMG = S('s', fontSize=7.9, leading=10.2, textColor=MUT); TH = S('th', f='DB', fontSize=7.6, leading=9.5, textColor=MUT)
TD = S('td', fontSize=8.6, leading=11); NR = S('nr', fontSize=8.6, leading=11, alignment=2); MSG = S('m', f='DI', fontSize=8.3, leading=11, textColor=BODY)
W = 7.3 * inch
CACHE = '/tmp/refurb_report_cache'; os.makedirs(CACHE, exist_ok=True)

def photo(img, w, h):
    if not img: return Spacer(w, h)
    import hashlib
    url = img if img.startswith('http') else f'https://images.craigslist.org/{img}_600x450.jpg'   # full URL = any source
    p = os.path.join(CACHE, (hashlib.md5(img.encode()).hexdigest() if img.startswith('http') else img) + '.jpg')
    if not os.path.exists(p):
        subprocess.run(['curl', '-s', '-L', '-m', '25', '-o', p, url])
    try:
        im = PImage.open(p); iw, ih = im.size; s = min(w / iw, h / ih)
        return Image(p, iw * s, ih * s)
    except Exception:
        return Spacer(w, h)

def qr(url, size=1.0):
    p = os.path.join(CACHE, 'qr_' + hashlib.md5(url.encode()).hexdigest() + '.png')
    if not os.path.exists(p):
        q = qrcode.QRCode(box_size=10, border=3, error_correction=qrcode.constants.ERROR_CORRECT_L); q.add_data(url); q.make(fit=True)
        q.make_image(fill_color='black', back_color='white').save(p)
    return Image(p, size * inch, size * inch)

def build(spec, out):
    def deco(c, doc):
        c.saveState(); c.setFillColor(NAVY); c.rect(0, 10.78 * inch, 8.5 * inch, 0.22 * inch, stroke=0, fill=1)
        c.setFont('DB', 7.8); c.setFillColor(MUT); c.drawString(0.6 * inch, 10.46 * inch, spec.get('header', 'REFURBISH  ·  FINDS REPORT'))
        c.drawRightString(7.9 * inch, 10.46 * inch, spec['date']); c.setStrokeColor(HAIR); c.setLineWidth(.5)
        c.line(0.6 * inch, 10.38 * inch, 7.9 * inch, 10.38 * inch); c.setFont('D', 7.8)
        c.drawCentredString(4.25 * inch, 0.45 * inch, str(doc.page)); c.restoreState()
    doc = BaseDocTemplate(out, pagesize=letter, leftMargin=0.6 * inch, rightMargin=0.6 * inch, topMargin=0.85 * inch, bottomMargin=0.62 * inch, title=spec['title'])
    doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(0.6 * inch, 0.62 * inch, W, 9.6 * inch, id='f', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=deco)])
    st = [Paragraph(spec.get('kicker', 'THE LIST'), KICK), Paragraph(spec['title'], TITLE), Paragraph(spec['intro'], LEDE), Spacer(1, 12)]
    d = [[Paragraph('#', TH), Paragraph('ITEM', TH), Paragraph('PAY', TH), Paragraph('SELLS FOR', TH), Paragraph('PROFIT', TH), Paragraph('WHERE', TH), Paragraph('PAID', TH)]]
    for it in spec['items']:
        lab, col = TIER[it['tier']]
        d.append([Paragraph(str(it['rank']), TD), Paragraph(f"{it['name']}<br/><font size=6.6 color='#{col.hexval()[2:]}'><b>{lab}</b></font>", TD),
                  Paragraph(f"<b>${it['pay']:,}</b>", NR), Paragraph(f"~${it['resale']:,}", NR), Paragraph(f"<b>~${it['profit']:,}</b>", NR),
                  Paragraph(it['where'].split(' (')[0], TD), Paragraph('$_____', SMG)])
    t = Table(d, colWidths=[.32 * inch, 2.68 * inch, .6 * inch, .8 * inch, .7 * inch, 1.45 * inch, .75 * inch], repeatRows=1)
    sty = [('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4), ('TOPPADDING', (0, 0), (-1, -1), 4),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('LINEBELOW', (0, 0), (-1, 0), .8, NAVY), ('LINEBELOW', (0, 1), (-1, -2), .4, HAIR)]
    for r in range(1, len(d)):
        if r % 2 == 0: sty.append(('BACKGROUND', (0, r), (-1, r), BAND))
    t.setStyle(TableStyle(sty)); st += [t, Spacer(1, 12), Paragraph('How to read it', H2), Paragraph(spec['howto'], BOD)]
    if spec.get('passed'): st += [Spacer(1, 10), Paragraph('Checked and rejected', H2), Paragraph(spec['passed'], SMG)]
    st += [PageBreak(), Paragraph('THE FINDS', KICK), Paragraph('What it is, what it sells for, what to ask', TITLE), Spacer(1, 10)]
    for it in spec['items']:
        lab, col = TIER[it['tier']]
        econ = (f"pay <b>${it['pay']:,}</b>" + (f" (asking ${it['ask']:,})" if it.get('ask') and it['ask'] != it['pay'] else '') +
                f" &nbsp;→&nbsp; sells for about <b>${it['resale']:,}</b> &nbsp;→&nbsp; <font color='#A23B1E'><b>~${it['profit']:,} profit</b></font> after fees and shipping both ways")
        left = [Paragraph(f"<font color='#{col.hexval()[2:]}' size=7.4><b>#{it['rank']} · {lab}</b></font>", SMG), Paragraph(it['name'], ITEM),
                Paragraph(econ, BOD), Paragraph(it['where'], SMG), Spacer(1, 4), Paragraph(f"<b>What it is.</b> {it['what']}", BOD), Spacer(1, 3),
                Paragraph(f"<b>Sold prices.</b> {it['evidence']}", BOD), Spacer(1, 3), Paragraph(f"<b>Check before paying.</b> {it['check']}", BOD),
                Spacer(1, 3), Paragraph(f"<b>Seller.</b> {it['seller']}", SMG)]
        right = [photo(it.get('img'), 1.75 * inch, 1.55 * inch), Spacer(1, 6), qr(it['url'], 1.0), Paragraph('scan to open listing', SMG)]
        inner = Table([[left, right]], colWidths=[W - 2.05 * inch, 1.85 * inch])
        inner.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('ALIGN', (1, 0), (1, 0), 'CENTER'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                                   ('RIGHTPADDING', (0, 0), (0, 0), 10), ('RIGHTPADDING', (1, 0), (1, 0), 0), ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
        msg = Paragraph(f"<b>Draft message (not sent):</b> {it['message']}", MSG) if it.get('message') else Spacer(1, 2)
        foot = Paragraph('Message OK’d ☐    Sent ☐    Reply ☐    Paid $__________    Notes ____________________________', SMG)
        outer = Table([[inner], [msg], [foot]], colWidths=[W])
        outer.setStyle(TableStyle([('LINEBEFORE', (0, 0), (0, -1), 2.4, col), ('LEFTPADDING', (0, 0), (-1, -1), 11), ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                                   ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('BACKGROUND', (0, 1), (0, 1), BAND),
                                   ('LINEBELOW', (0, 2), (0, 2), .5, HAIR)]))
        st += [KeepTogether([outer]), Spacer(1, 12)]
    doc.build(st); return out

if __name__ == '__main__':
    print(build(json.load(open(sys.argv[1])), sys.argv[2]))
