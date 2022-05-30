class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if mid ** 2 == x:
                return mid
            
            elif mid ** 2 < x:
                if (mid + 1) ** 2 > x:
                    return mid
                lo = mid + 1
            
            else:
                hi = mid - 1
        return lo