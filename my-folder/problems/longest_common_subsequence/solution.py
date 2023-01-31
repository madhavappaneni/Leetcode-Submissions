class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # @lru_cache(None)
        # def solve(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     elif text1[i] == text2[j]:
        #         return 1 + solve(i - 1, j - 1)
        #     else:
        #         return max(solve(i-1, j), solve(i, j - 1))
        
        # return solve(len(text1) - 1, len(text2) - 1)

        dp = [[0] * (len(text2) + 1) for _ in range(1 + len(text1))]
        
        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]