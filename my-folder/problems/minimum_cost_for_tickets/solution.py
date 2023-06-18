class Solution:
    def mincostTickets(self, days, costs) -> int:

        # def helper(idx):
        #     print(idx)
        #     if idx >= len(days):
        #         return 0
        #     return min(

        #     )
        # return helper(0)

        # dp = [0] * (len(days) + 1)
    
        # for i, x in enumerate(days):
        #     dp[i + 1] = min(
        #         dp[bisect.bisect(days, x - d, 0, i)] + c
        #         for d, c in zip((1, 7, 30), costs)
        #     )
        
        # return dp[-1]

        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)
        return dp(1)