def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return False

    stack = []
    open_brackets = ['[', '{', '(']
    symbol_dict = {'}': '{', ']': '[', ')': '('}
    if s[0] not in open_brackets:
        return False

    for i in s:
        if i in open_brackets:
            stack.append(i)
        elif stack[-1] == symbol_dict.get(i):
            stack.pop()
    if len(stack):
        return False
    return True

print(isValid('[{]')==False)
print(isValid('()[]{}')==True)
print(isValid('')==False)
print(isValid('{({[]})}')==True)
print(isValid('][')==False)
print(isValid('[])')==False)
