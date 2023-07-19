class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

            dp = [1] + [-1] * (high + 1)
            
            def helper(n):
                if dp[n] != -1:
                    return dp[n]
                count = 0
                if n >= zero:
                    count += helper(n - zero)
                if n >= one:
                    count += helper(n - one)
                dp[n] = count % mod
                return dp[n]

            
            ans = 0
            mod = 10 ** 9 + 7
            return sum(helper(end) for end in range(low, high + 1)) % mod

            # dp = [1] + [0] * high
            # mod = 10 ** 9 + 7

            # for i in range(1, high + 1):
            #     dp[i] = (dp[i - zero] + dp[i - one]) % mod
            # return sum(dp[low:high + 1]) % mod