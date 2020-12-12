#!/usr/bin/env python3

import sys

DIRECTIONS = ['E', 'S', 'W', 'N']

def travel(dir_lst):
    status = {'E' : 0, 'S' : 0, 'W' : 0, 'N' : 0}
    waypoint = {'E' : 10, 'S' : -1, 'W' : -10, 'N' : 1}

    for dir in dir_lst:
        if dir[0] in DIRECTIONS:
            waypoint[dir[0]] += dir[1]
            opposite = (DIRECTIONS.index(dir[0]) + 2) % len(DIRECTIONS)
            waypoint[DIRECTIONS[opposite]] -= dir[1]
        elif dir[0] == 'L':
            for _ in range(dir[1] // 90):
                temp_1 = waypoint['E']
                waypoint['E'] = waypoint['S']
                waypoint['S'] = waypoint['W']
                waypoint['W'] = waypoint['N']
                waypoint['N'] = temp_1
        elif dir[0] == 'R':
            for _ in range(dir[1] // 90):
                temp_1 = waypoint['E']
                waypoint['E'] = waypoint['N']
                waypoint['N'] = waypoint['W']
                waypoint['W'] = waypoint['S']
                waypoint['S'] = temp_1
        elif dir[0] == 'F':
            status['E'] += waypoint['E'] * dir[1]
            status['S'] += waypoint['S'] * dir[1]
            status['W'] += waypoint['W'] * dir[1]
            status['N'] += waypoint['N'] * dir[1]

    print(abs(status['E']) + abs(status['N']))

def main():
    dir_lst = []
    for dir in sys.stdin:
        dir_lst.append((dir[0], int(dir[1:])))

    travel(dir_lst)


if __name__ == '__main__':
    main()
