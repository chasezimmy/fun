# Convert Array

class Solution:
	def convert_array(self, arr, letter):
		for i in range(1, 4):
			if i == 1:
				arr[i], arr[(i*letter) +1] = arr[(i*letter)+1], arr[i]
			if i == 2:
				arr[i], arr[(i*letter) +2] = arr[(i*letter)+2], arr[i]
		arr[5], arr[7] = arr[7], arr[5]
		print arr


	def getIndex(self, currentIndex, N):
		#print currentIndex
		print (currentIndex%3)*N + (currentIndex/3)
		return (currentIndex%3)*N + (currentIndex/3)

	def convert_array_extra(self, arr):
		N=len(arr)/3
		return [arr[self.getIndex(i, N)] for i in range(len(arr))]

	def convert_array1(self, arr):
		N=len(arr)/3
		for currentIndex in range(len(arr)):
			swapIndex=self.getIndex(currentIndex, N)
			while swapIndex<currentIndex:
				swapIndex=self.getIndex(swapIndex, N)
			arr[currentIndex], arr[swapIndex] = arr[swapIndex], arr[currentIndex]
		return arr

s = Solution()
arr = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
#arr = ['a1', 'a2', 'b1', 'b2']
letter = 2
print s.convert_array1(arr)



