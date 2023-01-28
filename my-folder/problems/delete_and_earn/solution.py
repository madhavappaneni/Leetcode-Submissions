class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # points = defaultdict(int)
        # maxNum = float('-inf')
        # for num in nums:
        #     points[num] += num
        #     maxNum = max(maxNum, num)
        
        # @lru_cache(None)
        # def solve(num):
        #     if num == 0:
        #         return 0
        #     if num == 1:
        #         return points[num]
        #     return max(solve(num - 1), solve(num - 2) + points[num])
        
        # return solve(maxNum)

        points = defaultdict(int)
        maxNum = float('-inf')
        for num in nums:
            points[num] += num
            maxNum = max(maxNum, num)

        dp = [0] * (maxNum + 1)
        dp[0] = 0
        dp[1] = points[1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
        
        return max(dp)