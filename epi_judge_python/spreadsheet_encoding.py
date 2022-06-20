from test_framework import generic_test
import string
import functools


def ss_decode_col_id(col: str) -> int:
    # n = 0
    # for i in range(len(col)):
    #     n += (string.ascii_uppercase.index(col[~i]) + 1) * (26 ** i)
    return functools.reduce(
        lambda result, d: (string.ascii_uppercase.index(d) + 1) + result * 26, col, 0
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
