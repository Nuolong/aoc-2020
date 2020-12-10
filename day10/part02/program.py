#!/usr/bin/env python3

import sys

def count_seq(n, nums):
    mem = [0] * (n + 1)
    mem[0] = 1

    for i in nums:
        mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3]

    return mem[n]

def main():
    nums = []
    for num in sys.stdin:
        nums.append(int(num))

    nums.sort()
    print(count_seq(max(nums), nums))

if __name__ == '__main__':
    main()
