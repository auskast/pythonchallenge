import urllib
import re


def getnothing(nothing):
    return urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing)


def main():
    nothing = '12345'
    pattern = re.compile('nothing is (\d+)')
    while True:
        data = getnothing(nothing).read()
        print data
        search = pattern.search(data)
        if search:
            nothing = search.group(1)
            print nothing
        else:
            break


if __name__ == '__main__':
    main()
