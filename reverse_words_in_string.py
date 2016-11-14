# Reverse Word Order in a String
# http://www.ardendertat.com/2011/10/31/programming-interview-questions-12-reverse-words-in-a-string/

class Solution:
	def reverse_order1(self, string):
		words = string.split(' ')[::-1]
		return words


s = Solution()
string = "Interviews are awesome!"
print ' '.join(s.reverse_order1(string))