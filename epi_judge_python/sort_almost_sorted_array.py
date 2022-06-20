from typing import Iterator, List

from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    h = []
    res = []
    for i, s in enumerate(sequence):
        if i <= k:
            heapq.heappush(h, s)
        else:
            res.append(heapq.heappop(h))
            heapq.heappush(h, s)
    while h:
        res.append(heapq.heappop(h))
        
    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )
