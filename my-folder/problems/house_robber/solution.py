class Solution:
    def rob(self, nums: List[int]) -> int:
#         @lru_cache()        
#         def robHelper(i):
#             if i == 0:
#                 return nums[i]
#             if i == 1:
#                 return max(nums[1], nums[0])
#             return max(robHelper(i - 1), robHelper(i-2) + nums[i])
    
#         return robHelper(len(nums) - 1)   
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        n = len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
        