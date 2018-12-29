def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True

    stack = []
    open_brackets = ['[', '{', '(']
    symbol_dict = {'}': '{', ']': '[', ')': '('}
    if s[0] not in open_brackets:
        return False

    for i in s:
        if i in open_brackets:
            stack.append(i)
        else:
            try:
                if stack.pop() != symbol_dict.get(i):
                    return False
            except:
                return False
    if len(stack):
        return False
    return True

print(isValid('[{]')==False)
print(isValid('()[]{}')==True)
print(isValid('')==True)
print(isValid('{({[]})}')==True)
print(isValid('][')==False)
print(isValid('[])')==False)
print(isValid('[)')==False)
print(isValid(')))')==False)
print(isValid("(])")==False)
print(isValid("{()}]")==False)
print(isValid('(')==False)
