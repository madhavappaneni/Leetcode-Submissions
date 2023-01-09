class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         @lru_cache(maxsize = None)
#         def helper(i, j):
#             if i == len(text1) or j == len(text2):
#                 return 0
        
#             if text1[i] == text2[j]:
#                 return 1 + helper(i+1, j+1)
#             return max(helper(i+1, j), helper(i, j+1))
                
#         return helper(0, 0)
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m+1)]
        
#         for i in range(m + 1):
#             for j in range(n + 1):
                
                    
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[-1][-1]