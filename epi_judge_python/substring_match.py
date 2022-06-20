from test_framework import generic_test
from functools import reduce


def rabin_karp(t: str, s: str) -> int:
    shash = reduce(lambda res, x: res * 26 + ord(x), s, 0)
    thash = reduce(lambda res, x: res * 26 + ord(x), t[: len(s)], 0)
    if shash == thash:
        return 0
    for i in range(1, len(t) - len(s) + 1):
        thash -= ord(t[i - 1]) * (26 ** (len(s) - 1))
        thash *= 26
        thash += ord(t[i + len(s) - 1])
        if shash == thash and t[i: i + len(s)] == s:
            return i
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
