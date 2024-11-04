def buy_and_sell(prices):
    min_price, max_profit = float("inf"), 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


list = [5, 3, 2, 7, 6, 8]
print(buy_and_sell(list))
