# Leetcode371_sumOfTwoIntegers.py

def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # Solution 1: use bitwise operation
    while b:
        carry = a & b
        a ^= b
        b = carry << 1

    return a

print(getSum(6, 3) == 9)
print(getSum(9, 4) == 13)

