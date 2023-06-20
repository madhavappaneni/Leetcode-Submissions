class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # @lru_cache(None)
        # def helper(idx, currMax):
        #     if idx == len(nums):
        #         return 0
        #     if nums[idx] > currMax:
        #         return max(
        #             1 + helper(idx + 1, nums[idx]),
        #             helper(idx + 1, currMax)
        #         )
        #     else:
        #         return helper(idx + 1, currMax)
        
        # return helper(0, float('-inf'))

        dp = [1] * (len(nums))

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j]) 
        
        return max(dp)

