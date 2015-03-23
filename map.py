import string

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def transform(input):
    trans = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    output = input.translate(trans)
    return output


def main():
    global input
    url = "http://www.pythonchallenge.com/pc/def/map.html"
    print transform(input)

if __name__ == '__main__':
    main()
