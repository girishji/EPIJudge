from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    res = 0
    while x > 0:
        res <<= 1
        if x & 1 > 0:
            res |= 1
        x >>= 1
    print(bin(res))
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_bits.py", "reverse_bits.tsv", reverse_bits
        )
    )
