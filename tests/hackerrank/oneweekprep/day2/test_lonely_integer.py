import unittest
import hackerrank.oneweekprep.day2.lonely_integer as sut

CASES = [
    {
        "descr": "example1",
        "arr": [1, 2, 3, 4, 3, 2, 1],
        "result": 4,
    },
]


class TestLonelyIntNaiveSolution(unittest.TestCase):
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
