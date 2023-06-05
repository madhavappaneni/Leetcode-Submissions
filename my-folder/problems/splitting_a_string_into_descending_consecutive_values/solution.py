class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(currIdx, currVal):
            if currIdx == len(s) and currVal != int(s):
                return True
            
            for i in range(currIdx, len(s)):
                nextVal = int(s[currIdx:i + 1])
                if currVal == float('inf') or (currVal - nextVal == 1):
                    if backtrack(i + 1, nextVal):
                        return True
            return False

        return backtrack(0, float('inf'))