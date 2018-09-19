import math

def abs_diff(a, b):
    diff = a - b
    if diff < 0:
        diff = -1 * diff

    return diff


class Series:
    def transform(self, k):
        return k

    def series_sum(self, n):
        total = 0
        for i in range(n):
            total += self.transform(i + 1)

        return total


class PiSeries(Series):
    def transform(self, k):
        return math.pow(-1, k - 1) * (1 / (2 * k - 1))