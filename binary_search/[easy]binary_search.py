from typing import List


def search(nums: List[int], target: int) -> int:
    """
    We usually use (right + left) // 2 to find the middle number. But if right is too big, plus it with left will make
    some errors. That's why we need left + (right - left) // 2.
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if nums[left] == target else -1
