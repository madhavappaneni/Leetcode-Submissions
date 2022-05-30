# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 0, n
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            check = isBadVersion(mid)
            
            if check == True:
                hi = mid
            else:
                lo = mid + 1
            
        return lo