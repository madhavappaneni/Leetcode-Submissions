class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # @lru_cache(maxsize = None)
        # def helper(i):
        #     if i >= len(nums):
        #         return 0
            
        #     return max(nums[i] + helper(i + 2), helper(i + 1))
        
        # return helper(0)
    
        # dp = [-1] * (len(nums))
        # if len(nums) <= 2:
        #     return max(nums)

        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1] , dp[i-2] + nums[i])
        
        # return dp[-1]

        robSecond = 0
        robFirst = nums[0]

        for i in range(1, len(nums)):
            current = max(robFirst, robSecond + nums[i])
            robSecond = robFirst
            robFirst = current
        
        return robFirst
