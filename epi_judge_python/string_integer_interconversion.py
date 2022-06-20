from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if x < 0:
        negative = True
        x = -x
    else:
        negative = False
    res = ""
    if x == 0:
        res = "0"
    else:
        while x > 0:
            res = digits[x % 10] + res
            x //= 10
    if negative:
        res = '-' + res
    return res


def string_to_int(s: str) -> int:
    digits = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    base = 1
    negative = False
    if s[0] == "-":
        s = s[1:]
        negative = True
    elif s[0] == "+":
        s = s[1:]
    res = 0
    while s:
        res += digits[s[-1]] * base
        base *= 10
        s = s[:-1]
    if negative:
        res = -res
    return res


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
