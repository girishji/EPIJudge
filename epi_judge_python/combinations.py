from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:

    result = []

    def solve(start, n, k, comb):
        nonlocal result
        if len(comb) == k:
            result.append(comb)
        else:
            for i in range(start, n + 1):
                tc = comb.copy()
                tc.append(i)
                solve(i + 1, n, k, tc)

    solve(1, n, k, [])
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            "combinations.tsv",
            combinations,
            comparator=test_utils.unordered_compare,
        )
    )
