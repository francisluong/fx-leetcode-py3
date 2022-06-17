import unittest
import problems.p4 as sut

CASES = {
    "example1": {
        "nums1": [1, 3],
        "nums2": [2],
        "result": 2,
    },
    "example2": {
        "nums1": [1, 2],
        "nums2": [3, 4],
        "result": 2.5,
    },
}


class TestP4(unittest.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()

    def run_cases(self, solver_obj):
        failed_cases = []
        for descr, vals in CASES.items():
            expected = vals["result"]
            nums1 = vals["nums1"]
            nums2 = vals["nums2"]
            merge_expected = nums2 + nums1
            merge_expected.sort()
            merge_result = solver_obj.merge(nums1, nums2)
            info = f"MERGE: {descr} {nums1} {nums2}- expected: {merge_expected}, result: {merge_result}"
            if merge_result != merge_expected:
                failed_cases.append(info)
            result = solver_obj.findMedianSortedArrays(nums1, nums2)
            info = f"MEDIAN: {descr} {nums1} {nums2}- expected: {expected}, result: {result}"
            if result != expected:
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_naive(self):
        return self.run_cases(self.naive)
