def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    d = {}
    ans = []
    nums.sort()
    max_digit = nums[-1]

    if

    for i in nums[:-1]:
        if max_digit - i in d and d[max_digit - i] >= 1:
            ans.append([i, max_digit - i])
            d[max_digit - i] -= 1
        else:
            d[i] = d.get(i, 0) + 1

    ans += [max_digit]

    if len(ans) == k:
        return True
    return False

print(canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
