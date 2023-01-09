class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        # @lru_cache(2001)
        # def maxScoreHelper(left, i):
        #     if i == m:
        #         return 0
        #     right = n - 1 - (i - left)
        #     return max(maxScoreHelper(left, i + 1) + nums[right] * multipliers[i], maxScoreHelper(left + 1, i + 1) + nums[left] * multipliers[i] )
        
        # m,n = len(multipliers), len(nums)
        # return maxScoreHelper(0, 0)
        
        m,n = len(multipliers), len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)
                dp[i][left] = max(dp[i+1][left] + nums[right] * multipliers[i], dp[i + 1][left + 1] + nums[left] * multipliers[i])
        
        return dp[0][0]

            
