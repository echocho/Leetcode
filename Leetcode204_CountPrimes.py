import math

class Solution(object):
    import math
    def isPrime(self, num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        cnt = 0
        for i in range(2, n):
            if self.isPrime(i):
                cnt += 1
        return cnt

print(Solution().countPrimes(1500000))