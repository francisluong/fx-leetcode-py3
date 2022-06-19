#!/bin/python3
"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def new_hour(hour: int, is_am):
    result = hour
    offset = 0
    if hour == 12:
        if is_am:
            result = 0
        else:
            result = 12
    elif not is_am:
        # not 12 and PM
        offset = 12
    result += offset
    result = str(result).zfill(2)
    return result


class NaiveSolution:
    def solve(self, time_str: str):
        if time_str.endswith("AM"):
            is_am = True
        else:
            is_am = False
        parts = time_str.split(":")
        hour = int(parts[0])
        newhour = new_hour(hour, is_am)
        parts[0] = newhour
        parts[2] = parts[2][0:2]
        return ":".join(parts)


def timeConversion(s):
    solver = NaiveSolution()
    return solver.solve(s)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
