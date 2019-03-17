class Solution:
	# O(n)
	def plusOne(self, digits):
		"""
		params: list[int]
		rtype: list[int]
		"""
		if not len(digits):
			return 

		for i in range(len(digits) - 1, -1, -1):
			if digits[i] != 9:
				digits[i] += 1
				return digits
			digits[i] = 0
		return [1] + digits

print(Solution().plusOne([1,2,3])==[1,2,4])
print(Solution().plusOne([1,8,9])==[1,9,0])
print(Solution().plusOne([1,9,9])==[2,0,0])
print(Solution().plusOne([9,9,9])==[1,0,0,0])
print(Solution().plusOne([9,8,9])==[9,9,0])
print(Solution().plusOne([1,2])==[1,3])
print(Solution().plusOne([9])==[1,0])
print(Solution().plusOne([8])==[9])
print(Solution().plusOne([])==None)