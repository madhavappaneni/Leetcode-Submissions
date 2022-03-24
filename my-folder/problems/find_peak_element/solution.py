class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        if len(nums) == 1:
            return 0

        while start <= end:
            mid = start + (end - start) // 2
            if mid > 0 and mid < len(nums) - 1:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid

                elif nums[mid - 1] > nums[mid]:
                    end = mid - 1

                else:
                    start = mid + 1
            elif mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    start = mid + 1

            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    end = mid - 1

        return mid