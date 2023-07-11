def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    min_prices = prices[0]
    for p in prices:
        if min_prices > p:
            min_prices = p
        elif (p - min_prices) > profit:
            profit = p - min_prices
    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))
