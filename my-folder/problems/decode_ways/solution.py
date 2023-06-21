class Solution:
    def numDecodings(self, s: str) -> int:

        # @lru_cache(None)
        # def helper(idx):
        #     if idx == len(s):
        #         return 1
            
        #     if idx >= len(s):
        #         return 0
            
        #     ans = 0
        #     if int(s[idx]) == 0:
        #         return 0
        #     if int(s[idx]) > 0:
        #         ans += helper(idx + 1)
        #     if 0 < int(s[idx: idx + 2]) <= 26:
        #         ans += helper(idx + 2)
        #     return ans
        # return helper(0)


        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
    
        for i in range(2, len(s) + 1):

            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            
            if 10 <= int(s[i-2: i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]

