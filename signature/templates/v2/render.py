from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageSequence
import numpy as np, sys, os, json
SLUG,NAME,TITLE,WA=sys.argv[1:5]
M=28; SCALE=500/560   # display scale vs design px
num='+974 '+WA[:4]+' '+WA[4:]
h=open('card.html').read().replace('NAME',NAME).replace('TITLE',TITLE).replace('NUMBER',num)
open('card_r.html','w').write(h)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':800,'height':400},device_scale_factor=2)
    pg.goto('file://./card_r.html'); pg.wait_for_timeout(400)
    pg.locator('#card').screenshot(path='base.png'); b.close()
base=Image.open('base.png').convert('RGBA')
g=Image.open('../../images/capstone-emblem-premium-navy.gif')
gf=[(f.convert('RGBA'),f.info.get('duration',40)) for f in ImageSequence.Iterator(g)]
full=base.copy(); full.alpha_composite(gf[0][0],(52,44))
a=np.array(full.convert('RGB')).astype(int); ink=np.abs(a-np.array([0,56,80])).sum(2)>60
ys,xs=np.where(ink); x0,y0,x1,y1=xs.min(),ys.min(),xs.max()+1,ys.max()+1
m=2*M; box=(x0-m,y0-m,x1+m,y1+m); W,H=box[2]-box[0],box[3]-box[1]
OW=round(W/2*SCALE)*2; OH=round(H*OW/W)
big=Image.new('L',(OW*4,OH*4),0); ImageDraw.Draw(big).rounded_rectangle([0,0,OW*4-1,OH*4-1],radius=int(36*SCALE*4*OW/OW),fill=255)
mask=big.resize((OW,OH),Image.LANCZOS)
frames=[];durs=[]
for f,d in gf:
    fr=base.copy(); fr.alpha_composite(f,(52,44)); fr=fr.crop(box).resize((OW,OH),Image.LANCZOS); fr.putalpha(mask)
    frames.append(fr); durs.append(d)
transp=np.array(mask)<128
rgb=[fr.convert('RGB') for fr in frames]
mont=Image.new('RGB',(OW,OH*4))
for i,k in enumerate([0,len(rgb)//3,2*len(rgb)//3,len(rgb)-1]): mont.paste(rgb[k],(0,OH*i))
pal=mont.quantize(colors=255,method=Image.MEDIANCUT,dither=Image.NONE).getpalette()[:255*3]+[0,0,0]
P=np.array(pal,np.float32).reshape(-1,3)[:255]
out=[]
for fr in rgb:
    aa=np.array(fr,np.float32).reshape(-1,3); idx=np.empty(len(aa),np.uint8)
    for s in range(0,len(aa),40000): idx[s:s+40000]=np.argmin(((aa[s:s+40000,None,:]-P[None])**2).sum(-1),1)
    idx=idx.reshape(OH,OW); idx[transp]=255
    im=Image.fromarray(idx,'P'); im.putpalette(pal); out.append(im)
PP=f'../../people/{SLUG}/'
out[0].save(PP+'card.gif',save_all=True,append_images=out[1:],duration=durs,loop=0,transparency=255,disposal=1)
frames[0].save('f0.png')
json.dump({'w':OW//2,'h':OH/2},open('size.json','w'))
print('ink box',box,'out',OW,OH,'display',OW//2,OH/2,os.path.getsize(PP+'card.gif'))
