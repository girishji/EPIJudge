from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools


def find_missing_element(stream: Iterator[int]) -> int:
    stream, stream_copy = itertools.tee(stream)
    count = [0] * (2**16)
    for s in stream:
        count[s >> 16] += 1
    candidate = next(i for i, cn in enumerate(count) if cn < 2**16)
    seen = [0] * (2**16)
    for s in stream_copy:
        if s >> 16 == candidate:
            seen[s & 0xFFFF] = 1
    unseen = next(i for i, fl in enumerate(seen) if fl == 0)
    return candidate << 16 | unseen


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure("{} appears in stream".format(res))
    except ValueError:
        raise TestFailure("Unexpected no missing element exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "absent_value_array.py",
            "absent_value_array.tsv",
            find_missing_element_wrapper,
        )
    )
