#!/usr/bin/env python3

import sys
import re

count = 0

def parse(passwords):
    global count

    for p in passwords:
        letterCount = 0

        parsed = re.split('-|\s|(:\s)', p)
        for i, c in enumerate(parsed[-1]):
            if c == parsed[4]:
                if i == int(parsed[0]) - 1 or i == int(parsed[2]) - 1:
                    letterCount += 1
        if letterCount == 1:
            count += 1


def main():
    passwords = []
    for i in sys.stdin:
        passwords.append(i.strip())

    parse(passwords)
    print(count)

if __name__ == '__main__':
    main()
