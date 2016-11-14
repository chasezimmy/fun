x = 1243
arr = [int(i) for i in str(x)] 

for i in range(len(arr) - 1, -1, -1):
	if arr[i] > arr[i - 1]:
		arr[i], arr[i - 1] = arr[i - 1], arr[i]
		break

#print arr


class Solution:
	def new_highest(self, n):
		str_n = str(n)
		length = len(str_n)

		for i in range(length - 2, -1, -1):
			curr = str_n[i]
			right = str_n[i + 1]
			if curr < right:
				temp = sorted(str_n[i:])
				next_ = temp[temp.index(curr) + 1]
				temp.remove(next_)
				temp = ''.join(temp)
				return  int(str_n[:i] + next_ + temp)

		# If it doesn't exist
		return n

s = Solution()
print s.new_highest(x)