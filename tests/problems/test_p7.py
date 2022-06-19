import unittest
import problems.p7 as sut

CASES = {
    "example1": {
        "x": 123,
        "result": 321,
    },
    "example2": {
        "x": -123,
        "result": -321,
    },
    "example3": {
        "x": 120,
        "result": 21,
    },
    "example4": {
        "x": 1534236469,
        "result": 0,
    },
    "oor1": {
        "x": -(2**31) - 1,
        "result": 0,
    },
    "oor2": {
        "x": 2**31,
        "result": 0,
    },
}


class TestP7(unittest.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()
        self.optim = sut.OptimizedSolution()

    def run_cases(self, solver_obj):
        failed_cases = []
        for descr, case in CASES.items():
            expected = case["result"]
            s = case["x"]
            result = solver_obj.reverse(s)
            info = {
                "result": result,
                "descr": descr,
                "case": case,
            }
            if result != expected:
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_naive(self):
        return self.run_cases(self.naive)

    def test_optimized(self):
        return self.run_cases(self.optim)

    def test_to_list(self):
        self.assertEqual((["1", "2", "3"], False), sut.to_list(123))
        self.assertEqual((["1", "2", "3"], True), sut.to_list(-123))

    def test_to_i(self):
        self.assertEqual(123, sut.to_i(["1", "2", "3"], False))
        self.assertEqual(-123, sut.to_i(["1", "2", "3"], True))

    def test_is_oor_10(self):
        self.assertTrue(sut.is_oor_10(sut.INT_MIN, 0))
        self.assertTrue(sut.is_oor_10(sut.INT_MAX, 0))
        self.assertTrue(sut.is_oor_10(sut.INT_MAX / 10, 8))
        self.assertTrue(sut.is_oor_10(sut.INT_MIN / 10, -9))
        self.assertFalse(sut.is_oor_10(sut.INT_MAX / 10, 0))
        self.assertFalse(sut.is_oor_10(sut.INT_MIN / 10, 0))
        self.assertFalse(sut.is_oor_10(123, 0))
