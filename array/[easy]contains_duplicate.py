def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i-1] == sorted_nums[i]:
            return True
    return False


print(contains_duplicate([1, 3, 2, 1]))
