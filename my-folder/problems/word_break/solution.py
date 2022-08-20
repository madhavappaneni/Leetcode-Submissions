class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        # @lru_cache
        # def helper(idx):
        #     if idx == len(s):
        #         return True
        #     for i in range(idx, len(s)):
        #         if s[idx: i + 1] in wordDict and helper(i + 1):
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
        