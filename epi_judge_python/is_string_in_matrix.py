from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:

    result = False

    def solve(i, j, k):
        nonlocal result
        if (
            result
            or not 0 <= i < len(grid)
            or not 0 <= j < len(grid[0])
            or k == len(pattern)
            or grid[i][j] != pattern[k]
        ):
            return
        if k == len(pattern) - 1:
            result = True
            return
        if k not in explored[i][j]:
            solve(i + 1, j, k + 1)
            solve(i - 1, j, k + 1)
            solve(i, j + 1, k + 1)
            solve(i, j - 1, k + 1)
            explored[i][j].add(k)

    explored = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == pattern[0]:
                solve(i, j, 0)
                if result:
                    return True
    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_in_matrix.py",
            "is_string_in_matrix.tsv",
            is_pattern_contained_in_grid,
        )
    )
