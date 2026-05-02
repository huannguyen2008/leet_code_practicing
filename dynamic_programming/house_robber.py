from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    cache = [0] * n

    if n == 1:
        return nums[0]

    cache[0] = nums[0]
    cache[1] = max(cache[0], nums[1])

    for i in range(2, n):
        cache[i] = max(cache[i - 1], nums[i] + cache[i - 2])
    return cache[n - 1]
