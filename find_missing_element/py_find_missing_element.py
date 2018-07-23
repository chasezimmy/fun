# Find Missing Element
# http://www.ardendertat.com/2011/09/27/programming-interview-questions-4-find-missing-element/

class Solution:

	# O(NlogN)
	def findMissingElement1(self, arr1, arr2):
		arr1.sort()
		arr2.sort()
		for num1, num2 in zip(arr1, arr2):
			if num1 != num2:
				return num1
		return arr1[-1]

	# O(N) Time, O(1) Space Complextiy
	def findMissingElement2(self, arr1, arr2):
		res = 0
		for num in arr1+arr2:
			res^=num
		return res

	# O(N) - My Solution (overflow if N is large)
	def findMissingElement(self, arr1, arr2):
		return sum(arr1) - sum(arr2)


sol = Solution()
a1 = [4, 1, 0, 2, 9, 6, 8, 7, 5, 3]
a2 = [6, 4, 7, 2, 1, 0, 8, 3, 9]

print sol.findMissingElement2(a1, a2)