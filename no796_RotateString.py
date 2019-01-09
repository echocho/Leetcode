class Solution1:
	# Brute force 
	# O(n**2), but acceptable here as the length of A is upto 100
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

 class Solution2:
 	# if B == A, len(B) == len(A) and B is a substring of A+A
 	def rotateString(self, A, B):
 		return len(A) == len(B) and B in A + A 