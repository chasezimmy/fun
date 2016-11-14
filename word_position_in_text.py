# Find Word Positions in Text
# http://www.ardendertat.com/2011/12/20/programming-interview-questions-23-find-word-positions-in-text/

class Solution:
	"""
	Naive apprach (also doesn't solve the problem, find the count instead of position)
	"""
	def string_position(self, file_path):
		text_file = open(file_path, 'r')
		content = text_file.read().split(' ')

		look = {'ocean' : 0}

		count = 1

		for n in content:
			if look.has_key(n):
				look[n] = count
				count +=1

		return look

	"""
	Correct Approach, hashmap and enumerate
	"""
	def string_position1(self, file_path):
		text_file = open(file_path, 'r')
		content = text_file.read().split(' ')

		look = {'ocean' : []}

		for i, n in enumerate(content):
			if look.has_key(n):
				look[n].append(i)

		return look

s = Solution()
print "Naive: %r" % s.string_position('../test.txt')
print "Correct: %r" % s.string_position1('../test.txt')



