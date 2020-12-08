#!/usr/bin/env python3

import sys

def follow(instr):
    visited = []
    current = 0
    acc = 0

    while current not in visited:
        if current == len(instr) - 1:
            return acc, current
        if instr[current][0] == 'nop':
            visited.append(current)
            current += 1
        elif instr[current][0] == 'acc':
            acc += instr[current][1]
            visited.append(current)
            current += 1
        elif instr[current][0] == 'jmp':
            visited.append(current)
            current += instr[current][1]

    return acc, current

def find_success(instr):
    finish = len(instr) - 1

    for i in instr:
        if i[0] == 'nop':
            i[0] = 'jmp'
            acc, fin = follow(instr)
            if fin == finish:
                return acc
            i[0] = 'nop'
        elif i[0] == 'jmp':
            i[0] = 'nop'
            acc, fin = follow(instr)
            i[0] = 'jmp'
            if fin == finish:
                return acc

def main():
    instr = []
    for line in sys.stdin:
        instr.append(line.strip().split())
        instr[-1][1] = int(instr[-1][1])

    print(find_success(instr))

if __name__ == '__main__':
    main()
