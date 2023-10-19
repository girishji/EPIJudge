from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    cand = None
    count = 0
    for s in stream:
        if not cand or not count:
            cand = s
            count = 1
            continue
        count += 1 if s == cand else -1
    return cand if cand else ''


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "majority_element.py", "majority_element.tsv", majority_search_wrapper
        )
    )
