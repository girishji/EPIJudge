from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    count, res = 0, []
    for ch in s:
        if ch.isdigit():
            count = 10 * count + int(ch)
        else:
            res.append(count * ch)
            count = 0
    return ''.join(res)


def encoding(s: str) -> str:
    res = ''
    count = 1
    if len(s) < 1:
        return ''
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            res += str(count) + s[i]
            prev = s[i]
            count = 0
    return res


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
