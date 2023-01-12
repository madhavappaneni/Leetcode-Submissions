class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # n = len(coins)

        # def coinChangeHelper(remAmount):
        #     if remAmount == 0:
        #         return 0
        #     if remAmount < 0:
        #         return -1
        #     mini = float('inf')
        #     for coin in coins:
        #         ans = coinChangeHelper(remAmount - coin)
        #         if ans != -1:
        #             mini = min(ans, mini)
        #     return mini + 1 if mini != float(inf) else -1
        
        # return coinChangeHelper(amount)

        dp = [float(inf)] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1


