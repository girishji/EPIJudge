from typing import List

from test_framework import generic_test
from collections import namedtuple


def matrix_search(A: List[List[int]], x: int) -> bool:
    rows, cols = len(A), len(A[0])
    m, n = 0, cols - 1
    while m < rows and n >= 0:
        if x == A[m][n]:
            return True
        if x < A[m][n]:
            n -= 1
        else:
            m += 1
    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_row_col_sorted_matrix.py",
            "search_row_col_sorted_matrix.tsv",
            matrix_search,
        )
    )
