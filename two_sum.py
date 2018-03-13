class Solution:
    # O(n^2) don't do this
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cur = 0
        k = len(nums)
        run = k - 1

        for i in range(k):
            cur = i
            for j in range(k):
                run = j
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

    # O(n)
    def two_sum(self, nums, target):
        lookup = {}
        for i, n in enumerate(nums):
            if target - n in lookup:
                return [lookup[target-n], i]
            lookup[n] = i
