from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    le, ri = 0, len(A) - 1
    while le <= ri:
        mid = le - (le - ri) // 2
        diff = (A[mid] - A[mid - 1]) if mid > 0 else -1
        if diff < 0:
            return mid
        elif A[mid] > A[ri]:
            le = mid + 1
        elif A[mid] < A[le]:
            ri = mid - 1
        else:
            return le
    return -1


# search_smallest([100, 101, 102, 2, 5])

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )
