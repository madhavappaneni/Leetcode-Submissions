class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def getBitCount(n):
            count = 0
            while n > 0:
                n &= n - 1
                count += 1
            return count

        if num1 < num2:
            return -1

        for i in range(102):
            diff = num1 - num2 * i
            numBits = getBitCount(diff)
            if numBits <= i <= diff:
                return i

        return -1
