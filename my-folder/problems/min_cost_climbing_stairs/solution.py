class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # @lru_cache(None)
        # def helper(i):
        #     if i >= len(cost):
        #         return 0
        #     else:
        #         return min(helper(i + 1), helper(i + 2)) + cost[i]
        
        # return min(helper(0), helper(1))

        dp = [0] * (len(cost))

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])
        

