from typing import List

from test_framework import generic_test


def rotate(matrix, k, n):
    to = [(k, i) for i in range(k, k + n - 1)]
    ri = [(i, k + n - 1) for i in range(k, k + n - 1)]
    bo = [(k + n - 1, i) for i in range(k + n - 1, k, -1)]
    le = [(i, k) for i in range(k + n - 1, k, -1)]
    for a, b, c, d in zip(to, ri, bo, le):
        (
            matrix[b[0]][b[1]],
            matrix[c[0]][c[1]],
            matrix[d[0]][d[1]],
            matrix[a[0]][a[1]],
        ) = (
            matrix[a[0]][a[1]],
            matrix[b[0]][b[1]],
            matrix[c[0]][c[1]],
            matrix[d[0]][d[1]],
        )


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)
    for i in range(len(square_matrix) // 2):
        rotate(square_matrix, i, n)
        n -= 2
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_rotation.py", "matrix_rotation.tsv", rotate_matrix_wrapper
        )
    )
