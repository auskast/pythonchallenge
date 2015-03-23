import pickle
import urllib


def main():
    banner = pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
    for row in banner:
        print ''.join(val[1] * val[0] for val in row)


if __name__ == '__main__':
    main()
