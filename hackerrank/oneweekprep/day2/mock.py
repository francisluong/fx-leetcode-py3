#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def np_reverse_single_row_col(np_matrix, index, axis):
    if axis == 0:
        # fetch row
        popped = np_matrix[index, :]
    else:
        # fetch column
        popped = np_matrix[:, index]
    temp_np_matrix = np.delete(np_matrix, index, axis=axis)
    new_np_matrix = np.insert(temp_np_matrix, index, np.flip(popped), axis=axis)
    return new_np_matrix


def reverse_row(np_matrix, index):
    return np_reverse_single_row_col(np_matrix, index, axis=0)


def reverse_col(np_matrix, index):
    return np_reverse_single_row_col(np_matrix, index, axis=1)


def half_sums(np_array):
    "return 2 sums, one for sum of each half of an even array"
    half = int(np_array.size / 2)
    sum1 = sum(np_array[0:half])
    sum2 = sum(np_array[half : int(np_array.size)])
    return sum1, sum2


def sum_top_quarter(npm):
    rows, cols = npm.shape
    result = 0
    half_cols = int(cols / 2)
    half_rows = int(rows / 2)
    for row_index in range(half_rows):
        a = npm[row_index]
        b = a[0:half_cols]
        result += sum(b)
    return result


class NaiveSolution:
    def solve(self, matrix):
        # arrays are 2n x 2n - always even so we can divide them in half
        # ...sum the halves and swap if the right/bottom end is higher
        npm = np.array(matrix)
        rows, cols = npm.shape
        for row_index in range(rows):
            row = npm[row_index, :]
            sum1, sum2 = half_sums(row)
            if sum1 < sum2:
                npm = reverse_row(npm, row_index)
        for col_index in range(int(cols / 2)):
            col = npm[:, col_index]
            sum1, sum2 = half_sums(col)
            if sum1 < sum2:
                npm = reverse_col(npm, col_index)
        return npm


class SecondSolution:
    def solve(self, matrix):
        npm = np.array(matrix)
        rows, cols = npm.shape
        # we can work rows from the outside in
        # start with rows 0 and -1, then 1, -2
        # is the left half larger or the right half?
        # take the max of each colunn and then we can sum them
        # then we flip columns on the high side until the top row is set
        # if the top row needs horiz flip, do that too


def flippingMatrix(matrix):
    solver = NaiveSolution()
    # need to return an integer for the sum of top left quadrant
    result_npm = solver.solve(matrix)
    return sum_top_quarter(result_npm)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + "\n")

    fptr.close()
