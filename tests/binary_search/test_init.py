import unittest
import binary_search as sut

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BSACase:
    arr: List[int]
    val: int
    expected: Optional[int]  # index


class TestBinarySearch(unittest.TestCase):
    def run_cases(self, cases: List[BSACase], func):
        for case in cases:
            got = func(case.arr, case.val)
            x_idx = case.expected
            if x_idx:
                x_val = case.arr[x_idx]
            else:
                x_val = None
            self.assertEqual(
                x_idx,
                got,
                f"\n> Case: {case.val} / {case.arr} for fn: {func.__name__} "
                f"\n--- Got: {got} "
                f"\n--- Expected: x_idx: {x_idx} (x_val: {x_val})",
            )

    def test_find_first_index_gt_val(self):
        cases = [
            BSACase(arr=[1, 2, 3, 4, 5], val=3, expected=3),
            BSACase(arr=[1, 3, 3, 3, 5], val=3, expected=4),
            BSACase(arr=[5], val=3, expected=0),
            BSACase(arr=[1, 3], val=3, expected=1),
        ]
        self.run_cases(cases, sut.find_first_index_gt_val)

    def test_find_last_index_lt_val(self):
        cases = [
            BSACase(arr=[1, 2, 3, 4, 5], val=3, expected=1),
            BSACase(arr=[1, 2, 2, 3, 5], val=3, expected=2),
        ]
        self.run_cases(cases, sut.find_last_index_lt_val)

    def test_find_first_index_of_exact_match(self):
        cases = [
            BSACase(arr=[1, 2, 3, 4, 5], val=3, expected=2),
            BSACase(arr=[1, 1, 2, 2, 3, 3], val=2, expected=2),
            BSACase(arr=[1, 1, 2, 2, 3, 3], val=4, expected=None),
            BSACase(arr=[1, 1, 2, 2, 3, 3], val=0, expected=None),
        ]
        self.run_cases(cases, sut.find_first_index_of_exact_match)


if __name__ == "__main__":
    unittest.main()
