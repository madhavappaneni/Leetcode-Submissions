class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        N = len(nums)

        # @lru_cache(None)
        # def dfs(i):
        #     if i == N - 1:
        #         return True
        #     if nums[i] == 0:
        #         return 0
        #     for j in range(i + 1, min(len(nums) - 1, i + nums[i]) + 1):
        #         if dfs(j):
        #             return True
        #     return False
        
        # return dfs(0)

        # dp = [False] * (N)
        # dp[0] = True

        # for i in range(N):
        #     if dp[i]:
        #         for j in range(1, nums[i] + 1):
        #             if i + j < N:
        #                 dp[i + j] = True
        #             if i + j == N - 1:
        #                 return True
        # return dp[-1]

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0