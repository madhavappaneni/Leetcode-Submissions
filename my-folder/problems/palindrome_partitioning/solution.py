class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def backtrack(currIdx, prefix):
            # print('func', currIdx, prefix)
            if currIdx == len(s):
                out.append(prefix.copy())
            
            for i in range(currIdx, len(s)):
                # print(i, s[currIdx:i + 1], s[currIdx:i + 1] == s[currIdx:i + 1][::-1])
                if s[currIdx:i + 1] == s[currIdx:i + 1][::-1]:
                    backtrack(i + 1, prefix + [s[currIdx:i + 1]])
            
            return
        
        backtrack(0, [])
        return out
                