class Solution1(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

class Solution2(object):
    # without loop
    def isPoserOfThree(self, n):
        return n > 0 and 1162261467 % n == 0