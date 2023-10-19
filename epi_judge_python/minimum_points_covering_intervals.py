import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple("Interval", ("left", "right"))


def find_minimum_visits(intervals: List[Interval]) -> int:
    intervals.sort(key=lambda iv: iv.left)
    result = 0
    overlap = None
    for interval in intervals:
        if not overlap:
            result += 1
            overlap = interval
        else:
            if interval.left <= overlap.right:
                overlap = Interval(interval.left, min(interval.right, overlap.right))
            else:
                result += 1
                overlap = interval

    return result


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_points_covering_intervals.py",
            "minimum_points_covering_intervals.tsv",
            find_minimum_visits_wrapper,
        )
    )
