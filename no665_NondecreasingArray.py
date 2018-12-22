def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return True
    
    modified = False
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            if modified:
                return False
            if i >=2 and nums[i] < nums[i-2]:
                nums[i] = nums[i-1]
            modified = True
    return True