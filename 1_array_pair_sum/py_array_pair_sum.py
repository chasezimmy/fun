# Array Pair Sum
# http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/

class Solution:
	# O(N^2)
	def pair_sum(self, arr, sum_):
		arr1 = list(set(arr))
		sol_list = []
		temp= []
		for i in range(len(arr1)):
			nw = arr1[i:] + arr1[:i]
			for n in range(1,len(nw)):
				pair_s = sorted([nw[0],nw[n]])
				if sum(pair_s) == sum_ and pair_s not in sol_list and len(pair_s) == 2:
					sol_list.append(pair_s)
		return sol_list

	# O(NlogN)
	def pair_sum1(self, arr, k):
		if len(arr) < 2:
			return
		pairs = []
		sort = list(sorted(set(arr)))
		l, r = (0, len(sort) - 1)
		while l < r:
			curr_sum = sort[l] + sort[r]
			if curr_sum == k:
				pairs.append((sort[l], sort[r]))
				l += 1 #or right-=1
			elif curr_sum < k:
				l += 1
			else:
				r -= 1
		return pairs

	# O(N)
	def pair_sum2(self, arr, k):
		length = len(arr)
		if length < 2:
			return

		seen = set()
		output = set()

		for n in arr:
			target = k - n
			if target not in seen:
				seen.add(n)
			else:
				output.add((min(n, target), max(n, target)))

		return output


s = Solution()
arr = [1, 1, 2, 3, 4]
sum_ = 5
print s.pair_sum2(arr, sum_)


