from test_framework import generic_test
import math


def square_root(x: float) -> float:
    le, md, ri = 0.0, 0.0, max(1, x)
    while le < ri:
        md = (le + ri) / 2
        # print(le, md, ri)
        if md * md < x:
            le = md
        else:
            ri = md
        if math.isclose(le, ri):
            return le
    return md

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "real_square_root.py", "real_square_root.tsv", square_root
        )
    )
