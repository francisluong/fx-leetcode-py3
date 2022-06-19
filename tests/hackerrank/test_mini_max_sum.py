import unittest
import hackerrank.mini_max_sum as sut

CASES = [
    {
        "descr": "example1",
        "arr": [1, 3, 5, 7, 9],
        "result": [
            "16",
            "24",
        ],
    },
    {
        "descr": "example2",
        "arr": [1, 2, 3, 4, 5],
        "result": [
            "10",
            "14",
        ],
    },
]


class TestMiniMaxSum(unittest.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()

    def run_cases(self, solver_obj):
        failed_cases = []
        for case in CASES:
            expected = case["result"]
            arr = case["arr"]
            result = solver_obj.solve(arr)
            info = {
                "result": result,
                "case": case,
            }
            if result != expected:
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_naive(self):
        return self.run_cases(self.naive)
