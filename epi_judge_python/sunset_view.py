from typing import Iterator, List

from test_framework import generic_test
from collections import namedtuple


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack = []
    for b in sequence:
        stack.append(b)
    res = [0]
    mx = stack.pop()
    i = 0
    while stack:
        b = stack.pop()
        i += 1
        if b > mx:
            res.append(i)
            mx = b
    return list(reversed(res))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sunset_view.py", "sunset_view.tsv", examine_buildings_with_sunset
        )
    )
