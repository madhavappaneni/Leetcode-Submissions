class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
            
        @lru_cache(None)
        def helper(i, j):
            if i == len(s1) and j == len(s2):
                return True
            
            if i < len(s1) and s1[i] == s3[i + j] and helper(i + 1, j):
                return True
            
            if j < len(s2) and s2[j] == s3[i + j] and helper(i, j + 1):
                return True
            return False
        
        return helper(0, 0)
        