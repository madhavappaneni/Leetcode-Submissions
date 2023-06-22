class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def robSimple(houses):
            n = len(houses)
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
        
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            
            return max(dp)

        
        return max(robSimple(nums[1:]), robSimple(nums[:-1]))