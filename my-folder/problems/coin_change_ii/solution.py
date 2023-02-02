class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # def solve(remAmount, idx):
        #     if remAmount < 0 or idx < 0:
        #         return 0
        #     if remAmount == 0:
        #         return 1
        #     return solve(remAmount - coins[idx], idx) + solve(remAmount, idx - 1)
        # return solve(amount, len(coins) - 1)

        # dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # for i in range(len(coins) + 1):
        #     dp[i][0] = 1
        
        # for i in range(1, len(coins) + 1):
        #     for j in range(1, amount + 1):
        #         dp[i][j] = dp[i-1][j]
        #         if j - coins[i-1] >= 0:
        #             dp[i][j] += dp[i][j - coins[i-1]]
        # return dp[-1][-1]

        dp = [0] * (amount + 1)

        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                if i >= coin:
                    dp[i] += dp[i-coin]
        return dp[-1]
