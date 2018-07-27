# First Non-Repeated Character
# http://www.ardendertat.com/2011/11/14/programming-interview-questions-15-first-non-repeated-character-in-string/

class Solution:
	def first_non_rep(self, s):
		count = {}
		for c in s:
			if c not in count:
				count[c] = 0
			count[c] += 1

		return [c for c in s if count[c] == 1]
		return "NONE"

s = Solution()
string = "AABBCDD"
print(''.join(s.first_non_rep(string)))