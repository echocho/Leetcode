class Solution1:
	# simple recursion but memory exceeded 
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 1:
			return 1
		if n == 2:
			return 2
		return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution2:
	# dynamic programming
	def climbStairs(self, n):
        if n == 0 or n == 1: 
            return 1
        nums = [0] * (n + 1)
        nums[0], nums[1] = 1, 1
        for i in range(2, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[n]