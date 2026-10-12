import json,subprocess,urllib.parse,time,sys,concurrent.futures as cf
a=[x for x in json.load(open('areas.json')) if x['Country']=='US']
CATS=sys.argv[1].split(',')
SINCE=time.time()-float(sys.argv[2])*3600
def get(area,path,lat,lon):
    p={"batch":f"{area}-0-360-0-0","cc":"US","lang":"en","searchPath":path,"lat":lat,"lon":lon,"search_distance":150,"sort":"date","max_price":200,"purveyor":"owner"}
    url="https://sapi.craigslist.org/web/v8/postings/search/full?"+urllib.parse.urlencode(p)
    for t in range(3):
        try:
            out=subprocess.run(["curl","-s","--max-time","40",url],capture_output=True,text=True).stdout
            return json.loads(out)["data"]
        except Exception: time.sleep(2)
    return None
def parse(d,ar,cat):
    dec=d.get("decode");
    if not isinstance(dec,dict): return []
    res=[]
    for it in d["items"]:
        rec={"pid":dec["minPostingId"]+it[0],"posted":dec["minPostedDate"]+it[1],"price":it[3],"title":it[-1],"imgs":[],"slug":None,"uuid":None,"area":ar['Hostname'],"region":ar['Region'],"cat":cat}
        for x in it[4:-1]:
            if isinstance(x,list):
                if x[0]==4: rec["imgs"]=[i.split(":",1)[1] for i in x[1:]]
                elif x[0]==6: rec["slug"]=x[1]
                elif x[0]==13: rec["uuid"]=x[1]
        if rec["posted"]>=SINCE and rec["imgs"]: res.append(rec)
    return res
jobs=[(ar,c) for ar in a for c in CATS]
out={}
def work(j):
    ar,c=j; d=get(ar['AreaID'],c,ar['Latitude'],ar['Longitude'])
    return parse(d,ar,c) if d else []
with cf.ThreadPoolExecutor(10) as ex:
    for n,res in enumerate(ex.map(work,jobs)):
        for r in res: out.setdefault(r["pid"],r)
        if n%200==0: print(n,len(out),flush=True)
json.dump(list(out.values()),open(f'cl_nat_{int(time.time())}.json','w'))
print("DONE",len(out))
