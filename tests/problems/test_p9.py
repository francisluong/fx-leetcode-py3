import leet
import problems.p9 as sut

CASE_COLLECTION = leet.CaseCollection()
CASE_COLLECTION.add_case("example1", [121], True)
CASE_COLLECTION.add_case("example2", [-121], False)
CASE_COLLECTION.add_case("example3", [10], False)
CASE_COLLECTION.add_case("example4", [1221], True)
CASE_COLLECTION.add_case("example5", [12321], True)


class TestP9NaiveSolution(leet.TestCase):
    def setUp(self) -> None:
        self.sut = sut.NaiveSolution()

    def test_offset_is_match(self):
        self.assertTrue(self.sut.offset_is_match("121", 0))


class TestP9(leet.TestCase):
    def setUp(self) -> None:
        self.naive = sut.NaiveSolution()
        self.optim = sut.OptimizedSolution()

    def test_naive(self):
        return self.run_cases(CASE_COLLECTION, self.naive)

    def test_optimized(self):
        return self.run_cases(CASE_COLLECTION, self.optim)
