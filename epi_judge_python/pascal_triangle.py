from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if not n:
        return []
    res = [[1]]
    for i in range(n - 1):
        row = [1]
        for j in range(len(res[i]) - 1):
            row.append(res[i][j] + res[i][j + 1])
        row.append(1)
        res.append(row)
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
