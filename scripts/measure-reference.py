import sys, numpy as np
from PIL import Image
def hx(c): return '#%02X%02X%02X'%tuple(int(v) for v in c[:3])
def runs(mask):
    out=[];s=None
    for i,v in enumerate(mask):
        if v and s is None: s=i
        if not v and s is not None: out.append((s,i-1)); s=None
    if s is not None: out.append((s,len(mask)-1))
    return out
for p in sys.argv[1:]:
    im=Image.open(p).convert('RGB'); a=np.asarray(im).astype(int); H,W,_=a.shape
    bg=np.median(np.array([a[2,2],a[2,W-3],a[H-3,2],a[H-3,W-3]]),axis=0)
    d=np.abs(a-bg).sum(axis=2); notbg=d>30
    colfrac=notbg.mean(axis=0); rowfrac=notbg.mean(axis=1)
    cols=[r for r in runs(colfrac>0.15) if r[1]-r[0]>20]
    rows=[r for r in runs(rowfrac>0.15) if r[1]-r[0]>20]
    print(f"\n=== {p.split('/')[-1]}  {W}x{H}  ratio {W/H:.3f}  outer bg {hx(bg)} rgb{tuple(int(x) for x in bg)}")
    print(" column runs:",cols); print(" row runs:",rows)
    for ri,(y0,y1) in enumerate(rows):
      for ci,(x0,x1) in enumerate(cols):
        sub=notbg[y0:y1+1,x0:x1+1]
        # tighten box
        ys=np.where(sub.mean(axis=1)>0.3)[0]; xs=np.where(sub.mean(axis=0)>0.3)[0]
        if len(ys)==0 or len(xs)==0: continue
        py0,py1=y0+ys[0],y0+ys[-1]; px0,px1=x0+xs[0],x0+xs[-1]
        w=px1-px0+1;h=py1-py0+1
        # corner radius estimate: on the top row, first non-bg x offset
        topr=notbg[py0+1,px0:px1]; rad=int(np.argmax(topr)) if topr.any() else -1
        leftc=notbg[py0:py1,px0+1]; rad2=int(np.argmax(leftc)) if leftc.any() else -1
        crop=im.crop((px0,py0,px1+1,py1+1))
        q=crop.quantize(colors=7,method=Image.Quantize.MEDIANCUT)
        pal=q.getpalette()[:21]; cnt=sorted(q.getcolors(),reverse=True)
        tot=sum(c for c,_ in cnt)
        cols_s=", ".join(f"{hx(pal[i*3:i*3+3])} {100*c/tot:.0f}%" for c,i in cnt)
        print(f" panel r{ri}c{ci}: x{px0}-{px1} y{py0}-{py1}  {w}x{h} ratio {w/h:.3f} (w/h; 1290/2796=0.461)  radius~{rad}/{rad2}px ({100*max(rad,rad2)/w:.1f}% of w)")
        print(f"   palette: {cols_s}")
    if len(cols)>1:
        gaps=[cols[i+1][0]-cols[i][1]-1 for i in range(len(cols)-1)]; print(" col gaps:",gaps)
