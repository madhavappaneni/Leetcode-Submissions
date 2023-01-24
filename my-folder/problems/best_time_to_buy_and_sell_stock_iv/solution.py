class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def solve(txnsRemaining, idx, holdingStock):
            if txnsRemaining == 0 or idx == len(prices):
                return 0
            doNothing = solve(txnsRemaining, idx + 1, holdingStock)
            doSomething = None
            if holdingStock:
                doSomething = solve(txnsRemaining - 1, idx + 1, not holdingStock) + prices[idx]
            else:
                doSomething = solve(txnsRemaining, idx + 1, not holdingStock) - prices[idx]
            return max(doSomething, doNothing)
    
        return solve(k, 0, False)