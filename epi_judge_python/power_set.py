from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    result = []
    for n in range(1 << len(input_set)):
        res = []
        for i in range(len(input_set)):
            if n & 1 > 0:
                res.append(input_set[~i])
            n >>= 1
        result.append(res)

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
