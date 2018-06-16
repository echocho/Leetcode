def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # To improve time complexity, use a dictionary to store and retrieve data O(1) each time
    # 1. iterate nums, and put complements in the dictionary
    # 2. at the same time, check if a number's complement is in the dictionary
    # O(n)
    my_dict = {}
    for i in range(len(nums)):
        if target - nums[i] not in my_dict:
            my_dict[nums[i]] = i
        else:
            return [my_dict[target - nums[i]], i]


print(twoSum([2, 2, 1, 5], 4)  == [0, 1])
print(twoSum([3,3], 6) == [0, 1])
print(twoSum([3,2,4], 6) == [1, 2])
