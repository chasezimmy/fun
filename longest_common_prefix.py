# Longest Common Prefix
import os

class Solution:

	# Very Niave O(nk) approach
	def longest_common_prefix(self, arr):
		for i in range(len(arr)):
			runner = 0
			j = 1
			while runner < len(arr[i]) / 2 + 2:
				if arr[i][:j] not in memo:
					memo[arr[i][:j]] = 1
				else:
					memo[arr[i][:j]] += 1
				runner += 1
				j += 1
		return max(memo, key=memo.get)

	# O(n) - Only solves array with common prefixes
	def longest_common_prefix1(self, arr):
		if not arr: return ''
		s1 = min(arr)
		s2 = max(arr)

		for i, c in enumerate(s1):
			if c != s2[i]:
				return s1[:i]
		return s1

s = Solution()
arr = ['rocket', 'rockstar', 'rockbottom', 'rock', 'rollingstone']
#arr = ['shuffle', 'shuttle', 'shut']
memo = {}

print s.longest_common_prefix1(arr)

# Builtin
print os.path.commonprefix(arr)
