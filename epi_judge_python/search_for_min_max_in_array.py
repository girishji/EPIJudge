import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple("MinMax", ("smallest", "largest"))


def find_min_max(A: List[int]) -> MinMax:
    n = len(A)
    gmin, gmax = float("inf"), float("-inf")
    for i, j in zip(range(n // 2 if n % 2 == 0 else n // 2 + 1), range(n // 2, n)):
        (mn, mx) = (A[i], A[j]) if A[i] < A[j] else (A[j], A[i])
        gmin = mn if mn < gmin else gmin
        gmax = mx if mx > gmax else gmax
    return MinMax(gmin, gmax) if n > 1 else MinMax(A[0], A[0])


def res_printer(prop, value):
    def fmt(x):
        return "min: {}, max: {}".format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            "search_for_min_max_in_array.tsv",
            find_min_max,
            res_printer=res_printer,
        )
    )
