"""
You are given an array of n integers and a positive integer, k. Find and print the number of (i,j) pairs where i < j  and  arr[i] + arr[j] is divisible by k.

For example, arr = [1,2,3,4,5,6] and k = 5. Our three pairs meeting the criteria are [1,4], [2,3] and [4,6]. So we return three.
"""

class Solution:
	def divisible_sum_pairs(self, n, arr, k):
        cache = 0

        for j in range(1, n):
            for i in range(j):
                if i < j and (ar[i] + ar[j]) % k == 0:
                    cache += 1

        return cache



sol = Solution()
arr = [1,3,2,6,1,2]
n = len(arr)
k = 3

print( sol.divisible_sum_pairs(n, arr, k) )