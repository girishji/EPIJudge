import functools
from typing import List
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient,
    check_sequence_is_uniformly_random,
    compute_combination_idx,
    run_func_with_retries,
)
from test_framework.test_utils import enable_executor_hook


def random_subset(n: int, k: int) -> List[int]:
    # res = list(range(n))
    # for i in range(k):
    #     rn = random.randint(i, n - 1)
    #     res[i], res[rn] = res[rn], res[i]
    # return res[:k]
    swapped = {}
    res = []
    for i in range(k):
        rn = random.randrange(i, n)
        res.append(swapped.get(rn, rn))
        swapped[rn] = swapped.get(i, i) # cannot be just i
    return res

    #     rn = random.randrange(i, n)
    #     rnx = swapped.get(rn, rn)
    #     if swapped.get(i):
    #         print(i, swapped[i], rn)
    #     idx = swapped.get(i, i)
    #     swapped[rn] = idx
    #     swapped[i] = rnx
    # return [swapped[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes,
            0.01,
        )

    run_func_with_retries(functools.partial(random_subset_runner, executor, n, k))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "random_subset.py", "random_subset.tsv", random_subset_wrapper
        )
    )
