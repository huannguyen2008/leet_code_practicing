from typing import List


def find_min(nums: List[int]) -> int:
    """
    We compare the mid with most-right element, until the loop done then our min is on the nums[l].
    :param nums:
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

    return nums[l]
