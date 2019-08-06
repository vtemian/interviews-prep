from typing import List


def solve(stocks: List[int]) -> int:
    profit  = 0
    min_price = stocks[0]

    for price in stocks:
        sold_today = price - min_price

        profit = max(profit, sold_today)
        min_price = min(price, min_price)

    return profit


result = solve([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
assert result == 30, result
