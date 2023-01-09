class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower = -1000000
        for num in preorder:
            if num < lower:
                return False
            while stack and num > stack[-1]:
                lower = stack.pop()
            stack.append(num)
        return True
            