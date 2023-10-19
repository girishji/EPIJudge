import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple("Item", ("weight", "value"))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    def solve(k, available):
        if k < 0:
            return 0
        if optimal[k][available] == -1:
            without_item = solve(k - 1, available)
            with_item = (
                solve(k - 1, available - items[k].weight) + items[k].value
                if available >= items[k].weight
                else 0
            )
            optimal[k][available] = max(with_item, without_item)
        return optimal[k][available]

    optimal = [[-1] * (capacity + 1) for _ in range(len(items))]
    return solve(len(items) - 1, capacity)

    # optimal = [0] * (capacity + 1)
    #
    # for item in items:
    #     if item.weight < capacity:
    #         temp = [0] * (capacity + 1)
    #         for k in range(item.weight, capacity + 1):
    #             temp[k] = max(optimal[k], optimal[k - item.weight] + item.value)
    #         optimal = temp
    # return optimal[capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "knapsack.py", "knapsack.tsv", optimum_subject_to_capacity_wrapper
        )
    )
