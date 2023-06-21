class Solution:
    def longestPalindrome(self, s: str) -> str:

        resL = 0
        resR = 0
        resLen = 0

        for i in range(len(s)):
            left, right = i, i

            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    resLen = right - left + 1
                    resL = left
                    resR = right
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    resLen = right - left + 1
                    resL = left
                    resR = right
                left -= 1
                right += 1
        return s[resL: resR + 1]
