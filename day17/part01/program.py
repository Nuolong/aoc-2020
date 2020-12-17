#!/usr/bin/env python3

import sys
from collections import defaultdict
import copy

def neighbors(space):
    new_space = copy.deepcopy(space)

    for x in range(-15, 15):
        for y in range(-15, 15):
            for z in range(-15, 15):
                count = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        for dz in (-1, 0, 1):
                            if (dx or dy or dz) and space.get((x + dx, y + dy, z + dz), '.') == '#':
                                count += 1
                if space.get((x, y, z), '.') == '#' and not (2 <= count <= 3):
                    new_space[(x, y, z)] = '.'
                elif space.get((x, y, z), '.') == '.' and count == 3:
                    new_space[(x, y, z)] = '#'

    return new_space

def main():
    space = defaultdict(str)

    for idx_1, line in enumerate(sys.stdin):
        for idx_2, val in enumerate(line.strip()):
            space[(idx_1, idx_2, 0)] = val

    for x in range(6):
        space = neighbors(space)

    num = 0
    for s in space.values():
        if s == '#':
            num += 1

    print(num)


if __name__ == '__main__':
    main()
