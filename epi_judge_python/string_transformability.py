from typing import Set

from test_framework import generic_test
import string
import collections


def transform_string(D: Set[str], s: str, t: str) -> int:
    StrDist = collections.namedtuple("StrDist", ['str', 'dist'])

    def at_unit_dist(s):
        result = []
        for i, ch in enumerate(s):
            for repl in string.ascii_lowercase:
                if repl != ch:
                    st = s[:i] + repl + s[i + 1 :]
                    if st in D:
                        D.remove(st)
                        result.append(st)
        return result

    que = collections.deque()
    que.append(StrDist(s, 0))
    D.remove(s)

    while que:
        nextstr = que.popleft()
        if nextstr.str == t:
            return nextstr.dist
        for st in at_unit_dist(nextstr.str):
            que.append(StrDist(st, nextstr.dist + 1))

    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_transformability.py",
            "string_transformability.tsv",
            transform_string,
        )
    )
