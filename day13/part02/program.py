#!/usr/bin/env python3

import sys
import math

# Method accredited to pbui

def find_next_time(start, increment, bus, i):
    while (start + i) % bus:
        start += increment
    return start

def main():
    input()
    busses = [int(x) if x != 'x' else 0 for x in input().split(",")]
    time = busses[0]
    increment = time

    for i, bus in enumerate(busses):
        if not bus or not i:
            continue
        time = find_next_time(time, increment, bus, i)
        increment *= bus

    print(time)

if __name__ == '__main__':
    main()
