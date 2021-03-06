class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0 or n % 3 != 0:
            return False
        if n == 3:
            return True
        return self.isPowerOfThree(n/3)