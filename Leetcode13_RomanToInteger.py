class Solution(object):
    # Time complexity: O(n), n = len(s)
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(0, len(s) - 1):
            if ref[s[i]] < ref[s[i+1]]:
                total -= ref[s[i]]
            else:
                total += ref[s[i]]
        return total + ref[s[-1]]

print(Solution().romanToInt('III') == 3)
print(Solution().romanToInt('MCMXCIV') == 1994)
print(Solution().romanToInt('LVIII') == 58)

