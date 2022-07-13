class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        
        for i, val in enumerate(temperatures):
            while len(stack) > 0 and val > stack[-1][0]:
                p = stack.pop()
                out[p[1]] = i - p[1]
            stack.append([val, i])
        return out