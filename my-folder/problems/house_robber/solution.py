class Solution:
    def rob(self, nums: List[int]) -> int:
        # @lru_cache()
        # def helper(idx):
        #     if idx > len(nums) - 1:
        #         return 0
        #     return max(nums[idx] + helper(idx + 2), helper(idx + 1))

        # def helper(idx):
        #     if idx < 0:
        #         return 0
        #     return max(nums[idx] + helper(idx - 2), helper(idx - 1))

        # return helper(len(nums) - 1)

        n = len(nums)
        dp = [0] * n
        if n <= 2:
            return max(nums)

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return max(dp)
