# Cuisenaire rods
# 6 = [[6], [3, 3], [2, 2, 2], [1, 1, 1, 1, 1, 1]]

class Solution:
	def cuisenaire_rods(self, n):
		rods = []
		for i in range(n, 0, -1):
			if n % i == 0:
				rods.append(['|'+str(i)+'|']*(n/i))
		return rods

s = Solution()
n = 6

for c in s.cuisenaire_rods(n):
	print ''.join(c)