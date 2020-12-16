#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

FIELD = r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$'

def error_rate(fields, tickets):
    error = 0
    for ticket in tickets:
        for field in ticket:
            f = False
            for min_1, max_1, min_2, max_2 in fields.values():
                if min_1 <= field <= max_1 or min_2 <= field <= max_2:
                    f = True
            if not f:
                error += field

    return error

def main():
    fields = defaultdict(tuple)
    tickets = []

    for line in sys.stdin:
        if s := re.findall(FIELD, line):
            fields[s[0][0]] = tuple(map(int, (s[0][1], s[0][2], s[0][3], s[0][4])))
        elif line.startswith("your ticket:"):
            input()
        elif line.startswith("nearby tickets:"):
            while t := sys.stdin.readline():
                tickets.append(list(map(int, t.strip().split(","))))
            break

    print(error_rate(fields, tickets))

if __name__ == '__main__':
    main()
