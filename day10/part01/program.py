#!/usr/bin/env python3

import sys

def find_jolts(nums):
    diff_1 = 0
    diff_3 = 1  # for last-to built-in joltage
    start = 0

    while nums:
        curr = nums.pop(0)
        if start + 1 == curr:
            diff_1 += 1
            start = curr
        elif start + 3 == curr:
            diff_3 += 1
            start = curr

    return diff_1 * diff_3


def main():
    nums = []
    for num in sys.stdin:
        nums.append(int(num))

    nums.sort()
    print(find_jolts(nums))

if __name__ == '__main__':
    main()
