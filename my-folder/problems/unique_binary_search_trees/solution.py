class Solution:
    def numTrees(self, n: int) -> int:
        
        # @lru_cache(None)
        # def helper(m):
        #     if m == 0 or m == 1:
        #         return 1
        #     return sum(helper(i) * helper(m - i - 1) for i in range(m))
        
        # return helper(n)


        # bottom up

        dp = [1] * (n + 1)

        for node in range(2, n + 1):
            total = 0
            for root in range(1, node + 1):
                total += dp[root - 1] * dp[node - root]
            dp[node] = total
        
        return dp[n]