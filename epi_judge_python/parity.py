from test_framework import generic_test


def _parity(x: int) -> int:
    r = 0
    while x:
        r ^= 1
        x = x & (x - 1)
    return r


pp = [_parity(i) for i in range(2**16)]
m1 = ~0 << (16 * 3)
m2 = m1 >> 16
m3 = m2 >> 16
m4 = m3 >> 16


def parity(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    mask = 0xffff
    for _ in range(4):
        if pp[x & mask] > 0:
            result ^= 1
        x >>= 16
    return result


if __name__ == "__main__":
    exit(generic_test.generic_test_main("parity.py", "parity.tsv", parity))
