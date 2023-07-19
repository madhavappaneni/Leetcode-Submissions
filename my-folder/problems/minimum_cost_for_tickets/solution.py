class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # @lru_cache(None)
        # def helper(idx):
        #     if idx >= len(days):
        #         return 0
            
        #     first = costs[0] + helper(bisect_left(days, days[idx] + 1))
        #     second = costs[1] + helper(bisect_left(days, days[idx] + 7))
        #     third = costs[2] + helper(bisect_left(days, days[idx] + 30))
            
        #     return min(first, second, third)
        
        # return helper(0)

        dp = [0] * (len(days) + 1)

        for idx in range(len(days) - 1, -1, -1):
            dp[idx] = min(
                costs[0] + dp[bisect_left(days, days[idx] + 1)],
                costs[1] + dp[bisect_left(days, days[idx] + 7)],
                costs[2] + dp[bisect_left(days, days[idx] + 30)]
            )
        
        return dp[0]