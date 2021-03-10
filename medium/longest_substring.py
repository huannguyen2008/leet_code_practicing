def longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    a = b = longest_length = 0
    sub_s = {}
    while b < len(s):
        if s[b] not in sub_s.values():
            sub_s[b] = s[b]
            b += 1
            longest_length = max(len(sub_s), longest_length)
        else:
            del sub_s[a]
            a += 1
    return longest_length, sub_s


print(longest_substring("aab"))
