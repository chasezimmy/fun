"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

def sum_to_k(list, k):
    return any([True if k - _ in list else False for _ in list])


def sum_to_k_one_pass(list, k):
    for _ in list:
        if k - _ in list:
            return True
    return False

list = [10, 15, 3, 7]
k = 17

print(sum_to_k(list, k))