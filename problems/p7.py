"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-2**31, 2**31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
INT_MAX = 2**31 - 1
INT_MIN = -(2**31)


def is_oor(x):
    if x < INT_MIN or x > INT_MAX:
        return True
    else:
        return False


def is_oor_10(curr_result, pop):
    if curr_result < INT_MIN / 10:
        return True
    elif curr_result > INT_MAX / 10:
        return True
    elif curr_result == INT_MAX / 10 and pop > 7:
        return True
    elif curr_result == INT_MIN / 10 and pop < -8:
        return True
    else:
        return False


def to_list(x):
    """char-listify abs of x and return string and is_neg boolean"""
    is_neg = x < 0
    list_x = list(str(abs(x)))
    return list_x, is_neg


def to_i(list_x, is_neg):
    if is_neg:
        mult = -1
    else:
        mult = 1
    return int("".join(list_x)) * mult


class NaiveSolution:
    def reverse(self, x: int) -> int:
        list_x, is_neg = to_list(x)
        lenx = len(list_x)
        for i in range(lenx):
            j = lenx - (i + 1)
            if i >= j:
                break
            tmp = list_x[i]
            list_x[i] = list_x[j]
            list_x[j] = tmp
        result = to_i(list_x, is_neg)
        if is_oor(result):
            return 0
        else:
            return result


class OptimizedSolution:
    """avoid string conversion by sticking with integers"""

    def reverse(self, x: int) -> int:
        result = 0
        mult = 1
        if x < 0:
            mult = -1
        y = abs(x)
        while y != 0:
            y, pop = divmod(y, 10)
            if is_oor_10(result, pop):
                return 0
            result = result * 10 + pop
        return result * mult


Solution = OptimizedSolution
