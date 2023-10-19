from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    def has_two_sum(A, t):
        left, right = 0, len(A) - 1
        while left <= right:
            if A[left] + A[right] == t:
                return True
            elif A[left] + A[right] > t:
                right -= 1
            else:
                left += 1
        return False

    A.sort()
    return any(has_two_sum(A, t - a) for a in A)

    # aset = set(A)
    # for i in A:
    #     for j in A:
    #         if t - i - j in aset:
    #             return True
    # return False


if __name__ == "__main__":
    exit(generic_test.generic_test_main("three_sum.py", "three_sum.tsv", has_three_sum))
