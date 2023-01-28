class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        peak = 100001
        valley = 100001
        for price in prices:
            if price < peak:
                total += peak - valley
                valley = price
                peak = price
            else:
                peak = price
        total += peak - valley
        return total