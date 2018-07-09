# Leetcode633_SumOfSquareNumbers.py

import math
def judgeSquareSum(c):
    # O(sqrt(c)log(c))

    s_root = int(math.sqrt(c))
    for i in range(int(s_root) + 1):
        if math.sqrt(int(c - i**2)).is_integer():
            return True
    return False

print(judgeSquareSum(5) == True)
print(judgeSquareSum(10) == True)
print(judgeSquareSum(25) == True)
print(judgeSquareSum(0) == True)
print(judgeSquareSum(3) == False)
print(judgeSquareSum(11) == False)
print(judgeSquareSum(1) == True)
print(judgeSquareSum(2))


