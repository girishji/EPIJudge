from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    xneg = x < 0
    if xneg:
        x = -x
    result = 0
    while x > 0:
        digit = x % 10
        x //= 10
        result = result * 10 + digit
    if xneg:
        result = -result
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_digits.py", "reverse_digits.tsv", reverse
        )
    )
