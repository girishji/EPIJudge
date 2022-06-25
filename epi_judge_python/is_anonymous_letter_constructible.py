from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    lcnt = collections.Counter(letter_text)
    mcnt = collections.Counter(magazine_text)
    for k, v in lcnt.items():
        if v > mcnt[k]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
