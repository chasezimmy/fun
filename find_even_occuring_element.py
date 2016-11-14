# Find Even Occuring Element

class Solution:

	# Naive approach: O(n^2)
	def naive(self, arr):
		for i in arr:
			if arr.count(i) % 2 == 0:
				return True, i
				break
		return False

	# Hashmap: O(n)
	def hashmap(self, arr):
		count = 1
		hashmap = {}
		for i in arr:
			if i not in hashmap:
				hashmap[i] = count
			else:
				hashmap[i] += 1
		for n, i in hashmap.items():
			if i % 2 == 0:
				return True, n
		return False

	# Bit Magic: O(n)
	def xor(self, arr):
		return reduce(lambda x, y: x^y, arr+list(set(arr)))
 
s = Solution()
arr = [1, 2, 3, 4,2,3]
print s.naive(arr)
print s.hashmap(arr)
print s.xor(arr)