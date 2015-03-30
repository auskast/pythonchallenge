import urllib


def main():
    evil = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx').read()
    img1 = open('img1.jpg', 'w')
    img2 = open('img2.jpg', 'w')
    img3 = open('img3.jpg', 'w')
    img4 = open('img4.jpg', 'w')
    img5 = open('img5.jpg', 'w')
    for i in range(0, len(evil), 5):
        img1.write(evil[i])
        img2.write(evil[i+1])
        img3.write(evil[i+2])
        img4.write(evil[i+3])
        img5.write(evil[i+4])
    img1.close()
    img2.close()
    img3.close()
    img4.close()
    img5.close()


if __name__ == '__main__':
    main()
