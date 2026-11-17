import glob, os, sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
W,H=1872,1404
# The riddle often sits at the edge (Icarus's legs, the Ambassadors' skull), so crop only works already close to 4:3.
# Portrait works keep their own shape: the layout puts a note beside them instead of white bars.
os.makedirs("out2",exist_ok=True)
for f in sorted(glob.glob("raw2/*.jpg")):
    n=os.path.basename(f)
    im=ImageOps.autocontrast(ImageOps.grayscale(Image.open(f)),cutoff=(0.5,0.5))
    r=im.width/im.height
    if r<1.05: im=im.resize((round(H*r),H),Image.LANCZOS)
    elif 1.2<=r<=1.5: im=ImageOps.fit(im,(W,H),Image.LANCZOS)
    else: im=ImageOps.pad(im,(W,H),Image.LANCZOS,color=255)
    im.save("out2/"+n,quality=88,optimize=True); print(n, round(r,2), im.size)
