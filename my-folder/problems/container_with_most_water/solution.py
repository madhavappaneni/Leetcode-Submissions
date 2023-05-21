class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        maxArea = float('-inf')
        while start < end:
            area = (end - start) * min(height[start], height[end])
            maxArea = max(maxArea, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxArea