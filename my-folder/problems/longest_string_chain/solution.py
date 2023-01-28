class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        dp = collections.defaultdict(int)
        for word in words:
            if len(word) == 1:
                dp[word] = 1
            for i in range(0, len(word)):
                dp[word] = max(dp[word], 1 + dp.get((word[:i] + word[i + 1:]), 0))
        return max(dp.values())
            
        