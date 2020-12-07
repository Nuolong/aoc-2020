#!/usr/bin/env python3

import sys
import re

OUTER_COLOR = r'([a-z]+ [a-z]+) bags contain'
INNER_COLOR = r'(?: (\d+) ([a-z]+ [a-z]+) bags?[,.])'

has_shiny_gold = set()

def shiny_gold(has_bag, color):
    global has_shiny_gold
    if color in has_bag:
        for clr in has_bag[color]:
            try:
                has_shiny_gold.add(clr)
            except KeyError:
                has_shiny_gold = {clr}
            shiny_gold(has_bag, clr)

def main():
    has_bag = {}
    count = 0

    for line in sys.stdin:
        outer_color = re.findall(OUTER_COLOR, line)[0]
        for inner_count, inner_color in re.findall(INNER_COLOR, line):
            try:
                has_bag[inner_color].add(outer_color)
            except KeyError:
                has_bag[inner_color] = {outer_color}

    shiny_gold(has_bag, "shiny gold")
    print(len(has_shiny_gold))


if __name__ == '__main__':
    main()
