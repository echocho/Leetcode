# Leetcode541_reverseString.py
def reverseStr(s, k):
    '''
    :type s: str
    :type k: int
    :rtype: str '''
    lst = list(s)
    for i in range(0, len(lst), 2*k):
        lst[i:i+k] = lst[i:i+k][::-1] # or reversed(lst[i:i+k])
    
    return ''.join(lst)
        
print(reverseStr('abcdefg', 2))


