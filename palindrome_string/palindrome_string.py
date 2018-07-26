# Check if a string is palindrome or not

class Solution:
	# Runner
	def is_palindrome(self, string):
		palindrome = False
		for i in range(len(string)//2 +1):
			if string[i] == string[-1 - i]:
				palindrome = True
			else:
				return False
		return palindrome

	# Pythonic
	def is_palindrome2(self, string):
		return string == string[::-1]

sol = Solution()
string = 'Sore was I ere I saw Eros'
<<<<<<< HEAD:palindrome_string/palindrome_string.py
print(sol.isPalindrome2(string.lower()))
=======
print sol.is_palindrome2(string.lower())
>>>>>>> 0a64e548694dcc45d4a52fc0d934e4e54bb14908:palindrome_string/palindrome_string.py
