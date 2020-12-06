#!/usr/bin/env python3

import sys
import math

def main():
    group = {}
    total = 0
    people = 0

    for i in sys.stdin:
        if i == "\n":
            total += sum(x == people for x in group.values())
            group = {}
            people = 0

        for j in i.split():
            people += 1
            for char in j:
                group[char] = group.get(char, 0) + 1

    # for last input
    total += sum(x == people for x in group.values())
    print(total)


if __name__ == '__main__':
    main()
