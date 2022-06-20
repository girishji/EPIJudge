from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    minv = prices[0]
    diff = 0
    for i, p in enumerate(prices):
        diff = max(p - minv, diff)
        minv = min(p, minv)
    return diff


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
