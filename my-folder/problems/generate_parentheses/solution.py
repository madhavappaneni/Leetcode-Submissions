class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        
        def helper(curr = [], left = 0, right = 0):
            if left == n and right == n:
                out.append(''.join(curr))
            if left < n:
                curr.append('(')
                helper(curr, left + 1, right)
                curr.pop()
            if right < left:
                curr.append(')')
                helper(curr, left, right + 1)
                curr.pop()
        helper()
        return out
        
            