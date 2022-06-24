#!/bin/python3

"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen

Alternative Sorting
Another sorting method, the counting sort, does not require comparison.
Instead, you create an integer array whose index range covers the entire
range of values in your array to sort. Each time a value occurs in the
original array, you increment the counter at that index. At the end,
run through your counting array, printing the value of each non-zero
valued index that number of times.

NOTE: For this exercise, always return a frequency array with 100 elements.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


class NaiveSolution:
    def solve(self, integer_array):
        result = [0] * 100
        for x in integer_array:
            result[x] += 1
        return result


def countingSort(arr):
    solver = NaiveSolution()
    return solver.solve(arr)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
