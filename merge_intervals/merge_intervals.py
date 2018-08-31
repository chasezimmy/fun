"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

class Solution:
	def merge_intervals(self, arr):
		result = []
		for start, end in sorted(arr, key=lambda x: x[0]):
			if result and start <= result[-1][1]:
				prev_start, prev_end = result[-1]
				result[-1] = (prev_start, max(end, prev_end))
			else:
				result.append((start, end))

			print(result)

		return result


sol = Solution()
arr = [(1, 3), (5, 8), (4, 10), (20, 25)]
arr = [(1,3), (2,4), (5,7), (6,8)]
print(sol.merge_intervals(arr))