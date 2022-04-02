class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        
        for i in range(n-2, -1, -1):
            dp[i%2 == 0] = sum(dp)
        
        return dp[1]