# Repeated Number in array between 1 and 1,000,000

class Solution:
	def repeated_num(self, n):
		arr = [7]

		for i in range(1, n + 1):
			arr.append(i)
		x = n*(n + 1) / 2
		return sum(arr) - x

s = Solution()
n = 10000000
print s.repeated_num(n)