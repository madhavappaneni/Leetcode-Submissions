class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1 
        n, res = len(s), 0
        while n > 0:
            n -= 1
            if(s[n] != " "): res += 1
            elif res>0: return res
        return res
            