class Solution:
    def numSquares(self, n: int) -> int:
        
        numMap = [i ** 2 for i in range(1, floor(sqrt(n)) + 1)]

        # @lru_cache(None)
        # def helper(num):
        #     print(num)
        #     if num < 0:
        #         return -1
        #     if num == 0:
        #         return 0
        #     else:
        #         minVal = float('inf')
        #         for sq in numMap:
        #             if num - sq >= 0:
        #                 val = helper(num - sq)
        #                 if val != -1:
        #                     minVal = min(minVal, val + 1)
        #         return minVal if minVal != float('inf') else -1
        
        # return helper(n)
                                

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(n + 1):
            for sq in numMap:
                if i - sq >= 0:
                    dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[-1]

