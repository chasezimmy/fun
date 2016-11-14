# Factorial 

class Solution:
	# Iterative
	def factorial(self, n):
		if n < 1:
			return 1
		fact = 1
		for i in range(n, 1, -1):
			fact *= i
		return fact

	# Recursive
	def factorial_rec(self, n):
		return 1 if n < 1 else n * self.factorial_rec(n - 1)


s = Solution()
n = 10
print s.factorial_rec(n)