def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = roman_dict[s[len(s) - 1]]
    i = len(s) - 1
    while 0 < i < len(s):
        if roman_dict[s[i]] <= roman_dict[s[i - 1]]:
            num += roman_dict[s[i - 1]]
        else:
            num -= roman_dict[s[i - 1]]
        i -= 1
    return num


print(roman_to_int('IX'))
