import gzip
import difflib


def main():
    deltas = [line.rstrip() for line in gzip.open('deltas.gz').readlines()]
    left = []
    right = []
    for line in deltas:
        left.append(line[:53])
        right.append(line[56:])
    diffs = list(difflib.Differ().compare(left, right))
    img_left = open('left.png', 'wb')
    img_right = open('right.png', 'wb')
    img_common = open('common.png', 'wb')

    for line in diffs:
        line_bytes = bytearray([(chr(int(b, 16))) for b in line[2:].split()])
        if line.startswith('-'):
            map(img_left.write, line_bytes)
        elif line.startswith('+'):
            map(img_right.write, line_bytes)
        else:
            map(img_common.write, line_bytes)

    img_left.close()
    img_right.close()
    img_common.close()


if __name__ == '__main__':
    main()
