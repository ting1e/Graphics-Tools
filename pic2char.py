from PIL import Image,ImageSequence
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`'.")


def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]




IMG="wjz.gif"
WIDTH=150
HEIGHT=60


if __name__ == '__main__':

    with Image.open(IMG) as img:
        for f in ImageSequence.Iterator(img):
            im=f.copy()
            im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
            txt=""
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    txt += get_char(*im.convert('RGB').getpixel((j,i)))
                txt += '\n'
            print(txt)



    
