from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    freq = {}
    for i, w in enumerate(paragraph):
        if w not in freq:
            freq[w] = (i, len(paragraph))
        else:
            d = freq[w]
            freq[w] = (i, min(d[1], i - d[0]))
    minval = min([d[1] for d in freq.values()]) if freq else -1
    return minval if minval < len(paragraph) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
