class Solution:
	# use two variables to keep track of lowest price and max profit
	# O(n)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, lowestPrice = 0, float('inf')
        for i in range(len(prices)):
        	if prices[i] < lowestPrice:
        		lowestPrice = prices[i]
        	elif prices[i] - lowestPrice > maxProfit:
        		maxProfit = prices[i] - lowestPrice
        return maxProfit

print(Solution().maxProfit([7,1,5,3,6,4])==5)
print(Solution().maxProfit([7,6,4,3,1])==0)
print(Solution().maxProfit([7,4,1,2,6,8])==7)
        