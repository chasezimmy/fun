def longest_non_cont_inc_subarray(arr):
  length = len(arr)
  cache = [1] * length

  for i in range(length):
    for j in range(length):
      if i == j:
        break
      if arr[i] > arr[j]:
        cache[i] = min(cache[i], cache[j]) + 1
  return max(cache)
 
def longest_cont_inc_subarray(arr):
  max_end = 1
  max_cur = 1

  for i, n in enumerate(arr):
    if arr[i] > arr[i - 1]:
      max_end += 1
    else:
      max_cur = max(max_end, max_cur)
      max_end = 1

  return max_cur


arr = [3, 4, -1, 0, 6, 2,9, 3]

longest_non_cont_inc_subarray(arr)
longest_cont_inc_subarray(arr)