"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

https://leetcode.com/problems/median-of-two-sorted-arrays/

The overall run time complexity should be O(log (m+n)).
"""

from typing import List

MAX = 10**6 + 1


def median(nums):
    l = len(nums)
    r = int(l / 2)
    if l % 2 == 0:
        # even... do average

        return (nums[r - 1] + nums[r]) / 2.0
    else:
        return nums[r]


def val_or_max(nums, index, length):
    if index < length:
        return nums[index]
    else:
        return MAX


class NaiveSolution:
    def merge(self, nums1, nums2):
        result = []
        index1 = index2 = 0
        l1 = len(nums1)
        l2 = len(nums2)
        while index1 <= l1 and index2 <= l2:
            v1 = val_or_max(nums1, index1, l1)
            v2 = val_or_max(nums2, index2, l2)
            if v1 == MAX and v2 == MAX:
                return result
            elif v1 < v2:
                result.append(v1)
                index1 += 1
            else:
                result.append(v2)
                index2 += 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        return median(merged)


Solution = NaiveSolution
