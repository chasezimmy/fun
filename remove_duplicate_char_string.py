# Remove Duplicate Character in String

class Solution:

	# O(n)
	def remove_duplicate(self, s):
		char_in_s = []
		seen = set()
		for c in s:
			if c not in seen:
				seen.add(c)
				char_in_s.append(c)

		return ''.join(char_in_s)

s = Solution()
string = "tree traversal"
print s.remove_duplicate(string)