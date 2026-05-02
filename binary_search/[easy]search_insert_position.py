import math
from typing import List


def search_insert(nums: List[int], target: int):
    l = 0
    r = len(nums) - 1

    if target > nums[r]:
        return len(nums)
    if target <= nums[0]:
        return 0

    while r >= l:
        if (r - l) == 1 and nums[r] > target:
            return r
        m = math.ceil((l + r) / 2)
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m
        elif nums[m] > target:
            r = m
    return None
