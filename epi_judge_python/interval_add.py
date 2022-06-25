import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple("Interval", ("left", "right"))


def add_interval(
    disjoint_intervals: List[Interval], new_interval: Interval
) -> List[Interval]:
    res = []
    for di in disjoint_intervals:
        if di.left < new_interval.left:
            res.append(di)
        else:
            break
    if res and res[-1].right >= new_interval.left:
        res[-1] = Interval(res[-1].left, new_interval.right)
    else:
        res.append(new_interval)
    new_interval = res[-1]
    for di in disjoint_intervals:
        if di.left <= new_interval.right and di.right > new_interval.right:
            new_interval = Interval(res[-1].left, di.right)
            res[-1] = new_interval
        elif di.left > new_interval.right:
            res.append(di)
    return res


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals, Interval(*new_interval))
    )


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            "interval_add.tsv",
            add_interval_wrapper,
            res_printer=res_printer,
        )
    )
