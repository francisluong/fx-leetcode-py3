import unittest

import numpy as np

import hackerrank.oneweekprep.day2.mock as sut

M2X2 = np.arange(4)
M2X2.resize(2, 2)


M4X4 = np.arange(16)
M4X4.resize(4, 4)

CASES = [
    {
        "descr": "example1",
        "arr": [
            [1, 2],
            [3, 4],
        ],
        "expected": [
            [4, 1],
            [2, 3],
        ],
    },
    {
        "descr": "example2_not_yet_workingr",
        "arr": [
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108],
        ],
        "expected": [
            [119, 114, 42, 112],
            [56, 125, 101, 49],
            [15, 78, 56, 43],
            [62, 98, 83, 108],
        ],
    },
]


class TestDay2Mock(unittest.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()

    def run_cases(self, solver_obj):
        failed_cases = []
        for case in CASES:
            expected = case["expected"]
            arr = case["arr"]
            result = solver_obj.solve(arr)
            info = {
                "result": result,
                "case": case,
            }
            if not np.array_equal(result, expected):
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_naive(self):
        return self.run_cases(self.naive)

    def test_reverse_row_2x2(self):
        matrix = M2X2
        result = sut.reverse_row(matrix, 0)
        expected = np.array(
            [
                [1, 0],
                [2, 3],
            ]
        )
        info = {
            "expected": expected,
            "matrix": matrix,
            "result": result,
        }
        self.assertEqual(True, np.array_equal(expected, result), str(info))

    def test_reverse_col_2x2(self):
        matrix = M2X2
        result = sut.reverse_col(matrix, 0)
        expected = np.array(
            [
                [2, 1],
                [0, 3],
            ]
        )
        info = {
            "expected": expected,
            "matrix": matrix,
            "result": result,
        }
        self.assertEqual(True, np.array_equal(expected, result), str(info))

    def test_half_sums(self):
        self.assertEqual((1, 5), sut.half_sums(np.arange(4)))

    def test_sum_top_quarter(self):
        self.assertEqual(0, sut.sum_top_quarter(M2X2))
        self.assertEqual(2, sut.sum_top_quarter(np.array([[2, 1], [0, 3]])))
        self.assertEqual(10, sut.sum_top_quarter(M4X4))
