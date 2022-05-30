import math
from leet.linklist import ListNode
from typing import List, Optional

"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string `s`, find the length of the longest substring without repeating characters.
"""


def all_unique(s: str) -> bool:
    """
    return `True` if `s` has all uniq chars
    :param s:
    :return:
    """
    return len(s) == len(set(s))


class NaiveSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = len(s)
        if len(s) < 2:
            return len(s)
        max = 1
        for i in range(last):
            for j in range(i, last):
                this_substr = s[i : j + 1]
                if all_unique(this_substr):
                    if max < len(this_substr):
                        max = len(this_substr)
        return max


Solution = NaiveSolution
