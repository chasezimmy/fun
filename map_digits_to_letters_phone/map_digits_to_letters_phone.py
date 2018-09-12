"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

class Solultion:

	map = {
		'1': ['a', 'b', 'c'],
		'2': ['d', 'e', 'f'],
		'3': ['g', 'h', 'i'],
		'4': ['j', 'k', 'l'],
		'5': ['m', 'n', 'o'],
		'6': ['p', 'q', 'r'],
		'7': ['s', 't', 'u'],
		'8': ['v', 'w', 'x'],
		'9': ['y', 'z']
	}

	def map_digits_to_letters(self, digits):
		digit = digits[0]
		
		if len(digits) == 1:
			return self.map[digit]

		result = []

		for char in self.map[digit]:
			for perm in self.map_digits_to_letters(digits[1:]):
				result.append(char + perm)
		return result

sol = Solultion()
string = '12345678912345'
print(sol.map_digits_to_letters(string))