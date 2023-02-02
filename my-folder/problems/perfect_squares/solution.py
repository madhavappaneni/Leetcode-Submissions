class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        squares = [i * i for i in range(1, int(sqrt(n)) + 1)]
        for i in range(n + 1):
            for square in squares:
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]