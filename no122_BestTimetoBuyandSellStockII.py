class Solution:
	# O(n)
	# each vally and peak should be a transaction, since we can have multiple transactions
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowestPrice, highestPrice, maxProfit = float('inf'), 0, 0
        prices += [-1]
        # print('prices', prices)
        for i in range(0, len(prices) - 1):
        	# print('i', i)
        	if prices[i] < lowestPrice:
        		# print('1st')
        		lowestPrice = prices[i]
        		# print('lowestPrice, highestPrice, maxProfit', lowestPrice, highestPrice, maxProfit)
        	elif prices[i] > lowestPrice and prices[i + 1] < prices[i]:
        		# print('2nd')
        		highestPrice = prices[i]
        		maxProfit += prices[i] - lowestPrice
        		lowestPrice = prices[i + 1]
        		# print('lowestPrice, highestPrice, maxProfit', lowestPrice, highestPrice, maxProfit)	
        	elif prices[i] > lowestPrice and prices[i + 1] > prices[i]:
        		# print('3rd')
        		highestPrice = prices[i + 1]
        		# print('lowestPrice, highestPrice, maxProfit', lowestPrice, highestPrice, maxProfit)
        return maxProfit

print(Solution().maxProfit([7,1,5,3,6,4])==7)
print(Solution().maxProfit([1,2,3,4,5])==4)
print(Solution().maxProfit([7,6,4,3,1])==0)