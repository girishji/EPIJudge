from test_framework import generic_test


def square_root(k: int) -> int:
    le, mid, ri = 0, 0, k
    while le <= ri:
        mid = le - (le - ri) // 2
        if mid * mid <= k:
            le = mid + 1
        else:
            ri = mid - 1

    return mid - 1 if k > 1 else k


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root
        )
    )
