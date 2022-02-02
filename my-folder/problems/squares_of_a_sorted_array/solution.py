class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans.append(nums[right] ** 2)
                right = right - 1 
            else:
                ans.append(nums[left] ** 2)
                left = left + 1
            
        return ans[::-1]
                