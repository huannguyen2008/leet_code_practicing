def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    is_neg = False
    if x == 0:
        return 0
    revs_number = 0
    if x < 0:
        is_neg = True
    x = abs(x)
    while x != 0:
        remainder = x % 10
        x = int(x / 10)
        revs_number = (revs_number * 10) + remainder
        if x < 1:
            break
    if 2147483647 < revs_number or revs_number < -2147483648:
        return 0
    else:
        return int(revs_number) if is_neg is False else -int(revs_number)


print(reverse(1534236469))
