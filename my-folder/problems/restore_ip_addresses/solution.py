class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out = set()

        def isValidPart(p):
            return p != "" and int(p) >= 0 and int(p) <= 255 and len(str(int(p))) == len(p)

        def helper(start, curr, k):
            if k == 0:
                if len(curr) == len(s) + 3:
                    # print(start, curr, k)
                    out.add(curr)
                return
            for idx in range(start, len(s) + 1):
                newStr = s[start: idx + 1]
                if isValidPart(newStr):
                    newInput = newStr if not curr else curr + "." + newStr
                    helper(idx + 1, newInput, k - 1)
        helper(0, "", 4)
        return out
