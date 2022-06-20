from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    dist = len(square_matrix) - 1
    if dist < 0:
        return []
    result = square_matrix[0][:]
    downleft = True
    col = dist 
    row = 1
    while dist > 0:
        if downleft:
            result += [square_matrix[i][col] for i in range(row, row + dist)]
            col -= 1
            row = row + dist - 1
            result += [square_matrix[row][j] for j in range(col, col - dist, -1)]
            row -= 1
            col = col - dist + 1
        else:
            result += [square_matrix[i][col] for i in range(row, row - dist, -1)]
            col += 1
            row = row - dist + 1
            result += [square_matrix[row][j] for j in range(col, col + dist)]
            row += 1
            col = col + dist - 1
        dist -= 1
        downleft = not downleft
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
