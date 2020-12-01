#!/usr/bin/env python3

import sys

def find2020(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i):
            if nums[i] + nums[i+j] == 2020:
                return nums[i] * nums[i+j]


def main():
    nums = []
    for i in sys.stdin:
        nums.append(int(i))

    print(find2020(nums))

if __name__ == '__main__':
    main()
