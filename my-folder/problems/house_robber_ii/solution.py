class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def robSimple(houses):
            n = len(houses)
            dp = [0] * n
            if n <= 2:
                return max(houses)

            dp[0], dp[1] = houses[0], max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            print(dp)
            return max(dp)
        
        return max(robSimple(nums[1:]), robSimple(nums[:-1]))