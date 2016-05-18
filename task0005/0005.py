#-*-coding:utf-8-*-
import os
import Image
path = raw_input("输入路径名称：")
for f in os.listdir(path):
    img = Image.open(os.path.join(path,f))
    width = img.size[0]
    height = img.size[1]
    out = img
    if width >1136:
        width = 1136
        out = img.resize((width,height),Image.ANTIALIAS)
    if height>640:
        height = 640
        out = img.resize((width,height),Image.ANTIALIAS)
    os.mkdir('./img/')
    out.save('./img/'+f)

