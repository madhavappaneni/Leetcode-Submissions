class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start, end = 0, 0
        prefix_sum = 0
        max_sum = min(nums)
        while end < len(nums):
            if prefix_sum >= 0:
                prefix_sum += nums[end]
                max_sum = max(max_sum, prefix_sum)
                end += 1
            else:
                start = end + 1
                prefix_sum = 0
        return max_sum
