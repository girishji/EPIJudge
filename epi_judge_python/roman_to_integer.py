from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    map1 = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    num = 0
    for i in range(len(s)):
        if (
            s[i] in ["I", "X", "C"]
            and i + 1 < len(s)
            and s[i : i + 2] in ["IV", "IX", "XL", "XC", "CD", "CM"]
        ):
            num -= map1[s[i]]
        else:
            num += map1[s[i]]

    return num


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", "roman_to_integer.tsv", roman_to_integer
        )
    )
