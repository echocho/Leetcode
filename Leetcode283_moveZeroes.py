# Leetcode283_moveZeroes.py

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    zero_cnt = nums.count(0)
    nums[:] = [i for i in nums if i != 0]
    nums += [0] * zero_cnt

    return nums


print(moveZeroes([0,1,0,3,12]) == [1,3,12,0,0])
print(moveZeroes([0,0,0]) == [0,0,0])
print(moveZeroes([0,0,0,3,2,1,0]) == [3,2,1,0,0,0,0])
print(moveZeroes([0,0,1,2,4,3,0,0,9,0]) == [1,2,4,3,9,0,0,0,0,0])
print(moveZeroes([0,1]) == [1,0])
print(moveZeroes([1,0,2,0,3]) == [1,2,3,0,0])
