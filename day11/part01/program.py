#!/usr/bin/env python3

import sys

INPUT_COLS = 92
INPUT_ROWS = 99

# calculates new matrix of seats. marks if any changes were made
def adjacents(seats):
    adj_mat = [['.' for _ in range(INPUT_COLS + 2)]]
    changed = False
    for i in range(1, INPUT_ROWS + 1):
        row = []
        for j in range(1, INPUT_COLS + 1):
            count = 0

            if seats[i-1][j-1] == '#':
                count += 1
            if seats[i+1][j] == '#':
                count += 1
            if seats[i+1][j-1] == '#':
                count += 1
            if seats[i][j-1] == '#':
                count += 1
            if seats[i][j+1] == '#':
                count += 1
            if seats[i-1][j] == '#':
                count += 1
            if seats[i-1][j+1] == '#':
                count += 1
            if seats[i+1][j+1] == '#':
                count += 1

            if seats[i][j] == 'L' and not count:
                row.append('#')
                changed = True
            elif seats[i][j] == '#' and count >= 4:
                row.append('L')
                changed = True
            else:
                row.append(seats[i][j])

        adj_mat.append(["."] + row + ["."])

    adj_mat.append(['.' for _ in range(INPUT_COLS + 2)])

    return adj_mat, changed

# count num of occupied seats
def count_occ(seats):
    count = 0
    for i in range(1, INPUT_ROWS + 1):
        for j in range(1, INPUT_COLS + 1):
            if seats[i][j] == '#':
                count += 1

    return count

def main():

    # read input into 2D matrix, pad it with "floor"
    seats = [['.' for _ in range(INPUT_COLS + 2)]]

    for _ in range(INPUT_ROWS):
        seats.append(["."] + list(sys.stdin.readline().strip()) + ["."])

    seats.append(['.' for _ in range(INPUT_COLS + 2)])

    # flag
    changed = True
    while changed:
        seats, changed = adjacents(seats)

    print(count_occ(seats))

if __name__ == '__main__':
    main()
