#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


class NaiveSolution:
    def count_by_value(self, integer_array):
        result = defaultdict(lambda: 0)
        for x in integer_array:
            result[x] += 1
        return result

    def solve(self, integer_array):
        count_by_value = self.count_by_value(integer_array)
        for val, count in count_by_value.items():
            if count == 1:
                return val


def lonelyinteger(a):
    solver = NaiveSolution()
    return solver.solve(a)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + "\n")

    fptr.close()
