from typing import List


class Solution:
    """
    2 function to find left and right index for the target. We use binary search to find the first index that equals to
    the target. And then keeps looking left or right to find the last index that equals to the target.
    """
    def search_range(self, nums: List[int], target: int) -> List[int]:
        result = [0] * 2
        result[0] = self.find_left(nums, target)
        result[1] = self.find_right(nums, target)
        return result

    @staticmethod
    def find_left(nums: List[int], target: int) -> int:
        idx = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
            if nums[m] == target:
                idx = m
        return idx

    @staticmethod
    def find_right(nums: List[int], target: int) -> int:
        idx = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
            if nums[m] == target:
                idx = m
        return idx
