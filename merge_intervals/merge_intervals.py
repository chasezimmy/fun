"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

class Solution:
	def merge_intervals(self, arr):
		
		if arr is None:
			return

		behind = arr[0]
		interval = [[False, False], [False, False]]
		merge = arr

		for n in range(len(arr)):
			if (n+1) >= len(arr):
				continue

			for i in range(len(arr[n])):
				for j in range(len(arr[n+1])):
					if arr[n][i] > arr[n+1][j]:
						interval[i][j] = True

			if True in interval[0] or True in interval[1]:
				merge.pop(n)
				
			interval = [[False, False], [False, False]]

		return merge

sol = Solution()
arr = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(sol.merge_intervals(arr))