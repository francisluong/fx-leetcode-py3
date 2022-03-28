from typing import List

"""
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def brute(self, nums: List[int], target: int) -> List[int]:
        c = len(nums)
        for l in range(0, c - 1):
            for r in range(l + 1, c):
                if nums[l] + nums[r] == target:
                    return l, r

    def hash_linear(self, nums: List[int], target: int) -> List[int]:
        index_by_value = {}
        for i in range(len(nums)):
            val = nums[i]
            diff = target - nums[i]
            if diff in index_by_value:
                return i, index_by_value[diff]
            else:
                index_by_value[val] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return self.brute(nums, target)
        return self.brute(nums, target)
