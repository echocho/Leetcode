class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B:
            return True
        if not A or not B:
            return False
        A, B = list(A), list(B)
        for i in range(len(A) - 1):
            if A[i+1:] + A[:i+1] == B:
                return True
        return False