class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True
        unmatched = [(a,b) for a, b in zip(A, B) if a != b]
        return len(unmatched) == 2 and unmatched[0] == unmatched[1][::-1]

print(Solution().buddyStrings('ab', 'ba')==True)
print(Solution().buddyStrings('ab', 'ab')==False)
print(Solution().buddyStrings('aa', 'aa')==True)
print(Solution().buddyStrings('aaaaabc', 'aaaaacb')==True)
print(Solution().buddyStrings('', 'aa')==False)
print(Solution().buddyStrings('aab', 'aac')==False)
print(Solution().buddyStrings('abcaa', 'abcbb')==False)