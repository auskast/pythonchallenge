def main():
    text = ''.join([line.rstrip() for line in open('ocr.txt')])
    myMap = {}
    for c in text:
        myMap[c] = myMap.get(c, 0) + 1
    avg = len(text) / len(myMap)
    output = ''.join([c for c in text if myMap[c] < avg])
    print output

if __name__ == '__main__':
    main()
