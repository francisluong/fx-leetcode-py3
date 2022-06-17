"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
"""


def is_palin(s: str):
    result = False
    i = 0
    j = len(s) - 1
    while True:
        if i == j:
            return True
        is_equal = s[i] == s[j]
        if not is_equal:
            return False
        elif i == j - 1 and is_equal:
            return True
        elif is_equal:
            i += 1
            j -= 1
            continue

    return result


class NaiveSolution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        longest = s[0]
        for i in range(slen):
            for j in range(i + 1, slen + 1):
                this_sub = s[i:j]
                palin = is_palin(this_sub)
                # print(f"s: {s}, longest: {longest}, this_sub: {this_sub}, palin: {palin}, i: {i}, j: {j}, ")
                if palin and len(this_sub) > len(longest):
                    longest = this_sub
        return longest


class ExpandSolution:
    """
    effectively for each value of i expand from center of i,i
    and i,i+1
    """

    def lenPalinByExpansion(self, s, left, right):
        """
        this could have been simpler, maybe return start and end instead

        but it is what it is, and it returns the expanded length given the left/right
        starting indices
        """
        max_offset = 0
        init_len = right + 1 - left
        # if out of range or the 2 values are not matching, exit early len 1
        if left < 0 or right >= len(s) or s[left] != s[right]:
            result = 1
            # print(f"  - no iter: s: {s}, len: {len(s)}")
        else:
            # incr test each candidate width/offset starting with +/- 1
            cand_offset = 1
            l = left - cand_offset
            r = right + cand_offset
            # print(f"  - iter: s: {s}, cand_offset: {cand_offset}, l: {l}, r: {r}")
            while l >= 0 and r < len(s) and s[l] == s[r]:
                max_offset = cand_offset
                cand_offset += 1
                l = left - cand_offset
                r = right + cand_offset
                # print(f"  - iter: s: {s}, cand_offset: {cand_offset}, l: {l}, r: {r}")
            result = max_offset * 2 + init_len
        # print(
        #     f"  - expand: s: {s}, max_offset: {max_offset}, left: {left}, right: {right} -> result: {result} ({s[left - max_offset:right + max_offset+1]})"
        # )
        return result

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        maxlen = 0
        maxi = 0
        for i in range(len(s)):
            # test expansion around 1 char or 2 char figures
            len1 = self.lenPalinByExpansion(s, i, i)
            len2 = self.lenPalinByExpansion(s, i, i + 1)
            currmax = max([len1, len2])
            if currmax > maxlen:
                maxlen = currmax
                maxi = i
            # print(f" - s:  {s}, i: {i}, maxlen: {maxlen}")
        start = maxi - int((maxlen - 1) / 2)
        end = maxi + int(maxlen / 2)
        # print(f"start: {start}, end: {end} -> result: {s[start:end + 1]}")
        return s[start : end + 1]


Solution = ExpandSolution
