import unittest
import problems.p2 as sut
from leet import linklist as ll

CASES = [
    {
        "l1": [2, 4, 3],
        "l2": [5, 6, 4],
        "expect": [7, 0, 8],
    },
]


class TestP2(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = sut.Solution()

    def run_cases(self, solver_fn):
        for case_dict in CASES:
            expected = case_dict["expect"]
            listnode1 = ll.into_list_nodes(case_dict["l1"])
            listnode2 = ll.into_list_nodes(case_dict["l2"])
            case = str(
                ["Case:", solver_fn.__name__, listnode1.values(), listnode2.values()]
            )
            result = solver_fn(listnode1, listnode2)
            self.assertEqual(expected, result, case)

    def test_brute_naive(self):
        return self.run_cases(self.sut.brute_naive)
