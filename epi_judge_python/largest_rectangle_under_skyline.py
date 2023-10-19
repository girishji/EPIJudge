from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(heights: List[int]) -> int:
    if not heights:
        return 0
    area = min(heights) * len(heights)

    for i, ht in enumerate(heights):
        left = right = i
        while right < len(heights) and ht <= heights[right]:
            right += 1
        while left >= 0 and ht <= heights[left]:
            left -= 1
        area = max(area, ht * (right - left - 1))
    return area


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "largest_rectangle_under_skyline.py",
            "largest_rectangle_under_skyline.tsv",
            calculate_largest_rectangle,
        )
    )
