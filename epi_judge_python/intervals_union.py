import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple("Endpoint", ("is_closed", "val"))

Interval = collections.namedtuple("Interval", ("left", "right"))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    endpts = [(n.left.val, True, n.left.is_closed) for n in intervals] + [
        (n.right.val, False, n.right.is_closed) for n in intervals
    ]
    endpts.sort(key=lambda x: (x[0], x[1], not x[2] if x[1] else x[2]))
    overlap = 0
    res = []
    left = None
    adjoint = False
    for pt in endpts:
        if not overlap:
            if (
                res
                and (pt[2] or res[-1].right.is_closed)
                and res[-1].right.val == pt[0]
            ):
                adjoint = True
            else:
                left = Endpoint(pt[2], pt[0])
            overlap += 1
        else:
            overlap = overlap + 1 if pt[1] else overlap - 1
            if not overlap:
                right = Endpoint(pt[2], pt[0])
                if adjoint:
                    res[-1] = Interval(res[-1].left, right)
                    adjoint = False
                else:
                    res.append(Interval(left, right))

    return res


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [
        (i.left.val, i.left.is_closed, i.right.val, i.right.is_closed) for i in result
    ]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intervals_union.py", "intervals_union.tsv", union_of_intervals_wrapper
        )
    )
