#!/usr/bin/env python3

import sys
import re
from collections import defaultdict
from itertools import product

MASK = r'mask = (.+)'
MEM = r'mem\[(\d+)\] = (\d+)'

memory = defaultdict(int)

def apply_masks(mask, mem_lst):
    for inst in mem_lst:
        # address
        addr_res = [0] * 36
        addr = bin(int(inst[0]))[2:]
        for i, bit in enumerate(addr[::-1]):
            addr_res[i] = bit
        for m in mask:
            if m[1] == '0':
                continue
            addr_res[m[0]] = m[1]

        addr_lst = get_addr(addr_res)

        for a in addr_lst:
            memory[a] = int(inst[1])

def get_addr(addr_res):
    addr_lst = []
    x_count = 0
    for bit in addr_res:
        if bit == 'X':
            x_count += 1
    perm_list = list(product(['0', '1'], repeat=x_count))

    for perm in perm_list:
        curr_x = 0
        new_addr = []
        for bit in addr_res:
            if bit == 'X':
                new_addr.append(perm[curr_x])
                curr_x += 1
            else:
                new_addr.append(bit)
        new_addr.reverse()
        addr_lst.append(int(''.join(map(str, new_addr)), 2))

    return addr_lst

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
            mask = [(i, x) for i, x in enumerate(re.findall(MASK, line)[0][::-1])]
    apply_masks(mask, mem_lst)

    print(sum(memory.values()))

if __name__ == '__main__':
    main()
