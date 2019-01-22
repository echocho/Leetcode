class Solution:
    # iterate both strings, compare index and i-th letter; check if only two pairs of index and letter are unmatched
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if not A or not B:
            return False
        
        unmatched = []
        seen = set(list(A))
        for idx, chrt in enumerate(B):
            if chrt not in seen:
                return False
            if chrt != A[idx]:
                unmatched.append(chrt)
        # print(len(unmatched))
        if len(unmatched) == 0 and len(seen) == 1:
            return True
        return len(unmatched) == 2

print(Solution().buddyStrings('ab', 'ba')==True)
print(Solution().buddyStrings('ab', 'ab')==False)
print(Solution().buddyStrings('aa', 'aa')==True)
print(Solution().buddyStrings('aaaaabc', 'aaaaacb')==True)
print(Solution().buddyStrings('', 'aa')==False)
print(Solution().buddyStrings('aab', 'aac')==False)
print(Solution().buddyStrings('abcaa', 'abcbb')==False)