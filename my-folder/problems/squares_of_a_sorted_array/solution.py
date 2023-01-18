class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        left, right = 0, len(nums) - 1
        final = len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans[final] = nums[right] ** 2
                right -= 1
                final -= 1
            else:
                ans[final] = nums[left] ** 2
                left += 1
                final -= 1
        return ans
