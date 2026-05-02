def check_len_palindromic_from_middle(s, left, right):
    if left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1   # length of the palindrome substring
    # ( R - 1 ) - ( L + 1 ) + 1   (ex: case "racecar" will return R = 7, L = 0)
    # R - 1 - L - 1 + 1
    # R - L - 2 + 1
    # R - L - 1


def longest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    start = 0
    end = 0
    if n <= 1:
        return s
    for i in range(0, n):
        # case that length of palindrome is odd, we check on the same character, ex "abcba"
        odd = check_len_palindromic_from_middle(s, i, i)
        # case that length of palindrome is even, we check on 2 characters from the middle, ex "cbbd"
        even = check_len_palindromic_from_middle(s, i, i + 1)
        palindrome_len = max(odd, even)
        if palindrome_len > end - start:
            start = i - (palindrome_len - 1) // 2
            end = i + palindrome_len // 2
    palindrome = s[start:(end + 1)]
    return palindrome


print(longest_palindrome("cbbd"))
