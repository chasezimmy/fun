"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


def product_list_division(list):
    if list[0] == 0:
        res = list[0]
    else:
        res = 1
    has_0 = 0
    product = []

    for i in list:
        if i == 0:
            has_0 += 1
            continue
        res *= i

    print(res, has_0)

    for i in list:
        if i == 0 and has_0==1:
            product.append(res)
        elif has_0 > 0:
            product.append(0)

        else:
            product.append(res//i)

    return product


def product_list(list):
    p = 1
    result = []

    for i in range(len(list)):
        result.append(p)
        p = p * list[i]

    p = 1
    for i in range(len(list) - 1, -1, -1):
        result[i] = result[i] * p
        p = p * list[i]

    return result


list = [1, 2, 3, 4, 5]
print(product_list(list))