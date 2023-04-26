from PIL import Image
import math

def qipan(width, height, color1, color2, interval):
    im = Image.new('RGB',(width,height))
    hInterval = height/interval
    wInterval = width/interval
    for h in range(height):
        for w in range(width):
            if (int(h/hInterval)+int(w/wInterval)) % 2 == 1:
                im.putpixel((w,h), color1)
            else:
                im.putpixel((w,h), color2)
    im.show()

qipan(500, 500, (50,50,50), (240,240,240), 4)
