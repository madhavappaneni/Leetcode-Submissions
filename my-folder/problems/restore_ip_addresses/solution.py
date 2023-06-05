class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []
        def backtrack(currIdx, prefix, count):
            print(currIdx, prefix)
            if currIdx == len(s) and count == 4:
                out.append(prefix)

            for i in range(currIdx, len(s)):
                subStr = s[currIdx:i + 1]
                if 0 <= int(subStr) <= 255 and len(subStr) == len(str(int(subStr))):
                    newPrefix = s[currIdx: i + 1] if not prefix else prefix + "." + s[currIdx: i + 1]
                    backtrack(i + 1, newPrefix, count + 1)
            
            return
        
        backtrack(0, "", 0)
        return out

                