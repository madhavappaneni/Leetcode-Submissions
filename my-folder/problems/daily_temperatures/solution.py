class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                prevIdx = stack.pop()
                answer[prevIdx] = i - prevIdx
            stack.append(i)
        return answer