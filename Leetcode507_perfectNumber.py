# Leetcode507_perfectNumber.py
def checkPerfectNumber(num):
    #  O(n**0.5)
    if num == 0 or num == 1:
        return False
    sqrt_num = num**0.5
    sqrt_num_real = int(sqrt_num.real)
    total = 0
    for i in range(1, sqrt_num_real+1):
        if num % i == 0:
            total += i
            total += (num / i)
    return (total-num) == num


    # Brute force, limit time exceeded
    # O(n)
    '''
    total = 0
    if num % 2 == 0:
        half_num = num/2
        # print('even half_num= ', half_num)
    else:
        half_num = num/2 + 0.5
        # print('odd half_num= ', half_num)

    for i in range(1, int(half_num) +1):
        # print('i', i)
        if num % i == 0:
            total += i
    return sum(positive_divisor) == num
    '''

print(checkPerfectNumber(28))
print(checkPerfectNumber(-6))