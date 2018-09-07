"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
"""

class Solution:
	def product_array_puzzle(self, arr):

		temp = []
		length = len(arr) -1 
		product = 1

		for n in arr:
			temp.append(product)
			product *= n

		product = 1

		for i, n in enumerate(arr[::-1]):
			temp[length - i] = product * temp[length - i]
			product *= n

		return temp


sol = Solution()
arr = [1, 2, 3, 4]
print(sol.product_array_puzzle(arr))