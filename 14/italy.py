import urllib
from StringIO import StringIO

from PIL import Image


def main():
    wire = Image.open(StringIO(urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/wire.png').read()))
    out = Image.new('RGB', (100, 100))
    offset = 0
    dirx = 1
    diry = 0
    x = y = 0
    for p in range(0, 10000):
        out.putpixel((x, y), wire.getpixel((p, 0)))
        # top right -> go down
        if dirx == 1 and x == 99 - offset:
            dirx = 0
            diry = 1
        # bottom left -> go up
        elif dirx == -1 and x == offset:
            dirx = 0
            diry = -1
        # bottom right -> go left
        elif diry == 1 and y == 99 - offset:
            dirx = -1
            diry = 0
        # top left -> come in a layer, go right
        elif diry == -1 and y == offset + 1:
            offset += 1
            dirx = 1
            diry = 0
        x += dirx
        y += diry
    out.save('italy.png')


if __name__ == '__main__':
    main()
