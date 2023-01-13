class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, len(nums) - 1
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        while low <= high:
            mid = (low + high) >> 1
            smaller = (mid - 1) % n
            larger = (mid + 1) % n
            # print(mid, smaller, larger, low, high, nums[smaller] > nums[mid] and nums[mid] < nums[larger], nums[mid])
            if nums[smaller] > nums[mid] and nums[mid] < nums[larger]:
                return nums[mid]
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return 0
        
                
                
            
