from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPro = 0
        
        while r < len(prices):
        	##Profit
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                maxPro = max(profit, maxPro)
                
            else:
                l=r ## This is done because in the check above l was greater than r which means r was at lowest which is 
                	#best situation, so we jump there.

            r+=1 ## slide every run
        return maxPro

