class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            if i == 0:
                left = 0
                right -= nums[i]
            elif i == len(nums) - 1:
                right = 0
                left += nums[i - 1]
            else:
                left += nums[i-1]
                right -= nums[i]
            if left == right:
                return i
        return -1