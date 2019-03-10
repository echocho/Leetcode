# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    # binary search
    # O(log n)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        mid = (left + right) // 2
        while left < right:
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
            mid = (left + right) // 2
        return right
        