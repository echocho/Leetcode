# Leetcode191_NumberOf1Bits.py

# Solution 1: convert integer into binary and then count the 1s in it
# O(n), with n representing the size of the number

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    n = bin(n)[2:]
    return n.count('1')

print(hammingWeight(11) == 3)
print(hammingWeight(128) == 1)
print(hammingWeight(30) == 4)
