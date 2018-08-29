"""
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

class Solution:

	def longest_increasing_subsequence(self, arr):
		cache = [1] * len(arr)

		for i in range(1, len(arr)):
			for j in range(i):
				if arr[i] > arr[j]:
					cache[i] = max(cache[i], cache[j] + 1)
		
		return cache

sol = Solution()
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(sol.longest_increasing_subsequence(arr))