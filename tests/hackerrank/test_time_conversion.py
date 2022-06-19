import unittest
import hackerrank.time_conversion as sut

CASES = [
    {
        "descr": "example1",
        "s": "12:01:00PM",
        "result": "12:01:00",
    },
    {
        "descr": "example2",
        "s": "12:01:00AM",
        "result": "00:01:00",
    },
    {
        "descr": "example3",
        "s": "07:05:45PM",
        "result": "19:05:45",
    },
]


class TestTimeConversion(unittest.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()

    def run_cases(self, solver_obj):
        failed_cases = []
        for case in CASES:
            expected = case["result"]
            s = case["s"]
            result = solver_obj.solve(s)
            info = {
                "solver_result": result,
                "case": case,
            }
            if result != expected:
                failed_cases.append(info)
        self.assertEqual([], failed_cases)

    def test_naive(self):
        return self.run_cases(self.naive)

    def test_new_hour(self):
        self.assertEqual("00", sut.new_hour(12, True))
        self.assertEqual("01", sut.new_hour(1, True))
        self.assertEqual("11", sut.new_hour(11, True))
        self.assertEqual("12", sut.new_hour(12, False))
        self.assertEqual("13", sut.new_hour(1, False))
        self.assertEqual("23", sut.new_hour(11, False))
