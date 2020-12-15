#!/usr/bin/env python3

import sys
from collections import defaultdict

def play(nums):
    turns = nums
    history = defaultdict(int)

    for num in nums:
        history[num] = 1

    while len(turns) < 2020:
        last_num = turns[-1]
        if history[last_num] == 1:
            turns.append(0)
            history[0] = history.get(0, 0) + 1
        else:
            first = None
            for i, num in reversed(list(enumerate(turns))):
                if num == last_num and first == None:
                    first = i
                    continue
                elif num == last_num and first != None:
                    turns.append(first - i)
                    history[first - i] = history.get(first - i, 0) + 1
                    break

    return turns


def main():
    nums = list(map(int, input().split(",")))
    print(play(nums)[-1])

if __name__ == '__main__':
    main()
