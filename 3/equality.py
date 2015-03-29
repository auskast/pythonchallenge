def solution1(text):
    text = 'x' + text + 'x'
    output = ''
    for i in range(3, len(text) - 4):
        if (text[i-4] + text[i] + text[i+4]).islower() and (text[i-3:i] + text[i+1:i+4]).isupper():
            output += text[i]
    return output


def solution2(text):
    text = 'xx' + text + 'xx'
    markers = ''.join(['1' if c.isupper() else '0' for c in text])
    pattern = '011101110'

    def f(res, t, _markers):
        n = len(_markers.partition(pattern)[0])
        return f(res + t[n+4], t[n+4:], _markers[n+4:]) if n != len(_markers) else res
    return f('', text, markers)


def main():
    text = ''.join([line.rstrip() for line in open('equality.txt')])
    print solution2(text)


if __name__ == '__main__':
    main()
