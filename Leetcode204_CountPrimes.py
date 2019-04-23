import math
import timeit

class Solution1:
    # Time complexity too high
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

class Solution2:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i : n : i] = [False] * len(primes[i * i : n : i])
        return sum(primes)

print('input 1500000')
print('timing solution1')
print(timeit.Timer(lambda: Solution1().countPrimes(1500000)).timeit(number=1))
print('timing solution2')
print(timeit.Timer(lambda: Solution2().countPrimes(1500000)).timeit(number=1))
