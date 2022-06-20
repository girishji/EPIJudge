from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    # break y into binary, sum of 2's powers
    tempx = 0
    result = 1
    yneg = y < 0
    if yneg:
        y = -y
    while y > 0:
        if not tempx:
            if not yneg:
                tempx = x
            else:
                tempx = 1 / x
        else:
            tempx *= tempx
        if y & 1 > 0:
            result *= tempx
        y >>= 1

    return result


if __name__ == "__main__":
    exit(generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power))
