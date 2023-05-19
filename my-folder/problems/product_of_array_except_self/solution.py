class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left = [1] * len(nums)
        # right = [1] * len(nums)
        # n = len(nums)

        # for i in range(1, n):
        #     left[i] = left[i - 1] * nums[i - 1]
        #     right[n - i - 1] = right[n - i] * nums[n - i]

        # return [left[i] * right[i] for i in range(n)]

        n = len(nums)
        left = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        carry = 1

        for i in reversed(range(n)):
            left[i] = left[i] * carry
            carry = carry * nums[i]
        
        return left
