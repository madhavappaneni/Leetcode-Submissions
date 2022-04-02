class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        countDiff = 0
        while start <= end:
            if s[start] != s[end]:
                one = s[start:end]
                two = s[start+1: end+1]
                return one == one[::-1] or two == two[::-1]
            start += 1
            end -= 1
        return True