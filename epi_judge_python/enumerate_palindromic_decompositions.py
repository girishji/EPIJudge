from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    result = []

    def palindrome(txt):
        return txt == txt[::-1]

    def solve(st, part):
        nonlocal result
        if st >= len(text):
            result.append(list(part))
            return
        # print(st, text[st], part)
        for n in range(st + 1, len(text) + 1):
            if palindrome(text[st:n]):
                solve(n, part + [text[st:n]])

    solve(0, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            "enumerate_palindromic_decompositions.tsv",
            palindrome_decompositions,
            comp,
        )
    )
