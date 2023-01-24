class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def solve(idx, holdingStock):
            if idx >= len(prices):
                return 0
            doNothing = solve(idx + 1, holdingStock)
            doSomething = None
            if holdingStock:
                doSomething = solve(idx + 2, not holdingStock) + prices[idx]
            else:
                doSomething = solve(idx + 1, not holdingStock) - prices[idx]
            return max(doSomething, doNothing)
    
        return solve(0, False)