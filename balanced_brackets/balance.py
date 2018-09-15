#
# Chase Zimmerman
#

def is_balanced(string):
	""" Map open brackets to close with stacks, pop them to find balance, as all things should be """

	stack = []
	cache = []
	opened = "({["
	closed = ")}]"
	mapped = dict(zip(opened, closed))

	for i,n in enumerate(string):

		if n in opened:
			stack.append([mapped[n], i])
		elif n in closed:
			if stack and n == stack[-1][0]:
				stack.pop()
			else:
				cache.append([n, i])

	combine = stack + cache

	if combine:

		first = combine[0]
		for n in stack + cache:
			if first[1] > n[1]:
				first = n	
		return first[1]		
	else:
		return -1

def main():
	
	tests = [
		"hello world",
		"{}",
		"{{{foo();}}}{}",
		"{{}{}}",
		"{{{}",
		"}",
		"{}{foo{}"
	]

	for test in tests:
		print(is_balanced(test))

if __name__ == '__main__':
	main()
