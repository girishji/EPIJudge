from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:

    def solve(row, idx):
        if weights[row][idx] == -1:
            if row == 0:
                weights[0][0] = triangle[0][0]
            else:
                if idx == 0:
                    weights[row][idx] = solve(row - 1, 0) + triangle[row][0]
                elif idx == row:
                    weights[row][idx] = solve(row - 1, idx - 1) + triangle[row][idx]
                else:
                    weights[row][idx] = min(
                        solve(row - 1, idx - 1), solve(row - 1, idx)
                    ) + triangle[row][idx]
        return weights[row][idx]

    weights = [[-1] * len(row) for row in triangle]
    for i in range(len(triangle)):
        solve(len(triangle) - 1, i)
    return min(weights[len(triangle) - 1]) if triangle else 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_weight_path_in_a_triangle.py",
            "minimum_weight_path_in_a_triangle.tsv",
            minimum_path_weight,
        )
    )
