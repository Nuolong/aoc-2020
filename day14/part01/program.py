#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

MASK = r'mask = (.+)'
MEM = r'mem\[(\d+)\] = (\d+)'

memory = defaultdict(int)

def apply_masks(mask, mem_lst):
    for inst in mem_lst:
        res = [0] * 36
        num = bin(int(inst[1]))[2:]
        for i, bit in enumerate(num[::-1]):
            res[i] = bit
        for m in mask:
            res[m[0]] = m[1]
        res.reverse()
        memory[inst[0]] = int(''.join(map(str, res)), 2)


def main():
    mem_lst = []
    mask = None
    for line in sys.stdin:
        mem = re.findall(MEM, line)
        if mem:
            mem_lst.append(mem[0])
        else:
            if mask:
                apply_masks(mask, mem_lst)
            mem_lst = []
            mask = [(i, x) for i, x in enumerate(re.findall(MASK, line)[0][::-1]) if x != 'X']
    apply_masks(mask, mem_lst)

    print(sum(memory.values()))

if __name__ == '__main__':
    main()
