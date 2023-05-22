class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bruteforce
        # maxprofit = float('-inf')
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = (prices[j] - prices[i])
        #         maxprofit = max(maxprofit, profit)
        
        # return maxprofit if maxprofit > 0 else 0

        # onepass
        maxprofit = float('-inf')
        minValue = float('inf')

        for i in range(len(prices)):

            if prices[i] > minValue:
                maxprofit = max(maxprofit, prices[i] - minValue)
            else:
                minValue = min(minValue, prices[i])
        
        return maxprofit if maxprofit > 0 else 0