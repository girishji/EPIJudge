from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    i = len(perm) - 1
    while i > 0 and perm[i - 1] > perm[i]:
        i -= 1
    if i == 0:
        return []
    i -= 1
    next = min([p for p in perm[i + 1 :] if p > perm[i]])
    return perm[: i] + [next] + sorted([p for p in perm[i:] if p != next])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", "next_permutation.tsv", next_permutation
        )
    )
