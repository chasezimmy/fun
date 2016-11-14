# Prime Number

class Solution:
	def is_prime(self, n):
		if n % 2 == 0 or n < 2: return False
		for i in range(3, int(n**0.5) + 1, 2):
			if n % i == 0:
				return False
		return True

s = Solution()
n = 27
ans = 'YES' if s.is_prime(n) else 'NO'
print "Is %d prime: %s" % (n, ans)


