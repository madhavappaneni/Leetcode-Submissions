class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return True if self.getString(s) == self.getString(t) else False
    
    def getString(self, string):
        lo, hi = 0, len(string) - 1
        res = collections.deque()
        carry = 0
        for i in string:
            if i != '#':
                res.append(i)
            elif res:
                res.pop()
        return "".join(res)