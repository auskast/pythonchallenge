import urllib2
from urllib import quote_plus, unquote_plus
import re
import bz2
import xmlrpclib


def getpattern(pattern, data):
    search = pattern.search(data)
    return search.group(1) if search else None


def main():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s'
    nothing = '12345'
    pattern = re.compile(r'nothing is (\d+)')
    cpattern = re.compile(r'info=([^;]*);')
    compressed = []
    while True:
        data = urllib2.urlopen(url % nothing)
        cookie = data.info().getheader('Set-Cookie')
        info = getpattern(cpattern, cookie)
        if info:
            compressed.append(info)
        nothing = getpattern(pattern, data.read())
        if not nothing:
            break
    message = bz2.decompress(unquote_plus(''.join(compressed)))
    print message
    server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
    print server.phone('Leopold')
    info = quote_plus('the flowers are on their way')
    req = urllib2.Request('http://www.pythonchallenge.com/pc/stuff/violin.php', headers={'Cookie': 'info=' + info})
    print urllib2.urlopen(req).read()


if __name__ == '__main__':
    main()
