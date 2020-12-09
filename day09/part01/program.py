#!/usr/bin/env python3

import sys

def abide(window, n):
    for i, w_n in enumerate(window):
        diff = n - w_n
        if diff in window[i + 1:]:
            return True
    return False

def find_rulebreaker(nums, preamble_len):
    window = nums[0:preamble_len]
    strt_remain = nums[preamble_len:]

    for n in strt_remain:
        if (abide(window, n)):
            window.append(n)
            window.pop(0)
        else:
            return n

def main():
    nums = []
    for num in sys.stdin:
        nums.append(int(num))

    print(find_rulebreaker(nums, 25))

if __name__ == '__main__':
    main()
