class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, hi = 0, len(nums)
        
        while low < hi:
            mid = (low + hi) >> 1

            num = nums[mid] if ((nums[mid] < nums[0]) == (target < nums[0])) else (float('-inf') if target < nums[0] else float('inf'))

            if num < target:
                low = mid + 1
            elif num > target:
                hi = mid
            else:
                return mid
        return -1