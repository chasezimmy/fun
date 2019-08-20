"""

42 -> but in Python (it's using backtracking)

Given a map of 4x4 (this solution can handle NxN), place boxes of height 1 to 4 on each available square in a way
that every row and column sees the correct number of boxes from each the possible
points of view (left/right for rows, up/down for columns).

• Ex (for 4x4): The box of height 3 will hide the box of height 1 from the left, so we have 3
visible boxes, and only one from the right, because the box of height 4 is hiding
everything.



• Ex pic:
                        Column Up
                +---+---+---+---+---+---+
                |   | 4 | 3 | 2 | 1 |   |
                +---+---+---+---+---+---+
                | 4 | 1 | 2 | 3 | 4 | 1 |
                +---+---+---+---+---+---+
                | 3 | 2 | 3 | 4 | 1 | 2 |
     Row Left   +---+---+---+---+---+---+     Row Right
                | 2 | 3 | 4 | 1 | 2 | 2 |
                +---+---+---+---+---+---+
                | 1 | 4 | 1 | 2 | 3 | 2 |
                +---+---+---+---+---+---+
                |   | 1 | 2 | 2 | 2 |   |
                +---+---+---+---+---+---+
                        Column Down

          col up  col down row left  row right
   list = 4321    1222     4321     1222

"""

import math


def used_in_column(table, n, c, col):
    for row in range(n):
        if table[row][col] == c:
            return True
    return False


def used_in_row(table, n, c, row):
    for col in range(n):
        if table[row][col] == c:
            return True
    return False


def count_boxes(table, input, n, c, row, col):
    table[row][col] = c  # temp set current position as current character
    check_box_count = check_col_up(table, input, n, col) and \
        check_row_left(table, input, n, row) and \
        check_col_down(table, input, n, col) and \
        check_row_right(table, input, n, row)
    table[row][col] = 0

    return check_box_count


def check_col_up(table, input, n, col):
    max_block_height = 0
    block_total = 0
    quadrant = 0
    for i in range(n):
        if max_block_height < table[i][col]:
            max_block_height = table[i][col]
            block_total += 1

        if block_total > input[(col % n) + (quadrant*n)]:  # column up is 0, parses the input list
            return False
    return True


def check_col_down(table, input, n, col):
    max_block_height = 0
    block_total = 0
    quadrant = 1
    for i in range(n-1, 0, -1):
        if max_block_height < table[i][col]:
            max_block_height = table[i][col]
            block_total += 1

        if block_total > input[(col % n) + (quadrant*n)]:  # col down 1
            return False
    return True


def check_row_left(table, input, n, row):
    max_block_height = 0
    block_total = 0
    quadrant = 2
    for i in range(n):
        if max_block_height < table[row][i]:
            max_block_height = table[row][i]
            block_total += 1

        if block_total > input[(row % n) + (quadrant*n)]:
            return False
    return True


def check_row_right(table, input, n, row):
    max_block_height = 0
    block_total = 0
    quadrant = 3

    for i in range(n-1, 0, -1):
        if max_block_height < table[row][i]:
            max_block_height = table[row][i]
            block_total += 1

        if block_total > input[(row % n) + (quadrant*n)]:
            return False
    return True


def is_safe(table, c, input, n, row, col):
    return \
        table[row][col] == 0 and \
        not used_in_row(table, n, c, row) and \
        not used_in_column(table, n, c, col) and \
        count_boxes(table, input, n, c, row, col)


def find_zero(table, n, l):
    for row in range(n):
        for col in range(n):
            if table[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def solve(table, input, n):

    l = [0, 0]

    if not find_zero(table, n, l):
        return True

    row = l[0]
    col = l[1]

    for c in range(1, n + 1):
        if is_safe(table, c, input, n, row, col):

            table[row][col] = c

            if solve(table, input, n):
                return True

            table[row][col] = 0

    return False


def main():

    table_4x4 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    table_3x3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    table_2x2 = [
        [0, 0],
        [0, 0]
    ]

    input_4x4 = [4, 3, 2, 1, 1, 2, 2, 2, 4, 3, 2, 1, 1, 2, 2, 2]
    input_4x4_invalid = [2, 2, 1, 4, 2, 2, 4, 1, 2, 2, 1, 3, 2, 2, 3, 1] # invalid
    input_3x3 = [1, 3, 2, 2, 1, 2, 1, 3, 2, 2, 1, 2]

    input_2x2 = [1, 2, 2, 1, 1, 2, 2, 1]

    table = table_4x4
    input = input_4x4

    n = int(math.sqrt(len(input)))

    if solve(table, input, n):
        print(table)


if __name__ == '__main__':
    main()
