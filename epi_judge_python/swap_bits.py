from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    # ib = (x & 1 << i == 0)
    # jb = (x & 1 << j == 0)
    # if ib == jb:
    #     return x
    # if ib:
    #     x |= 1 << i 
    # else:
    #     x &= ~(1 << i)
    # if jb:
    #     x |= 1 << j 
    # else:
    #     x &= ~(1 << j)
    # return x
    if (x >> i & 1) != (x >> j & 1):
        x ^= 1 << i | 1 << j
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
