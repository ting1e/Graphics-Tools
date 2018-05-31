#coding=utf-8
import os
from PIL import Image, ImageDraw
import re

IMG="123.png"

with Image.open(IMG) as img:
    WIDTH, HEIGHT = img.size
    out = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
    single=10
    draw=ImageDraw.Draw(out)
    newWidth=int(WIDTH/single)
    newHeigh=int(HEIGHT/single)

    for i in range(newWidth):
        print(i)
        for j in range(newHeigh):
            rgb=[0,0,0]

            for x in range(5):
                for y in range(5):
                    a,b,c = img.convert('RGB').getpixel((x*single/5+i*single,y*single/5+j*single))
                    rgb[0]+=a
                    rgb[1]+=b
                    rgb[2]+=c

            draw.rectangle((i*single,j*single,i*single+single,j*single+single),fill=(int(rgb[0]/25),int(rgb[1]/25),int(rgb[2]/25)))


out.save('1_'+IMG)