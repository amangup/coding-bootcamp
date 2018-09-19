import math
from important_code import abs_diff, Series, PiSeries


EPSILON = 1E-4


class TestAbsDiff:
    def test_positive(self):
        assert 1 == abs_diff(2, 1)

    def test_negative(self):
        assert 1 == abs_diff(1, 2)


class TestSeries:
    def test_100_terms(self):
        series = Series()
        assert 5050 == series.series_sum(100)


class TestPiSeries:
    def test_20000_terms(self):
        series = PiSeries()
        assert math.isclose(math.pi / 4, series.series_sum(200000), abs_tol=EPSILON)