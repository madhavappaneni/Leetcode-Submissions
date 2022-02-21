class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, hi = 1, num

        while low <= hi:
            mid = low + (hi - low) // 2
            # print(low, hi, mid)
            if mid ** 2 == num:
                return mid
            
            if mid ** 2 > num:
                hi = mid - 1
            
            if mid ** 2 < num:
                low = mid + 1
        
        return None