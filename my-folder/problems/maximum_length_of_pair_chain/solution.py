class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # pairs.sort(key = lambda x: x[0])
        # dp = [1] * len(pairs)
        # for i in range(len(pairs)):
        #     for j in range(i):
        #         if pairs[i][0] > pairs[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        pairs.sort(key = lambda x: x[1])
        ans, curr = 0, float('-inf')
        for pair in pairs:
            if curr < pair[0]:
                curr = pair[1]
                ans += 1
        return ans