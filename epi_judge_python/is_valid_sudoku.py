from typing import List

from test_framework import generic_test


def is_valid(array, rows, cols):
    # v = [False] * 10
    # for i in rows:
    #     for j in cols:
    #         if array[i][j]:
    #             if not v[array[i][j]]:
    #                 v[array[i][j]] = True
    #             else:
    #                 return False
    # return True
    elems = [array[i][j] for i in rows for j in cols if array[i][j]]
    return len(elems) == len(set(elems))


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    ranges = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    return all(
        [is_valid(partial_assignment, [i], range(9)) for i in range(9)]
        + [is_valid(partial_assignment, range(9), [i]) for i in range(9)]
        + [is_valid(partial_assignment, i, j) for i in ranges for j in ranges]
    )
    # for i in ranges:
    #     for j in ranges:
    #         if not is_valid(partial_assignment, i, j):
    #             return False
    # return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
