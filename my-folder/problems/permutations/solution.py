class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(currIdx):
            if currIdx == len(nums):
                out.append(nums.copy())
            for i in range(currIdx, len(nums)):
                nums[currIdx], nums[i] = nums[i], nums[currIdx]
                backtrack(currIdx + 1)
                nums[currIdx], nums[i] = nums[i], nums[currIdx]
            
            return

        backtrack(0)
        return out
