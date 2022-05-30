class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        if hi == -1:
            return (-1, -1)
        lo1 = -1
        lo2 = -1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[lo] != target:
            return (-1, -1)
        lo1 = lo

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2 + 1

            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid

        lo2 = lo

        return lo1, lo2