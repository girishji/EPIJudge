from typing import List

from test_framework import generic_test
import bisect
from collections import namedtuple


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    Item = namedtuple("Item", ["val", "idx", "slen"])
    seen = []
    for i, v in enumerate(A[::-1]):
        bisection = bisect.bisect_left(seen, v, key=lambda item: item.val)
        maxslen = 0
        for i in range(bisection, len(seen)):
            maxslen = max(maxslen, seen[i].slen)
        nitem = Item(v, i, maxslen + 1)
        seen.insert(bisection, nitem)

    retval = -1
    for item in seen:
        retval = max(item.slen, retval)
    return retval


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            "longest_nondecreasing_subsequence.tsv",
            longest_nondecreasing_subsequence_length,
        )
    )
