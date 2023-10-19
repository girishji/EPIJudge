from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    result = []

    def solve(partial, rest):
        nonlocal result
        if not rest:
            result.append(partial)
            return
        for e in rest:
            part = partial + [e]
            tmp = rest.copy()
            tmp.remove(e)
            solve(part, tmp)

    solve([], A)
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "permutations.py",
            "permutations.tsv",
            permutations,
            test_utils.unordered_compare,
        )
    )
