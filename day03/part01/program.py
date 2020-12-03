#!/usr/bin/env python3

import sys

startX = 0
startY = 0
moveY = 1
moveX = 3
inputLength = 30

def travel(plane):
    trees = 0
    currentX = startX
    currentY = startY

    if plane[startY][startX] == '#':
        trees += 1

    while True:
        currentX += moveX
        currentY += moveY

        if currentY >= len(plane):
            break

        if currentX > inputLength:
            currentX = currentX - inputLength - 1

        if plane[currentY][currentX] == '#':
            trees += 1

    return trees



def main():
    plane = []
    for i in sys.stdin:
        plane.append([c for c in str(i.strip())])

    print(travel(plane))

if __name__ == '__main__':
    main()
