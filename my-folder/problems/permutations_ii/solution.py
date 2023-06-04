class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        def backtrack(currIdx):
            if currIdx == len(nums):
                out.append(nums.copy())

            lookup = set()
            
            for i in range(currIdx, len(nums)):
                if nums[i] not in lookup:
                    lookup.add(nums[i])
                    nums[currIdx], nums[i] = nums[i], nums[currIdx]
                    backtrack(currIdx + 1)
                    nums[currIdx], nums[i] = nums[i], nums[currIdx]
            
            return

        backtrack(0)
        return out
