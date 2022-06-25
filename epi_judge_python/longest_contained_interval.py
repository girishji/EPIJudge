from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    aset = set(A)
    dist = 0
    while aset:
        d = 0
        eli = eld = aset.pop()
        while eli + 1 in aset:
            d += 1
            aset.discard(eli + 1)
            eli += 1
        while eld - 1 in aset:
            d += 1
            aset.discard(eld - 1)
            eld -= 1
        dist = max(d, dist)

    return dist + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_contained_interval.py",
            "longest_contained_interval.tsv",
            longest_contained_range,
        )
    )
