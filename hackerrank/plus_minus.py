#!/bin/python3
"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with
6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to
six decimal places, though answers with absolute error of up to 10**-4 are acceptable.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def fmt_6f(num):
    return "%.6f" % num


class NaiveSolution:
    def solve(self, integer_array):
        pos = neg = zero = 0
        for num in integer_array:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
            else:
                zero += 1
        items = len(integer_array)
        return [fmt_6f(x / items) for x in [pos, neg, zero]]


def plusMinus(arr):
    solver = NaiveSolution()
    [print(x) for x in solver.solve(arr)]


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
