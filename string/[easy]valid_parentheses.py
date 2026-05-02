def is_valid(s):
    """
        :type s: str
        :rtype: bool
        """
    if len(s) % 2 == 1:
        return False
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' and stack[-1] == '(':
            stack.pop(-1)
        elif c == '}' and stack[-1] == '{':
            stack.pop(-1)
        elif c == ']' and stack[-1] == '[':
            stack.pop(-1)
    if not stack:
        return True


print(is_valid('()()()()'))
print(is_valid('{[]}'))
