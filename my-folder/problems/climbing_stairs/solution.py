class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-2] + dp[i-1]
        return max(dp)