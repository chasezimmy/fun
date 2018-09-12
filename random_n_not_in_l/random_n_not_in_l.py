"""
Given an integer n and a list of integers l, 
write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""

import random

class Solution:

	
	def n_not_in_l_naive(self, n, l):
		""" Naive, may run forever!! """

		rand = None
		while rand not in l:
			rand = random.randint(0, n-1)

		return rand

	def n_not_in_l(self, n, l):
		""" O(n) time/space """

		rand = [i for i in range(n)]
		cache = []

		for i in rand:
			if i not in l:
				cache.append(i)

		return random.choice(cache)

def main():
	n = 10
	l = [1, 2, 3, 5, 7, 9]

	sol = Solution()
	print(sol.n_not_in_l(n, l))

if __name__=="__main__":
	main()