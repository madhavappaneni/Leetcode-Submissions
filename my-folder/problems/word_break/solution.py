class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)

        # @lru_cache(None)
        # def helper(idx):
        #     if idx == len(s):
        #         return True
        #     for i in range(idx, len(s)):
        #         if s[idx:i + 1] in wordDictSet and helper(i + 1):
        #             return True
        #     return False

        # return helper(0)

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if s[j: i] in wordDictSet and dp[j]:
                    dp[i] = True
        return dp[-1]