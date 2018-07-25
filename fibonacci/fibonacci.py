# Fibonnaci

class Solution:
	# Dynamic Programming
	def fib(self, n):
		n1, n2 = 0, 1
		for i in range(1, n):
			n1, n2 = n2, n1 + n2
		return n1 + n2

	# MIT Dynamic Programming w/ Memoization
	def fib_memo(self, n):
		if n in memo: return memo[n]
		if n <= 2: f = 1
		else: f = self.fib_memo(n-1) + self.fib_memo(n-2)
		memo[n] = f
		return f

	def fib_bottom_up(self, n):
		for k in range(1, n + 1):
			if k <= 2: f = 1
			else: f = fib[k - 1] + fib[k - 2]
			fib[k] = f
		return fib[n]

	# Recursion
	def fib_rec(self, n):
		if n == 0:
			return 1
		if n == 1:
			return 1

		return self.fib_rec(n - 1) + self.fib_rec(n - 2)

s = Solution()
memo = {}
fib = {}

print "1:", s.fib(1000)
