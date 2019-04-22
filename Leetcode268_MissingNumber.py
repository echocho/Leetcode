# Time complexity: O(N)
# Use XOR. XOR (all elements in nums) with (all elements from 0 to len(nums)+1)
# Those nums appear twice will be xor-ed out (to 0) and the one left is the missing one. 
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for elem in range(len(nums)+1):
            xor ^= elem
        for elem in nums:
            xor ^= elem
        return xor
