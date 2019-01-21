# solution1: scan maximum common prefix one by one
# time complexity: O(total characters of all words)
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    strs = sorted(strs, key=lambda x: len(x))
    # print(strs)
    prefix = strs[0]
    # print('prefix', prefix)
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            return ""
    return prefix 

print(longestCommonPrefix(["flower","flow","flight"]) == 'fl')
print(longestCommonPrefix(['', '']) == '')
print(longestCommonPrefix([]) == '')
print(longestCommonPrefix(["dog","racecar","car"]) == '')
print(longestCommonPrefix(["aba","ab",'abc','aacc']) == 'a')
print(longestCommonPrefix(["a", "b", "bc", "acc"]) == "")
print(longestCommonPrefix(["a", "a", "bc", "acc"]) == "")
print(longestCommonPrefix(["a"]) == "a")