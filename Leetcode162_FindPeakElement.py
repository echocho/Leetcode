# Leetcode162_FindPeakElement.py

def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # ----- Solution 1: iterate the list once; check if nums[i] > nums[i+1]; peak could appear as the first
    # ----- element, last element in list, or somewhere in the middle. In whichever case, we don't need to compare
    # ----- nums[i] with nums[i-1]
    # ----- O(N)
    # if not nums:
    #     return
    # if len(nums) == 1:
    #     return 0
    # i = 0
    # while i + 1 < len(nums):
    #     if nums[i] > nums[i + 1]:
    #         return i
    #     i += 1
    # return len(nums) - 1

    # ----- Solution 2: iterative binary search
    # ----- O(logN)
    if not nums:
        return

    if len(nums) == 1:
        return 0

    left_indx, right_indx = 0, len(nums) - 1

    while left_indx < right_indx:
        mid_indx = (left_indx + right_indx) // 2

        if nums[mid_indx] < nums[mid_indx + 1]:
            left_indx = mid_indx + 1
        else:
            right_indx = mid_indx

    return left_indx


print(findPeakElement([1,2,3,1]) == 2)
print(findPeakElement([1,2,1,3,5,6,4]) == 5)
print(findPeakElement([2]) == 0)
print(findPeakElement([]) == None)
print(findPeakElement([1,2]) == 1)
print(findPeakElement([6,5,4,3,2,1]) == 0)
print(findPeakElement([1,2,3,4,5,6]) == 5)

