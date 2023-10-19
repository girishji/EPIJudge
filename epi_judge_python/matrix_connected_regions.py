from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[int]]) -> None:

    def dfs(x, y, color):
        Xlen, Ylen = len(image), len(image[0])
        adj = [
            (i, j)
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            if 0 <= i < Xlen and 0 <= j < Ylen and image[i][j] == color
        ]
        for pix in adj:
            image[pix[0]][pix[1]] = 0 if color else 1
        for pix in adj:
            dfs(pix[0], pix[1], color)

    color = image[x][y]
    image[x][y] = 0 if color else 1
    dfs(x, y, color)

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_connected_regions.py", "painting.tsv", flip_color_wrapper
        )
    )
