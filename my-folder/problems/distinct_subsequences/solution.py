class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # def solve(i, j):
        #     if j < 0: return 1
        #     if i < 0: return 0
        #     if s[i] == t[j]: return solve(i-1, j-1) + solve(i - 1, j)
        #     return solve(i - 1, j)
        # return solve(len(s)-1, len(t)-1)
        # if s == t:
        #     return 1
        # if len(s) < len(t):
        #     return 0
        # dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # for i in range(len(s) + 1):
        #     dp[i][0] = 1
        # for i in range(1, len(s) + 1):
        #     for j in range(1, len(t) + 1):
        #         if s[i-1] == t[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[-1][-1]

        # @lru_cache(None)
        # def helper(i, j):
        #     if j >= len(t):
        #         return 1
        #     if i >= len(s):
        #         return 0
        #     if s[i] == t[j]:
        #         return helper(i + 1, j + 1) + helper(i + 1, j)
        #     else:
        #         return helper(i + 1, j)
        
        # return helper(0, 0)

        # if s == t:
        #     return 1
        # if len(s) < len(t):
        #     return 0

        # m, n = len(s), len(t)

        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # for i in range(m + 1):
        #     dp[i][0] = 1

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        # return dp[-1][-1]


        if s == t:
            return 1
        if len(s) < len(t):
            return 0

        m, n = len(s), len(t)

        prev = [0] * (n + 1)
        prev[0] = 1

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = 1

            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j] + prev[j - 1]
                else:
                    curr[j] = prev[j]
            prev = curr
        return prev[-1]

