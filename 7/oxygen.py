from PIL import Image
import StringIO
import urllib


def main():
    oxygen = Image.open(StringIO.StringIO(urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()))
    y = oxygen.size[1] / 2
    imgstr = ''.join([chr(oxygen.getpixel((x, y))[0]) for x in range(0, oxygen.size[0], 7)])
    arr = imgstr[imgstr.index('[')+1:imgstr.index(']')].split(', ')
    output = ''.join([chr(int(num)) for num in arr])
    print output


if __name__ == '__main__':
    main()
