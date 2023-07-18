class Solution:
    def integerBreak(self, n: int) -> int:


        # # @lru_cache(None)
        # # def helper(m):
        # #     if m == 1 or m == 2:
        # #         return 1
        # #     ans = 1
        # #     for i in range(1, m):
        # #         ans = max(ans, i * helper(m - i), i * (m - i))
        # #     return ans
        
        # # return helper(n)

        # dp = [1] * (n + 1)
        
        # for i in range(3, n + 1):
        #     for j in range(1, i):
        #         dp[i] = max(dp[i], (j) * dp[i - j], (j) * (i - j))
                
        # return dp[-1]

        @lru_cache(None)
        def helper(m):
            if m == 1 or m == 2:
                return 1
            ans = 1
            for i in range(1, m):
                ans = max(ans, i * helper(m - i), i * (m - i))
            return ans
        
        return helper(n)