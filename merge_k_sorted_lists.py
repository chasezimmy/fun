# Merge k Sorted Lists
import heapq

class Solution:
	def merge_k_lists(self, k_lists):
		min_heap = []
		for i in range(len(k_lists)):
			if k_lists[i]:
				gen = (x for x in k_lists[i])
				heapq.heappush(min_heap, (next(gen), gen))
		res = []

		while min_heap:
			val, gen = heapq.heappop(min_heap)
			res.append(val)

			try:
				heapq.heappush(min_heap, (next(gen), gen))
			except StopIteration:
				pass

		return res

s = Solution()
llists = [[1, 3, 5, 7],
		  [2, 4, 6, 8],
		  [0, 9, 10, 11]]

print s.merge_k_lists(llists)


