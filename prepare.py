import glob, os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
W,H=1872,1404
os.makedirs("out",exist_ok=True); th=[]
B={"carceri-xiv":.04,"kumoi-cherry":.04,"lonely-tower":.09,"montmajour":.09,"three-trees":.05,"kambara-snow":.02,"pines-left":.06,"pines-right":.06}
for f in sorted(glob.glob("raw/*.jpg")):
    n=os.path.basename(f)
    im=ImageOps.grayscale(Image.open(f))
    im=ImageOps.fit(im,(W,H),Image.LANCZOS,bleed=B.get(n[:-4],0),centering=(0.5,0.5))
    im=ImageOps.autocontrast(im,cutoff=(0.5,0.5))
    im.save("out/"+n,quality=88,optimize=True)
    th.append(im.resize((468,351)))
sheet=Image.new("L",(4*480,((len(th)+3)//4)*363),128)
for i,t in enumerate(th): sheet.paste(t,(6+(i%4)*480,6+(i//4)*363))
sheet.save("sheet.jpg",quality=85)
print(sorted(os.listdir("out")))
