import unittest
import problems.p1 as sut

CASES = [
    {
        "nums": [2, 7, 11, 15],
        "target": 9,
        "expect": {0, 1},
    },
    {
        "nums": [3, 2, 4],
        "target": 6,
        "expect": {1, 2},
    },
    {
        "nums": [3, 3],
        "target": 6,
        "expect": {0, 1},
    },
    {
        "nums": range(10001),
        "target": 19999,
        "expect": {10000, 9999},
    },
    {
        "nums": range(10001),
        "target": 1,
        "expect": {0, 1},
    },
]


class TestP1(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = sut.Solution()

    def run_cases(self, solver_fn):
        for case_dict in CASES:
            expected = case_dict["expect"]
            nums = case_dict["nums"]
            target = case_dict["target"]
            case = str([solver_fn.__name__, nums, target])
            result = solver_fn(nums, target)
            self.assertEqual(set(expected), set(result), case)

    def test_brute(self):
        return self.run_cases(self.sut.brute)

    def test_linear(self):
        return self.run_cases(self.sut.hash_linear)
