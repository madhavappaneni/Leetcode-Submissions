class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largestDiff = float("-inf")
        leastIndex = 0
        i = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[leastIndex]:
                largestDiff = max(largestDiff, prices[i] - prices[leastIndex])
            else:
                leastIndex = i
        return largestDiff if largestDiff > 0 else 0
            
        