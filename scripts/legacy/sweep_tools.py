"""Refurbish sweep toolkit – run in the cloud container (python3). Saved from sweep 4, Sept 21 2026.
Sources: Craigslist JSON API (sapi), OfferUp SSR JSON, ShopGoodwill buyer API, contact-sheet builder.
Facebook runs in the browser – see site-access-methods.md for the in-page snippet."""
import json,subprocess,urllib.parse,time,sys
BASE="https://sapi.craigslist.org/web/v8/postings/search/full"
def get(params):
    url=BASE+"?"+urllib.parse.urlencode(params)
    out=subprocess.run(["curl","-s","--max-time","30",url],capture_output=True,text=True).stdout
    return json.loads(out)["data"]
def search(path="sss",query=None,lat=32.934,lon=-97.229,dist=30,max_price=200,owner=True,extra=None,maxn=5000,since=0):
    res=[];off=0
    while True:
        p={"batch":f"21-{off}-360-0-0","cc":"US","lang":"en","searchPath":path,"lat":lat,"lon":lon,"search_distance":dist,"sort":"date"}
        if query:p["query"]=query
        if max_price:p["max_price"]=max_price
        if owner:p["purveyor"]="owner"
        if extra:p.update(extra)
        d=get(p); dec=d["decode"]
        if not isinstance(dec,dict): break
        minid=dec["minPostingId"]; mind=dec["minPostedDate"]
        locs=dec.get("locationDescriptions",[])
        for it in d["items"]:
            rec={"pid":minid+it[0],"posted":mind+it[1],"cat":it[2],"price":it[3],"title":it[-1],"imgs":[],"slug":None,"uuid":None,"loc":None}
            for x in it[4:-1]:
                if isinstance(x,list):
                    if x[0]==4: rec["imgs"]=[i.split(":")[1] for i in x[1:]]
                    elif x[0]==6: rec["slug"]=x[1]
                    elif x[0]==13: rec["uuid"]=x[1]
                elif isinstance(x,str) and x.startswith("1:"):
                    pass
            res.append(rec)
        tot=d["totalResultCount"]; off+=360
        if since and res and min(r["posted"] for r in res[-len(d["items"]):])<since: break
        if off>=tot or off>=maxn or not d["items"]: break
        time.sleep(1.5)
    return res,tot
def url(r): return f"https://www.craigslist.org/view/d/{r['slug']}/{r['uuid']}"
def img(r,i=0,size="300x300"): return f"https://images.craigslist.org/{r['imgs'][i]}_{size}.jpg" if r["imgs"] else ""

CATS=["ata","ara","bka","cba","cla","ela","foa","hsa","jwa","msa","pha","sga","tla","taa","vga","zip","ema","baa","gra","fua","bfa","syp","sya","moa","ppa","haa","bia"]
def sweep_cat(path,since,lo=0,hi=200,depth=0):
    """Return all posts in category since ts, splitting price bands when a page is full."""
    extra={"min_price":lo} if lo>0 else {}
    res,tot=search(path=path,max_price=hi if path!="zip" else None,extra=extra,maxn=360)
    new=[r for r in res if r["posted"]>=since]
    full=len(res)>=360 and min(r["posted"] for r in res)>=since
    if full and hi-lo>1 and depth<6:
        mid=(lo+hi)//2
        time.sleep(1)
        return sweep_cat(path,since,lo,mid,depth+1)+sweep_cat(path,since,mid+1,hi,depth+1)
    return new

# ---------------- OfferUp ----------------
import re,json,sys,subprocess,urllib.parse
CK="ou.location=%7B%22city%22%3A%22Keller%22%2C%22state%22%3A%22TX%22%2C%22zipCode%22%3A%22[zip]%22%2C%22longitude%22%3A-97.229%2C%22latitude%22%3A32.934%2C%22source%22%3A%22user%22%7D"
def ssr(params):
    url="https://offerup.com/search?"+urllib.parse.urlencode(params)
    h=subprocess.run(["curl","-s","-b",CK,url],capture_output=True,text=True).stdout
    d=json.loads(re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S).group(1))
    sf=d['props']['pageProps']['searchFeedResponse']
    out=[]
    for t in sf['looseTiles']:
        l=t.get('listing')
        if l: out.append(l)
    for m in sf.get('modules') or []:
        for t in m.get('tiles',[]) or []:
            if t.get('listing'): out.append(t['listing'])
    return out, sf.get('nextPageCursor')

def pull(q=None,pages=10,price_max=200,seen=set()):
    out=[];cur=None
    for i in range(pages):
        p={"PRICE_MAX":price_max,"SORT":"-posted"}
        if q:p["q"]=q
        if cur:p["pageCursor"]=cur
        L,cur=ssr(p)
        new=[l for l in L if l["listingId"] not in seen]
        out+=new
        if not cur or not new: break
    return out

# ---------------- ShopGoodwill ----------------
import json,subprocess
def sg(search="",page=1,size=40,low=0,high=200,sort="1",desc="false",seller="",cat=0,pickup="false",closed="false"):
    body={"isSize":False,"isWeddingCatagory":"false","isMultipleCategoryIds":False,"isFromHeaderMenuTab":False,"layout":"","searchText":search,"selectedGroup":"","selectedCategoryIds":"","selectedSellerIds":seller,"lowPrice":str(low),"highPrice":str(high),"searchBuyNowOnly":"","searchPickupOnly":pickup,"searchNoPickupOnly":"false","searchOneCentShippingOnly":"false","searchDescriptions":"false","searchClosedAuctions":closed,"closedAuctionEndingDate":"1/1/2026","closedAuctionDaysBack":"7","searchCanadaShipping":"false","searchInternationalShippingOnly":"false","sortColumn":sort,"page":str(page),"pageSize":str(size),"sortDescending":desc,"savedSearchId":0,"useBuyerPrefs":"true","searchUSOnlyShipping":"true","categoryLevelNo":"1","categoryLevel":1,"categoryId":cat,"partNumber":"","catIds":""}
    out=subprocess.run(["curl","-s","-X","POST","https://buyerapi.shopgoodwill.com/api/Search/ItemListing","-H","content-type: application/json","-d",json.dumps(body)],capture_output=True,text=True).stdout
    return json.loads(out)

# ---------------- Contact sheets ----------------
import os,io,hashlib,concurrent.futures as cf,subprocess
from PIL import Image,ImageDraw,ImageFont
CACHE="/home/claude/sweep/imgcache"; os.makedirs(CACHE,exist_ok=True)
F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
F2=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
def fetch(u):
    if not u: return None
    p=os.path.join(CACHE,hashlib.md5(u.encode()).hexdigest()+".jpg")
    if not os.path.exists(p):
        subprocess.run(["curl","-s","--max-time","20","-o",p,u])
    try: return Image.open(p).convert("RGB")
    except Exception: return None
def sheet(items,out,cols=8,cell=200,label=lambda i,x:""):
    """items: list of (key, imgurl, caption)"""
    rows=(len(items)+cols-1)//cols; H=cell+30
    im=Image.new("RGB",(cols*cell,rows*H),"white"); d=ImageDraw.Draw(im)
    with cf.ThreadPoolExecutor(16) as ex: imgs=list(ex.map(lambda t:fetch(t[1]),items))
    for n,((key,u,cap),g) in enumerate(zip(items,imgs)):
        x=(n%cols)*cell; y=(n//cols)*H
        if g:
            g.thumbnail((cell-4,cell-4)); im.paste(g,(x+(cell-g.width)//2,y+(cell-g.height)//2))
        d.rectangle([x,y,x+44,y+16],fill="yellow"); d.text((x+2,y+1),str(key),fill="black",font=F)
        d.text((x+2,y+cell+1),cap[:30],fill="black",font=F2); d.text((x+2,y+cell+14),cap[30:60],fill="black",font=F2)
    im.save(out,quality=80); return out

# ---------------- Title junk filter ----------------
import re
DROP=re.compile(r"\b(iphone|ipad|samsung|galaxy|airpods?|ps5|ps4|xbox (one|series)|nintendo switch|tv|television|monitor|laptop|macbook|chromebook|printer|router|modem|tires?|rims?|wheels?|mattress|box spring|crib|stroller|car ?seat|diapers?|formula|new in box|brand new|nib|nwt|bnib|sealed|wanted|looking for|iso|services?|cleaning|repair service|delivery|hauling|moving boxes|pallets?|firewood|mulch|dirt|gravel|fence|lumber|plywood|sheetrock|drywall|shingles|concrete|pavers|tickets?|puppy|kitten|dog food|cat food|scrubs|uniform|leggings|shein|fashion nova|dress size|jeans size|shoes size \d+|nike|jordans?|yeezy|adidas|gift card|vape|cartridge|toner|ink|air fryer|instant pot|keurig|vacuum|dyson|shark|roomba|treadmill|elliptical|dumbbells?|weights|bench press|pool table|trampoline|swing set|playhouse|power wheels|kids bike|bike|bicycle|scooter|hoverboard|golf cart|generator|pressure washer|lawn ?mower|weed eater|trimmer|leaf blower|chainsaw|window unit|ac unit|water heater|washer|dryer|refrigerator|fridge|freezer|stove|oven|dishwasher|microwave|sofa|couch|sectional|recliner|loveseat|bed frame|headboard|bunk bed|dresser|nightstand|bookshelf|bookcase|tv stand|entertainment center|dining (table|set)|kitchen table|desk|office chair|gaming chair|cabinet|curtains?|blinds|rugs?|carpet)\b",re.I)
def keep(title):
    return not DROP.search(title or "")

# ---------------- Craigslist post detail (body + 600x450 images) ----------------
import re,subprocess,html as H
def post(u):
    h=subprocess.run(["curl","-s","-L","--max-time","20",u],capture_output=True,text=True).stdout
    body=re.search(r'<section id="postingbody">(.*?)</section>',h,re.S)
    t=re.sub(r'<[^>]+>',' ',body.group(1)) if body else ''
    t=H.unescape(re.sub(r'\s+',' ',t)).replace('QR Code Link to This Post','').strip()
    attrs=re.findall(r'<span class="valu">(.*?)</span>',h,re.S)
    imgs=list(dict.fromkeys(re.findall(r'https://images\.craigslist\.org/[^"\s]+?_600x450\.jpg',h)))
    posted=re.search(r'datetime="([^"]+)"',h)
    return {"body":t,"imgs":imgs,"posted":posted.group(1) if posted else None,"attrs":[re.sub('<[^>]+>','',a).strip() for a in attrs]}


# ===================== estatesales.net (added sweep 6) =====================
import json,subprocess,concurrent.futures as cf,datetime as dt
BASE="https://www.estatesales.net"
def _get(u):
    r=subprocess.run(["curl","-s","-m","30",u],capture_output=True,text=True); return json.loads(r.stdout)
def sales(lat=32.934,lon=-97.229,miles=40):
    """All published sales within `miles` of (lat,lon). No login needed."""
    return _get(f"{BASE}/api/sale-details?bypass=bycoordinatesanddistance:{lat}_{lon}_{miles}")
def pictures(sale_id):
    """Every picture in a sale: list of dicts with url (1200px), thumbnailUrl (325px), description, utcDateCreated."""
    return _get(f"{BASE}/api/sale-details/{sale_id}?include=pictures").get("pictures",[])
def window(ss,days_ahead=7,types=("EstateSales","MovingSales","MovedOffsiteToWarehouse","MovedOffsiteToStore","ByAppointment")):
    now=dt.datetime.utcnow(); end=now+dt.timedelta(days=days_ahead)
    out=[]
    for s in ss:
        if s.get("typeName") not in types or not s.get("pictureCount"): continue
        st=dt.datetime.fromisoformat(s["firstUtcStartDate"].rstrip("Z")); en=dt.datetime.fromisoformat(s["lastUtcEndDate"].rstrip("Z"))
        if en>=now and st<=end: out.append(s)
    return out
def all_pictures(ss,workers=8):
    with cf.ThreadPoolExecutor(workers) as ex: res=list(ex.map(lambda s:pictures(s["id"]),ss))
    return {s["id"]:p for s,p in zip(ss,res)}


# ===================== liveness check (added sweep 6) =====================
"""Is a listing still up? Works from the container for Craigslist, OfferUp, estatesales.net. Facebook needs the browser (see site-access-methods.md)."""
import subprocess,re,json
def _get(u):
    r=subprocess.run(["curl","-s","-L","-m","20","-w","\n%{http_code}",u],capture_output=True,text=True); b,_,c=r.stdout.rpartition("\n"); return b,int(c or 0)
def craigslist(url):
    b,c=_get(url)
    if c==404 or re.search(r"posting has been (deleted|flagged)|This posting has expired",b,re.I): return "GONE"
    return "LIVE" if c==200 else f"?{c}"
def offerup(url):
    b,c=_get(url)
    if c==404: return "GONE"
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',b,re.S)
    if not m: return f"?{c}"
    d=json.loads(m.group(1)); rq=d["props"]["pageProps"].get("initialApolloState",{}).get("ROOT_QUERY",{})
    L=next((v for k,v in rq.items() if k.startswith("listing(")),None)
    if not L: return "GONE"
    st=L.get("state","")
    if st and st!="LISTED": return "GONE ("+st+")"
    return "LIVE"
def check(url):
    if "craigslist.org" in url: return craigslist(url)
    if "offerup.com" in url: return offerup(url)
    return "CHECK IN BROWSER"
if __name__=="__main__" and False:
    import sys
    for u in sys.argv[1:]: print(check(u),u)


# ===================== browser snippets (added sweep 7) =====================
TERAPEAK_JS = r'''window.TPR=async(q,days=365,pages=1,extra='')=>{const now=Date.now(); const out=[]; for(let pg=0;pg<pages;pg++){const u='/sh/research/api/search?marketplace=EBAY-US&keywords='+encodeURIComponent(q)+'&dayRange='+days+'&endDate='+now+'&startDate='+(now-days*864e5)+'&offset='+(pg*50)+'&limit=50&tabName=SOLD&tz=America%2FChicago&modules=searchResults'+extra;
 const ms=(await (await fetch(u)).text()).split('\n\n').filter(Boolean).map(s=>{try{return JSON.parse(s)}catch(e){return null}}).filter(Boolean);
 const sr=ms.find(m=>m._type==='SearchResultsModule'); if(!sr||!sr.results)break;
 const flat=o=>{let a=[];(function w(x){if(!x)return; if(x._type==='TextSpan'&&x.text)a.push(x.text); if(typeof x==='object')for(const k in x)w(x[k])})(o);return a};
 out.push(...sr.results.map(r=>flat(r).join(' | '))); if(sr.results.length<50)break; await new Promise(r=>setTimeout(r,1200))} return out};
window.COMP=async(q,{days=365,min=0,max=0,ex=null,n=6,pages=1}={})=>{const rows=(await TPR(q,days,pages,(min?'&minPrice='+min:'')+(max?'&maxPrice='+max:''))).map(s=>{const f=s.split(' | '); const p=parseFloat((f[3]||'').replace(/[$,]/g,'')); return {t:f[1]||'',p,d:f[f.length-1]}}).filter(r=>!ex||!new RegExp(ex,'i').test(r.t));
 const ps=rows.map(r=>r.p).sort((a,b)=>a-b); const q_=x=>ps[Math.floor(ps.length*x)];
 return q+' | n='+rows.length+' | p25 $'+q_(.25)+' | median $'+q_(.5)+' | p75 $'+q_(.75)+'\n  '+rows.slice(0,n).map(r=>'$'+r.p+' '+r.t.slice(0,55)+' ('+r.d+')').join('\n  ')};'''

HIBID_JS = r'''window.HQ=`query LS($pageNumber: Int!, $pageLength: Int!, $zip: String, $miles: Int, $status: AuctionLotStatus, $searchText: String, $sortOrder: EventItemSortOrder) {
 lotSearch(input: {zip: $zip, miles: $miles, status: $status, searchText: $searchText, sortOrder: $sortOrder, countAsView: false}, pageNumber: $pageNumber, pageLength: $pageLength, sortDirection: ASC) {
  pagedResults { totalCount results { id lead description featuredPicture { thumbnailLocation } lotState { highBid bidCount minBid buyNow timeLeftSeconds } auction { id auctioneer { name city } } } } } }`;
window.HB=async(v)=>(await fetch('/graphql',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({query:HQ,variables:Object.assign({pageNumber:1,pageLength:100,status:'OPEN'},v)})})).json();
// harvest: for p in 1..40: HB({zip:'[zip]',miles:40,pageNumber:p,sortOrder:'TIME_LEFT'})'''

# ===================== gsalr.com (added sweep 7) =====================
"""gsalr.com garage/yard/estate sales (same company as estatesales.org). No login.
POST /block/city/listings returns the ~30 sales nearest a lat/lon (radius is ignored), so tile the area with a grid and dedupe."""
import subprocess,re,html,json,concurrent.futures as cf,math
def _post(lat,lon,day=None):
    d=f"lat={lat}&lon={lon}&radius=18"+(f"&day={day}" if day else "")
    return subprocess.run(["curl","-s","-m","30","-X","POST","https://gsalr.com/block/city/listings","-H","Content-Type: application/x-www-form-urlencoded","--data",d],capture_output=True,text=True).stdout
def parse(h):
    out=[]
    for b in h.split('class="listing')[1:]:
        m=re.search(r'data-id="(\d+)"',b)
        if not m: continue
        g=lambda p:(re.search(p,b,re.S) or [None,None])[1]
        out.append({"id":m.group(1),"lat":float(g(r'data-lat="([-\d.]+)"') or 0),"lon":float(g(r'data-lon="([-\d.]+)"') or 0),
          "type":html.unescape(g(r'class="sale-type[^"]*">([^<]+)') or ""),"title":html.unescape(g(r'class="sale-title"[^>]*>([^<]+)') or ""),
          "url":g(r'href="(https://gsalr\.com/[^"?]+\.html)"'),"city":html.unescape(g(r'addressLocality">([^<]+)') or ""),
          "street":html.unescape(g(r'streetAddress"><span[^>]*>[^<]*</span>\s*([^<]+)') or ""),
          "start":g(r'itemprop="startDate" content="([^"]+)"'),"end":g(r'itemprop="endDate" content="([^"]+)"'),
          "descr":html.unescape(re.sub(r'<[^>]+>',' ',g(r'itemprop="description">(.*?)</p>') or "")).strip(),
          "photos":int(g(r'class="photo-count">(\d+)') or 0),"thumb":g(r'<img src="(https://eso-cdn[^"]+)"')})
    return out
def grid(lat=32.934,lon=-97.229,miles=35,step=8):
    pts=[]; dl=step/69.0; dn=step/(69.0*math.cos(math.radians(lat))); n=int(miles/step)
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if (i*step)**2+(j*step)**2<=miles**2: pts.append((round(lat+i*dl,4),round(lon+j*dn,4)))
    return pts
def sweep(**kw):
    with cf.ThreadPoolExecutor(6) as ex: pages=list(ex.map(lambda p:_post(*p),grid(**kw)))
    seen={}
    for h in pages:
        for s in parse(h): seen.setdefault(s["id"],s)
    return list(seen.values())
def photos(url):
    """All photo URLs on a sale page (full-size: drop the '-t' thumbnail suffix)."""
    h=subprocess.run(["curl","-s","-m","30",url+"?gallery=1"],capture_output=True,text=True).stdout
    return list(dict.fromkeys(re.findall(r'https://ps\.tlstatic\.com/image/w\d+-h\d+/[^"\s]+?\.jpe?g',h)))


# ===================== estate photo zoom (added sweep 7) =====================
"""Usage: python3 esn_zoom.py OUT.jpg idx1 idx2 ... -> 4-col sheet of full-size photos (420px cells) with sale/city/caption."""
import sys,json
def esn_zoom(out,ks):
    idx=json.load(open('/home/claude/sweep/esn_idx.json'))
    sheet([(k,idx[k]['url'],(idx[k]['city']+' '+(idx[k]['desc'] or ''))[:60]) for k in ks],out,cols=4,cell=420)

# ===================== Facebook category feed (added sweep 8) =====================
FB_CATEGORY_JS = r"""
// On a category page (e.g. /marketplace/fortworth/antiques?sortBy=creation_time_descend):
const html=document.documentElement.innerHTML; const re=/"queryID":"(\d+)","variables":/g; let m;
while((m=re.exec(html))){let j=m.index+m[0].length,d=0,k=j; for(;k<html.length;k++){const c=html[k]; if(c==='{')d++; else if(c==='}'){d--; if(!d){k++;break}}}
  const v=html.slice(j,k); if(v.includes('"bqf"')&&v.includes('"count"')){window.DOC=m[1]; window.CV=JSON.parse(v); break}}
window.FBT={dtsg:require('DTSGInitialData').token, lsd:require('LSD').token, uid:require('CurrentUserInitialData').USER_ID};
window.FBQ=async(vars)=>{const b=new URLSearchParams({av:FBT.uid,__user:FBT.uid,__a:'1',fb_dtsg:FBT.dtsg,lsd:FBT.lsd,fb_api_caller_class:'RelayModern',fb_api_req_friendly_name:'CometMarketplaceSearchContentContainerQuery',variables:JSON.stringify(vars),server_timestamps:'true',doc_id:DOC}); return (await fetch('/api/graphql/',{method:'POST',body:b,headers:{'content-type':'application/x-www-form-urlencoded','x-fb-lsd':FBT.lsd}})).text()};
window.FBC=window.FBC||{};
window.FBSEO=async(seo,{maxPages=40,lat=32.934,lon=-97.229,km=50,maxPrice=200,days=null,shipping=true}={})=>{const V=JSON.parse(JSON.stringify(CV)); V.buyLocation={latitude:lat,longitude:lon}; const B=V.params.browse_request_params;
 Object.assign(B,{commerce_search_and_rp_category_id:null,commerce_enable_shipping:shipping,filter_location_latitude:lat,filter_location_longitude:lon,filter_radius_km:km,filter_price_upper_bound:maxPrice*100,commerce_search_and_rp_ctime_days:days,commerce_search_sort_by:'CREATION_TIME_DESCEND'});
 V.params.custom_request_params.seo_url=seo; V.params.custom_request_params.serp_landing_settings={virtual_category_id:seo}; V.count=24; let cur=null,pages=0,got=0;
 while(pages<maxPages){V.cursor=cur; let f; try{f=JSON.parse((await FBQ(V)).split('\n')[0])?.data?.marketplace_search?.feed_units}catch(e){break} if(!f)break;
  for(const e of f.edges){const L=e.node&&e.node.listing; if(!L||!L.id||FBC[L.id])continue; FBC[L.id]={id:L.id,t:L.marketplace_listing_title,p:+L.listing_price?.amount,c:L.location?.reverse_geocode?.city,img:L.primary_listing_photo?.image?.uri,sold:L.is_sold||L.is_pending,cat:seo}; got++}
  pages++; if(!f.page_info?.has_next_page)break; cur=f.page_info.end_cursor; await new Promise(r=>setTimeout(r,600))} return seo+':'+pages+'p/+'+got};
// then: localStorage.GRIDDATA=JSON.stringify(Object.values(FBC).map(x=>[x.id,x.p,x.t,x.img,x.c])); close this tab; review on facebook.com/robots.txt with G(start)
"""
FB_LIGHT_GRID_JS = r"""
window.D=JSON.parse(localStorage.GRIDDATA);
window.G=(s)=>{document.body.style.margin='0'; document.body.innerHTML='<div style="display:grid;grid-template-columns:repeat(20,1fr);grid-auto-rows:118px;gap:1px;font:9px/10px arial">'+D.slice(s,s+140).map((L,i)=>`<div style="overflow:hidden"><img src="${L[3]}" style="width:100%;height:92px;object-fit:cover"><b>${s+i} $${L[1]}</b> ${(L[2]||'').replace(/</g,'').slice(0,24)}</div>`).join('')+'</div>'; return D.length};
"""
