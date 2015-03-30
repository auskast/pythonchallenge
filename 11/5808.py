import urllib
from StringIO import StringIO

from PIL import Image


def main():
    cave = Image.open(StringIO(urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg').read()))
    even = Image.new('RGB', (640, 480))
    odd = Image.new('RGB', (640, 480))
    for x in range(0, cave.size[0], 2):
        for y in range(0, cave.size[1], 2):
            even.putpixel((x, y), cave.getpixel((x, y)))
            odd.putpixel((x+1, y+1), cave.getpixel((x+1, y+1)))

    even = even.resize((cave.size[0] / 2, cave.size[1] / 2))
    odd = odd.resize((cave.size[0] / 2, cave.size[1] / 2))

    even.save('even.jpg')
    odd.save('odd.jpg')


if __name__ == '__main__':
    main()
