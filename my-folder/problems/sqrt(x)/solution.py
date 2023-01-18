class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        if x == 0 or x == 1:
            return x
        mid = 0
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left - 1