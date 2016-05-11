#!/usr/bin/env python
from PIL import Image,ImageDraw,ImageFont
def add_num(num,fonttype,fill):
        im = Image.open("./12.jpg")
        text = str(num)
        x,y = im.size
        font = ImageFont.truetype(fonttype,x/5);
        draw = ImageDraw.Draw(im)
        draw.text((x-x/5,0),text,fill,font)
        im.save('./output.jpg')

num = 5
fonttype = "verdana.ttf"
fill = (255,0,255)
add_num(num,fonttype,fill)

