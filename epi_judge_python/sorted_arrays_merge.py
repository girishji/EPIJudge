from typing import List

from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    idx = [0] * len(sorted_arrays)
    min_heap = [(sa[0], i) for i, sa in enumerate(sorted_arrays) if len(sa) > 0]
    heapq.heapify(min_heap)
    res = []
    while min_heap:
        top = heapq.heappop(min_heap)
        res.append(top[0])
        si = top[1]
        idx[si] += 1
        if (idx[si] < len(sorted_arrays[si])):
            heapq.heappush(min_heap, (sorted_arrays[si][idx[si]], si))
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
