class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) + 1):
            diff = target-nums[i]
            if diff in nums and not i == nums.index(diff):
                return [i, nums.index(diff)]