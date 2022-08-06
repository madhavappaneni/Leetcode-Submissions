class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        str1, str2 = text1, text2
        dp = [[0]*(len(str2)+1) for _ in range(1 + len(str1))]
        for i in range(len(str1) + 1):
            for j in range(len(str2) + 1):
                if i == 0 or j == 0:
                    continue
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[-1][-1]