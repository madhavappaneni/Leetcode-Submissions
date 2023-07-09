class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                elem1, elem2 = int(stack.pop()), int(stack.pop())
                ans = None
                if token == '+': ans = elem1 + elem2
                if token == '-': ans = elem2 - elem1
                if token == '*': ans = elem1 * elem2
                if token == '/': ans = elem2 / elem1
                stack.append(ans)
            else:
                stack.append(token)
        return int(stack[-1])
