class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # def getOneBits(n):
            # count = 0
            # while n:
            #     n = n & (n-1)
            #     count += 1
            # return count
        ans = [0] 
        for i in range(1, n + 1):
            ans.append(ans[i & (i-1)] + 1)
        return ans