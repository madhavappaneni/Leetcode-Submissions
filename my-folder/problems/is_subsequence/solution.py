class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        counterS = 0
        counterT = 0
        
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        while i < len(t) and counterS < len(s) and counterT < len(t):
            if s[counterS] == t[counterT]:
                counterS += 1
                counterT += 1
            elif s[counterS] != t[counterT]:
                counterT += 1
            i += 1
        
        if counterS == len(s):
            return True
        return False            
