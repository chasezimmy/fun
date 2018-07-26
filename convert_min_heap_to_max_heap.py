# Convert Min-Heap to Max-Heap

class Solution:
	# O(nlogn)
	def max_heapify(self, arr, n, i):
		left  = 2 * i + 1
		right = 2 * i + 2
		largest = i

		if left < n and arr[i] < arr[left]:
			largest = left
		if right < n and arr[largest] < arr[right]:
			largest = right
		if largest != i:
			arr[i], arr[largest] = arr[largest], arr[i]
			self.max_heapify(arr, n, largest)

	def heap_sort(self, arr):
		n = len(arr)
		
		for i in range(n, -1, -1):
			self.max_heapify(arr, n, i)

		return arr


s = Solution()
arr = [3, 5, 6, 8, 9, 9, 10, 12, 18, 20]
print(s.heap_sort(arr))