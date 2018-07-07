# Leetcode189_RotateArray.py

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Solution 1: Note that when k == len(nums) + n, nums is actually the same when k == n. Therefore, to reduce run time, first
    # divide len(nums) with k.
    # O(n)
    if not nums:
        return

    if k == 0 or len(nums) == 1:
        nums[:] = nums[:]
    else:
        if k > len(nums):
            k = k % len(nums)
        target = nums[-k:]
        remain = nums[:-k]
        nums[:k] = target
        nums[k:] = remain

    return nums


print(rotate([1,2,3,4,5,6], 13) == rotate([1,2,3,4,5,6], 1))
print(rotate([], 3) == None)
print(rotate([1,2,3,4,5,6], 3) == [4,5,6,1,2,3])
print(rotate([1], 0) == [1])


