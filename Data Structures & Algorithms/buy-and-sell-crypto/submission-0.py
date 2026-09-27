class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i]:
                    profit.append(prices[j] - prices[i])

        if len(profit) == 0:
            return 0
        else:
            return max(profit)
            
            
        