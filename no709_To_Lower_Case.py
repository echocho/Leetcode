def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    res = ''
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            res += chr(ord(char) + 32)
        else:
            res += char
    return res

print(toLowerCase('HapPy')=='happy')
print(toLowerCase("LOVELY")=='lovely')