class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
#         @lru_cache()
#         def minCostHelper(idx):
#             if idx <= 1:
#                 return 0
#             return min(minCostHelper(idx - 1) + cost[idx - 1], minCostHelper(idx - 2) + cost[idx - 2]) 
        
#         return minCostHelper(len(cost))
        n = len(cost)
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[-1]