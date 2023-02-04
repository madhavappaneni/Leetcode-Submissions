class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        out = [1] * len(nums)
        
        n = len(nums)

        for i in range(1, n):
            left[i] = left[i-1] * nums[i - 1]
            right[n-i-1] = right[n-i] * nums[n - i]
        
        return [left[i] * right[i] for i in range(n)]


        