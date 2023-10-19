from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:

    result = []

    def solve(st, op, cl, num_pairs):
        print(st)
        if len(st) == 2 * num_pairs:
            result.append(st)
        else:
            if op + cl == num_pairs:
                solve(st + ')', op - 1, cl + 1, num_pairs)
                return
            if op > 0:
                solve(st + ')', op - 1, cl + 1, num_pairs)
            solve(st + '(', op + 1, cl, num_pairs)

    solve('', 0, 0, num_pairs)
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_balanced_parentheses.py",
            "enumerate_balanced_parentheses.tsv",
            generate_balanced_parentheses,
            test_utils.unordered_compare,
        )
    )
