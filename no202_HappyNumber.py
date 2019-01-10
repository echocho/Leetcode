class Solution:
    # to aviod endless looping, 
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen_before = set()
        happy = False 
        while not happy:
            n = sum([int(i)**2 for i in str(n)])
            if n in seen_before:
                return False
            seen_before.add(n)
            if n == 1:
                return True