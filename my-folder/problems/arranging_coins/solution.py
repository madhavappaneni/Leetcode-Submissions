class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n

        while low <= high:
            mid = (low + high) >> 1

            num = (mid * (mid + 1)) // 2

            if n == num:
                return mid
            elif num > n:
                high = mid - 1
            else:
                low = mid + 1
        
        return high