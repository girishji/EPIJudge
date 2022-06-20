from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    maxad = 0
    for i, a in enumerate(A):
        if a == 0 and maxad <= i and i != len(A) - 1:
            return False
        if a + i > maxad:
            maxad = a + i
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
