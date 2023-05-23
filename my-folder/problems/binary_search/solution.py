class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # low, high = 0, len(nums) - 1

        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return -1

        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) >> 1

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low if low < len(nums) and nums[low] == target else - 1