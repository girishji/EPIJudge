from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    if A[-1] != 9:
        A[-1] += 1
    else:
        A[-1] = 0
        residue = True
        for i in range(len(A) - 2, -1, -1):
            if residue:
                if A[i] == 9:
                    A[i] = 0
                    residue = True
                else:
                    A[i] += 1
                    residue = False
        if residue:
            A.insert(0, 1)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
