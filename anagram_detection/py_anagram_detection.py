# Anagram Detection
# http://www.ardendertat.com/2011/11/17/programming-interview-questions-16-anagram-strings/

class Solution:

	# Sub-Optimal O(n^2) < - Github question doesn't define Anagram correctly
	def anagram_detection1(self, parent, child):
		sol = 0
		hash_child = {}

		for c in child:
			if c not in hash_child:
				hash_child[c] = 0
			hash_child[c] += 1

		for i in range(len(parent)):
			hashmap = {}
			for c in parent[i:i+3]:
				if c not in hashmap:
					hashmap[c] = 0
				hashmap[c] += 1
			if hash_child == hashmap:
				sol += 1

		return sol


	# O(n) Solution
 	def anagram_detection2(self, parent, child):
		parent, child = self.get_letters(parent), self.get_letters(child)
		if len(parent) != len(child):
			return False

		count = {}
		for c in parent:
			if c not in count:
				count[c] = 0
			count[c] += 1

		for c in child:
			count[c] -= 1
			if count[c] < 0:
				return False

		return True

	def get_letters(self, text):
		return [c.lower() for c in text if c.isalpha()]



if __name__ == '__main__':
	test_cases = 2
	s = Solution()
	parent = ['Eleven plus two', 'Tom Marvolo Riddle']
	child = ['Twelve plus one', 'I am Lord Voldemort']
	for i in range(test_cases):
		print "Is '%s' an anagram of '%s': %r" % (parent[i], child[i], \
			s.anagram_detection2(parent[i], child[i]))



