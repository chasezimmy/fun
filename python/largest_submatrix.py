"""
    Find the maximum square sub-matrix of 1s in a matrix of 0s and 1s
"""

def submatrix(arr):
  max = 1
  row_len = len(arr)
  col_len = len(arr[0])
    
  cache = [[0 for k in range(col_len)] for l in range(row_len)]

  for i in range(row_len):
    for j in range(col_len):
      if i == 0 or j == 0:
        cache[i][j] = arr[i][j]
      elif arr[i][j] == 1:
        cache[i][j] = min(
          arr[i][j-1],
          arr[i-1][j-1],
          arr[i-1][j-1]
        ) + 1

      if cache[i][j] > max: max = cache[i][j]
  return max

arr = [
  [1, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 0, 0, 0]]

print(submatrix(arr))
