class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            curr = abs(nums[i])
            if nums[curr] < 0:
                return abs(nums[i])
            nums[curr] = -nums[curr]
            