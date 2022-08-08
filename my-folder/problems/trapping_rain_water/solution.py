class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = height[left], height[right]
        surfaceArea = 0
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                surfaceArea += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])                
                surfaceArea += rightMax - height[right]
                right -= 1
        return surfaceArea