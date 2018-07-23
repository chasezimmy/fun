# Largest Continuous Sum
# http://www.ardendertat.com/2011/09/24/programming-interview-questions-3-largest-continuous-sum/

class Solution:

	# Naive Solution O(n)
	def largest_continuous_sum(self, arr):
		if len(arr) == 0:
			return
		max_so_far = -2**31
		curr = 0
		runner = 0
		sum_ = arr[0]
		
		for i in range(len(arr)):
			if runner < len(arr)-1:
				runner += 1
			if sum_ + arr[runner] > max_so_far:
				max_so_far = sum_ + arr[runner]
				sum_ = max_so_far
			else:
				sum_ = 0
				curr = arr[i]
		return max_so_far

	# Correct Solution O(n)
	def largest_continuous_sum1(self, arr):
		if len(arr) == 0:
			return
		max_so_far = curr_sum = arr[0]
		for n in arr[1:]:
			curr_sum = max(curr_sum + n, n)
			max_so_far = max(curr_sum, max_so_far)
		return max_so_far


s = Solution()
arr = [1, 2, -1, -5, 1]
print s.largest_continuous_sum(arr)
print s.largest_continuous_sum1(arr)