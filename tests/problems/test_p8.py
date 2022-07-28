import leet
import problems.p8 as sut

CASE_COLLECTION = leet.CaseCollection()
CASE_COLLECTION.add_case("example1", ["  42"], 42)
CASE_COLLECTION.add_case("4193 with words", ["4193 with words"], 4193)
CASE_COLLECTION.add_case("empty", [""], 0)


class TestP8(leet.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()
        self.optim = sut.OptimizedSolution()

    def test_ascii_to_int(self):
        self.assertEqual(4, sut.ascii_to_int("4"))
        self.assertEqual(2, sut.ascii_to_int("2"))

    def test_handle_pos_neg(self):
        self.assertEqual((-1, "2"), sut.handle_pos_neg("-2"))
        self.assertEqual((1, "2"), sut.handle_pos_neg("+2"))
        self.assertEqual((1, "22"), sut.handle_pos_neg("22"))

    def test_naive_convert_ascii(self):
        self.assertEqual(42, self.naive.naive_convert_ascii("42"))

    def test_naive(self):
        return self.run_cases(CASE_COLLECTION, self.naive)

    def test_optimized(self):
        return self.run_cases(CASE_COLLECTION, self.optim)
