"""
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to
  a 32-bit signed integer (similar to C/C++'s atoi function).
"""

import re


def sanitize_string(s: str):
    return s.lstrip()


def handle_pos_neg(s: str) -> (int, str):
    if not s:
        return 1, 0
    char = s[0]
    rem = s[1:]
    if char == "-":
        return -1, rem
    elif char == "+":
        return 1, rem
    else:
        return 1, s


def consume_leading_zeroes(s: str) -> str:
    while s and s[0] == "0":
        s = s[1:]
    return s


def ascii_to_int(s: str) -> str:
    return ord(s[-1]) - 48


INT_MAX = 2**31 - 1
INT_MIN = -(2**31)


def clamp(val: int) -> int:
    if val > INT_MAX:
        return INT_MAX
    elif val < INT_MIN:
        return INT_MIN
    else:
        return val


class LeetSolution:
    # this must be overridden in subclass
    # otherwise unit tests are ignore/pass/no-op
    IMPLEMENTED = False

    def __init__(self):
        self.name = str(str(self.__class__))


class NaiveSolution(LeetSolution):
    IMPLEMENTED = True

    def naive_convert_ascii(self, s: str):
        result = 0
        digits = []
        while s and re.fullmatch(r"\d", s[0]):
            digits.append(ascii_to_int(s[0]))
            s = s[1:]
        order = len(digits) - 1
        for digit in digits:
            result += digit * (10**order)
            order -= 1
        return result

    def solve(self, s: str) -> int:
        clean = sanitize_string(s)
        multiplier, clean = handle_pos_neg(clean)
        clean = consume_leading_zeroes(clean)
        int_val = multiplier * self.naive_convert_ascii(clean)
        result = clamp(int_val)
        return result

    def myAtoi(self, s: str) -> int:
        return self.solve(s)


class OptimizedSolution(LeetSolution):
    """avoid string conversion by sticking with integers"""

    def solve(self, s: str) -> int:
        pass


Solution = NaiveSolution
