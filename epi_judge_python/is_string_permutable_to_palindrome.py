from test_framework import generic_test
import collections


def can_form_palindrome(s: str) -> bool:
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1
    ct = collections.Counter(s)
    if len(s) % 2 == 0:
        return all([v % 2 == 0 for v in ct.values()])
    else:
        odd = sum([v % 2 == 1 for v in ct.values()])
        return odd == 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
