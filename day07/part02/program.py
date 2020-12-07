#!/usr/bin/env python3

import sys
import re

OUTER_COLOR = r'([a-z]+ [a-z]+) bags contain'
INNER_COLOR = r'(?: (\d+) ([a-z]+ [a-z]+) bags?[,.])'


def bags_needed(bags_inside, color):
    count = 0
    if color in bags_inside:
        for bag, num in bags_inside[color]:
            count += int(num) + (int(num) * bags_needed(bags_inside, bag))
    return count



def main():
    bags_inside = {}
    count = 0

    for line in sys.stdin:
        outer_color = re.findall(OUTER_COLOR, line)[0]
        for inner_count, inner_color in re.findall(INNER_COLOR, line):
            try:
                bags_inside[outer_color].add((inner_color, inner_count))
            except KeyError:
                bags_inside[outer_color] = {(inner_color, inner_count)}

    print(bags_needed(bags_inside, "shiny gold"))



if __name__ == '__main__':
    main()
