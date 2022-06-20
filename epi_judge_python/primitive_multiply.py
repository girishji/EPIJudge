from test_framework import generic_test


def add(x: int, y: int) -> int:
    t0 = [[(0, 0), (1, 0)], [[1, 0], [0, 1]]]
    t1 = [[(1, 0), (0, 1)], [[0, 1], [1, 1]]]
    res = 0
    result = (2**64) - 1
    for i in range(64):
        if res == 0:
            bit, res = t0[x & 1][y & 1]
        else:
            bit, res = t1[x & 1][y & 1]
        if bit == 0:
            result ^= 1 << i
        x >>= 1
        y >>= 1
    return result


def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    if x < 0 or y < 0:
        raise ValueError("error")
    sh = 0
    res = 0
    while y != 0:
        if y & 1 != 0:
            x2 = x << sh
            res = add(res, x2)
        y >>= 1
        sh += 1
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "primitive_multiply.py", "primitive_multiply.tsv", multiply
        )
    )
