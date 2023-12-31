# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n

        while low < high:
            mid = (low + high) >> 1

            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid

        return low