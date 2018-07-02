def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # Solution 1: put elements in a hash table and then iterate

    # O(n)

    length = len(nums)

    if length == 0:
        return []

    no_dup = set(nums)
    ans = []

    for i in range(1, length + 1):
        if i not in no_dup:
            ans.append(i)
    return ans

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6])
print(findDisappearedNumbers([1]) == [])
print(findDisappearedNumbers([1,1,1]) == [2,3])
print(findDisappearedNumbers([]) == [])

