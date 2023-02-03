class Solution:
    def countSubstrings(self, s: str) -> int:
         
        dp = [[None] * (len(s) + 1) for _ in range(len(s) + 1)]

        count = 0
        for i in range(1, len(s) + 1):
            dp[i][i] = True
            count += 1

        for i in range(1, len(s) + 1):
            for j in range(1, i):
                if s[i-1] == s[j-1] and (i - j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    count += 1
        return count

