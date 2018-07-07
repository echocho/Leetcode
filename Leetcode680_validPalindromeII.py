# Leetcode680_validPalidromeII.py

class Solution:
    # Solution 1: Brute force. For each index i in the string, remove that character and check if the
    # remaining part is a palindrome (s == s[::-1])
    # O(n**2) This algorithm won't work well if the input is very large!!!!


    # def isPalindrome(self, a):
    #     return a == a[::-1]
    #
    # def validPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     if not s:
    #         return False
    #
    #     if self.isPalindrome(s) is True:
    #         return True
    #
    #     i = 0
    #     while i < len(s):
    #         seg = s[:i] + s[i + 1:]
    #         if self.isPalindrome(seg) is True:
    #             return True
    #         i += 1
    #     return False


    # Solution 2: There can be 2 situations. One is s == s[::-1] and two is s != s[::-1].
    # All in all, is the first letter and the last letter are the same, whether the whole string is a palindrome is very
    # likely dependent on the inner substring. In the second situation, since we can only remove ONE character,
    # if we see a s[i] != s[-1], we remove these two character
    # and check if the remaining is a palindrome.

    # O(n)
    def validPalindrome(self, s):
        if not s:
            return False

        if s == s[::-1]:
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # print('i', 'j', i, j)
                # print('s[i]', 's[j]', s[i], s[j])
                s1 = s[:i] + s[i + 1:]
                # print('s1', s1)
                s2 = s[:j] + s[j + 1:]
                # print('s2', s2)
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                return False
            i += 1
            j -= 1


print(Solution().validPalindrome('aba') == True)
print(Solution().validPalindrome('abca') == True)
print(Solution().validPalindrome('abcb') == True)
print(Solution().validPalindrome('abbaa') == True)
print(Solution().validPalindrome('cbabc') == True)
print(Solution().validPalindrome('abcd') == False)
