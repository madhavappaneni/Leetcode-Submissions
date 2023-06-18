class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # @lru_cache(None)
        # def helper(remAmount):
        #     if remAmount == 0:
        #         return 0
        #     if remAmount < 0:
        #         return -1
            
        #     minNumCoins = float('inf')
        #     for coin in coins:
        #         numCoins = helper(remAmount - coin)
        #         if numCoins != -1:
        #             minNumCoins = min(minNumCoins, 1 + numCoins)
        #     return minNumCoins if minNumCoins != float('inf') else -1
        
        # return helper(amount)
            
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
            
        return dp[amount] if dp[amount] != float('inf') else -1