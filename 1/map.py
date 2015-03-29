import string

data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def transform(data):
    trans = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    output = data.translate(trans)
    return output


def main():
    global data
    url = "http://www.pythonchallenge.com/pc/def/map.html"
    print transform(data)

if __name__ == '__main__':
    main()
