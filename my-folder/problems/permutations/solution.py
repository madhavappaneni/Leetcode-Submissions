class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        def helper(currIdx):
            if currIdx == n:
                out.append(nums.copy())
            else:
                for idx in range(currIdx, n):
                    nums[currIdx], nums[idx] = nums[idx], nums[currIdx]
                    helper(currIdx + 1)
                    nums[currIdx], nums[idx] = nums[idx], nums[currIdx]
        helper(0)
        return out
