#!/usr/bin/env python3

import sys

def follow(instr):
    current = 0
    acc = 0

    while instr[current][0] != 'DID':
        if instr[current][0] == 'nop':
            instr[current][0] = "DID"
            current += 1
        elif instr[current][0] == 'acc':
            acc += instr[current][1]
            instr[current][0] = "DID"
            current += 1
        elif instr[current][0] == 'jmp':
            instr[current][0] = "DID"
            current += instr[current][1]

    return acc

def main():
    instr = []
    for line in sys.stdin:
        instr.append(line.strip().split())
        instr[-1][1] = int(instr[-1][1])

    print(follow(instr))

if __name__ == '__main__':
    main()
