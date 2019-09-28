def remove(nums):
    s = set()
    for n in nums:
        s.add(n) 
    return list(s)

print(remove([1, 1, 2]))