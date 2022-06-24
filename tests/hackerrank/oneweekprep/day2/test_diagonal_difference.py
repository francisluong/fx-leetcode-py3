import unittest
import hackerrank.oneweekprep.day2.diagonal_difference as sut

CASES = [
    {
        "descr": "example1",
        "arr": [
            [1, 2, 3],
            [4, 5, 6],
            [9, 8, 9],
        ],
        "expected": 2,
    },
    {
        "descr": "example2",
        "arr": [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ],
        "expected": 15,
    },
]


class TestNaiveSolution(unittest.TestCase):
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
            if result != expected:
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_solve(self):
        self.run_cases(self.naive)
