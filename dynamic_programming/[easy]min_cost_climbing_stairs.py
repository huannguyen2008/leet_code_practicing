from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    In some case, when reaching n-1, it was good enough. Because the cost of n is heavy and was not necessary.
    :param cost:
    :return:
    """
    n = len(cost)
    cache = [0] * n

    if n == 1:
        return cost[0]

    cache[0] = cost[0]
    cache[1] = cost[1]

    for i in range(2, n):
        cache[i] = min(cache[i - 1] + cost[i], cache[i - 2] + cost[i])

    return min(cache[n - 1], cache[n - 2])
