class Solution(object):
	# O(1)
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		num = 0
		while n > 0:
			n = n & (n - 1)
			num += 1
		return num 

print(Solution().hammingWeight(11)==3)
print(Solution().hammingWeight(00000000000000000000000010000000)==1)
