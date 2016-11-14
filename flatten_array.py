# Flatten Array
# https://github.com/blakeembrey/code-problems/tree/master/problems/flatten-array

def naive(md_list):
	flat_str = str(md_list).replace('[', '').replace(']', '').replace(',', '')
	return map(int, flat_str.split())

def flatten_recursive(lst):
	return sum( ([x]  if not isinstance(x, list) else flatten_recursive(x) for x in lst), [] )

md_list = [1, 2, [3, [4], 5, 6], 7]

#print naive(md_list)
print flatten_recursive(md_list)