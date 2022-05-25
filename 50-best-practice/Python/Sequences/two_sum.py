def twoSumBruteForce(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums):
            if not j == i and num2 == target - num:
                return i, j


def twoSumDict(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict_nums = dict()
    for i, num in enumerate(nums):
        remain = target - num
        if remain in dict_nums:
            return dict_nums[remain], i
        dict_nums[num] = i


print(twoSumDict([2, 7, 11, 15], 9))
print(twoSumDict([1, 2, 3, 4, 5, 6, 123, 12, 543, 6546, 11, 22, 33, 44, 55, 66], 70))
print(twoSumDict([3, 3], 6))
