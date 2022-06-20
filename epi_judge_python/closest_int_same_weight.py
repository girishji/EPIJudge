from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    i = 0
    while (x & 1 << i) == 0:
        i += 1
    if i > 0:
        x ^= (1 << i) | (1 << i - 1)
    else:
        while (x & 1 << i) > 0:
            i += 1
        x |= 1 << i
        x ^= 1 << (i - 1)
    return x


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "closest_int_same_weight.py",
            "closest_int_same_weight.tsv",
            closest_int_same_bit_count,
        )
    )
