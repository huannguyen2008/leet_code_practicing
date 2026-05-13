from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Find the smallest element first so we know what kind rotated we are dealing with. Then we can know which parts of
    the array we have to search for the target.
    :param nums:
    :param target:
    :return:
    """
    l = 0
    r = len(nums) - 1

    while l < r:
        m = l + (r - l) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    if nums[l] == target:
        return l
    start = l

    l = 0
    r = len(nums) - 1

    if nums[start] <= target <= nums[r]:
        l = start
    else:
        r = start

    while l < r:
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        if nums[m] > target:
            r = m - 1
    return l if nums[l] == target else -1
