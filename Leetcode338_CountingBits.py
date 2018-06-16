# Leetcode338_CountingBits.py

def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    # method 1: Use built-in functions. Convert into binary first and then count.
    # O(n * size of integer num)
    """""
    ans = []
    for i in range(0, num+1):
        i = bin(i)[2:]
        ans.append(i.count('1'))
    return ans
    """""
    # method 2: Dynamic programming: n's binary represention ==
    # n/2's bin + '0' (if n is odd) or n/2 + '1' (if n is even). Built-in functions not needed.
    # O(n)
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]
    lst = [0, 1]
    for i in range(2, num+1):
        lst.append(lst[int(i/2)] + (i & 1))
    return lst
print(countBits(5))
        
