#!/usr/bin/env python3

import sys

def depart(arrival, busses):
    time = arrival

    while True:
        for bus in busses:
            if not time % bus:
                return bus * (time - arrival)
        time += 1

def main():
    arrival = int(input())
    busses = [int(x) for x in input().split(",") if x != 'x']

    print(depart(arrival, busses))

if __name__ == '__main__':
    main()
