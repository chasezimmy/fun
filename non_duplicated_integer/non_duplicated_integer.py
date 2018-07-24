"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
"""

class Solution:
	def non_duplicated_int(self, list):
		duplicates = {}

		for i in list:
			if i in duplicates:
				duplicates[i] += 1
			else:
				duplicates[i] = 1

		for k, i in duplicates.items():
			if i == 1:
				return k

sol = Solution()
print(sol.non_duplicated_int([13, 19, 13, 13]))