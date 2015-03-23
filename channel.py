import zipfile
import re


def main():
    raw = zipfile.ZipFile(open('channel.zip', 'r'))
    nothing = '90052'
    comments = []
    pattern = re.compile('nothing is (\d+)')
    while True:
        filename = nothing + '.txt'
        data = raw.read(filename)
        comments.append(raw.getinfo(filename).comment)
        search = pattern.search(data)
        if search:
            nothing = search.group(1)
        else:
            break
    print ''.join(comments)


if __name__ == '__main__':
    main()
