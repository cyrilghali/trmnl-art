import json,sys,time,urllib.request,urllib.parse,os
UA={"User-Agent":"trmnl-art/1.0 (personal e-ink frame)"}
Q=json.loads(sys.argv[1])
def get(u):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
        except Exception as e: print("retry",e,file=sys.stderr); time.sleep(10*(i+1))
out=json.load(open("raw2/sources2.json"))
for k,q in Q.items():
    if os.path.exists(f"raw2/{k}.jpg"): continue
    r=get("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({"action":"query","format":"json","generator":"search","gsrsearch":q+" filetype:bitmap","gsrnamespace":6,"gsrlimit":3,"prop":"imageinfo","iiprop":"url|size|mime","iiurlwidth":2400}))
    if not r: print(k,"API FAILED"); continue
    pages=sorted(json.loads(r).get("query",{}).get("pages",{}).values(),key=lambda p:p["index"])
    pages=[p for p in pages if p["imageinfo"][0]["mime"] in("image/jpeg","image/png","image/tiff")]
    if not pages: print(k,"NONE"); continue
    p=pages[0]; ii=p["imageinfo"][0]; data=get(ii.get("thumburl") or ii["url"])
    if not data: print(k,"FAILED"); time.sleep(20); continue
    open(f"raw2/{k}.jpg","wb").write(data); out[k]={"title":p["title"],"page":ii["descriptionurl"]}
    json.dump(out,open("raw2/sources2.json","w"),ensure_ascii=False,indent=1)
    print(k,"|",p["title"],ii["width"],ii["height"]); time.sleep(10)
