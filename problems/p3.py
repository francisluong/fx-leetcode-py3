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
        this_max = 1
        for i in range(last):
            for j in range(i, last):
                this_substr = s[i : j + 1]
                if all_unique(this_substr):
                    if this_max < len(this_substr):
                        this_max = len(this_substr)
        return this_max


class SlidingWindowSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        this_max = 0
        slen = len(s)
        for left in range(slen):
            # left-index loop
            encountered_chars = set()
            encountered_chars.add(s[left])
            for right in range(left + 1, slen):
                # right-index loop
                rchar = s[right]
                if rchar in encountered_chars:
                    break
                else:
                    encountered_chars.add(rchar)
            new_max = len(encountered_chars)
            this_max = max(this_max, new_max)
        return this_max


Solution = SlidingWindowSolution
