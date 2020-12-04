#!/usr/bin/env python3

import sys
import re

FIELD_RE = r'([a-z]+):(\#?\w+)'

def validate(dir):
    count = 0
    for entry in dir:
        if len(entry.keys()) == 7 and 'cid' not in entry.keys():
            count += 1
        elif len(entry.keys()) == 8:
            count += 1

    return count

def main():
    dir = []
    pp = {}

    for i in sys.stdin:
        if i == "\n":
            dir.append(pp)
            pp = {}

        for j in i.split():
            field, value = re.findall(FIELD_RE, j)[0]
            pp[field] = value

    # for last input
    dir.append(pp)
    print(validate(dir))

if __name__ == '__main__':
    main()
