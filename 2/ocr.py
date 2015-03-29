def main():
    text = ''.join([line.rstrip() for line in open('ocr.txt')])
    mymap = {}
    for c in text:
        mymap[c] = mymap.get(c, 0) + 1
    avg = len(text) / len(mymap)
    output = ''.join([c for c in text if mymap[c] < avg])
    print output

if __name__ == '__main__':
    main()
