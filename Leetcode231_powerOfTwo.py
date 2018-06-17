# Leetcode231_powerOfTwo.py

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    # Solution 1: divide n by two all the way till the end
    # eliminate zeros, negative, and check if n can be divided by 2 til the end
    # O(size of n)
    if n <= 0: return False
    if n == 1: return True
    if n == 2: return True
    if n % 2 != 0: return False
    while n > 2:
        n = n / 2
        if n % 2 != 0:
            return False
    return True

    # Solution 2: bitwise operation
    # any number which is the power of two should look like this 10, 100, 1000...
    # thus, when we & with the previous number, we get 0
    # O(1)
    """
    return n > 0 and (n & (n - 1)) == 0
    """



print(isPowerOfTwo(1) == True)
print(isPowerOfTwo(2) == True)
print(isPowerOfTwo(16) == True)
print(isPowerOfTwo(218) == False)
print(isPowerOfTwo(256) == True)
print(isPowerOfTwo(13) == False)
print(isPowerOfTwo(1024) == True)
print(isPowerOfTwo(0) == False)


