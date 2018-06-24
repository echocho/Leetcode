# Leetcode167_twoSum.py

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Solution 1: use a dictionary to store and retrieve data O(1) each time
    # 1. iterate nums, and put complements in the dictionary
    # 2. at the same time, check if a number's complement is in the dictionary
    # O(n)
    ''''
    my_dict = {}
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement not in my_dict:
            my_dict[numbers[i]] = i + 1
        else:
            return [my_dict[complement], i + 1]
    '''

    # Solution 2: since the array is already sorted, keep two pointers
    # 1. one starts from head (left) and the other from the end (right)
    # 2. increment left and decrement right and check if the two values pointed sum up to the target
    # O(n)
    left, right = 0, len(numbers) -1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left +1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

print(twoSum([2, 7, 11, 15], 9) == [1,2])
print(twoSum([1, 2, 2, 5], 4) == [2, 3])
print(twoSum([3, 3], 6) == [1, 2])
print(twoSum([2, 3, 4], 6) == [1, 3])

