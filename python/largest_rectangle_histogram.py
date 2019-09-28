def graph(arr):
    """
    not fully functional
    """
  length = len(arr)
  cache_front = arr[:]

  for i in range(length):
    for j in range(length):
      if i == j:
        break
      if min(arr[i], arr[j]) * (i-j+1) > cache_front[i]:
        cache_front[i] = min(arr[i], arr[j]) * (i-j+1)
      elif arr[i] > arr[j]:
        cache_front[i] = arr[i]

  return max(
    max(cache_front),
    min(arr) * length
  )

print(graph([2,1,2]))