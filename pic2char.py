# -*- coding: utf-8 -*-
from PIL import Image,ImageSequence,ImageDraw,ImageFont
import os
import argparse

IMG="timg.bmp"

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`'.")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':

    if IMG.split('.')[-1]!='gif':
        with Image.open(IMG) as img:

            WIDTH,HEIGHT=img.size
            WIDTH=int(WIDTH/8)
            HEIGHT=int(HEIGHT/10)
            img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

            im = Image.new("RGB", (WIDTH * 6, HEIGHT * 8), (255, 255, 255))
            dr = ImageDraw.Draw(im)
            font = ImageFont.load_default().font

            for i in range(HEIGHT):
                txt = ""
                for j in range(WIDTH):
                    txt += get_char(*img.convert('RGB').getpixel((j, i)))
                dr.text((0, 8 * i), txt, font=font, fill="#000000")
            im.save('_'+IMG)


    else:
        with Image.open(IMG) as img:

            WIDTH,HEIGHT=img.size
            WIDTH = int(WIDTH / 4)
            HEIGHT = int(HEIGHT / 5)

            images = []

            for _im in ImageSequence.Iterator(img):
                #    images.append(_im.copy())
                _im = _im.resize((WIDTH, HEIGHT), Image.NEAREST)

                im = Image.new("RGB", (WIDTH * 6, HEIGHT * 8), (255, 255, 255))
                dr = ImageDraw.Draw(im)
                font = ImageFont.load_default().font

                for i in range(HEIGHT):
                    txt = ""
                    for j in range(WIDTH):
                        txt += get_char(*_im.convert('RGB').getpixel((j, i)))
                    dr.text((0, 8 * i), txt, font=font, fill="#000000")

                images.append(im.copy())

        images[0].save("_"+IMG, save_all=True, append_images=images[1:])
    

