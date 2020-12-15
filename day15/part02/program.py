#!/usr/bin/env python3

import sys
from collections import defaultdict

def play(nums):
    turns = nums
    history = defaultdict(list)

    for i, num in enumerate(nums):
        history[num] = [i + 1]

    last_num = nums[-1]

    for turn in range(len(nums) + 1, 30000001):
        if len(history[last_num]) == 2:
            last_num = history[last_num][-1] - history[last_num].pop(0)
        else:
            last_num = 0
        history[last_num].append(turn)

    return last_num

def main():
    nums = list(map(int, input().split(",")))
    print(play(nums))

if __name__ == '__main__':
    main()
