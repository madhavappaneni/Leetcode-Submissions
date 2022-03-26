class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2

            if nums[mid] == nums[mid ^ 1]:
                start = mid + 1

            else:
                end = mid

        return nums[start]
