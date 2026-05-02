def my_sqrt(x: int):
    if x < 2:
        return x
    l = 1
    r = x
    ans = 0
    while r >= l:
        m = l + (r - l) // 2
        square = m * m

        if square == x:
            return m
        elif square < x:
            ans = m
            l = m + 1
        elif square > x:
            r = m - 1

    return ans
