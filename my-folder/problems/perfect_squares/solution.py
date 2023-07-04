class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)

        squares = [i ** 2 for i in range(int(sqrt(n)) + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(n + 1):
            for square in squares:
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i-square] + 1)
        # print(dp)
        return dp[-1]