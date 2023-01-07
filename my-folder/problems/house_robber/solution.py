class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memoization        
        # @lru_cache()
        # def robHelper(idx):
        #     if not 0 <= idx <= len(nums) - 1:
        #         return 0
        #     elif idx == 0:
        #         return nums[0]
        #     elif idx == 1:
        #         return max(nums[0], nums[1])
        #     else:
        #         return max(robHelper(idx - 1), nums[idx] + robHelper(idx - 2))
        
        # return robHelper(len(nums) - 1)

        n = len(nums)
        if (n) <= 2:
            return max(nums)
        dp = [0] * (n)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]