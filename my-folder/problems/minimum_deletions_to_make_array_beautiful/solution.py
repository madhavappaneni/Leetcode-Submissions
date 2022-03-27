class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        dummy = 0
        for i in range(len(nums)-1):
            if (i + dummy) % 2 == 0 and nums[i] == nums[i+1]:
                count += 1
                dummy += 1
        if ((len(nums) - dummy) % 2 == 1):
            count += 1
        return count
