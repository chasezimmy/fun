# Combine Two Strings

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		if not self.is_empty():
			return self.items[len(self.items) - 1]

class Solution:

	# Slower, but uses Stacks
	def is_shuffle(self, str1, str2, str3):
		rev = str3[::-1]
		stack1 = Stack()
		stack2 = Stack()
		stack3 = Stack()
		
		if len(str1) + len(str2) != len(str3):
			return False

		for i in str1:
			stack1.push(i)
		for i in str2:
			stack2.push(i)
		for i in rev:
			stack3.push(i)

		for ch in rev:
			if stack1.peek() == ch:
				stack3.pop()
				stack1.pop()
			if stack2.peek() == ch:
				stack3.pop()
				stack2.pop()
		return stack3.is_empty()

	# Faster, 
	def is_shuffle1(self, str1, str2, str3):
		i, j, k = 0, 0, 0
		if len(str1) + len(str2) != len(str3):
			return False

		while k <= len(str3) -1:
			if i < len(str1) and str1[i] == str3[k]:
				i += 1
			elif j < len(str2) and str2[j] == str3[k]:
				j += 1
			else:
				return False
			k += 1

		return len(str1) == i and len(str2) == j

s = Solution()
str1 = "abc"
str2 = "def"
str3 = "adbecf"
print s.is_shuffle1(str1, str2, str3)