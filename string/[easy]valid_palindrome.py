def is_palindrome(s):
    converted_s = (''.join(e for e in s if e.isalnum())).lower()
    left = 0
    right = len(converted_s) - 1
    while left <= right:
        if converted_s[left] != converted_s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
