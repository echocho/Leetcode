class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans, i, base = 0, 1, 5
        while base ** i <= n:
        	ans += n // base ** i 
        	i += 1
        return ans 

def answer_checker(n):
	total = 1
	zero_cnt = 0
	for i in range(1, n + 1):
		total *= i 
	for digit in str(total)[::-1]:
		if digit == '0':
			zero_cnt += 1
		else: 
			return zero_cnt

print(Solution().trailingZeroes(3)==answer_checker(3)==0)
print(Solution().trailingZeroes(5)==answer_checker(5)==1)
print(Solution().trailingZeroes(10)==answer_checker(10)==2)
print(Solution().trailingZeroes(20)==answer_checker(20)==4)
print(Solution().trailingZeroes(30)==answer_checker(30)==7)