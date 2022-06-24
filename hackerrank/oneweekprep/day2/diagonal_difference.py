#!/bin/python3

"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

"""

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


class NaiveSolution:
    def solve(self, integer_arrays):
        # start an index on the left and right
        # move inward by 1 each iteration
        # print(f"\n===\n{integer_arrays}")
        sum_i = sum_j = 0
        count = len(integer_arrays)
        i = -1
        j = count
        for integer_array in integer_arrays:
            i += 1
            j -= 1
            sum_i += integer_array[i]
            sum_j += integer_array[j]
            # print(f"i={i}: sum {sum_i} -- j={j}: sum {sum_j}")
        # print(f"diff: {sum_i - sum_j}")
        return abs(sum_i - sum_j)


def diagonalDifference(arr):
    solver = NaiveSolution()
    result = solver.solve(arr)
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
