class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # envelopes.sort(key = lambda x : (x[0], -x[1]))
        # n = len(envelopes)
        # dp = [1] * n

        # for i in range(n):
        #     for j in range(i):
        #         if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)

        envelopes.sort(key = lambda x : (x[0], -x[1]))
        n = len(envelopes)
        sub = [envelopes[0][-1]]
        for w, h in envelopes:
            if h > sub[-1]:
                sub.append(h)
            else:
                i = bisect_left(sub, h)
                sub[i] = h
        return len(sub)