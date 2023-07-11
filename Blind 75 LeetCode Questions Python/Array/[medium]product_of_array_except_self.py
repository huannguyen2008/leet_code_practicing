def product_except_self(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    output_arr = list(range(n))
    output_arr[0] = 1
    tmp = 1
    for i in range(1, n):    # loop from the left and multiply every element before the current element
        output_arr[i] = nums[i - 1] * output_arr[i - 1]
    for j in range(n - 1, -1, -1):      # loop from the right and multiply every element after the current element
        output_arr[j] = output_arr[j] * tmp
        tmp = tmp * nums[j]
    return output_arr


print(product_except_self([1, 2, 3, 4]))
