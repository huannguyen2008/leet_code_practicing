def arrange_coins(n: int) -> int:
    """
    The staircase of arranging coins would be something like 1 + 2 + 3 + ... + k = k(k+1)/2.
    We will use BS to find whether a `k` is present in the range 1->n or not.
    Complexity: O(logn)
    :param n:
    :return:
    """
    l = 1
    r = n

    if n == 1:
        return 1

    while l <= r:
        m = l + (r - l) // 2
        k = ((m + 1) * m) / 2

        if k == n:
            return m
        if k < n:
            l = m + 1
        if k > n:
            r = m - 1
    return r

print(arrange_coins(3))