import unittest
import hackerrank.plus_minus as sut

CASES = [
    {
        "descr": "example1",
        "arr": [1, 1, 0, -1, -1],
        "result": [
            "0.400000",
            "0.400000",
            "0.200000",
        ],
    },
    {
        "descr": "example2",
        "arr": [-4, 3, -9, 0, 4, 1],
        "result": [
            "0.500000",
            "0.333333",
            "0.166667",
        ],
    },
]


class TestPlusMinus(unittest.TestCase):
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
