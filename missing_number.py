# Missing Number
# Assumed Nonneg ints and Arithmetic progression with common difference of 1 

class Solution:

	# O(n)
	def missing_no(self, arr):
		length = len(arr)
		max_ = max(arr)
		sum_arr = sum(arr)
		sum_ = 0

		for i in range(1, max_ + 1):
			sum_ += i

		return sum_ - sum_arr

	# O(n) - slightly faster, max and sum found in O(n) not O(2n)
	def missing_no1(self, arr):
		length = len(arr)
		max_ = -2**31
		sum_arr = 0
		sum_ = 0

		for i in range(length):
			if arr[i] > max_:
				max_ = arr[i]
			sum_arr += arr[i]

		for i in range(1, max_ + 1):
			sum_ += i

		return sum_ - sum_arr


s = Solution()
arr = [-1, -2, -4, -5]

print s.missing_no1(arr)