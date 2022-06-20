from typing import List

from test_framework import generic_test, test_utils

import heapq


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    maxh = [(-A[0], 0)]

    res = []
    for _ in range(k):
        top = heapq.heappop(maxh)
        res.append(-top[0])
        i1 = top[1] * 2 + 1
        i2 = top[1] * 2 + 2
        if i1 < len(A):
            heapq.heappush(maxh, (-A[i1], i1))
        if i2 < len(A):
            heapq.heappush(maxh, (-A[i2], i2))
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare,
        )
    )
