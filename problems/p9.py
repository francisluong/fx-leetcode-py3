"""
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""


class LeetSolution:
    # this must be overridden in subclass
    # otherwise unit tests are ignore/pass/no-op
    IMPLEMENTED = False

    def __init__(self):
        self.name = str(str(self.__class__))


class NaiveSolution(LeetSolution):
    IMPLEMENTED = True

    def offset_is_match(self, stringified, offset):
        left_idx = offset
        right_idx = len(stringified) - offset - 1
        return stringified[left_idx] == stringified[right_idx]

    def solve(self, num: int) -> bool:
        print(num)
        stringified = str(num)
        for offset in range(len(stringified) // 2):
            if not self.offset_is_match(stringified, offset):
                return False
        return True

    def isPalindrome(self, x: int) -> bool:
        return self.solve(x)


class OptimizedSolution(LeetSolution):
    """avoid string conversion by sticking with integers"""

    IMPLEMENTED = True

    def solve(self, x: int) -> bool:
        if x < 0:
            # negative numbers
            return False
        if x % 10 == 0 and x != 0:
            # number ending in zero but not equal zero
            return False
        # use modulus to pop values and add them to a reverted number
        reverted = 0
        # exit loop when x == reverted [1221 -> 12, 12]
        # ...or x < reverted [12321 -> 12, 123]
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x = x // 10
        # for even length numbers, ==
        # ... for odd length numbers, ignore the middle number
        return x == reverted or x == reverted // 10

    def isPalindrome(self, x: int) -> bool:
        return self.solve(x)


Solution = OptimizedSolution
