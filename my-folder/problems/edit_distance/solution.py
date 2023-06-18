class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # @lru_cache(None)
        # def solve(i, j):
        #     if i == 0:
        #         return j
        #     elif j == 0:
        #         return i
        #     elif word1[i - 1] == word2[j - 1]:
        #         return solve(i - 1, j - 1)
        #     else:
        #         return min(solve(i-1, j), solve(i, j-1), solve(i-1, j-1)) + 1
        
        # return solve(len(word1), len(word2))

        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]


        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
        return dp[-1][-1]