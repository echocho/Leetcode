# Leetcode561_arrayPartition1.py

def arrayPairSum(nums):
    # method 1
    '''
    nums.sort()
    total = 0
    for i in range(0, len(nums), 2):
        total += min(nums[i], nums[i+1])
    return total 
    '''

    # method 2 - faster
    nums.sort()
    return sum(nums[::2])
    

print(arrayPairSum([1,4,3,2]))
print(arrayPairSum([4,7,10,2]))
print(arrayPairSum([23,4,567,43,2,17]))
print(arrayPairSum([1,-4,-3,2]))
print(arrayPairSum([1]))