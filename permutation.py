# Permutation

class Solution:
	def permutation(self, word):
		if len(word) == 1:
			return [word]

		perms = self.permutation(word[1:])
		char = word[0]
		res = []

		for perm in perms:
			for i in range(len(perm) + 1):
				res.append(perm[:i] + char + perm[i:])

		return res

s = Solution()
word = 'TRY'

print s.permutation(word)