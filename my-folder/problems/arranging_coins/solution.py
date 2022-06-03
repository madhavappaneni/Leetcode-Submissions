class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        
        while lo <= hi:
            mid = (lo + hi) // 2
            sumOfN = self.sumN(mid)
            
            if sumOfN == n:
                return mid
            elif sumOfN > n:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi
        
        
    def sumN(self, n):
        return n * (n + 1) / 2