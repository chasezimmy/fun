# Leetcode : https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums):
        """
        First attempt, messy and takes to long

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lookup = {}
        solution = {}
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue
                if n + m in lookup:
                    lookup[n + m].append((i, j))
                else:
                    lookup[n + m] = [(i, j)]

        for i, n in enumerate(nums):
            for k, v in lookup.items():
                if i in v:
                    continue
                if k + n == 0:
                    for _ in v:
                        if _[0] == i or _[1] == i:
                            continue
                        sum = sorted([nums[_[0]], nums[_[1]], n])
                        solution[tuple(sum)] = i
        return [list(k) for k, v in solution.items()]


class SolutionTwo:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return res