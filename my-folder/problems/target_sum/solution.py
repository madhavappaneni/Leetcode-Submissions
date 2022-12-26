class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = [0]
        targetSumMap = [[-1] * (len(nums) + 1) for _ in range(2 * sum(nums) + 1)]
        def helper(idx, currTarget):
            print(idx, currTarget, "test")
            if idx == len(nums):
                if currTarget == target:
                    return 1
                else:
                    return 0
            else:
                if targetSumMap[currTarget + sum(nums)][idx] != -1:
                    return targetSumMap[currTarget + sum(nums)][idx]
                add = helper(idx + 1, currTarget + nums[idx])
                sub = helper(idx + 1, currTarget - nums[idx])
                targetSumMap[currTarget + sum(nums)][idx] = add + sub
                return add + sub
        return helper(0, 0)
            
            