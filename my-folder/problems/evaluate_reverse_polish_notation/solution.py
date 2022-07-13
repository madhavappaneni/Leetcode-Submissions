class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                b, a = int(stack.pop()), int(stack.pop())
                operation = operations[token]
                stack.append(operation(a, b))
        return int(stack[-1])