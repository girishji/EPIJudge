import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    na = nb = 0
    for i in range(size):
        if s[i] == 'a':
            na += 1
        elif s[i] == 'b':
            nb += 1
    count = size + na - nb
    idx = 0
    for i in range(size):
        if s[i] != 'b':
            s[idx] = s[i]
            idx += 1
    idx2 = count - 1
    for i in reversed(range(idx)):
        if s[i] == 'a':
            s[idx2] = s[idx2 - 1] = 'd'
            idx2 -= 2
        else:
            s[idx2] = s[i]
            idx2 -= 1
    return count


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
