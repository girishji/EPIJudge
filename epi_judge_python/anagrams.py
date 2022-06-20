from typing import List

from test_framework import generic_test, test_utils
import collections


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    dd = collections.defaultdict(list)
    for s in dictionary:
        dd["".join(sorted(s))].append(s)
    return [group for group in dd.values() if len(group) > 1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare,
        )
    )
