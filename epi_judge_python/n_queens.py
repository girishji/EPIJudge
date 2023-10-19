from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def occupied(prow, pcol, n, board):
        for col, row in enumerate(board):
            if row == -1:
                continue
            if prow == row or pcol == col:
                # print("occupied0", prow, pcol)
                return True
            for i, j in zip(range(1, n - row), range(1, n - col)):
                if prow == row + i and pcol == col + j:
                    # print("occupied1", prow, pcol)
                    return True
            for i, j in zip(range(1, row + 1), range(1, col + 1)):
                if prow == row - i and pcol == col - j:
                    # print("occupied2", prow, pcol)
                    return True
            for i, j in zip(range(1, n - row), range(1, col + 1)):
                if prow == row + i and pcol == col - j:
                    # print("occupied3", prow, pcol)
                    return True
            for i, j in zip(range(1, row + 1), range(1, n - col)):
                if prow == row - i and pcol == col + j:
                    # print("occupied4", prow, pcol)
                    return True
        return False

    def place(row, board, n):
        nonlocal result
        for col in range(n):
            tmpb = board.copy()
            if occupied(row, col, n, tmpb):
                continue
            tmpb[col] = row
            if row + 1 < n:
                place(row + 1, tmpb, n)
            if all([q != -1 for q in tmpb]):
                result.append(tmpb)

    result = []
    for col in range(n):
        board = [-1] * n
        board[col] = 0
        if n > 1:
            place(1, board, n)
        if all([q != -1 for q in board]):
            result.append(board)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("n_queens.py", "n_queens.tsv", n_queens, comp))
