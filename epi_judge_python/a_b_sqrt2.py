from typing import List

from test_framework import generic_test


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    from collections import namedtuple

    AB = namedtuple("AB", "a b")
    res = []
    import math

    rt = math.sqrt(2)
    from sortedcontainers import SortedSet

    ss = SortedSet([(0, AB(0, 0))])
    while len(res) < k:
        n = ss.pop(0)
        res.append(n[0])
        ss.update(
            [
                (x.a + x.b * rt, x)
                for x in [AB(n[1].a + 1, n[1].b), AB(n[1].a, n[1].b + 1)]
            ]
        )

    return [] if not k else res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "a_b_sqrt2.py", "a_b_sqrt2.tsv", generate_first_k_a_b_sqrt2
        )
    )
