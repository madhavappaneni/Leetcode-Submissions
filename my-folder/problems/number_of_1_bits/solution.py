class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mask = 1
        # bits = 0
        # for i in range(32):
        #     if (mask & n) != 0:
        #         bits += 1
        #     mask <<= 1
        # return bits
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count