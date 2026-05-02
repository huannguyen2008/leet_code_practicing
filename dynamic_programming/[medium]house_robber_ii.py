from typing import List


def rob(nums: List[int]) -> int:
    """
    Instead of go from house 1 to house n to find the best plan just like the house robber 1, in this problem they make
    house 1 and house n to be adjacent. So what we do is separate into 2 cases: go from house 1 to house n-1, and go
    from house 2 to house n. Take the max of 2 cases then we will have our case.
    :param nums:
    :return:
    """
    n = len(nums)
    cache1 = [0] * n
    cache2 = [0] * n

    if n == 1:
        return nums[0]

    cache1[0] = nums[0]
    for i in range(1, n - 1):
        cache1[i] = max(cache1[i - 1], nums[i] + (cache1[i - 2] if i >= 2 else 0))

    cache2[1] = nums[1]
    for j in range(2, n):
        cache2[j] = max(cache2[j - 1], nums[j] + (cache2[j - 2] if j >= 2 else 0))

    return max(cache1[n - 2], cache2[n - 1])
