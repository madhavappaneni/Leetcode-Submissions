class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * (n+1) for _ in range(n+1)]
        
        maxAns = ""
        
        for i in range(n + 1):
            dp[i][i] = True
            if i < n:
                maxAns = s[i]
        
        maxLen = -1
        
        for i in range(1, n + 1):
            for j in range(1, i):
                if s[i-1] == s[j-1] and (i - j <= 2 or dp[i-1][j+1]):
                    if maxLen < i - j + 1:
                        maxLen = i - j + 1
                        maxAns = s[j-1:i]
                    dp[i][j] = True
        return maxAns
                    