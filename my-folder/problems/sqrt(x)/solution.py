class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 2 or x == 3:
            return 1
        prev = 0
        for i in range(x):
            sqr = i * i
            if prev < x and x < sqr:
                return i - 1
            elif x == sqr:
                return i
            prev = sqr
        return 0