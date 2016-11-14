# Split Text Into sub-strings according to rules
# http://stackoverflow.com/questions/3223218/an-interview-question-split-text-into-sub-strings-according-to-rules

import sys

def contains_digit(s):
	for c in list(s):
		if c.isdigit():
			return True
			break
	return False

m, n, text = int(3), int(5), "Hello 1337 h4x0r xD"
text_length, isDigit = len(text), [c in '0123456789' for c in text]
#print isDigit
chunks, i, j = [], 0, 0

while j < text_length:
	i = j
	j = min(text_length, j + n)

	while j < text_length and j - i < m and not contains_digit(text[j]):
		j += 1
	chunks += [text[i:j]]
print chunks

#while j < textLen:
#	i, j = j, min(textLen, j + n) 

#	print text[i:j]
#	if not any(isDigit[i:j]):
#		while j < textLen and j - i < m and not isDigit[j]:
#			j += 1
#	chunks += [text[i:j]]
#print chunks

#chunks, i, j = [], 0, 0
#while j < text_length:
#	pass #i, j = j, min()