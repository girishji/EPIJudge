from typing import List

from test_framework import generic_test
import random

 
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def pivot(L, R):
        if R - L <= 1:
            return L
        p = random.randrange(L, R)
        # print("pivot pt, ", p, A[p], 'L R', L, R)
        A[L], A[p] = A[p], A[L]
        p = L
        for i in range(L + 1, R):
            if A[i] > A[p]:
                A[i], A[p] = A[p], A[i]
                p += 1
                A[i], A[p] = A[p], A[i]
        return p

    L, R = 0, len(A)
    p = pivot(L, R)
    while p + 1 != k and L != R:
        if p < k - 1:
            L = p + 1
        else:
            R = p
        p = pivot(L, R)

    return A[p]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_largest_in_array.py", "kth_largest_in_array.tsv", find_kth_largest
        )
    )
