class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        max_area = 0
        while(low < high):
            max_area = max(max_area, min(
                height[low], height[high]) * (high - low))
            if(height[low] < height[high]):
                low += 1
            else:
                high -= 1
        return max_area