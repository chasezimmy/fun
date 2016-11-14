# Balanced Brackets
# http://www.ardendertat.com/2011/11/08/programming-interview-questions-14-check-balanced-parentheses/

class Solution:
	def is_balanced(self, s):
		if len(s) % 2 != 0:
			return False
		opening = set('([{<')
		match = set([ ('(',')'), ('[',']'), ('{','}'), ('<','>') ])
		stack = []
		for c in s:
			if c in opening:
				stack.append(c)
			else:
				if stack == []:
					return False
				last_open = stack.pop()
				if (last_open, c) not in match:
					return False
		return stack == []

s = Solution()
string = "({[]})"
print s.is_balanced(string)