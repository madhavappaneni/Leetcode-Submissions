class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0

        charSet = defaultdict(int)
        maxLen = 0
        l = 0
        for r in range(len(s)):
            charSet[s[r]] += 1
            maxCount = max(maxCount, charSet[s[r]])
            if r - l + 1 - maxCount > k:
                charSet[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen