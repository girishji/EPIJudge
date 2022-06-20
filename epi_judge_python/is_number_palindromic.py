from test_framework import generic_test
import math


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    dlen = math.floor(math.log10(x))
    msd = dlen
    while x > 0:
        md = x // (10 ** msd)
        if md != x % 10:
            return False
        x -= md * (10 ** msd)
        msd -= 2
        x //= 10
        
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
