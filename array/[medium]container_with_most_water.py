def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    a = result = 0
    b = len(height) - 1
    while a < b:
        if height[a] < height[b]:
            area = height[a] * (b - a)
            result = max(result, area)
            a += 1
        else:
            area = height[b] * (b - a)
            result = max(result, area)
            b -= 1
    return result


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
