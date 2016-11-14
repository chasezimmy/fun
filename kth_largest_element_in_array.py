# Kth Largest Element in Array
#http://www.ardendertat.com/2011/10/27/programming-interview-questions-10-kth-largest-element-in-array/

class Solution:
	def kth_largest(self, arr, k):
		sort = list(set(sorted(arr)))
		return sort[-k]

s = Solution()
arr = [3, 1, 2, 1, 4]
k = 4
print s.kth_largest(arr, k)