class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[-1]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        robbed = [0] * len(nums)
        robbed[0], robbed[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            robbed[i] = max(robbed[i - 2] + nums[i], robbed[i - 1])
        return robbed[-1]