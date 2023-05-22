class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        charSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

