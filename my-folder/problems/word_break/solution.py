class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        
        # @lru_cache()
        # def helper(idx):
        #     if idx == n:
        #         return True
        #     for i in range(idx, n):
        #         if s[idx:i+1] in wordDict and helper(i + 1): 
        #             return True
        # return helper(0)

        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
