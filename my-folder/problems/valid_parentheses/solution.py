class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        bracketMap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for char in s:
            if char in ['(', '[', '{']:
                d.append(char)
            else:
                if len(d) > 0:
                    p = d.pop()
                    if bracketMap[p] != char:
                        return False
                else:
                    return False
                
        return True if len(d) == 0 else False