#!/usr/bin/env python3

import sys

DIRECTIONS = ['E', 'S', 'W', 'N']

def travel(dir_lst):
    status = {'E' : 0, 'S' : 0, 'W' : 0, 'N' : 0}
    pointing = 0 # East

    for dir in dir_lst:
        if dir[0] in DIRECTIONS:
            status[dir[0]] += dir[1]
            opposite = (DIRECTIONS.index(dir[0]) + 2) % len(DIRECTIONS)
            status[DIRECTIONS[opposite]] -= dir[1]
        elif dir[0] == 'L':
            pointing -= (dir[1] // 90) % len(DIRECTIONS)
            pointing %= len(DIRECTIONS)
        elif dir[0] == 'R':
            pointing += (dir[1] // 90) % len(DIRECTIONS)
            pointing %= len(DIRECTIONS)
        elif dir[0] == 'F':
            status[DIRECTIONS[pointing]] += dir[1]
            opposite = (pointing + 2) % len(DIRECTIONS)
            status[DIRECTIONS[opposite]] -= dir[1]

    print(abs(status['E']) + abs(status['N']))


def main():
    dir_lst = []
    for dir in sys.stdin:
        dir_lst.append((dir[0], int(dir[1:])))

    travel(dir_lst)


if __name__ == '__main__':
    main()
