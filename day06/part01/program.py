#!/usr/bin/env python3

import sys
import math

def main():
    group = set()
    total = 0

    for i in sys.stdin:
        if i == "\n":
            total += len(group)
            group = set()

        for j in i.split():
            group = group | {char for char in j}

    # for last input
    total += len(group)
    print(total)


if __name__ == '__main__':
    main()
