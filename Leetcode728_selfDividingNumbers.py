# Leetcode728_selfDividingNumbers.py
def selfDividingNumbers(left, right):
    # solution 1: come up with myself 
    nums = [num for num in range(left, right+1)]
    del_nums = []
    i = 0

    for num in nums:
        # print('num = ', num)
        if '0' in str(num):
            del_nums.append(num)
    # print('del_nums', del_nums)
        else:
            num_digit = len(str(num))
            for i in range(0, num_digit):
                if num % int(str(num)[i]) != 0:
                    del_nums.append(num)

    return set(nums) - set(del_nums)

    # ---solution 2: more efficient solution??
    '''def dividNum(n): 
        for i in str(n):
            if i == '0' or n % int(i) != 0:
                return False
        return True
    
    res = []
    for n in range(left, right+1):
        if dividNum(n):
            res.append(n)
    return res 
    '''
    
print(selfDividingNumbers(10, 2289))
        