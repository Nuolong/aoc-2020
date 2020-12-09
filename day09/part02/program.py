#!/usr/bin/env python3

import sys

def find_ctg(window, invalid_num):
    curr_sum = window[0]
    start = 0
    end = 1

    while end < len(window) - 1:
        # front window value is removed from window
        while curr_sum > invalid_num and start < end:
            curr_sum -= window[start]
            start += 1

        # contiguous subarray found
        if curr_sum == invalid_num:
            sub_arr = window[start:end]
            return max(sub_arr) + min(sub_arr)
        # new value added to end of window
        else:
            curr_sum += window[end]
            end += 1


def abide(window, n):
    for i, w_n in enumerate(window):
        diff = n - w_n
        if diff in window[i + 1:]:
            return True
    return False

def find_rulebreaker(nums, preamble_len):
    window = nums[0:preamble_len]
    strt_remain = nums[preamble_len:]

    for i, n in enumerate(strt_remain):
        if (abide(window, n)):
            window.append(n)
            window.pop(0)
        else:
            return i, n

def main():
    nums = []
    for num in sys.stdin:
        nums.append(int(num))

    i, invalid_num = find_rulebreaker(nums, 25)
    print(find_ctg(nums[:i], invalid_num))


if __name__ == '__main__':
    main()
