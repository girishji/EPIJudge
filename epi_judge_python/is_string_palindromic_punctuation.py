from test_framework import generic_test
import string


def is_palindrome(s: str) -> bool:
    fr = 0
    ba = len(s) - 1
    while fr < ba:
        while fr < len(s) and (
            s[fr] in string.punctuation or s[fr] in string.whitespace
        ):
            fr += 1
        while ba >= 0 and (s[ba] in string.punctuation or s[ba] in string.whitespace):
            ba -= 1
        if fr < ba and s[fr].lower() != s[ba].lower():
            return False
        fr += 1
        ba -= 1
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
