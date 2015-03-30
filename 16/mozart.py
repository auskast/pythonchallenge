import urllib
from StringIO import StringIO

from PIL import Image


MAGENTA = 195


def main():
    mozart = Image.open(StringIO(urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif').read()))
    img = mozart.copy()
    for y in range(mozart.size[1]):
        line = [mozart.getpixel((x, y)) for x in range(mozart.size[0])]
        magenta = line.index(MAGENTA)
        line = line[magenta:] + line[:magenta]
        for x, pixel in enumerate(line):
            img.putpixel((x, y), pixel)
    img.save('mozart.gif')


if __name__ == '__main__':
    main()
