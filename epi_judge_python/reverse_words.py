import functools
import string
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reverse_range(b, e):
        for j in range((e - b) // 2):
            s[b + j], s[e - j - 1] = s[e - j - 1], s[b + j]

    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]
    bi = 0
    for i in range(len(s)):
        if s[i] in string.whitespace:
            if bi < i - 1:
                reverse_range(bi, i)
            bi = i + 1
            while bi < len(s) and s[bi] in string.whitespace:
                bi += 1
    if len(s) - bi > 1:
        reverse_range(bi, len(s))

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
