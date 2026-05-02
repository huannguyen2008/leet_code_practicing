def two_sum(nums, target):
    """
        :param j:
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums):
            if not j == i and num2 == target - num:
                return i, j


# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([1, 2, 3, 4, 5, 6, 123, 12, 543, 6546, 11, 22, 33, 44, 55, 66], 70))
# print(two_sum([3, 3], 6))
