from test_framework import generic_test
import bisect


def change_making(cents: int) -> int:
    coins = [1, 5, 10, 25, 50, 100]
    result = 0
    while cents:
        part = bisect.bisect(coins, cents)
        cents -= coins[part - 1]
        result += 1

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "making_change.py", "making_change.tsv", change_making
        )
    )
