class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out, right = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        left = 1
        for i in range(len(nums)):
            left = left * nums[i-1] if 0 < i < len(nums) else 1
            out[i] = left * right[i]
        return out