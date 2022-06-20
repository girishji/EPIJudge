from test_framework import generic_test
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    n = 0
    num_as_string, negative = (
        (num_as_string[1:].lower(), True)
        if num_as_string[0] == "-"
        else (num_as_string.lower(), False)
    )
    for i in range(len(num_as_string)):
        n += string.hexdigits.index(num_as_string[~i]) * (b1**i)
    res = "" if n != 0 else "0"
    while n > 0:
        res = string.hexdigits[n % b2].upper() + res
        n //= b2
    if negative:
        res = "-" + res
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
