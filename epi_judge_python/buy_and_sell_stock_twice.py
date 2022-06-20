from typing import List

from test_framework import generic_test


# def max_profit(startidx: int, endidx: int, prices: List[float]):
#     if not startidx < endidx:
#         return 0
#     minp = prices[startidx]
#     profit = 0
#     idx = 0
#     for i in range(startidx, endidx):
#         p = prices[i]
#         if profit < p - minp:
#             idx = i
#             profit = p - minp
#         minp = min(p, minp)
#     return (idx, profit)


# def buy_and_sell_stock_twice(prices: List[float]) -> float:
#     profit_twice = 0
#     for bidx in range(len(prices)):
#         sidx = bidx + 1
#         while sidx < len(prices):
#             profit = prices[sidx] - prices[bidx]
#             if profit > 0:
#                 profit_twice = max(profit + max_profit(sidx + 1, prices), profit_twice)
#             sidx += 1
#     return profit_twice


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    buy1, sell1, buy2, sell2 = prices[0], 0, float("inf"), prices[-1]
    pr1, pr2 = 0, 0
    profit1, profit2 = [], []
    for i in range(len(prices)):
        sell1 = max(prices[i], sell1)
        if prices[i] < buy1:
            buy1 = prices[i]
            sell1 = 0
        pr1 = max(sell1 - buy1, pr1)
        profit1.append(pr1)
    for i in reversed(range(1, len(prices))):
        buy2 = min(prices[i], buy2)
        if prices[i] > sell2:
            sell2 = prices[i]
            buy2 = float("inf")
        pr2 = max(sell2 - buy2, pr2)
        profit2.insert(0, pr2)
    profit2.insert(0, 0)

    # print(profit1)
    # print(profit2)
    res = 0
    for p1, p2 in zip(profit1, profit2):
        res = max(res, p1 + p2)
    return res


# buy_and_sell_stock_twice([12,11,13,9,12,8,14,13,15])

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock_twice.py",
            "buy_and_sell_stock_twice.tsv",
            buy_and_sell_stock_twice,
        )
    )
