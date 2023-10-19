import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str, dictionary: Set[str]) -> List[str]:

    result = []

    def solve(dictn, partial):
        if not partial:
            return True
        if not dictn:
            return False
        while dictn:
            word = dictn.pop()
            print("word", word, "partial", partial)
            i = 0
            while i < len(partial):
                pt = partial.find(word, i)
                i += pt + 1 if pt != -1 else 1
                if pt != -1:
                    before = solve(dictn.copy(), partial[0:pt])
                    after = solve(dictn.copy(), partial[pt + len(word) :])
                    if all([before, after]):
                        result.append(word)
                        return True
        return False

    if solve(dictionary.copy(), domain):
        print("result", result)
        return result
    return []


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary, decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary)
    )

    if not decomposable:
        if result:
            raise TestFailure("domain is not decomposable")
        return

    if any(s not in dictionary for s in result):
        raise TestFailure("Result uses words not in dictionary")

    if "".join(result) != domain:
        raise TestFailure("Result is not composed into domain")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            "is_string_decomposable_into_words.tsv",
            decompose_into_dictionary_words_wrapper,
        )
    )
