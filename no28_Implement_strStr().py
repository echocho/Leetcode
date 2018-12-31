# solution: iterate and compare segs
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1
    start = 0
    end = len(needle)
    while start < end and end <= len(haystack):
        if haystack[start:end] == needle:     
            return start
        start += 1
        end += 1
    return -1


print(strStr('hello', 'll')==2)
print(strStr('hello', 'llo')==2)
print(strStr('hellollo', 'hllo')==-1)
print(strStr('chowchow', '')==0)
print(strStr('aaaaa', 'bbbba')==-1)
print(strStr('aaa', 'aaaa')==-1)