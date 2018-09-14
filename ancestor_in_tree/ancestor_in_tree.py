"""
1   3     7
 \\//    //
   2    5
   \\ //\\  
     4    6
arr = [[parent, child],...[parent, child]]
"""

def parent_child(arr):
	relationship = {}

	for n in arr:
		if n[0] not in relationship:
			relationship[n[0]] = {'parent': 1, 'child' : 0}
		else:
			relationship[n[0]]['parent'] += 1

		if n[1] not in relationship:
			relationship[n[1]] = {'parent': 0, 'child' : 1}
		else:
			relationship[n[1]]['child'] += 1

	return relationship

arr = [[1, 2], [3, 2], [2, 4], [5, 4], [5, 6], [7, 5]]
parent_child(arr)