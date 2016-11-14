def mostFreqInt(arr):
	most = dict()

	for elem in arr:
		if elem not in most:
			most[elem] = 1
		else:
			most[elem] += 1

	print max(most, key=most.get)
a = [1, 2, 3, 3, 4]

mostFreqInt(a)