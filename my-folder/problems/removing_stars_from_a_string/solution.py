class Solution:
    def removeStars(self, s: str) -> str:
        output = []

        for ch in s:
            if ch == '*':
                output.pop()
            else:
                output.append(ch)
        
        return ''.join(output)
