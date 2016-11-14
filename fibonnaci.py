# Fibonnaci
import timeit

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

start1 = timeit.default_timer()
print "1:", s.fib(1000)
stop1 = timeit.default_timer()

start2 = timeit.default_timer()
#print "2:", s.fib_rec(40)
stop2 = timeit.default_timer()

start3 = timeit.default_timer()
#print "3:", s.fib_memo(40)
stop3 = timeit.default_timer()

start4 = timeit.default_timer()
#print "4:", s.fib_bottom_up(1000000)
stop4 = timeit.default_timer()

print "\n"
print "Dynamic - My Attempt:", stop1 - start1
#print "Recursion:", stop2 - start2
#print "MIT Memoization:", stop3 - start3
#print "MIT Bottom-Up:", stop4 - start4
#print memo
