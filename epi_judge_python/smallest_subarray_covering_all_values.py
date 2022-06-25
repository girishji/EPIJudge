import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple("Subarray", ("start", "end"))


def find_smallest_sequentially_covering_subset(
    paragraph: List[str], keywords: List[str]
) -> Subarray:
    sta, end = -1, len(paragraph)
    kw2 = 0
    for i, w in enumerate(paragraph):
        if w != keywords[0]:
            continue
        st = i
        if st < kw2:
            sta = st
            continue
        idx, kw = i + 1, 1
        while kw < len(keywords) and idx < len(paragraph):
            if keywords[kw] == paragraph[idx]:
                kw2temp = idx if kw == 1 else 0
                kw += 1
                if kw == len(keywords):
                    en = idx
                    if en - st < end - sta:
                        kw2 = kw2temp
                        sta, end = st, en
                    break
            idx += 1

    return Subarray(sta, end)


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph, keywords):
    result = executor.run(
        functools.partial(
            find_smallest_sequentially_covering_subset, paragraph, keywords
        )
    )

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError("Subarray start index is negative")

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            "smallest_subarray_covering_all_values.tsv",
            find_smallest_sequentially_covering_subset_wrapper,
        )
    )
