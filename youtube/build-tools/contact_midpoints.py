import sys,json,math
from pathlib import Path
from PIL import Image,ImageDraw
for arg in sys.argv[1:]:
 r=Path(arg);s=json.loads((r/'beat_sheet.json').read_text());out=r/'_qc/master';tilew=400;tileh=250;im=Image.new('RGB',(1600,tileh*math.ceil(len(s['beats'])/4)),'white');draw=ImageDraw.Draw(im)
 for i,b in enumerate(s['beats']):
  f=out/f"{b['beat_id']}-50.jpg";x=i%4*tilew;y=i//4*tileh;pic=Image.open(f).resize((400,225));im.paste(pic,(x,y));draw.text((x+8,y+230),b['beat_id'],fill='black')
 im.save(out/'midpoints.jpg',quality=90);print(out/'midpoints.jpg')
