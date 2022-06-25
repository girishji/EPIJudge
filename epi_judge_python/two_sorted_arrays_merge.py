from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    x = m + len(B) - 1
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[x] = A[i]
            i, x = i - 1, x - 1
        else:
            A[x] = B[j]
            j, x = j - 1, x - 1
    # while i >= 0:
    #     A[x] = A[i]
    #     x, i = x - 1, i - 1
    while j >= 0:
        A[x] = B[j]
        x, j = x - 1, j - 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
