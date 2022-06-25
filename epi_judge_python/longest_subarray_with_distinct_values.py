from typing import List

from test_framework import generic_test
import collections


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    seen = collections.OrderedDict()
    dist = 0
    for i, w in enumerate(A):
        if w in seen:
            dist = max(dist, i - seen[iter(seen).__next__()])
            while seen.popitem(False)[0] != w:
                pass
        seen[w] = i
    if A:
        dist = max(dist, len(A) - seen[iter(seen).__next__()])

    return dist


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            "longest_subarray_with_distinct_values.tsv",
            longest_subarray_with_distinct_entries,
        )
    )
