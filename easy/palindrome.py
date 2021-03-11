def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    r = str(x)[::-1]
    if r == str(x):
        return True
    else:
        return False


print(reverse(121))
