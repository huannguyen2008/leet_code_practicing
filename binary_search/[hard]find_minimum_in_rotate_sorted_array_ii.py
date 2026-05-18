from typing import List


def find_min(nums: List[int]) -> int:
    """
    We compare the mid with most-right element, until the loop done then our min is on the nums[l].
    Problem is: the numbers in the list can be duplicated, so we add the condition: when mid = most-right, we shift the
    right by -1.
    :param nums:
    :return:
    """
    l = 0
    r = len(nums) - 1

    while l < r:
        m = l + (r - l) // 2
        if nums[m] > nums[r]:
            l = m + 1
        elif nums[m] < nums[r]:
            r = m
        else:
            r = r - 1

    return nums[l]
