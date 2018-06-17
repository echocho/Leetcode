# Leetcode283_moveZeroes.py

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    # Solution 1: iterate the list, find none zero elements and put them in order, starting from index.
    # And then fill the remaining slots with 0s.

    # O(n)

    i = 0
    for j in range(0, len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    for j in range(i, len(nums)):
        nums[j] = 0
    return nums


print(moveZeroes([0,1,0,3,12]) == [1,3,12,0,0])
print(moveZeroes([0,0,0]) == [0,0,0])
print(moveZeroes([0,0,0,3,2,1,0]) == [3,2,1,0,0,0,0])
print(moveZeroes([0,0,1,2,4,3,0,0,9,0]) == [1,2,4,3,9,0,0,0,0,0])
print(moveZeroes([0,1]) == [1,0])
print(moveZeroes([1,0,2,0,3]) == [1,2,3,0,0])
