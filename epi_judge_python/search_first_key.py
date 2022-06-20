from typing import List

from test_framework import generic_test
import bisect


def search_first_of_k(A: List[int], k: int) -> int:
    # res = bisect.bisect_left(A, k)
    # return res if res < len(A) and A[res] == k else -1
    le, ri = 0, len(A) - 1
    while le <= ri:
        mid = le - (le - ri) // 2
        if k == A[mid] and (mid == 0 or (A[mid - 1] < A[mid])):
            return mid
        if k > A[mid]:
            le = mid + 1
        else:
            ri = mid - 1
    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )
