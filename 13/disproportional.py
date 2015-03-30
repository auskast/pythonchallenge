import xmlrpclib
import urllib


def main():
    server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
    print server.system.listMethods()
    print server.phone('Evil')
    evil = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/evil4.jpg').read()
    print evil
    print server.phone('Bert')


if __name__ == '__main__':
    main()
