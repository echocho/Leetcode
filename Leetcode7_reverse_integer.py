def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if not x:
        return 0

    flag = False
    x_str = str(x)
    if x_str[0] == '-':
        flag = True
        x_str = x_str[1:]
    
    # remove end zeros
    while x_str[-1] == '0':
        x_str = x_str[:-1]
    
    rev = x_str[::-1]
    if flag:
        rev = '-' + rev
    rev = int(rev)
    # check overflow
    if rev > 2**31 - 1 or rev < -2**31:
        rev = 0
        
    return rev

print(reverse(-12400))
print(reverse(898349349))
print(reverse(49030498230489238408230498092384023984928048304802398409280))