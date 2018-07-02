# Leetcode279_perfectSquares.py

import math


dp = {}
def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    global dp
    t = 1
    while t ** 2 < n:
        if n not in dp:
            dp[n] = n
        dp[n] = min(1 + numSquares(n - t ** 2), dp[n])
        t += 1
    if t ** 2 == n:
        dp[n] = 1
    return dp[n]


#
# print(numSquares(1) == 1)
print(numSquares(2) == 2)
print(numSquares(3) == 3)
print(numSquares(4) == 1)
print(numSquares(5))
print(numSquares(5) == 2)
print(numSquares(6) == 3)
print(numSquares(7) == 4)
print(numSquares(35))
