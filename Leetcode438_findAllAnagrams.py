# Leetcode438_findAllAnagrams.py
import collections

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    ans = []
    p_counter = collections.Counter(p)
    # print(p_counter)
    s_counter = collections.Counter(s[:len(p)-1])
    # print(s_counter)
    
    for i in range(len(p)-1, len(s)):
        # print(i)
        s_counter[s[i]] += 1
        # print(s[i])
        # print('begin: ', s_counter)
        
        if s_counter == p_counter:
            ans.append(i-len(p)+1)
            # print(ans)
        
        s_counter[s[i-len(p)+1]] -= 1
        # print(s[i])
        # print('subtract: ', s_counter)

        if s_counter[s[i-len(p)+1]] == 0:
            # print('yes, zero: ', s[i])
            del s_counter[s[i-len(p)+1]]
        # print('del: ', s_counter)

    return ans

print(findAnagrams('cbaebabacd', 'abc'))
'''    
def permute(lst):
    res = []
    if len(lst) == 1:
        return lst
    for i, a in enumerate(lst):
        print('i, a: ', i, a)
        for p in permute(lst[:i] + lst[i+1:]):
            # print('lst[:i] + lst[i+1:]: ', lst[:i] + lst[i+1:])
            # print('p: ', p)
            res.append(a+p)
            # print('res: ', res)
    return res'''
