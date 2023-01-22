class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n, res = abs(num), ''
        while n > 0:
            res = str(n % 7) + res
            n /= 7
        return '-' * (num < 0) + res or "0"
            