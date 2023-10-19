from typing import List

from test_framework import generic_test


def minimum_messiness(words: List[str], line_length: int) -> int:
    print(words)

    def solve(lnum):
        if lines[-lnum]

    from collections import OrderedDict
    lines = OrderedDict()
    remain = line_length
    start = 0
    for i, w in enumerate(words):
        if len(w) < remain:
            remain -= len(w) if remain == line_length else len(w) + 1
        elif len(w) == remain:
            remain = line_length
            lines[(i, start)] = 0
        else:
            assert i > 0
            lines[(i - 1, start)] = remain
            start = i
            remain = line_length - len(w)
            if remain == 0:
                lines[(i, i)] = 0
                remain = line_length

    messiness = sum((x * x for x in lines.values()))

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
