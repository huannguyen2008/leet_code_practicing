def max_sub_array(nums):
    cur_sum = nums[0]
    max_sum = cur_sum
    for i in range(1, len(nums)):
        cur_sum = max(nums[i] + cur_sum, nums[i])
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(max_sub_array([5, 4, -1, 7, 8]))
