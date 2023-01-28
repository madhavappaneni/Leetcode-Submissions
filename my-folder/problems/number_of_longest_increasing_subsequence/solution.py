class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1] * n
        count = [1] * n
        m = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
            m = max(m, dp[i]) 
        return sum(c for l, c in zip(dp, count) if l == m)