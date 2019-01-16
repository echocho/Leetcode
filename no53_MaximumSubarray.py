class Solution(object):
	# Kadane's algorithm
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ends_here, max_so_far = nums[0]
        for i in range(1, nums[1:]):
        	max_ends_here = max(i, max_ends + i)
        	max_so_far = max(max_so_far, max_ends)
        return max_so_far