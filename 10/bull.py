def printcount(n):
    res = '1'
    for i in range(0, n):
        out = []
        for c in res:
            if len(out) == 0 or out[-1][0] != c:
                out.append((c, 1))
            else:
                out[-1] = (c, out[-1][1] + 1)
        res = ''.join([str(a[1]) + a[0] for a in out])
    return res


def main():
    print len(printcount(30))


if __name__ == '__main__':
    main()
