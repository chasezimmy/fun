# Reverse String

class Solution:
	# Built In
	def reverse_string1(self, string):
		return string[::-1]

	# Doing the work
	def reverse_string2(self, string):
		arr = [x for x in string]
		length = len(arr) - 1
		for i in range(length):
			arr[i], arr[length - i] = arr[length - i], arr[i]
		return arr

s = Solution()
string = "Hello"
print s.reverse_string1(string)
print ''.join(s.reverse_string2(string))

