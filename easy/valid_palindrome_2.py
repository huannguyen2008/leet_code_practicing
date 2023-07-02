def helper(self, s, i):
    new_s = s[:i] + s[i + 1:]
    return True if new_s == new_s[::-1] else False


def valid_palindrome(self, s):
    """
    :param self:
    :type s: str
    :rtype: bool
    """
    reversed_s = s[::-1]
    if reversed_s == s:
        return True
    left = 0
    right = len(s) - 1

    for i in range(0, len(reversed_s) - 1):
        if reversed_s[i] == s[i]:
            left += 1
            right -= 1
        else:
            return self.helper(s, left) or self.helper(s, right)
