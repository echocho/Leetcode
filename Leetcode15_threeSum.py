# Leetcode15_threeSum.py

import itertools

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Solution 1: iterate and get all possible sub arrays
    # O(n**2)
    ans = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ans.append([nums[i], nums[j], nums[j]])

    return [elem for elem in ans if sum(elem) == 0]


print(threeSum([-1, 0, 1, 2, -1, -4]) == [[-1,-1,2],[-1,0,1]])



