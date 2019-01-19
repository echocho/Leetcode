class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return ord(s) - 64
        res = 0
        to_process = list(zip([chrt for chrt in s], [i for i in range(len(s) - 1, -1, -1)]))
        for i, j in to_process:
            res += (ord(i) - 64) * 26**j
        return res