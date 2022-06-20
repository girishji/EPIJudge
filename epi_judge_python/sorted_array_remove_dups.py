import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if not len(A):
        return 0
    ue = A[0]
    sentry = A[0] - 1
    ns = 0
    si = -1
    for i in range(1, len(A)):
        if A[i] == ue:
            A[i] = sentry
            ns += 1
            if si == -1:
                si = i
        else:
            ue = A[i]

    if not ns:
        return len(A)
    i = 0
    while i < len(A):
        if i > si and A[i] != sentry:
            A[si] = A[i]
            A[i] = sentry
            si += 1
        i += 1
    return len(A) - ns


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_array_remove_dups.py",
            "sorted_array_remove_dups.tsv",
            delete_duplicates_wrapper,
        )
    )
