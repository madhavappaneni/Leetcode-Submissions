class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Sum = sum(nums)
        if abs(target) > Sum:
            return 0
        if (target + Sum) % 2 != 0:
            return 0
        target = round((sum(nums) + target) // 2)
        
        dp = [[0] * (target + 1) for _ in range(len(nums) + 1)]
        for row in range(len(nums) + 1):
            for col in range(target + 1):
                if col == 0:
                    dp[row][col] = 1
        for row in range(1, len(nums) + 1):
            for col in range(target + 1):
                if nums[row - 1] <= col:
                    dp[row][col] = dp[row - 1][col] + dp[row - 1][col - nums[row - 1]]
                else:
                    dp[row][col] = dp[row - 1][col]
        return dp[-1][-1]
                    