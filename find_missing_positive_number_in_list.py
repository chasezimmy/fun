"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""


def find_missing_number(nums):
    n = len(nums)
    sum = n * (n+1) // 2
    diff = 0

    for i in nums:
        if i > 0:
            diff += i

    return sum - diff


def find_missing_number_maxmin(nums):
    max_num = max(nums)
    min_num = 2**32

    # find min number greater than 0
    for i in nums:
        if i < min_num and i >= 0:
            min_num = i

    for i in range(min_num, max_num + 1):
        if i not in nums:
            return i


def find_missing_number_kaz(nums):
   nums.sort(reverse=True)
   print(nums)
   for i in nums:
       mn = min(nums)
       if mn < 0:
           nums.pop()
   print(mn)
   if mn == 1 or mn == 0:
       x = mn + 1
       if x in nums:
           x = x + 1
   else:
       x = mn - 1
   return x

nums = [3, 5]
print(find_missing_number(nums))



nums = [3, 4, -1, 1]
print(find_missing_number_kaz(nums))
