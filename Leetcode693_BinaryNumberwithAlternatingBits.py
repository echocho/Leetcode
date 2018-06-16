# Leetcode693_BinaryNumberwithAlternatingBits.py

# convert integer into binary and iterate its bits
# O(n)

def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    n = bin(n)[2:]
    i = 0
    while i+1 < len(n):
        if n[i] == n[i + 1]:
            return False
        i += 1
    return True
print(hasAlternatingBits(5) == True)
print(hasAlternatingBits(7) == False)
print(hasAlternatingBits(11) == False)
print(hasAlternatingBits(10) == True)