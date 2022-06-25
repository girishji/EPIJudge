from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    i, j = 0, 0
    res = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] == B[j]:
            if not res or res[-1] != A[i]:
                res.append(A[i])
            i += 1
            j += 1
        else:
            j += 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
