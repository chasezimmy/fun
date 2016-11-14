# Convert Max-Heap to Min-Heap

class Solution:
	# O(nlogn)
	def min_heapify(self, arr, n, i):
		left  = 2 * i + 1
		right = 2 * i + 2
		largest = i

		if left < n and arr[i] < arr[left]:
			largest = left
		if right < n and arr[largest] < arr[right]:
			largest = right
		if largest != i:
			arr[i], arr[largest] = arr[largest], arr[i]
			self.min_heapify(arr, n, largest)

	def heap_sort(self, arr):
		n = len(arr)

		for i in range(n -1, 0, -1):
			arr[i], arr[0] = arr[0], arr[i]
			self.min_heapify(arr, i, 0)
		return arr

s = Solution()
arr = [20, 18, 10, 12, 9, 9, 3, 5, 6, 8]
print s.heap_sort(arr)