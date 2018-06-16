# Leetcode191_NumberOf1Bits.py

# convert integer into binary and then count the ones in it
# O(n)

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