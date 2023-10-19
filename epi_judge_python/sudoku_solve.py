import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    L = 9

    if all(partial_assignment[i][j] for i in range(L) for j in range(L)):
        return True
    rows, cols, quad = {}, {}, {}
    for i in range(3):
        for j in range(3):
            quad[(i, j)] = set()
    for i in range(L):
        prow, pcol = set(), set()
        for j in range(L):
            if partial_assignment[i][j]:
                if partial_assignment[i][j] in prow:
                    return False
                prow.add(partial_assignment[i][j])
            if partial_assignment[j][i]:
                if partial_assignment[j][i] in pcol:
                    return False
                pcol.add(partial_assignment[j][i])
            qi, qj = i // 3, j // 3
            if partial_assignment[i][j]:
                if partial_assignment[i][j] in quad[(qi, qj)]:
                    return False
                quad[(qi, qj)].add(partial_assignment[i][j])
        rows[i] = prow
        cols[i] = pcol

    candidate = []
    for i in range(L):
        for j in range(L):
            if partial_assignment[i][j]:
                continue
            cnums = []
            for n in range(1, 10):
                if any([n in rows[i], n in cols[j], n in quad[(i // 3, j // 3)]]):
                    continue
                cnums.append(n)
            if len(cnums) == 0:
                return False
            elif len(cnums) == 1:
                partial_assignment[i][j] = cnums[0]
                return solve_sudoku(partial_assignment)
            else:
                if not candidate or len(candidate[2]) > len(cnums):
                    candidate = [i, j, cnums]
    if not candidate:
        return False
    for c in candidate[2]:
        temp = copy.deepcopy(partial_assignment)
        temp[candidate[0]][candidate[1]] = c
        if solve_sudoku(temp):
            # partial_assignment = temp
            # return True
            partial_assignment[candidate[0]][candidate[1]] = c
            return solve_sudoku(partial_assignment)
        # partial_assignment[candidate[0]][candidate[1]] = c
        # if solve_sudoku(partial_assignment):
        #     return True



    return False


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure("Cell left uninitialized")
        if x < 0 or x > len(seq):
            raise TestFailure("Cell value out of range")
        if x in seen:
            raise TestFailure("Duplicate value in section")
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j]
        for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure("Initial cell assignment has been changed")

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure("Initial cell assignment has been changed")
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure("Initial cell assignment has been changed")

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sudoku_solve.py", "sudoku_solve.tsv", solve_sudoku_wrapper
        )
    )
