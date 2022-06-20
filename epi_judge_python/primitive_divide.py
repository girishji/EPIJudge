from test_framework import generic_test


def divide(x: int, y: int) -> int:
    # TODO - you fill in here.
    if x < y:
        return 0
    q = 1
    den = y
    while y <= x:
        y <<= 1
        q <<= 1
    return (q >> 1) + divide(x - (y >> 1), den)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
