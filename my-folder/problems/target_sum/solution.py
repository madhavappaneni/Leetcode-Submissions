class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize = None)
        def helper(currIdx, currTarget):
            if currIdx == len(nums):
                return int(currTarget == 0)

            return helper(currIdx + 1, currTarget - nums[currIdx]) + helper(currIdx + 1, currTarget + nums[currIdx])
            
        return helper(0, target)
            
            