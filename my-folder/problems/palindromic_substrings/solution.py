class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[None] * (n + 1) for _ in range(n + 1)]
        # def arrayPrint(arr):
        #     for a in arr:
        #         print(a)
        count = -1
        for i in range(n + 1):
            dp[i][i] = True
            count += 1
            
        for i in range(1, n + 1):
            for j in range(1, i):
                if s[i-1] == s[j-1] and (i - j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    count += 1
        return count