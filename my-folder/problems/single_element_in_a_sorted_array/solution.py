class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) >> 1
            # print(mid, nums[mid] != nums[mid - 1], nums[mid] != nums[mid + 1])
            nei = mid + 1 if mid % 2 == 0 else mid - 1
            if nums[mid] == nums[nei]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]

