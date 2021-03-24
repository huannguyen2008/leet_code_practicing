def int_to_roman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman_num = ''
    # divmod(1994, 1000) will return (1, 994), so this algo basically run through roman_list, divide every number,
    # get the number of character in roman with divmod()[0], divmod()[1] is the next num.
    while num >= 1:
        for i in roman_list:
            roman_num += divmod(num, i[0])[0] * i[1]
            num = divmod(num, i[0])[1]
    return roman_num


print(int_to_roman(1994))
print('MCMXCIV')
