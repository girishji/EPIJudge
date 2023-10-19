from typing import List
import itertools

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    Xlen, Ylen = len(board), len(board[0])
    enclosed = [[True] * Ylen for _ in range(Xlen)]

    def dfs(x, y):
        nonlocal enclosed, Xlen, Ylen
        if not enclosed[x][y]:
            return
        enclosed[x][y] = False
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < Xlen and 0 <= j < Ylen and board[i][j] == "W":
                dfs(i, j)

    for x, y in itertools.chain(
        zip(range(Xlen), [0] * Xlen),
        zip(range(Xlen), [Ylen - 1] * Xlen),
        zip([0] * Ylen, range(Ylen)),
        zip([Xlen - 1] * Ylen, range(Ylen)),
    ):
        if board[x][y] == "W":
            dfs(x, y)

    for x in range(Xlen):
        for y in range(Ylen):
            if enclosed[x][y] and board[x][y] == "W":
                board[x][y] = "B"


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_enclosed_regions.py",
            "matrix_enclosed_regions.tsv",
            fill_surrounded_regions_wrapper,
        )
    )
