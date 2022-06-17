import unittest
import problems.p5 as sut

CASES = {
    "example1": {
        "s": "babad",
        "result": "bab",
    },
    "example2": {
        "s": "cbbd",
        "result": "bb",
    },
    "example3": {
        "s": "bb",
        "result": "bb",
    },
}


class TestP5(unittest.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()
        self.optim = sut.ExpandSolution()

    def run_cases(self, solver_obj):
        failed_cases = []
        for descr, vals in CASES.items():
            expected = vals["result"]
            s = vals["s"]
            result = solver_obj.longestPalindrome(s)
            info = {
                "result": result,
                "vals": vals,
            }
            if result != expected:
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_naive(self):
        return self.run_cases(self.naive)

    def test_optimized(self):
        return self.run_cases(self.optim)

    def test_is_palin(self):
        self.assertTrue("b")
        self.assertTrue("bb")
        self.assertTrue("abba")
        self.assertTrue("babab")
        self.assertFalse("")

    def test_lenPalinByExpansion(self):
        self.assertEqual(1, self.optim.lenPalinByExpansion("cbba", 0, 0))
        self.assertEqual(1, self.optim.lenPalinByExpansion("cbba", 0, 1))
        self.assertEqual(2, self.optim.lenPalinByExpansion("cbba", 1, 2))
        self.assertEqual(1, self.optim.lenPalinByExpansion("cbba", 2, 2))
        self.assertEqual(1, self.optim.lenPalinByExpansion("cbba", 2, 3))
