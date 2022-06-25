from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort(reverse=True)
    if A[-1] > 1:
        return 1
    for x in range(A[-1], sum(A) + 1):
        s = 0
        for a in A:
            if s + a < x:
                s += a
            elif s + a == x:
                s += a
                break
        if s != x:
            return x

    return sum(A) + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "smallest_nonconstructible_value.py",
            "smallest_nonconstructible_value.tsv",
            smallest_nonconstructible_value,
        )
    )
