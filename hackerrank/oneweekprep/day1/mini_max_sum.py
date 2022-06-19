#!/bin/python3
"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one&h_r=next-challenge&h_v=zen

Given five positive integers, find the minimum and maximum values that
can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line
of two space-separated long integers.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


class NaiveSolution:
    def solve(self, integer_array):
        integer_array.sort()
        min = sum(integer_array[0:4])
        max = sum(integer_array[1:5])
        return [str(x) for x in [min, max]]


def miniMaxSum(arr):
    # Write your code here
    solver = NaiveSolution()
    min, max = solver.solve(arr)
    print(f"{min} {max}")


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
