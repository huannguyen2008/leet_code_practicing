def climb_stairs(n: int) -> int:
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # if n not in self.cache:
    #     self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    # return self.cache[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    cache = [0] * n
    cache[0] = 1
    cache[1] = 2
    for i in range(2, n):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n - 1]
