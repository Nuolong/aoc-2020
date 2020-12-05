#!/usr/bin/env python3

import sys
import math

def findRC(locs):
    upper = 127
    lower = 0
    upperC = 7
    lowerC = 0
    row, col = 0, 0

    for letter in locs:
        if letter == 'F':
            upper = lower + (upper - lower) // 2
        elif letter == 'B':
            lower = math.ceil((upper + lower) / 2)
        elif letter == 'L':
            upperC = lowerC + (upperC - lowerC) // 2
        elif letter == 'R':
            lowerC = math.ceil((upperC + lowerC) / 2)

    if locs[6] == 'F':
        row = lower
    else:
        row = upper

    if locs[-1] == 'L':
        col = lowerC
    else:
        col = upperC

    return 8 * row + col

def main():
    locList = [i.strip() for i in sys.stdin]

    idList = [findRC(id) for id in locList]

    for i in range(min(idList), max(idList)):
        if i not in idList:
            print(i)

if __name__ == '__main__':
    main()
