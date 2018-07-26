"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def non_adjacent_sum(list):
    temp = -2**32
    sum1 = list[0]
    sum = list[0]

    for i in list:
        sum = max(temp + i, sum1)
        temp = sum1
        sum1 = sum
    return sum


list = [2, 4, 6, 2, 5]
print(non_adjacent_sum(list))
