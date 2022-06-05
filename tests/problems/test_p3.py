import unittest
import problems.p3 as sut

ANSWER_BY_CASE = {
    " ": 1,
    "": 0,
    "au": 2,
    "abcabcbb": 3,
    "bbbbb": 1,
    "pwwkew": 3,
}


class TestP3(unittest.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()
        self.slide = sut.SlidingWindowSolution()

    def run_cases(self, solver_fn):
        failed_cases = []
        for case_str, expected_substr_length in ANSWER_BY_CASE.items():
            result = solver_fn(case_str)
            info = f"{case_str} - expected: {expected_substr_length}, result: {result}"
            if result != expected_substr_length:
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_all_unique(self):
        IS_UNIQ_BY_STR = {
            "b": True,
            "bb": False,
            "abc": True,
            "pwek": True,
        }
        failed_cases = []
        for case_str, expected_bool in IS_UNIQ_BY_STR.items():
            result = sut.all_unique(case_str)
            if expected_bool != result:
                info = f"{case_str}: expected: {expected_bool}, result: {result}"
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_brute_naive(self):
        return self.run_cases(self.naive.lengthOfLongestSubstring)

    def test_sliding_window(self):
        return self.run_cases(self.slide.lengthOfLongestSubstring)
