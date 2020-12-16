#!/usr/bin/env python3

import sys
import re
from collections import defaultdict
import math

FIELD = r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$'
meaning_dict = defaultdict(str)

def remove_tickets(fields, ticket):
    return all(any((min_1 <= val <= max_1 or min_2 <= val <= max_2) for min_1, max_1, min_2, max_2 in fields.values()) for val in ticket)

def find_meaning(fields, tickets, omit):
    meaning = []

    for i in range(20):
        all_fields = list(fields.keys())
        for field in omit:
            try:
                all_fields.remove(field)
            except ValueError:
                continue

        for ticket in tickets:
            value = ticket[i]
            for key in fields:
                min_1, max_1, min_2, max_2 = fields[key]
                if min_1 <= value <= max_1 or min_2 <= value <= max_2:
                    continue
                else:
                    try:
                        all_fields.remove(key)
                    except ValueError:
                        continue

        if len(all_fields) == 1:
            meaning_dict[i] = all_fields[0]
            return all_fields[0]

def main():
    fields = defaultdict(tuple)
    tickets = []

    for line in sys.stdin:
        if s := re.findall(FIELD, line):
            fields[s[0][0]] = tuple(map(int, (s[0][1], s[0][2], s[0][3], s[0][4])))
        elif line.startswith("your ticket:"):
            my_ticket = input().split(",")
        elif line.startswith("nearby tickets:"):
            while t := sys.stdin.readline():
                tickets.append(list(map(int, t.strip().split(","))))
            break

    # remove tickets
    tickets = [ticket for ticket in tickets if remove_tickets(fields, ticket)]

    omit = []
    while len(meaning_dict) < 20:
        omit.append(find_meaning(fields, tickets, omit))

    ans = 1
    for key, val in meaning_dict.items():
        if val.startswith("departure"):
            ans *= int(my_ticket[key])

    print(ans)

if __name__ == '__main__':
    main()
