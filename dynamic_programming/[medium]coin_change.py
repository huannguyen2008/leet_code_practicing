from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Bottom up DP: try to find best case for each `a` in amount, from 1. In each `a`, we loop through all the coin to
    find which coin is suitable for this `a`. Note that we use `dif` to see if we should use that coin or not.
    - float('inf'): this lil guy use to set the `a` if it does not have any case.
    :param coins:
    :param amount:
    :return:
    """
    cache = [0] * (amount + 1)
    coins.sort()
    for i in range(1, amount + 1):
        minn = float('inf')
        for c in coins:
            dif = i - c
            if dif < 0:
                break
            minn = min(minn, cache[dif] + 1)

        cache[i] = minn

    if cache[amount] < float('inf'):
        return cache[amount]
    else:
        return -1

print(coin_change([474,83,404,3], 264))
