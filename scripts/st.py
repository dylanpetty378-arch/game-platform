"""Contact-sheet helper for the Lens pipeline (subset of claude/st.py)."""
import os,hashlib,subprocess,concurrent.futures as cf
from PIL import Image,ImageDraw,ImageFont
CACHE="/home/claude/sweep/imgcache"; os.makedirs(CACHE,exist_ok=True)
F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
F2=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
def fetch(u):
    if not u: return None
    p=os.path.join(CACHE,hashlib.md5(u.encode()).hexdigest()+".jpg")
    if not os.path.exists(p) or os.path.getsize(p)==0:
        subprocess.run(["curl","-s","-L","--max-time","20","-o",p,u])
    try: return Image.open(p).convert("RGB")
    except Exception: return None
def sheet(items,out,cols=8,cell=200):
    """items: list of (key, imgurl, caption)"""
    rows=(len(items)+cols-1)//cols; H=cell+30
    im=Image.new("RGB",(cols*cell,rows*H),"white"); d=ImageDraw.Draw(im)
    with cf.ThreadPoolExecutor(16) as ex: imgs=list(ex.map(lambda t:fetch(t[1]),items))
    for n,((key,u,cap),g) in enumerate(zip(items,imgs)):
        x=(n%cols)*cell; y=(n//cols)*H
        if g:
            g.thumbnail((cell-4,cell-4)); im.paste(g,(x+(cell-g.width)//2,y+(cell-g.height)//2))
        d.rectangle([x,y,x+48,y+16],fill="yellow"); d.text((x+2,y+1),str(key),fill="black",font=F)
        d.text((x+2,y+cell+1),cap[:30],fill="black",font=F2); d.text((x+2,y+cell+14),cap[30:60],fill="black",font=F2)
    im.save(out,quality=80); return out
