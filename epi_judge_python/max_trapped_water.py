from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    assert len(heights) > 1
    left, right = 0, len(heights) - 1

    def trapped(le, ri):
        return min(heights[le], heights[ri]) * (ri - le)

    max_water = 0
    while left < right:
        max_water = max(max_water, trapped(left, right))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_trapped_water.py", "max_trapped_water.tsv", get_max_trapped_water
        )
    )
