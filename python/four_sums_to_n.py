"""
    Four elements sum to a given n
"""

def four_sum(arr, n):
    four_sums = []
    cache = {}
    cache_index = 0
    sum_list = []
    for x, i in enumerate(arr):
        for j in arr[x + 1:]:
            cache[cache_index] = {"sum": i + j, "composite": {i, j}}
            sum_list.append(i + j)
            cache_index += 1
    print(cache)
    for x, i in enumerate(sum_list):
        if n - i in sum_list:
            for y, j in enumerate(sum_list[x+1:]):
                y = y + x + 1
                if j == n - i and len(cache[y]['composite'].intersection(cache[x]['composite'])) != 1:
                    print(cache[x]['composite'], cache[y]['composite'])
                    four_sums.append(cache[y]['composite'].union(cache[x]['composite']))

    print(four_sums)

four_sum([1, 2, 3, 4, 5, 0], 10)