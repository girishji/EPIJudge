from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    share = target_payroll / len(current_salaries)
    excess = sum(share - s for s in current_salaries if s < share)
    if not excess:
        return share
    import math

    for i, s in enumerate(current_salaries):
        if s > share:
            n = len(current_salaries) - i
            if excess / n < s - share or math.isclose(excess / n, s - share):
                return excess / n + share
            else:
                excess -= (s - share) * n
                share = s

    return -1.0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "find_salary_threshold.py", "find_salary_threshold.tsv", find_salary_cap
        )
    )
