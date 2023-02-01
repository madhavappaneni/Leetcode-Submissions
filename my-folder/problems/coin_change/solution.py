class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @lru_cache(None)
        # def solve(remAmount):
        #     if remAmount < 0:
        #         return -1
        #     if remAmount == 0:
        #         return 0
        #     minCoins = float('inf')

        #     for coin in coins:
        #         if remAmount >= coin:
        #             numCoins = solve(remAmount - coin)
        #             if numCoins != -1:
        #                 minCoins = min(minCoins, numCoins + 1)
        #     return minCoins if minCoins != float('inf') else -1
        # return solve(amount)

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            
        return dp[-1] if dp[-1] != float('inf') else -1